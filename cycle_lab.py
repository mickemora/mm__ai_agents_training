import os
from dotenv import load_dotenv
from openai import OpenAI
 
load_dotenv()
client = OpenAI()


##############################
#2.- Define a Helpder function
def chat_cycle(messages):
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return resp.choices[0].message.content


######################
#3.- Single-Turn Prompting
messages = [{"role": "user", "content": "Explain Agentic AI in one sentence."}]
print("Single-turn conversation:")
print(chat_cycle(messages))
print("\n")


#4.- Multi-Turn Conversations
#########################

conversation = [
    {"role": "system", "content": "You are a friendly teaching assistant."},
    {"role": "user", "content": "What is an AI agent?"},
]
print("Multi-turn conversation:")
reply1 = chat_cycle(conversation)
print("AI:", reply1)
print("\n")


# Add another turn
conversation.append({"role": "assistant", "content": reply1})
conversation.append({"role": "user", "content": "Can you give me an example in healthcare?"})
reply2 = chat_cycle(conversation)
print("AI:", reply2)
print("\n")


#############################
#6.- Controlled Output Cycles

messages = [
    {"role": "system", "content": "You are a JSON-only assistant."},
    {"role": "user", "content": "List 3 tools used in Agentic AI."}
]
print("Controlled output conversation:")
print(chat_cycle(messages))
print("\n")


#########################
#7.- Q&A Agent Simulation

conversation = [{"role": "system", "content": "You are an educational AI tutor."}]

while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit","quit"]: break
    conversation.append({"role": "user", "content": user_input})
    reply = chat_cycle(conversation)
    print("AI:", reply)
    conversation.append({"role": "assistant", "content": reply})

print("\n")