# create a class customer
class Customer:
    # create class variable to store lists of customers
    list_customers = []
    
    def __init__(self, name, memberType = None):
        self.__name = name
        self.__memberType = memberType
        
    # chek if name is a member
    def isMember(self):
        """
        This function returns true if a customer exists.
        It reruens false if a customer does not exist 
        """
        return f'{self.__name} is a customer'
    
    # get customer name
    def getName(self):
        """ Returns the name of the customer """
        return self.__name
    
    # set name
    def setName(self, name):
        """ Sets the name of the customer """
        self.__name = name
    
    # get member type
    def getMemberType(self):
        """ Gets the Membership type of a customer """
        return self.__memberType
    
    
    # set member type 
    def setMemberType(self, memberType):
        """ Sets the Membership type of a customer """
        self.__memberType = memberType
        
    
    def __repr__(self):
        return f'{self.__name}'
    


"""
Please Check and run the gui.py file to test the functionality of this class.
"""
