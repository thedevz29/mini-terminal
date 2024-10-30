class Commands:
    def __init__(self, user):
        self.user = user
        if user == "Atharv":
            print("Access Granted")
        else:
            print("Acess Denied")
            exit()
            
    