has_high_income = True
has_good_credit = True
has_criminal_record = True

if has_high_income and has_good_credit:
    print("Eligible for loan")

if has_high_income or has_good_credit:
    print("Eligible for loan")    

if has_high_income and not has_criminal_record:
    print("Eligible for loan")    
else:    
    print("Not Eligible for loan")    

## logical operator
## AND : both
## OR : at least one
## NOT