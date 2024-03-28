RiskLevel = 0

psych_1 = input("Would you panic if your investment fell in value every now and then? (Yes/No): ")
psych_2 = input("Can you resist the urge to panic and sell your investment if it falls below what you paid for it? (Yes/No): ")
psych_3 = input("Do you invest without thoroughly analyzing your options? (Yes/No): ")
psych_4 = input("Are you quick to make investment decisions without careful consideration? (Yes/No): ")
psych_5 = input("Do you frequently have rapid and disorganized thoughts about your investment choices? (Yes/No): ")
psych_6 = input("Do you plan and prepare for investment opportunities well in advance? (Yes/No): ")
psych_7 = input("Are you disciplined and self-controlled in your investment decisions? (Yes/No): ")
psych_8 = input("Can you easily focus and concentrate on managing your investments? (Yes/No): ")
psych_9 = input("Do you consistently save and allocate resources for future investment needs? (Yes/No): ")

psych_1 = psych_1.lower()
psych_2 = psych_2.lower()
psych_3 = psych_3.lower()
psych_4 = psych_4.lower()
psych_5 = psych_5.lower()
psych_6 = psych_6.lower()
psych_7 = psych_7.lower()
psych_8 = psych_8.lower()
psych_9 = psych_9.lower()

if psych_1 == 'no':
    RiskLevel += 1
if psych_2 == 'yes':
    RiskLevel += 1
if psych_3 == 'yes':
    RiskLevel += 1
if psych_4 == 'no':
    RiskLevel += 1
if psych_5 == 'no':
    RiskLevel += 1
if psych_6 == 'yes':
    RiskLevel += 1
if psych_7 == 'yes':
    RiskLevel += 1
if psych_8 == 'yes':
    RiskLevel += 1
if psych_9 == 'no':
    RiskLevel += 1

print("Risk Level:", RiskLevel)