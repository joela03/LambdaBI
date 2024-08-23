import streamlit as st
import openai
from openai import OpenAI

client = OpenAI(api_key="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")

investment_options = {
    "Stocks and shares": {
        "Advantages": [
            "Potential for significant long-term profitability",
            "Tax-free returns (capital gains, dividend, and income tax)",
            "High return potential",
            "Lots of investment options available",
            "Very accessible with online trading platforms",
            "Considered liquid investments"
        ],
        "Disadvantages": [
            "Market volatility leading to potential losses",
            "Various fees and charges (exit, management, platform)",
            "No guaranteed returns",
            "Requires time, research, and market understanding"
        ]
    },
    "Bonds": {
        "Advantages": [
            "Regular fixed interest payments",
            "Considered less risky",
            "Variety of bond types available",
            "Experienced fund managers available"
        ],
        "Disadvantages": [
            "Bond prices fluctuate with interest rate changes",
            "Impact of inflation on bond prices",
            "Risk of issuer's ability to repay debt",
            "Low liquidity in some bonds"
        ]
    },
    "Savings account": {
        "Advantages": [
            "High level of security",
            "Easy access to funds",
            "Interest rates offered",
            "Generally low risk"
        ],
        "Disadvantages": [
            "Low returns compared to other investments",
            "Fluctuating interest rates",
            "Minimum balance requirements or fees",
            "Risk of savings losing value against inflation"
        ]
    },
    "ISA": {
        "Advantages": [
            "Tax-free incomes and gains",
            "Large flexibility in types of ISAs",
            "Annual investment cap with flexibility to spread across ISAs",
            "Easily accessible"
        ],
        "Disadvantages": [
            "Lower interest rates",
            "Risk tied to stock market performance",
            "Withdrawal restrictions on some ISAs"
        ]
    },
    "Real estate": {
        "Advantages": [
            "Potential long-term appreciation",
            "Regular rental income",
            "Diversification of investment portfolios",
            "Tax benefits"
        ],
        "Disadvantages": [
            "High level of barrier to entry",
            "High transactions and management costs",
            "Market and economic factors impact value",
            "Low liquidity"
        ]
    },
    "Pension funds": {
        "Advantages": [
            "Tax benefits",
            "Flexibility and portability",
            "Employer contributions (in some cases)"
        ],
        "Disadvantages": [
            "Market risk",
            "No guaranteed income",
            "Limited control over investment decisions"
        ]
    },
    "Foreign exchange": {
        "Advantages": [
            "Flexibility in investment amount",
            "High liquidity",
            "Various currency pairs to choose from",
            "Technical and fundamental analysis available"
        ],
        "Disadvantages": [
            "High volatility",
            "Lack of regulation",
            "Sensitivity to geopolitics"
        ]
    }
}


# Function to generate a response using OpenAI
def generate_response(user_name, user_questions, user_context):
    messages = [
        {"role": "system", "content": "You are a financial expert."},
    ]
    
    # Include the financial context in the messages
    messages.append({"role": "system", "content": "User Financial Context:"})
    messages.append({"role": "user", "content": user_context})
    
    for question in user_questions:
        messages.append({"role": "user", "content": question})

    full_prompt = f"{user_name} is asking:\n\nUser Context:\n{user_context}. The investment options you can advise them on are: Stocks and Shares, Bonds, Real Estate, Savings Accounts, ISAs, Pension Funds and Forex. Read the information below and use it to inform them about the option that best suits their user profile: :\n{investment_options}."
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=200,
        temperature=0.5,
    )

    # Access the content of the bot's response
    bot_response = response.choices[0].message.content

    return bot_response


# Layout of the Streamlit page
st.title("Investment and Financial Expert Assistant")

# Initialize session state variables
if 'page' not in st.session_state:
    st.session_state.page = 1
if 'user_context' not in st.session_state:
    st.session_state.user_context = {}
if 'chat_log' not in st.session_state:
    st.session_state.chat_log = []
if 'user_question' not in st.session_state:
    st.session_state.user_question = ""

# Function to handle personal details submission
def handle_personal_details_submit():
    user_context = {
        "name": user_name,
        "age": age,
        "gender": gender,
        "relationship_status": relationship_status
    }
    st.session_state.user_context.update(user_context)
    st.session_state.page = 2

