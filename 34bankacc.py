class bank:
    def __init__(self, accno, name, type, bal):
        self.account = accno
        self.nam = name
        self.t = type
        self.b = bal

    def dep(self, a1):
        self.b = self.b + a1
        print("Balance:", self.b)

    def widthw(self, a2):
        if self.b < a2:  # Fixed variable name from a1 to a2
            print("Insufficient balance")
        else:
            self.b = self.b - a2  # Fixed variable name from a1 to a2
            print("Balance:", self.b)

    def dis(self):
        print("Account no:", self.account)
        print("Name:", self.nam)
        print("Type:", self.t)
        print("Account balance:", self.b)  # Fixed variable name from b to self.b

a = int(input("Account number:"))
n = str(input("Name:"))
t = str(input("Account type:"))

b = int(input("Account balance:"))  # Convert balance to an integer
obj1 = bank(a, n, t, b)  # Pass balance as an integer
obj1.dis()
a1 = int(input("Enter the amount to deposit:"))  # Convert input to an integer
obj1.dep(a1)
a2 = int(input("Enter the amount to withdraw:"))  # Convert input to an integer
obj1.widthw(a2)


