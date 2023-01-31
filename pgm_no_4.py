numbers = [4, 5, 6, 7, 10, 9]

max_num = numbers[0]
i = 1

while i <len (numbers):
    if numbers[i] > max_num:
        max_num = numbers[i]
    i += 1

print("The maximum number is:",max_num)
