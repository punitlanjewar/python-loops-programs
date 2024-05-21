# print the table of given number excluding 5th position

number = 2

for i in range(1, 11):
    if i == 5:
        continue 
    print(number, 'X', i, '=', number * i)           