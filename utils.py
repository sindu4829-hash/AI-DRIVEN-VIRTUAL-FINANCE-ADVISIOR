def get_recommendation(profile, savings):
    if profile == 0:
        return "Low Risk → Invest in FD, Bonds"
    elif profile == 1:
        return "Medium Risk → Mutual Funds + Stocks"
    else:
        return "High Risk → Stocks, ETFs"