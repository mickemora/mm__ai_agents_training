#########################################################
#Use a stable public API (JSONPlaceholder) to fetch posts

import requests, json
 
BASE = "https://jsonplaceholder.typicode.com"

r = requests.get(f"{BASE}/posts/1", timeout=10)
r.raise_for_status()

data = r.json()
print(type(data), data["id"], data["title"])

#Inspect response metadata:
print("Status:", r.status_code)

print("\n")
print("Content-Type:", r.headers.get("content-type"))
print("\n")

print("Preview:", json.dumps(data, indent=2)[:300])
print("\n")


##################################################################
# JSONPlaceholder doesn't paginate, so we emulate pages of size 10
def fetch_posts_page(page:int, size:int=10):
    start = (page-1) * size + 1
    end = start + size - 1

    r = requests.get(f"{BASE}/posts", timeout=10)
    r.raise_for_status()

    all_posts = r.json()
    return all_posts[start-1:end]
 
page1 = fetch_posts_page(1); page2 = fetch_posts_page(2)
print("Page1 len:", len(page1), "| first title:", page1[0]["title"])
print("Page2 len:", len(page2))
print("\n")


###############################################################
#Practice mutating endpoints (JSONPlaceholder simulates writes)

new_post = {"title":"Agent Lab", "body":"Hello API", "userId":42}
created = requests.post(f"{BASE}/posts", json=new_post, timeout=10).json()
print("Created:", created)

update = {"title":"Agent Lab v2"}
print("Updating post id", created["id"])
print("\n")

#updated = requests.put(f"{BASE}/posts/{created['id']}", json=update, timeout=10).json()
update = {"id": 1, "title": "Agent Lab v2", "body": "Hello API", "userId": 42}
response = requests.put(f"{BASE}/posts/1",json=update,timeout=10)
response.raise_for_status()
updated = response.json()
print("Updated:", updated)


deleted = requests.delete(f"{BASE}/posts/{created['id']}", timeout=10)
print("Delete status:", deleted.status_code)
print("\n")

#########################################################
#Load a token securely and call an authenticated endpoint
import os
from dotenv import load_dotenv
load_dotenv()
 
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

headers = {"Accept":"application/vnd.github+json"}

if GITHUB_TOKEN:
    headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
 
gh = requests.get("https://api.github.com/rate_limit", headers=headers, timeout=10)

print("GitHub status:", gh.status_code)
print("Rate info:", gh.json().get("resources",{}).get("core",{}))

#Fetch issues from a public repo
print("\n")
print("Fetching issues from a public repo:")
owner, repo = "pallets", "flask"

issues = requests.get(f"https://api.github.com/repos/{owner}/{repo}/issues",
                      headers=headers, params={"state":"open","per_page":5}, timeout=10)
issues.raise_for_status()

for it in issues.json():
    print(f"#{it['number']} - {it['title']}")

print("\n")


###########################################################
#Add timeouts, raise_for_status(), and exponential backoff.

import time

def robust_get(url, headers=None, params=None, retries=3, backoff=1.5):
    for attempt in range(1, retries + 1):
        try:
            r = requests.get(url, headers=headers, params=params, timeout=10)

            if r.status_code == 429:  # rate limited
                wait = int(r.headers.get("Retry-After", 2))
                time.sleep(wait); continue

            if r.status_code >= 400:
                print("Status:", r.status_code)
                print("Response body:", r.text[:1000])

            r.raise_for_status()
            return r.json()

        except requests.RequestException as e:
            print(f"[Attempt {attempt}] Error: {e}")
            if attempt == retries: raise
            time.sleep(backoff**attempt)
 
data = robust_get(f"{BASE}/posts/2")
print("Robust fetch title:", data["title"])


#####################################################################
#Quickly assert expected keys so your agent doesn’t break downstream.

def validate_post(obj:dict):
    required = {"userId","id","title","body"}
    missing = required - obj.keys()
    assert not missing, f"Missing keys: {missing}"
 
validate_post(data)  # raises if shape changes
print("\n")


############################################################
#Expose a tiny, reusable function your future agent can use.

def search_github_issues(repo_fullname: str, q: str, per_page: int = 5):
    url = "https://api.github.com/search/issues"
    params = {
        "q": f"repo:{repo_fullname} is:issue {q}",
        "per_page": per_page,
        "sort": "created",
        "order": "desc"
    }
    return robust_get(url, headers=headers, params=params)

results = search_github_issues("pallets/flask", "bug")

for item in results.get("items", []):
    print("-", item["title"])


print("\n")