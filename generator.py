daily_sales =[5,6,7,8,2,3,4]


total_cups = sum(sale for sale in daily_sales if sale >5)
print(total_cups)