"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name
 
class SalariedEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def get_pay(self):
        return self.monthly_salary

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary}. Their total pay is {self.get_pay()}."

class ContractEmployee(Employee):
    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate

    def get_pay(self):
        return self.hours * self.rate

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour. Their total pay is {self.get_pay()}."

class CommissionedEmployee(SalariedEmployee):
    def __init__(self, name, monthly_salary, contracts, commission_per_contract):
        super().__init__(name, monthly_salary)
        self.contracts = contracts
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        return super().get_pay() + self.contracts * self.commission_per_contract

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a commission for {self.contracts} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."

class BonusCommissionedEmployee(SalariedEmployee):
    def __init__(self, name, monthly_salary, bonus_commission):
        super().__init__(name, monthly_salary)
        self.bonus_commission = bonus_commission

    def get_pay(self):
        return super().get_pay() + self.bonus_commission

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a bonus commission of {self.bonus_commission}. Their total pay is {self.get_pay()}."

class ContractCommissionedEmployee(ContractEmployee):
    def __init__(self, name, hours, rate, contracts, commission_per_contract):
        super().__init__(name, hours, rate)
        self.contracts = contracts
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        return super().get_pay() + self.contracts * self.commission_per_contract

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour and receives a commission for {self.contracts} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
