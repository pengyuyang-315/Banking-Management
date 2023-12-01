from investment import investment
from investment import mortgage
import sys

def edit_rate(inv,new_rate):
    inv.rate=new_rate

def edit_risk(inv,new_risk):
    inv.risk=new_risk

def show_all_investment(dict_mort,dict_zcb,dict_gov):
    print("All mortgage details")
    for key, value in dict_mort.items():
        print("Mortgage type: ",key,"Mortgage details: ",value.show_details()) #the mortgage dict should be key:representing the mortgage type and value: being a mortgage class
    print("All zero-coupon-bond details")
    for key, value in dict_zcb.items():
        print("Zero-coupon-bond type: ",key,"Zero-coupon-bond details: ",value.show_details())
    print("All government bond details")
    for key, value in dict_gov.items():
        print("Government bond type: ",key,"Government bond details: ",value.show_details())

def recommendation_bond(user_risk,user_rate,choose_type,dict_mort,dict_zcb,dict_gov):#choose_type being 1/2/3, representing mort/zcb/gov
    print("We will give you recommendation based on your risk and return rate preference.")
    print("The final investment recommendation we give you will best match the rate and risk you provided.")
    if choose_type==1:
        dict_use=dict_mort
    elif choose_type==2:
        dict_use=dict_zcb
    elif choose_type==3:
        dict_use=dict_gov
    
    min_sum=sys.maxsize#maximum int
    value_store=[]
    

    for value in dict_use.values():# to get the min tempsum
        temp_sum=abs(value.rate-user_rate)+abs(value.risk-user_risk)
        if temp_sum<min_sum:
            min_sum=temp_sum
    for value in dict_use.values():# to store the key of min tempsum
        temp_sum=abs(value.rate-user_rate)+abs(value.risk-user_risk)
        if temp_sum==min_sum:
            value_store.append(value)
    
    print("the final recommendation is: ")
    for value in value_store:
        value.show_details()

    


"""

invest_1=investment(0.05,1)
mortgage_1=mortgage(0.05,1,5,2000)
mortgage_1.show_details()
edit_rate(mortgage_1,0.1)
mortgage_1.show_details()
"""
