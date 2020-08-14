"""
unpacking tuples means to get each/an individual item
"""

stock_prices = [('HARL', 200), ('ARLT', 400), ('GBSN', 100)]

# print all of tuple
for item in stock_prices:
    #print(item)
    pass

# print just the ticker
for ticker, price in stock_prices:
    #print(ticker)
    pass

# increase price by 10%
for ticker, price in stock_prices:
    #print(price + (0.1 * price))
    pass


#with functions
work_hours = [('Donna', 100), ('Pat', 400), ('DaSheka', 800)]

# evaluate tuples for employee with the most hours
def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee

    return (employee_of_month,current_max)

#employee with the most hours
#print(employee_check(work_hours))
# alternate ---
name,hours = employee_check(work_hours)
#print(name)
#print(hours)

# find out how many values are available
item = employee_check(work_hours)
print(item)