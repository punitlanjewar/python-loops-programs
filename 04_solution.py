# print the string in reverse

string = "python"
reverse_string = ""

# for i in string[::-1]:
#     reverse_string = reverse_string + i
for i in string:
    reverse_string = i + reverse_string
print(reverse_string)