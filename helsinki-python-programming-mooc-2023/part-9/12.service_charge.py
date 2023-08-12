# WRITE YOUR SOLUTION HERE:

class BankAccount:
    def __init__(self, owner:str, account_number:str, balance:float):

        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance 

    def __service_charge(self):
        return self.__balance * .01 

    def deposit(self, amount:float):
        #add amount
        self.__balance += amount 

        service_charge = self.__service_charge()
        self.__balance -= service_charge

    
    def withdraw(self, amount:float):
        #withdraw amount
        self.__balance -= amount 

        service_charge = self.__service_charge()
        self.__balance -= service_charge


    @property
    def balance(self):
        return self.__balance
    
