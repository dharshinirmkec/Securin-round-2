#Calculate and display the distribution of all possible combinations
die_no_a = [1,2,3,4,5,6]
die_no_b = [1,2,3,4,5,6]

for i in die_no_a:
    for j in die_no_b:
       #printing the combinations
        print("(", i, ",", j, ")", sep="", end=" ")
    print()
