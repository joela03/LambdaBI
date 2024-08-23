

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn import tree


def get_yes_no_input(prompt):
    """Helper function to get a valid 'Yes' or 'No' input from the user."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ["yes", "no"]:
            return answer

        print("Invalid input. Please enter 'Yes' or 'No'.")


def calc_risk_level():
    """Calculate's the risk level of a user based on their answer to the psychological questionnaire"""
    RiskLevel = 0

    psych_1 = get_yes_no_input(
        "Would you panic if your investment fell in value every now and then? (Yes/No): ")
    psych_2 = get_yes_no_input(
        "Can you resist the urge to panic and sell your investment if it falls below what you paid for it? (Yes/No): ")
    psych_3 = get_yes_no_input(
        "Do you invest without thoroughly analyzing your options? (Yes/No): ")
    psych_4 = get_yes_no_input(
        "Are you quick to make investment decisions without careful consideration? (Yes/No): ")
    psych_5 = get_yes_no_input(
        "Do you frequently have rapid and disorganized thoughts about your investment choices? (Yes/No): ")
    psych_6 = get_yes_no_input(
        "Do you plan and prepare for investment opportunities well in advance? (Yes/No): ")
    psych_7 = get_yes_no_input(
        "Are you disciplined and self-controlled in your investment decisions? (Yes/No): ")
    psych_8 = get_yes_no_input(
        "Can you easily focus and concentrate on managing your investments? (Yes/No): ")
    psych_9 = get_yes_no_input(
        "Do you consistently save and allocate resources for future investment needs? (Yes/No): ")

    for answer in [psych_1, psych_2, psych_3, psych_4, psych_5, psych_6, psych_7, psych_8, psych_9]:
        if answer.lower() not in ["yes", "no"]:
            raise ValueError("Input must be 'Yes' or 'No'")

    for i in [psych_1, psych_4, psych_5, psych_9]:
        if i.lower() == "no":
            RiskLevel += 1
    for i in [psych_2, psych_3, psych_6, psych_7, psych_8]:
        if i.lower() == "yes":
            RiskLevel += 1

    if RiskLevel in [8, 9, 7]:
        return 3
    elif RiskLevel in [6, 5]:
        return 2
    elif RiskLevel in [4, 3]:
        return 1
    elif RiskLevel in [2, 1]:
        return 0


def calc_return_level():
    """Calculate's the return level that the customer would prefer"""

    valid_options = ["A", "B", "C", "D"]

    while True:
        ReturnLevel = input(
            "Do you want to try for higher returns compared to if you'd left your money in cash, despite the risks involved? (A: Strong Yes, B: Yes, C: No, D: Strong No): ")

        if ReturnLevel in valid_options:
            if ReturnLevel == "Yes":
                return 3
            elif ReturnLevel == "Strong Yes":
                return 2
            elif ReturnLevel == "Strong No":
                return 1
            else:
                return 0

        else:
            print("Invalid input. Please choose from A, B, C or D")


def calc_cap_and_fees():
    """Calculate's the cap and fees for the user"""
    valid_options = ['A', 'B', 'C', 'D', 'E']

    while True:
        answer = input(
            "Choose your annual income range (A: Under £20,000, B: £20,000-£40,000, C: £40,000-£60,000, D: £60,000-£80,000, E: Above £80,000): ")

        if answer in valid_options:
            if answer in ['A', 'B']:
                Cap = 1
                Fees = 0
            else:
                Cap = 0
                Fees = 1

            return {"Cap": Cap, "Fees": Fees}
        else:
            print("Invalid input. Please choose A, B, C, D or E.")


def calc_term_length():
    """Calculate's the preferred term length of a customer"""
    valid_options = ['A', 'B', 'C', 'D', 'E']
    while True:
        answer = input(
            "How long do you want to commit to this goal? (A: Less than 5 years, B: 5-10 years, C: 10-20 years D: 20-30 years, E: above 30 years): ")

        if answer in valid_options:
            if answer in ['A', 'B']:
                return 0
            else:
                return 1

        else:
            print("Invalid input. Please choose from A, B, C, D or E.")


def calc_ease_of_use():
    """Calculate's the ease of use level for the customer"""
    valid_options = ['A', 'B', 'C']

    while True:
        answer = input(
            "How familiar are you with different investment options? A: Not familiar, B: Somewhat familiar, C: Very familiar ")

        if answer in valid_options:
            if answer == "A":
                return 0
            elif answer == "B":
                return 2
            else:
                return 1

        else:
            print("Invalid input. Please choose from A, B or C")


def create_dataframe():
    """Create's a dataframe that we can use for our decision tree"""

    investment_options = [
        ["Stocks and Shares", 8, None, None, "LT", "Not familiar", "Y"],
        ["Bonds", 5, "Yes", None, "LT", "Somewhat familiar", "Y"],
        ["Real Estate", 4, "Strong Yes", None, "LT", "Somewhat familiar", "Y"],
        ["Savings Accounts", 2, "Strong No", None, "ST", "Very familiar", "N"],
        ["ISAs", 2, "No", "£20,000", ["LT", "ST"], "Very familiar", "N"],
        ["Pension Funds", 2, "Strong Yes", None, "LT", "Very familiar", "Y"],
        ["Forex", 9, None, None, "ST", "Somewhat familiar", "Y"]
    ]

    columns = ['InvestmentOption', 'RiskLevel', 'ReturnLevel',
               'Cap', 'TermLength', 'EaseToUse', 'Fees']

    return pd.DataFrame(investment_options, columns=columns)


def encode_dataframe(df):
    """Encoding dataframe values so we can implement the decision tree"""

    le = LabelEncoder()

    # Encode categorical variables
    df['RiskLevel_n'] = le.fit_transform(df['RiskLevel'])
    df['ReturnLevel_n'] = le.fit_transform(df['ReturnLevel'])
    df['Cap_n'] = le.fit_transform(df['Cap'])

    # Flatten lists in the TermLength column and then encode
    df['TermLength_n'] = df['TermLength'].apply(
        lambda x: ', '.join(x) if isinstance(x, list) else x)
    df['TermLength_n'] = le.fit_transform(df['TermLength_n'])

    df['EaseToUse_n'] = le.fit_transform(df['EaseToUse'])
    df['Fees_n'] = le.fit_transform(df['Fees'])

    return df


def decision_tree(df):

    inputs_n = df.drop(['InvestmentOption', 'RiskLevel', 'ReturnLevel',
                        'Cap', 'TermLength', 'EaseToUse', 'Fees'], axis=1)

    target = df['InvestmentOption']

    model = tree.DecisionTreeClassifier()
    model.fit(inputs_n, target)

    params = [[RiskLeveln, ReturnLeveln, Capn, TermLengthn, Easetousen, Feesn]]
    prediction = model.predict(params)

    return prediction


if __name__ == "__main__":
    RiskLeveln = calc_risk_level()
    ReturnLeveln = calc_return_level()
    output = calc_cap_and_fees()
    Feesn = output["Fees"]
    Capn = output["Cap"]
    TermLengthn = calc_term_length()
    Easetousen = calc_ease_of_use()
    df = create_dataframe()
    encoded_df = encode_dataframe(df)
    decision_tree_output = decision_tree(encoded_df)

    print(decision_tree_output)
