
# Seminar 1. Exercise 2

number = 843
digit_sum = 0

digit_sum = sum(int(digit) for digit in str(number))

print("Sum of numbers: ", digit_sum)


# Seminar 1. Exercise 4

S = int(input("Input total S: "))

PS_count = S // 4

K_count = 2 * (PS_count + PS_count)

print("Petya done: ", PS_count)
print("Sergey done: ", PS_count)
print("Katya done: ", K_count)

