from investment.investment import mortgage
from investment.investment import zero_coupon_bond
from investment.investment import government_bond
from investment.manage_investment import show_all_investment
from investment.manage_investment import recommendation_bond
def mortgage_initialization():
    # initialize 
    mortgage1 = mortgage(0.03,5,5,2000)
    mortgage2 = mortgage(0.04,7,5,3000)
    mortgage3 = mortgage(0.05,8,10,4000)
    mortgage_dict = {
        "low risk mortgage": mortgage1,
        "mid risk mortgage": mortgage2,
        "high risk mortgage": mortgage3
    }
    return mortgage_dict

def zcb_initialization():
    # initialize 
    zcb1 = zero_coupon_bond(0.03,5,2000,5)
    zcb2 = zero_coupon_bond(0.06,10,3000,8)
    zcb_dict = {
        "low risk zcb": zcb1,
        "high risk zcb": zcb2
    }
    return zcb_dict

def gov_initialization():
    # initialize 
    gov1 = government_bond(0.03,5,2000,4,1)
    gov2 = government_bond(0.05,5,3000,5,1)
    gov3 = government_bond(0.05,6,2000,3,2)
    gov_dict = {
        "low risk government bond": gov1,
        "mid risk government bond": gov2,
        "high risk government bond": gov3

    }
    return gov_dict