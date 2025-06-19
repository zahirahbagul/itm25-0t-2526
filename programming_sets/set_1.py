def savings(gross_pay, tax_rate, expenses):
    tax_deducted = tax_rate * gross_pay
    take_home_pay = int(gross_pay - tax_deducted)
    remaining = take_home_pay - expenses
    return remaining

def material_waste(total_material, material_units, num_jobs, job_consumption):
    used = num_jobs * job_consumption
    waste = total_material - used
    return str(waste) + material_units

def interest(principal, rate, periods):
    interest_earned = principal * rate * periods
    final_value = int(principal + interest_earned)
    return final_value
