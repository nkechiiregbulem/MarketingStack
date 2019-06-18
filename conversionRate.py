def conversion():
    visitors = input("Enter number of visitors?")
    visitors_val = int(visitors)
    print("Site Visitors:", visitors)
    action = input("Enter number of conversions?")
    action_val = int(action)
    print("Conversions:", action)
    CVR = action_val/visitors_val
    print("Conversion Rate:",("{:.0%}".format(CVR)))
    
 CVR()
