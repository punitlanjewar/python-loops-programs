# Repeat until user enter number b/w 1 and 10

while True:
    number = int(input('Enter value b/w 1 and 10: '))
    if number >= 1 and number <= 10:
        print('Thanks')
        break
    else:
        print('Invalid Number')    
