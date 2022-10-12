class Calc():
    # ^ naming convention- title case
    #               \/ \/ \/ -- taking out parameters we don't need to instantiate the class
    def __init__(self):
        self.rental = 0
        self.tax = 0
        self.insurence = 0
        self.percentage = None
        self.totalmonthlyincome = 0
    # Only 1 __init__
    # def __init__(self):
        

    def income(self):
        self.rental = int(input("Please enter the estimated amount of rental income: "))
        if self.rental >= 0:
            print(f"Your monthly estimated rent is {self.rental}")
        elif self.rental < 0:
            print("Invalid input, please try again.")

        #a consideration, maybe separate methods for these?  Up to you.
        self.tax = int(input(f"Please enter the estimated tax: "))
        if self.tax >= 0:
            print(f"Your monthly tax rate is {self.tax} ")
        elif self.tax < 0:
            print("Invalid Input, please try again.")

        self.insurence = int(input("Please enter the estimated insurence amount: "))    
        if self.insurence >= 0:
            print(f"Your monthly insurence is {self.insurence}")
        elif self.insurence < 0:
            print("Invalid Input, please try again.")

        self.percentage = int(input(f"Please enter the percentage amount: "))
        # I'm not sure exactly what % we're going for here but I'm guessing we have the info to calculate it from the inputs right?
        if self.percentage >= 0:
                    print(f" Your monthly percentage is {self.percentage}")
        elif self.percentage < 0:
            print("Invalid Input, please try again.")
        #Maybe something like self.percentage = self.expenses/self.income???
        

        

        #  Moved conditionals to corresponding inputs above for flow

        

        

        
    #def calc_income(self):
            self.totalmonthlyincome = self.rental + self.tax + self.percentage +  self.insurence
            print(self.totalmonthlyincome)
            print(f"The total monthly income is: ")
    #   <-----\/ \/ \/ 
            def run():
                do = input("Would you like the calculation of rental income ? [Y] yes, [N] no")
                if do.
                #Right track. . . if y: --> self.income() etc.

#Don't forget to instantiate your class at the end and then execute  --->  x = Calc()   x.run()