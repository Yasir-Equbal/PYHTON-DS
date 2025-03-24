import numpy as np

mobile_name = np.array(["Mobile1", "Mobile2", "Mobile3", "Mobile4", "Mobile5", 
                        "Mobile6", "Mobile7", "Mobile8", "Mobile9", "Mobile10"]) 
mobile_price = np.array([13999, 6298, 10999, 14999, 7298, 6385, 8999, 9999, 10999, 13868])
mobile_unit = np.array([9, 8, 9, 9, 8, 8, 9, 6, 5, 7])

total_value = np.dot(mobile_price, mobile_unit)
print("Total monetary value of the inventory:", total_value)

avg_units = np.mean(mobile_unit)
print("The average number of units per smartphone model:", avg_units)

avg_price = np.mean(mobile_price)
print("The average price of a smartphone:", avg_price)

max_price = np.max(mobile_price)
min_price = np.min(mobile_price)
print("Most expensive smartphone price:", max_price)
print("Cheapest smartphone price:", min_price)

mod_price = np.mod(mobile_price, 500)
print("Price modulo 500:", mod_price)
