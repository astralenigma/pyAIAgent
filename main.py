import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
# from subdirectory.filename import function_name
from prompts import system_prompt
from call_function import available_functions
verbose=False
if len(sys.argv)<2:
    print("Usage: python3 main.py <prompt>")
    sys.exit(1)
if len(sys.argv)>2:
    if sys.argv[2]=="--verbose":
        verbose=True

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
user_prompt=sys.argv[1]
client = genai.Client(api_key=api_key)
model_name='gemini-2.0-flash-001'

messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),
            ]
response=client.models.generate_content(model=model_name,
    contents=messages,
    config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt))

print(response.text)
if (response.function_calls):
    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        
if(verbose):
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")