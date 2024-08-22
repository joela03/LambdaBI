import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn import tree


def calc_risk_level():

    RiskLevel = 0

    psych_1 = input(
        "Would you panic if your investment fell in value every now and then? (Yes/No): ")
    psych_2 = input(
        "Can you resist the urge to panic and sell your investment if it falls below what you paid for it? (Yes/No): ")
    psych_3 = input(
        "Do you invest without thoroughly analyzing your options? (Yes/No): ")
    psych_4 = input(
        "Are you quick to make investment decisions without careful consideration? (Yes/No): ")
    psych_5 = input(
        "Do you frequently have rapid and disorganized thoughts about your investment choices? (Yes/No): ")
    psych_6 = input(
        "Do you plan and prepare for investment opportunities well in advance? (Yes/No): ")
    psych_7 = input(
        "Are you disciplined and self-controlled in your investment decisions? (Yes/No): ")
    psych_8 = input(
        "Can you easily focus and concentrate on managing your investments? (Yes/No): ")
    psych_9 = input(
        "Do you consistently save and allocate resources for future investment needs? (Yes/No): ")

    for answer in [psych_1, psych_2, psych_3, psych_4, psych_5, psych_6, psych_7, psych_8, psych_9]:
        if answer not in ["Yes", "No", "yes", "no"]:
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
    ReturnLevel = input(
        "Do you want to try for higher returns compared to if you'd left your money in cash, despite the risks involved? (Strong Yes/Yes/No/Strong No): ")

    if ReturnLevel == "Yes":
        return 3
    elif ReturnLevel == "Strong Yes":
        return 2
    elif ReturnLevel == "Strong No":
        return 1
    else:
        return 0


def fees():
    Fees = []
    Cap = input(
        "Choose your annual income range (Under £20,000/£20,000-£40,000/£40,000-£60,000/£60,000-£80,000/Above £80,000): ")
    if Cap in ['Under £20,000', '£20,000-£40,000']:
        Cap = 'N/A'
        Fees = 'N'
    else:
        Cap = '20000'
        Fees = 'Y'

    return {"Cap": Cap, "Return_Level": ReturnLevel, "Fees": Fees}


# Calculating TermLength
TermLength = input(
    "How long do you want to commit to this goal? (A: Less than 5 years, B: 5-10 years, C: 10-20 years D: 20-30 years, E: above 30 years): ")

if TermLength in ['Less than 5 years', '5-10 years']:
    TermLength = 'LT'
else:
    TermLength = 'ST'

# Calculating Easetouse
Easetouse = input(
    "How familiar are you with different investment options? (Not familiar/Somewhat familiar/Very familiar): ")

RiskLeveln = 0
ReturnLeveln = 0
Capn = 0
TermLengthn = 0
Easetousen = 0
Feesn = 0

# Manually encoding parameters so that they can be used in the decision tree
if RiskLevel in [8, 9, 7]:
    RiskLeveln = 3
elif RiskLevel in [6, 5]:
    RiskLeveln = 2
elif RiskLevel in [4, 3]:
    RiskLeveln = 1
elif RiskLevel in [2, 1]:
    RiskLeveln = 0

if ReturnLevel == "Yes":
    ReturnLeveln = 3
elif ReturnLevel == "Strong Yes":
    ReturnLeveln = 2
elif ReturnLevel == "Strong No":
    ReturnLeveln = 1
else:
    ReturnLeveln = 0

if Cap == "N/A":
    Capn = 1
else:
    Capn = 0

if Easetouse == "Not familiar":
    Easetousen = 0
elif Easetouse == "Somewhat familiar":
    Easetousen = 2
else:
    Easetousen = 1

if Fees == "Y":
    Feesn = 1
else:
    Feesn = 0


# Visually dispalying paramaters to check
print("RiskLevel:", RiskLevel)
print("ReturnLevel:", ReturnLevel)
print("Cap:", Cap)
print("TermLength:", TermLength)
print("Easetouse:", Easetouse)
print("Fees:", Fees)


# Research Team's table that has been manually inputted
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

# Converting table to dataframe so decision tree can manipulate it
df = pd.DataFrame(investment_options, columns=columns)

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

inputs_n = df.drop(['InvestmentOption', 'RiskLevel', 'ReturnLevel',
                   'Cap', 'TermLength', 'EaseToUse', 'Fees'], axis=1)

target = df['InvestmentOption']

# Calling decision tree
model = tree.DecisionTreeClassifier()
model.fit(inputs_n, target)

params = [[RiskLeveln, ReturnLeveln, Capn, TermLengthn, Easetousen, Feesn]]
prediction = model.predict(params)

print(prediction)

if __name__ == "__main__":
    RiskLeveln = calc_risk_level()
