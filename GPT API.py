import openai
openai.api_key_path = open("kapil_api_key.txt", "r").read().strip("\n")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": "What is the distance between sun and moon?"}]
)
kapil_message= []
kapil_input= input(":")
print("User_input:", kapil_input )

kapil_message.append({"role":"users", "content":"kapil_input"})
completion = openai.ChatCompletion.create(cdcd
  model="gpt-3.5-turbo",
  messages=kapil_message
)

reply_content = completion.choices[0].message.content
print(reply_content)