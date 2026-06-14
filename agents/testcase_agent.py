
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def generate_test_cases(
        requirement,
        acceptance_criteria):

    with open(
        "prompts/testcase_generation.md",
        "r"
    ) as file:

        prompt = file.read()

    prompt = prompt.replace(
        "{{requirement}}",
        requirement
    )

    prompt = prompt.replace(
        "{{acceptance_criteria}}",
        acceptance_criteria
    )

    response = client.chat.completions.create(

        model="openai/gpt-4o-mini",

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content
