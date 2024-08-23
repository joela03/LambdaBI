import streamlit as st
import openai

def generate_response(user_name, user_question):
    openai.api_key = "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"
    full_prompt = f"{user_name} is asking: {user_question}"
    response = openai.completions.create(
        model="text-davinci-003",
        prompt=full_prompt,
        max_tokens=500,
        temperature=0.5,
    )
    return response.choices[0].text

st.title("Investment and Financial Expert Assistant")

def handle_submit():
    if age and relationship_status and children and risk_preference:
        st.session_state.show_chatbot = True
    else:
        st.error("Please answer all the questions.")

if 'show_chatbot' not in st.session_state:
    st.session_state.show_chatbot = False

if not st.session_state.show_chatbot:
    st.header("Investment Option Personalization Questionnaire")
    age = st.text_input("What is your age:")
    relationship_status = st.selectbox("What is your relationship status", ['Single', 'In Relationship', 'Married', 'Divorced'])
    children = st.radio("Do you have children:", ['Yes', 'No'])
    risk_preference = st.radio("Are you interested in high risk or low risk options:", ['High Risk', 'Low Risk'])
    
    submit_button = st.button('Submit Questionnaire', on_click=handle_submit)

if st.session_state.show_chatbot:
    st.header("Financial Expert Chat Assistant")
    st.write("Thank you for submitting the questionnaire. I'm here to assist you with financial questions. What's your name?")

    user_name = st.text_input("Your Name", key="name_input")
    user_question = st.text_input("Ask a financial question:", key="question_input")

    send_question_button = st.button('Send Question', key='send_question')
    if send_question_button:
        if user_name and user_question:
            with st.spinner('Generating response...'):
                try:
                    response_text = generate_response(user_name, user_question)
                    st.text_area("Response", value=response_text, height=200, disabled=True)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.error("Please enter your name and a question to get a response.")


