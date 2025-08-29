def savings(gross_pay, tax_rate, expenses):
    after_tax = int(gross_pay * (1 - tax_rate))  # round down
    remaining = after_tax - expenses
    return remaining

def material_waste(total_material, material_units, num_jobs, job_consumption):
    total_material_consumed = num_jobs * job_consumption
    total_waste = total_material - total_material_consumed
    return str (total_waste) + material_units


def interest(principal, rate, periods):
    profit = principal* (rate * periods)
    total_value = profit + principal
    return total_value





