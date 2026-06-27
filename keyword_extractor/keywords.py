from dotenv import load_dotenv
import openai
import os

print('Loading Env variables...')
load_dotenv(override=True)

print('Setting up client...')
client = openai.OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

# response = client.chat.completions.create(
#     model="nvidia/nemotron-3-super-120b-a12b",
#     messages=[{"role": "user", "content": "Give me back a two word answer."}]
# )

with open('input.txt', 'r') as f:
    text_in = f.read()

message = {"role": "user", "content": text_in}
model = "meta/llama-3.2-3b-instruct"

print('Connecting to llm...')
completion = client.chat.completions.create(
    model=model,
    messages=[message],
    temperature=0.2,
    top_p=0.7,
    max_tokens=1024,
)

print('Outputting Message...')

with open('output.txt', 'w') as f:
    f.write(completion.choices[0].message.content)

print('Programme Finish')