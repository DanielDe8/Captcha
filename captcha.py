import random

code = ""
code2 = ""
o = True


abc = "abcdefghijklmnopqwxyz"
ABC = abc.upper()
num = "1234567890"
codes = []

while True:
    while o:
        code = ""
        for i in range(0, 5):
            x = random.randint(1, 3)

            if x == 1:
                code += random.choice(abc)
            if x == 2:
                code += random.choice(ABC)
            if x == 3:
                code += random.choice(num)
        print(code)
        code2 = input()
        if code == code2:
            o = False
            codes.append(code)
            print(f"Generated codes: {codes}.")
        else:
            print("Sorry. Try again")
            print("")

            codes.append(code)
        
