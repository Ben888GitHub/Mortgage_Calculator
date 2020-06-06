import math


class Mortgage:
    def __init__(self, monthInYears, percent):
        self.monthInYears = monthInYears
        self.percent = percent

    def vraiment(self):
        self.monthInYears = 12
        self.percent = 100
        # print(self.monthInYears, self.percent)
        print("Mortgage Calculator By Benedict Ryan")

        while True:
            try:
                principal = int(input("Principal ($1K - $1M): "))
                if (principal < 1000 or principal > 1000000):
                    print("Please enter between $1K and $1M")
                else:
                    print(principal)
                    break

            except ValueError:
                print("Please input numbers")

        while True:
            try:
                annualInterest = int(input("Annual Interest Rate (0 - 30): "))
                if (annualInterest < 0 or annualInterest > 30):
                    print("Enter value between 0 and 30: ")
                else:
                    print(annualInterest)
                    break
            except ValueError:
                print("Please input numbers ")

        monthlyInterest = annualInterest / self.percent / self.monthInYears

        while True:
            try:
                years = int(input("Period(Years): "))
                if (years < 0 or years > 30):
                    print("Enter value between 0 and 30: ")
                else:
                    print(years)
                    break
            except ValueError:
                print("Please input numbers  ")

        numberOfPayments = years * self.monthInYears

        mortgageValue = float(principal * (monthlyInterest * math.pow(1 + monthlyInterest, numberOfPayments))
                              / (math.pow(1 + monthlyInterest, numberOfPayments) - 1))

        currency = "${:,.2f}".format(mortgageValue)

        print("Mortgage: " + currency)


m = Mortgage(12, 100)
m.vraiment()
