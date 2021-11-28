bills = []
for number in range(1000):
    if number % 2 != 0:
        bills.append(number ** 3)
print(bills)
sum = 0
bills_num = []
for num in bills:
    x = num
    while x != 0:
        sum = sum + x % 10
        x = x // 10
    if sum % 7 == 0:
        bills_num.append(num)
    sum = 0
print(bills_num)
sum_num = 0
for element in bills_num:
    sum_num += element
print(sum_num)
new_list = [x+17 for x in bills]
print(new_list)
sum_17 = 0
bills_num_17 = []
for num_17 in new_list:
    x = num_17
    while x != 0:
        sum_17 = sum_17 + x % 10
        x = x // 10
    if sum_17 % 7 == 0:
        bills_num_17.append(num_17)
    sum_17 = 0
print(bills_num_17)
sum_num_17 = 0
for element_17 in bills_num_17:
    sum_num_17 += element_17
print(sum_num_17)