# Function to handle financial questionnaire submission
def handle_financial_questionnaire_submit():
    financial_context = {
        "income": income,
        "additional_income": additional_income,
        "expenses": expenses,
        "investment_length": investment_length,
        "investment_knowledge": investment_knowledge,
        "investment_balance": investment_balance,
        "financial_goals": financial_goals,
        "higher_returns_for_risk": higher_returns_for_risk,
        "resist_urge_to_panic_sell": resist_urge_to_panic_sell,
        "afford_to_lose_investment": afford_to_lose_investment,
        "willing_to_pay_fee": willing_to_pay_fee,
        "emergency_fund": emergency_fund,
        "pension_scheme": pension_scheme
    }
    st.session_state.user_context.update(financial_context)
    st.session_state.page = 3  # Proceed to the Chatbot Page

# Function to handle chatbot submission
def handle_chatbot_submit():
    user_question = st.session_state.user_question
    if user_question:
        st.session_state.chat_log.append(f"You: {user_question}")
        user_context_dict = st.session_state.user_context
        user_context_string = '\n'.join(f"{key}: {value}" for key, value in user_context_dict.items())
        response_text = generate_response(st.session_state.user_context["name"], [user_question], user_context_string)
        st.session_state.chat_log.append(f"Bot: {response_text}")
        st.session_state.user_question = ""  # Clear the input field after submission

# Function to check if all required inputs on the Financial Questionnaire Page are filled
def all_inputs_filled_on_financial_page():
    return (income is not None and
            additional_income is not None and
            expenses is not None and
            investment_length is not None and
            investment_knowledge is not None and
            investment_balance is not None and
            financial_goals is not None and
            higher_returns_for_risk is not None and
            resist_urge_to_panic_sell is not None and
            afford_to_lose_investment is not None and
            willing_to_pay_fee is not None and
            emergency_fund is not None and
            pension_scheme is not None)

# Personal Details and Personal Questions Page
if st.session_state.page == 1:
    st.header("Personal Details and Questions")
    user_name = st.text_input("What's your name?")
    age = st.text_input("What is your age?")
    gender = st.radio("Gender:", ['Male', 'Female', 'Other'])
    relationship_status = st.selectbox("Marital status:", ['Single', 'Married', 'Divorced', 'Widowed', 'Other'])
    if st.button('Next', key='next_personal'):
        handle_personal_details_submit()

# Financial Questionnaire Page
elif st.session_state.page == 2:
    st.header("Financial Questionnaire")
    income = st.select_slider("Choose your annual income range:", options=['Under £20,000', '£20,000-£40,000', '£40,000-£60,000', '£60,000-£80,000', 'Above £80,000'])
    additional_income = st.radio("Do you have additional income:", ['Yes', 'No'])
    expenses = st.select_slider("Choose your monthly expenses range:", options=['Under £1,000', '£1,000-£2,000', 'Above £2,000'])
    investment_length = st.select_slider("How long do you want to commit to this goal?", options=['Less than 5 years', '5-10 years', '10-20 years', '20-30 years', 'above 30 years'])
    investment_knowledge = st.radio("How familiar are you with different investment options?", ['Not familiar', 'Somewhat familiar', 'Very familiar'])
    investment_balance = st.text_input("How much are you wanting to invest?", key="Investment_balance_input")
    financial_goals = st.multiselect("What type of financial goals do you have? Select all that apply", ['Vacation', 'Home improvement', 'Education', 'Home purchase', 'Retirement', 'Wealth accumulation', 'Other'])
    higher_returns_for_risk = st.radio("Do you want to try for higher returns compared to if you'd left your money in cash, despite the risks involved?", ['Yes', 'No'])
    resist_urge_to_panic_sell = st.radio("Can you resist the urge to panic and sell your investment if it falls below what you paid for it?", ['Yes', 'No'])
    afford_to_lose_investment = st.radio("Can you afford to lose part of your investment?", ['Yes', 'No'])
    willing_to_pay_fee = st.radio("Are you willing to pay a fee for your investment?", ['Yes', 'No', 'Depends on the price'])
    emergency_fund = st.radio("Do you have an emergency fund in place?", ['Yes', 'No'])
    pension_scheme = st.radio("Have you got a Pension scheme in place?", ['Yes', 'No'])

    if st.button('Next', key='next_financial') and all_inputs_filled_on_financial_page():
        handle_financial_questionnaire_submit()

# Chatbot Page
elif st.session_state.page == 3:
    st.header("Financial Expert Chat Assistant")
    st.write(f"Hello, {st.session_state.user_context['name']}. I'm here to assist you with financial questions.")

    chat_log_display = "\n\n".join(st.session_state.chat_log)
    st.markdown(chat_log_display, unsafe_allow_html=True)

    st.session_state.user_question = st.text_input("Ask your financial question:", key="question_input", value=st.session_state.user_question)

    if st.button('Submit Question', key='submit_question_chat', on_click=handle_chatbot_submit):
        pass  # The handle_chatbot_submit function is called when the button is clicked
