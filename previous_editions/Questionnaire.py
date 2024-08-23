import time

data = []
user_data = "Current data collected: \n"

print("Please answer the questions so I can personalize your investment option")
time.sleep(0.5)

valid_inputs = {'A', 'B', 'C', 'D'}

Con1 = input("What is your age: ")
data.append(Con1)

while True:
    Con2 = input("What is your relationship status (A, B, C, or D): ")
    if Con2.upper() in valid_inputs:
        data.append(Con2.upper())
        break
    else:
        print("INVALID: You must enter A, B, C, or D")
        print()

Con3 = input("Do you have children: ")
data.append(Con3)

while True:
    Con4 = input("Are you interested in high risk or low risk options (A, B): ")
    if Con4.upper() in {'A', 'B'}:
        data.append(Con4.upper())
        break
    else:
        print("INVALID: You must enter A or B")
        print()

print(data)