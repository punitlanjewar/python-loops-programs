# print 1st non repeating character

string = 'teeter'

for char in string:
    if string.count(char) == 1:
        print(char)
        break