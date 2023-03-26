import openai
import gradio

# Use key to access API
openai.api_key = open("key.txt", "r").read().strip('\n')

# Basic completion statement
completion = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[{"role" : "user",
               "content": "What is the circumference of the moon in km?"}] # This content is what we want to input to ChatGPT
)

# Access reply content from basic completion
reply_content = completion.choices[0].message.content

# You have to keep track of the message history
# Allows you to make up assistant responses if you want
message_history = []
user_input = input(">: ")
print("User's input was", user_input)

message_history.append({"role": "user", "content": user_input})
completion = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=message_history
)

reply_content = completion.choices[0].message.content
