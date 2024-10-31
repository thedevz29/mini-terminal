class Commands:
    def __init__(self, user):
        self.user = user
        if user == "Atharv":
            print("Access Granted")
        else:
            print("Acess Denied")
            exit()
            
    def add(self):
        add_1 = float(input("Enter the first number which you want to add: "))
        add_2= float(input("Enter the second number you want to add:"))
        print(f"The sum is {add_1+add_2}")
    
    def subtract(self):
        
        sub_1 = float(input ("Please enter the first number : "))
        sub_2 = float(input("Please ener the second number : "))
        print(f"The difference is {sub_1-sub_2}:")
        
    def multiply(self):
        
        mul_1 = float(input ("Please enter the first number : "))
        mul_2 = float(input("Please ener the second number : "))
        print(f"The product is {mul_1*mul_2}")
        
    def divide(self):
        div_1= float(input ("Please enter the first number : "))
        div_2 = float(input("Please enter the second number : "))
        try:
            print(f"The qoutient is :{div_1/div_2}")
            
        except ZeroDivisionError:
            print("OOPS THERE IS A ZERODIVISION ERROR")


    

    