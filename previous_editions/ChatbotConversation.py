import openai
openai.api_key = "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"

messages = []
system_msg = input("Hi, I'm a chatbot built to assist you on investment options. What is your name?\n")
messages.append({"role": "system", "content": system_msg})

print("Hi,", system_msg, " How can I help you today?")
while input!= "quit()":
    message = input("")
    messages.append({"role": "user", "content": message})
    response = openai.completions.create(
        model="gpt-4-1106-preview",
        prompt=messages,
        max_tokens=150,
        temperature=0.7 
        )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n") 