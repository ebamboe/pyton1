print("Printing current and prevision number sum in a range(10)") 
previous_num = 0


for i in range(10):
    x_sum = previous_num + i
    print(f"Current Number {i} Prevision Number {previous_num} Sum: {x_sum}")
    previous_num = i
