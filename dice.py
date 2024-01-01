#total combinations
initial_a = [1,2,3,4,5,6]
initial_b = [1,2,3,4,5,6]

#initializing a function to evaluate it 
def combinations(a,b):
    #declare a array to represent the combinations
    combinations_arr = {}
    for i in a:
        for j in b:
            if i+j in combinations_arr :
                combinations_arr[i+j] += 1
            else:
                combinations_arr[i+j] = 1
    return combinations_arr

initial_combinations = combinations(initial_a, initial_b)

#another function for printing the output
def doomed_dice(a,b):
    print("Original die a:", a)
    print("Original die b:", b)

    #taking a random example
    set_in_a = [2,3]
    set_in_b = [2,3,4]
    for d1 in set_in_a:
        for d2 in set_in_a:
            for d3 in set_in_a:
                for d4 in set_in_a:
                    for b1 in set_in_b:                         
                        if combinations([1,d1,d2,d3,d4,4],[1,b1,b1+1,b1+2,b1+3,8])==initial_combinations:
                            print("New die a:", [1,d1,d2,d3,d4,4])
                            print("New die b:", [1,b1,b1+1,b1+2,b1+3,8])
                            return
         
doomed_dice(initial_a, initial_b)