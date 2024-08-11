#A mini terminal with commands decided by me
from datetime import datetime
import math
import turtle
import random
print("Welcome to the terminal made by Atharv Sharma")
login = str(input("Enter your password: "))
count = 0
if login == "thedevz29isdeveloper":
    print("TERMINAL UNLOCKED!")
    while True:
        c = str(input("##> "))
        if c == "print()":
            x = input("What do you want to print?  : ")
            print(x)
        elif c == "prtadmin()":
            print("The owner and administrator of this system is Atharv Sharma")
        elif c == "thedevz29()":
            print("oh its u thedevz29") 
        elif c == "exit()":
            print("OK")
            break
        elif c== "sum()":
            num1 = float(input("Enter the first number to add: "))
            num2 = float(input("Enter the second number to add: "))
            print("The sum is",num1+num2)
        elif c == "diff()":    
            a = float(input ("Please enter the first number : "))
            b = float(input("Please ener the second number : "))
            if a == b :
                print (a-b)
            elif a < b :
                print (a-b)
            else :
                print (a-b)     
        elif c == "multiply()":
            a = float(input ("Please enter the first number : "))
            b = float(input("Please ener the second number : "))
            if a == b :
                print (a*b)
            elif a < b :
                print (a*b)
            else :
                print (a*b)
        elif c == "divide()":
            a = float(input ("Please enter the first number : "))
            b = float(input("Please ener the second number : "))
            if a == b :
                print (a/b)
            elif a < b :
                print (a/b)
            else :
                print(a/b)
        elif c == "calcpower()":
            base = int(input("Enter the base of the exponent: "))
            power = int(input("Enter the power of the exponent: "))
            print("The answer is", base**power)
        elif c == "opfun()":
            print("This is a fun command. Just for fun LOL!!")
        elif c == "countstrlen()":
            str = str(input("Enter the string to count the length : "))
            print("The length of this string is", len(str),"characters")
        elif c == "currenttime()":
            time = datetime.now()
            current_time = time.strftime('%H:%M:%S')
            print('Current Time is:', current_time)
            print('Current Date and Time is:', time)
        elif c == "factorial()":
            factorial = int(input("Enter the number to calculate factorial of: "))
            print(math.factorial(factorial))
        elif c == "countnumlen()":
            num3 = int(input("Enter the number to count the length of: "))
            num3 = str(num3)
            print("The length of the number is: ",len(str(num3)))
        elif c == "correctthespelling":
            print("Welcome to the game developed by thedevz29 \n Here you have to correct the spellings of the word given in wrong spelling")
            print("Lets start")
            score = 0
            count = 0
            print("LEVEL 1")
            print("Your word is 'Simpathy' ")
            word1  = str(input("Enter the correct spelling:  "))
            if word1.lower() == "sympathy":
                print("CORRECT!!!!!!!!!!!!!!!!!!!!!")
                count += 1
                score += 10
                print("You have", count, "correct answers")
            else:
                print("WRONG!")
                

            print("LEVEL 2")
            print("Your word is 'Sustainible' ")
            word2  = str(input("Enter the correct spelling:  "))
            if word2.lower() == "sustainable": 
                print("CORRECT!!!!!!!!!!!!!!!!!!!!!")
                count += 1
                score += 10
                print("You have", count, "correct answers")
            else:
                print("WRONG!")
                
            print("LEVEL 3")
            print("Your word is 'Incarnete' ")
            word3  = str(input("Enter the correct spelling:  "))
            if word3.lower() == "incarnate":
                print("CORRECT!!!!!!!!!!!!!!!!!!!!!!!!!")
                count += 1
                score += 10
                print("You have", count, "correct answers")
            else:
                print("WRONG!")


            print("LEVEL 4")
            print("Your word is 'Nauseos' ")
            word4 = str(input("Enter the correct spelling:  "))
            if word4.lower() == "nauseous":
                print("CORRECT!!!!!!!!!!!!!")
                count += 1
                score += 10
                print("You have", count, "correct answers")
            else:
                print("WRONG!")


            print("LEVEL 5")
            print("Your word is 'Fushia'")
            word5 = str(input("Enter the correct spelling: "))
            if word5.lower() == "fuchia":
                print("CORRECT!!!!!!!!")
                count += 1
                score += 10
                print("You have", count, "correct answers")
            else:
                print("WRONG!")


            print("LEVEL 6")
            print("Your word is 'envioroment' ")
            word6 = str(input("Enter the correct spelling: "))
            if word6.lower() == 'environment':
                print("CORRECT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                count += 1
                score += 10
                print("You have", count, "correct answers")
            else:
                print("WRONG:")

            print("LEVEL 7")
            print("Your word is 'mathemetics'")
            word7 = str(input("Enter the correct spelling: "))
            if word6.lower() == "mathematics":
                print("CORRECT!!!!!!!!!!!!!!!!!")
                count += 1
                score += 10
                print("You have",count,"correct answers")
            else:
                print("WRONG!")
                
            print("LEVEL 8")
            print("Your word is 'missisipi' ")
            word8 = str(input("Enter the correct spelling: "))
            if word8.lower() == "missisippi":
                print("CORRECT!!!!")
                count += 1
                score += 10
                print("You have",count,"correct answers")
            else:
                print("WRONG!")

            print("LEVEL 9")
            print("Your word is 'watermalon'")
            word9 = str(input("Enter the correct spelling"))
            if word9.lower() == "watermelon":
                print("CORRECT!!!!!")
                count += 1
                score +=10
                print("You have",count,"correct answers")
            else:
                print("WRONG!")

            print("LEVEL 10")
            print("Your word is'abrogete'")
            word10 = str(input("Enter the correct spelling: "))
            if word10.lower() == "abrogate":
                print("CORRECT!!!!")
                count += 1
                score += 10
                print("You have", count,"correct answers")
            else:
                print("WRONG!")

            print("Your final score is", score)
            print("Your correct answers are", count)
        elif c == "guesstheword()":
            print("WELCOME TO MY GAME")
            print("Your have to type the correct word which has blanks in it: ")
            print("LETS START")

            score = 0
            count = 0
            print("LEVEL 1")
            print("YOUR WORD IS m_n_fe_t")
            lvl1 = str(input("Enter the word: "))
            if lvl1.lower() == "manifest":
                print("CORRECT")
                score += 10
                count += 1
                print("You got",count,"correct answers")
            else:
                print("WRONG!")

            print("LEVEL 2")
            print("Your word is'm_s_i_si__i'")
            lvl2 = str(input("Enter the word: "))
            if lvl2.lower() == "missisippi":
                print("CORRECT!")
                score+=10
                count+=1
                print("Your got",count,"correct answers")
            else:
                print("WRONG")

            print("LEVEL 3")
            print("Your word is p_o_gr_m_i_g")
            lvl3 = str(input("Enter the word: "))
            if lvl3.lower() == "programming":
                print("CORRECT!")
                score += 10
                count += 1
                print("You have", count,"correct answers")
            else:
                print("WRONG!")
                
            print("LEVEL 4")
            print("Your word is no__a_gi_")
            lvl4 = str(input("Enter the word: "))
            if lvl4.lower() == "nostalgia":
                print("CORRECT!")
                score += 10
                count += 1
                print("You have",count,"correct answers")
            else:
                print("WRONG")

            print("LEVEL 5")
            print("Your word is li__te_an_")
            lvl5 = str(input("Enter the word: "))
            if lvl5.lower == "lieutenant":
                print("CORRECT!")
                score += 10
                count += 1
                print("You have",count,"correct answers")
            else:
                print("Wrong")

            print("LEVEL 6")
            print("Your word is ma__a__re")
            lvl6 = str(input("Enter the word: "))
            if lvl6.lower() == "massacare":
                print("CORRECT!")
                score += 10
                count += 1
                print("You have",count,"correct answers")
            else:
                print("Wrong")

            print("LEVEL 7")
            print("Your word is s_p__m_")
            lvl7 = str(input("Enter the word: "))
            if lvl7.lower() == "supreme":
                print("CORRECT!")
                score += 10
                count += 1
                print("You have",count,"correct answers")
            else:
                print("Wrong")

            print("LEVEL 8")
            print("Your word is n_v_mb__")
            lvl8 = str(input("Enter the word: "))
            if lvl8.lower() == "november":
                print("CORRECT!")
                score += 10
                count += 1
                print("You have",count,"correct answers")
            else:
                print("Wrong")
            print("Your final score is", score)
            print("You have",count,"correct answers")
        elif c == "countdailyexpense()":
            miscellanios = float(input("Enter the miscellanios expense for the day: "))
            travel = float(input("Enter the travel expense for the day: "))
            food = float(input("Enter the food expense for the day: "))
            rent = float(input("Enter the rent expense for the day: "))
            saving = float (input("Enter the total saving for the day: "))
            total= "the total expense for the day is",miscellanios+travel+food+rent-saving
            print(total)
        elif c == "profalc()":
            product = input ("Please enter the name of your product : ")
            cp = float(input ("Please enter the cost price of your product (rs) : "))
            sp = float(input ("Please enter the selling price of your product (rs) : "))
            profit = cp-sp
            loss = sp-cp
            if cp < sp :
                print ("Your product", product, "is in", sp - cp, "rs profit")
                print ("Profit percentage: ",(cp/sp)*100,"%")
            elif cp > sp :
                print ("Your product", product, "is in", cp - sp, "rs loss")
                print("Loss percentage", (sp/cp)*100,"%")
            else :
                print ("Your product is in neither profit nor loss")
        elif c == "checkpalindrome()":
            var1 = str(input("Enter the string to check if it is palindrome or not: "))
            var2 = var1[::-1]
            print(var2)
            if var2 == var1:
                print("The string is palindrome")
            else:
                print("The string is not palindrome")
        elif c == "addstr()":
            str1 = input("Enter the first string: ")
            str2 = input("Enter the second string: ")
            print(str1+str2)
        elif c == "multiplystr()":
            str3 = input("Enter the string to repeat: ")
            int1 = int(input("Enter the number of time this string needs to be repeated"))
            print(str3*int1)
        elif c == "probability()":
            prob1 = int(input("Enter the number of favourable outcomes: "))
            prob2 = int(input("Enter the total number of outcomes: "))
            print ("The probablity for the event is ",prob1/prob2 * 100,"%")
        elif c == "remainder()":
            num4  = int(input("Enter the frist number: "))
            num5= int(input("Enter the second number: "))
            print(num4%num5)
        elif c == "calcdiscount()":
            price = float(input("Enter the price of the product: "))
            discount = float(input("Enter the discount percentage: "))
            finalprice = price-discount
            print(finalprice)
        elif c == "makestar()":
            turtle.Screen().setup(400,400)
            turtle.turtle.Screen().bgcolor("cyan")
            t = turtle.Turtle()

            t.penup()
            t.goto(-10,100)
            t.pendown()
            t.forward(100)
            t.lt(120)
            t.forward(100)
            t.lt(120)
            t.forward(100)
            t.lt(120)
            t.penup()
            t.lt(90)
            t.penup()
            t.fd(50)
            t.pendown()
            t.rt(90)
            t.fd(100)
            t.rt(120)
            t.fd(100)
            t.rt(120)
            t.fd(100)
            t.rt(120)

            turtle.done()
        elif c == "makepolygon()":
            turtle.Screen().setup(400,400)
            turtle.Screen().bgcolor("sky blue")
            t1 = turtle.Turtle()
            t1.penup()
            t1.goto(-40, 150)
            t1.pendown()
            numsides = int(input("How many sides do you want your shape to have?"))
            sidelength = int(input("How long do you want each side to be?"))
            for i in range(numsides):
                t1.forward(sidelength)
                t1.right(360/numsides)
            turtle.done()
        elif c == "rolldice()":
            l1= [1,2,3,4,5,6]
            print(random.choice(l1))
        elif c == "rockpaperscissors()":
            list1 = ["rock","paper","scissors"]
            score = 0
            while True:
                inp = str(input("Enter your choice(rock,paper,scissors): "))
                compinp = random.choice(list1)
                if inp == "rock":
                    print("Computer chose", compinp)
                    if compinp == "rock":
                        print("DRAW")
                    elif compinp == "paper":
                        print("You lose")
                    else:
                        score += 1
                        print(score)
                        print("YOU WIN")
                elif inp == "scissors":
                    print("Computer chose", compinp)
                    if compinp == "rock":
                        print("You lose")
                    elif compinp == "paper":
                        print(score)
                        print("YOU WIN")
                    else:
                        print("DRAW")
                elif inp == "paper":
                    print("Computer chose", compinp)
                    if compinp == "rock":
                        score+=1
                        print("YOU WIN")
                        print(score)
                    elif compinp == "scissors":
                        print("You lose")
                    else:
                        print("DRAW")
                else:
                    print("Wrong input")
                    
        else:
            print("Wrong command")
else:
    print("WRONG PASSWORD! Try again")
