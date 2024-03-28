import streamlit as st
import openai

def generate_response(user_name, user_questions, user_context):
    openai.api_key = "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"  
    full_conversation = '\n'.join(user_questions)
    full_prompt = f"{user_name} is asking: {full_conversation}\n\nUser Context:\n{user_context}"
    response = openai.completions.create(
        model="text-davinci-003",
        prompt=full_prompt,
        max_tokens=200,
        temperature=0.5,
    )
    return response.choices[0].text

st.title("Investment and Financial Expert Assistant")

if 'page' not in st.session_state:
    st.session_state.page = 1
if 'user_context' not in st.session_state:
    st.session_state.user_context = {}
if 'chat_log' not in st.session_state:
    st.session_state.chat_log = []
if 'user_question' not in st.session_state:
    st.session_state.user_question = ""

def handle_personal_details_submit():
    user_context = {
        "name": user_name,
        "age": age,
        "gender": gender,
        "relationship_status": relationship_status
    }
    st.session_state.user_context.update(user_context)
    st.session_state.page = 2

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
    st.session_state.page = 3

def handle_chatbot_submit():
    user_question = st.session_state.user_question
    if user_question:
        st.session_state.chat_log.append(f" {st.session_state.user_context['name']}: {user_question}")
        user_context_string = '\n'.join(f"{key}: {value}" for key, value in st.session_state.user_context.items())
        response_text = generate_response(st.session_state.user_context["name"], [user_question], user_context_string)
        st.session_state.chat_log.append(f"Bob The Bot: {response_text}")
        

if st.session_state.page == 1:
    st.header("Personal Details and Questions")
    user_name = st.text_input("What's your name?")
    age = st.text_input("What is your age?")
    gender = st.radio("Gender:", ['Male', 'Female', 'Other'])
    relationship_status = st.selectbox("Marital status:", ['Single', 'Married', 'Divorced', 'Widowed', 'Other'])
    if st.button('Next', key='next_personal'):
        handle_personal_details_submit()

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
    
    if st.button('Next', key='next_financial'):
        handle_financial_questionnaire_submit()

elif st.session_state.page == 3:
    st.header("Financial Expert Chat Assistant")
    st.write(f"Hello, {st.session_state.user_context['name']}. I'm here to assist you with financial questions.")

    chat_log_display = "\n\n".join(st.session_state.chat_log)
    st.markdown(chat_log_display, unsafe_allow_html=True)

    st.session_state.user_question = st.text_input("Ask your financial question:", key="question_input", value=st.session_state.user_question)

    if st.button('Submit Question', key='submit_question', on_click=handle_chatbot_submit):
        pass 
