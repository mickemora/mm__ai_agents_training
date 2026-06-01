import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def ask_gpt(prompt):

    response = client.responses.create(
        model="gpt-5-mini",
          input=[
            {
              "role": "developer",
              "content": [
                {
                  "type": "input_text",
                  "text": prompt
                }
              ]
            }
        ],
          text={
            "format": {
              "type": "text"
            },
            "verbosity": "medium"
          },
          reasoning={
            "effort": "medium",
            "summary": "auto"
          },
          tools=[],
          store=True,
          include=[
            "reasoning.encrypted_content",
            "web_search_call.action.sources"
        ]
    )

    return response.output_text

prompt = """
Solve: A train leaves at 3pm traveling 60 mph. Another leaves at 4pm at 90 mph. 

When will the faster train catch up? 

Think step by step.
"""

print(ask_gpt(prompt))
print("\n")