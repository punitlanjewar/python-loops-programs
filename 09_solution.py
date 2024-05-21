# print the duplicate from list 

item = ['apple', 'mango', 'orange', 'banana', 'apple']

unique_item = set()

for items in item:
    if items in unique_item:
        print('Duplicate:', items)
        break
    unique_item.add(items)