# calculate sum of even numbers and no of even numbers b/w the given number

n = 10
even_sum = 0
sum_even = 0

for i in range(1, n+1):
    if i % 2 == 0:
        even_sum += i
        sum_even += 1
print(even_sum)   
print(sum_even)     

