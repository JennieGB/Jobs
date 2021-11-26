bills = []
for number in range(1000):
    if number % 2 != 0:
        bills.append(number ** 3)
print(bills)
sum = 0
bills_sum = []
for num in bills:
    while num != 0:
        sum = sum + num % 10
        num = num // 10
        if sum % 7 == 0:
            bills_sum.append(sum)
    sum = 0
print(bills_sum)
i = 0
sum_seven = 0
for i in bills_sum:
    sum_seven += i
print(sum_seven)
for idx in range(len(bills)):
    bills[idx] += 17
print(bills[idx])
sum_seven_plus = 0
for idx in bills_sum:
    sum_seven_plus += idx
print(sum_seven_plus)
