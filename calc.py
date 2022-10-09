class calc():
    def __init__(self, rental, tax, insurence, percentage):
        self.rental = rental
        self.tax = tax
        self.insurence = insurence
        self.percentage = percentage


    def __init__(self):
        self.totalmonthlyincome = 0

    def income(self):
        self.rental = int(input("Please enter the estimated amount of rental income: "))
        self.tax = int(input(f"Please enter the estimated tax: "))
        self.percentage = int(input(f"Please enter the percentage amount: "))
        self.insurence = int(input("Please enter the estimated insurence amount: "))

        

        if self.rental >= 0:
            print(f"Your monthly estimated rent is {self.rental}")
        elif self.rental < 0:
            print("Invalid input, please try again.")

        if self.tax >= 0:
            print(f"Your monthly tax rate is {self.tax} ")
        elif self.tax < 0:
            print("Invalid Input, please try again.")

        if self.percentage >= 0:
            print(f" Your monthly percentage is {self.percentage}")
        elif self.percentage < 0:
            print("Invalid Input, please try again.")

        if self.insurence >= 0:
            print(f"Your monthly insurence is {self.insurence}")
        elif self.insurence < 0:
            print("Invalid Input, please try again.")
   
            self.totalmonthlyincome = self.rental + self.tax + self.percentage +  self.insurence
            print(self.totalmonthlyincome)
            print(f"The total monthly income is: ")
            
            def run():
                do = input("Would you like the calculation of rental income ? [Y] yes, [N] no")
                if do.