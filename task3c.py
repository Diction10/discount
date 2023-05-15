# create classDiscountTste

class DiscountRate:
    # declare class methods
    ServicePremium = 0.2
    ServiceGold = 0.15
    ServiceSilver = 0.1
    ProductDiscount = 0.1

    
    @classmethod
    def getServiceDiscountRate(cls, member_type):
        discount_rate = {
            'Premium' : DiscountRate.ServicePremium,
            'Gold' : DiscountRate.ServiceGold,
            'Silver' : DiscountRate.ServiceSilver
        }.get(member_type)

        return discount_rate
    
    @classmethod
    def getProductDiscountRate(cls, member_type):
        discount_rate = {
            'Premium' : DiscountRate.ProductDiscount,
            'Gold' : DiscountRate.ProductDiscount,
            'Silver' : DiscountRate.ProductDiscount
        }.get(member_type)

        return discount_rate
    

"""
Please Check and run the gui.py file to test the functionality of this class.
"""



    

    