# count the -ve numbers and +ve numbers from the list

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_count = 0
negative_number_count = 0

for num in numbers:
    if num > 0:
        # positive_number_count = positive_number_count + 1
        positive_number_count += 1
    else:
        # negative_number_count = negative_number_count + 1
        negative_number_count += 1
print(positive_number_count)            
print(negative_number_count)            