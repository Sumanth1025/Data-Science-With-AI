# # write code to find area of square
# s = float(input())
# a = s*s
# #:.nf determine the number of decimal places to display after the number.
# print(f"{a:.2f}")



# #write code to find area of rectangle
# l = float(input())
# b = float(input())
# a = l * b
# print(f"{a:.2f}")


# #write code to find area of triangle
# b = int(input())
# h = int(input())
# a = 0.5 * b * h
# print(f"{a:.2f}")


# #area of circle
# r = float(input())
# a = 3.14 * r * r
# print(f"{a:.2f}")


# #perimeter of square
# s = float(input())
# p = 4 * s
# print(f"{p:.2f}")

# #perimeter of rectangle
# l = float(input())
# b = float(input())
# p = 2 * (l + b)
# print(f"{p:.2f}")

# #perimeter of triangle
# a = float(input())
# b = float(input())
# c = float(input())
# p = a + b + c
# print(f"{p:.2f}")

# #perimeter of circle
# r = float(input())
# p = 2 * 3.14 * r
# print(f"{p:.2f}")



# a = float(input())
# b = float(input())
# c = float(input())
# if a + b > c and a + c > b and b + c > a:
#     print("The three values form a triangle.")
# else:
#     print("The three values do not form a triangle.")



#wap to calculate total marks of a student and average marks of a student
marks = [62,83,76,100,75,72]
total = 0
count = 0
for mark in marks:
    total += mark
    count += 1
print(f"Total marks: {total}")
average = total / count if count > 0 else 0
print(f"Average marks: {average:.2f}")