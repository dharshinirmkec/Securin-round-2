die_no_a = [1,2,2,3,3,4]
die_no_b = [1,3,4,5,6,8]

sum_combinations = {}

for i in die_no_a:
    for j in die_no_b:
        if (i+j) in sum_combinations:
            sum_combinations[i+j] += 1
        else:
            sum_combinations[i+j] = 1

#print(sorted(sum_combinations))


print("Enter the sum of values of two dices: ", end="")
sum = int(input())
print("Number of combinations to get the sum", sum, "is", sum_combinations[sum], "/36")    
