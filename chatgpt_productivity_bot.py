import openai
import gradio

openai.api_key = open("key.txt", "r").read().strip('\n')

completion = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[{"role" : "user",
               "content": "What is the circumference of the moon in km?"}]
)

print(completion)