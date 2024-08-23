import streamlit as st

def generate_specific_response(age, relationship_status, children, risk_preference):
    responses = {
        ("below 30", "Single", "No", "High Risk"): "Consider aggressive growth stocks, tech startups, or cryptocurrency investments.",
        ("below 30", "Single", "No", "Low Risk"): "Focus on low-risk, long-term investments like index funds or blue-chip stocks.",
        ("below 30", "Single", "Yes", "High Risk"): "Explore balanced mutual funds with a mix of stocks and bonds, suitable for a young single parent.",
        ("below 30", "Single", "Yes", "Low Risk"): "Secure investments like government bonds or high-grade corporate bonds are recommended for stability.",
        ("below 30", "In Relationship", "No", "High Risk"): "Joint investment in high-risk ventures like startups or real estate could be exciting.",
        ("below 30", "In Relationship", "No", "Low Risk"): "Consider joint savings accounts or low-risk mutual funds for shared financial growth.",
        ("below 30", "In Relationship", "Yes", "High Risk"): "Jointly explore diverse investment options, balancing risk with family needs.",
        ("below 30", "In Relationship", "Yes", "Low Risk"): "Joint low-risk investments like government bonds or conservative mutual funds are advisable.",
        ("below 30", "Married", "No", "High Risk"): "As a young couple, you might explore stock market trading or high-yield bonds.",
        ("below 30", "Married", "No", "Low Risk"): "Consider long-term, stable investments like real estate or joint savings plans.",
        ("below 30", "Married", "Yes", "High Risk"): "Balance high-risk opportunities like commodities trading with the need for family security.",
        ("below 30", "Married", "Yes", "Low Risk"): "Family-focused investments in education savings or health insurance plans are recommended.",
        ("below 30", "Divorced", "No", "High Risk"): "Post-divorce, you might consider revitalizing your portfolio with high-risk, high-reward stocks.",
        ("below 30", "Divorced", "No", "Low Risk"): "Focus on rebuilding with stable investments like bonds or dividend stocks.",
        ("below 30", "Divorced", "Yes", "High Risk"): "Carefully consider balancing risk with the need to provide for your children.",
        ("below 30", "Divorced", "Yes", "Low Risk"): "Prioritize secure, low-risk investments to ensure financial stability for your family.",
        ("30 or above", "Single", "No", "High Risk"): "Diversify with high-risk investments like emerging market stocks or venture capital.",
        ("30 or above", "Single", "No", "Low Risk"): "Prioritize capital preservation with investments in government securities or corporate bonds.",
        ("30 or above", "Single", "Yes", "High Risk"): "Balance high-risk investments with the need for stable returns for your child's future.",
        ("30 or above", "Single", "Yes", "Low Risk"): "Focus on secure, long-term investments like education savings plans or life insurance.",
        ("30 or above", "In Relationship", "No", "High Risk"): "Consider shared high-risk investments like joint business ventures or property development.",
        ("30 or above", "In Relationship", "No", "Low Risk"): "Joint low-risk investments like fixed deposits or joint real estate can be beneficial.",
        ("30 or above", "In Relationship", "Yes", "High Risk"): "Explore balanced portfolios, mixing high-risk options with stable investments for family security.",
        ("30 or above", "In Relationship", "Yes", "Low Risk"): "Prioritize family security with low-risk investments like education funds or health insurance.",
        ("30 or above", "Married", "No", "High Risk"): "As a mature couple, consider investing in high-risk markets or international funds for diversification.",
        ("30 or above", "Married", "No", "Low Risk"): "Explore stable and secure investment options like retirement funds or joint property ownership.",
        ("30 or above", "Married", "Yes", "High Risk"): "Consider a balanced approach with some high-risk investments alongside college funds or retirement savings.",
        ("30 or above", "Married", "Yes", "Low Risk"): "Focus on secure, family-oriented investments like life insurance, health plans, or low-risk mutual funds.",
        ("30 or above", "Divorced", "No", "High Risk"): "Explore new investment opportunities in high-risk areas like tech startups or foreign exchange.",
        ("30 or above", "Divorced", "No", "Low Risk"): "Rebuild your financial stability with low-risk investments like government bonds or dividend-yielding stocks.",
        ("30 or above", "Divorced", "Yes", "High Risk"): "Consider balanced investment strategies that offer growth while securing your children's future.",
        ("30 or above", "Divorced", "Yes", "Low Risk"): "Prioritize stable and low-risk investment avenues to ensure a secure financial future for your family."
    }

    age_key = "below 30" if int(age) < 30 else "30 or above"
    key = (age_key, relationship_status, children, risk_preference)

    return responses.get(key, "No specific advice available for this combination.")

st.title("Investment and Financial Expert Assistant")

def handle_submit():
    if age and relationship_status and children and risk_preference:
        st.session_state.show_response = True
        st.session_state.response = generate_specific_response(age, relationship_status, children, risk_preference)
    else:
        st.error("Please answer all the questions.")

if 'show_response' not in st.session_state:
    st.session_state.show_response = False
    st.session_state.response = ""

if not st.session_state.show_response:
    st.header("Investment Option Personalization Questionnaire")
    age = st.text_input("What is your age:")
    relationship_status = st.selectbox("What is your relationship status", ['Single', 'In Relationship', 'Married', 'Divorced'])
    children = st.radio("Do you have children:", ['Yes', 'No'])
    risk_preference = st.radio("Are you interested in high risk or low risk options:", ['High Risk', 'Low Risk'])
    
    submit_button = st.button('Submit Questionnaire', on_click=handle_submit)

if st.session_state.show_response:
    st.header("Personalized Investment Advice")
    st.write(st.session_state.response)