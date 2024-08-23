def generate_response(user_name, user_questions, user_context):
    messages = [
        {"role": "system", "content": "You are a financial expert."},
    ]

    # Include the financial context in the messages
    messages.append({"role": "system", "content": "User Financial Context:"})
    messages.append({"role": "user", "content": user_context})

    for question in user_questions:
        messages.append({"role": "user", "content": question})

    full_prompt = f"{user_name} is asking:\n\nUser Context:\n{
        user_context}. The investment options you can advise them on are: Stocks and Shares, Bonds, Real Estate, Savings Accounts, ISAs, Pension Funds and Forex. Read the information below and use it to inform them about the option that best suits their user profile: :\n{investment_options}."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=200,
        temperature=0.5,
    )

    # Access the content of the bot's response
    bot_response = response.choices[0].message.content

    return bot_response


if __name__ == "__main__":
    ...
