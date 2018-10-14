import re

print("Our Magical Calculator")
print("---------------------------------------")
print("Type 'Quit' for exit \n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
       equation = input("Enter your Equation : ")
    else:
        equation=input(previous)


    if equation == 'quit' or equation == 'Quit':
        print("Goodbye, Human ")
        run = False
    else:
        equation = re.sub('[a-zA-z.:,()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)



while run:
    performMath()
