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
        
    