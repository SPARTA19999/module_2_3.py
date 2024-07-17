my_list = [42,69,0,322,13,0,99,-6,-7,-8,-9,-10,-11]
numbers = []
i = 0
L = len(my_list)
while i < len(my_list):
    number = my_list[L-1-i]
    if number <= 0:
        numbers.append(number)
    else:
        print("положительное число - ", number)

    i += 1

print(numbers)