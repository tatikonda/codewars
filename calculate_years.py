def calculate_years(principal, interest, tax, desired):
    yrs = 0

    while principal < desired:
        yrs += 1
        tot_int = principal * interest
        int_tax = tot_int * tax
        principal = principal + (tot_int - int_tax)

    return yrs