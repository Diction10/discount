from task3a import Customer
from task3c import DiscountRate
from datetime import datetime

# create a class Visit
class Visit(Customer):
    
    def __init__(self,name,date,serviceExpense = None, 
                 productExpense = None,memberType=None):
        Customer.__init__(self, name, memberType=None)

        self.__date = date
        self.__serviceExpense = serviceExpense
        self.__productExpense = productExpense
    
    
    # set service expense
    def setServiceExpense(self, expense):
        """ Sets the Service  expense after discount has
        been applied according to their membership type.
        """
        self.__serviceExpense = expense
       

    # get service expense
    def getServiceExpense(self):
        """ Returns the service expense of the customer 
        after discount has been applied"""

        # get member type
        member_type = self.getMemberType()

        # return discount rate for the member
        discount_rate = DiscountRate.getServiceDiscountRate(member_type)

        if member_type != None and self.__serviceExpense != None:
            self.__serviceExpense = self.__serviceExpense * (1 - discount_rate)
        else:
            self.__serviceExpense
        
        return self.__serviceExpense 


    # get product expense
    def getProductExpense(self):
        """ Returns the Product expense of the customer 
        after discount has been applied"""

        # get member type
        member_type = self.getMemberType()

        # return discount rate for the member
        discount_rate = DiscountRate.getProductDiscountRate(member_type)

        if member_type != None and self.__productExpense != None:
            self.__productExpense = self.__productExpense * (1 - discount_rate)
        else:
            self.__productExpense

        return self.__productExpense
    
    
    # set product expense
    def setProductExpense(self, expense):
        """ Sets the Product  expense after discount has
        been applied according to their membership type.
        """
        self.__productExpense = expense
        
    
    # get total expense
    def getTotalExpense(self):
        """ Returns the total expense of the customer
        By adding their product expense with their service expense.
        """
        totalExpense = self.__productExpense + self.__serviceExpense
        return totalExpense
    
    # class to string
    def __repr__(self):
        return f'visited on {self.__date}'
    



"""
Please Check and run the gui.py file to test the functionality of this class.
"""
    


