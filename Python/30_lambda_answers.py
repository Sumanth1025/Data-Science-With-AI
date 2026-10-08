#1
nums = [3, -2, 5, -7, 4]
print(list(map(lambda x:x*x,filter(lambda x:x>0,nums))))

#2
names = ["Rahul Sharma", "Amit Kumar", "Priya Singh"]
print(list(map(lambda x:''.join(word[0] for word in x.split()),names)))


#3
nums = [10, 15, 20, 30, 45, 52]
print(list(filter(lambda x:x%3==0 and x%5==0,nums)))


#4
nums = [123, 456, 789, 120]
print(list(map(lambda x:x%10,nums)))


#5

words = ["python", "java", "sql"]
print(list(map(lambda x:"".join(reversed(x)), words)))



# 6
celsius = [0, 25, 100, -10]
print(list(map(lambda c:(c*1.8)+32,celsius)))



#7
words = ["cat", "python", "banana", "java", "computer"]
print(list(filter(lambda x:len(x)>5,words)))



#8
words = ["hello", "", "python", "", "java"]
print(list(filter(lambda x:x!="",words)))




#9w
names = ["John Doe", "Ravi Kumar", "Data Science"]
print(list(map(lambda x:x.lower().replace(" ", ""),names)))





#10
nums = [5, 10, 11, -12, 8, 15]
print(list(filter(lambda x:x*x>100,nums)))



#11
words = ["apple", "hi", "banana", "cat"]
print(sorted(words,key=lambda x: len(x)))



#12
nums = [23, 41, 15, 32, 19]
print(sorted(nums,key=lambda x:x%10))



#13
words = ["cat", "apple", "dog", "banana"]
print(sorted(words,key=lambda x:x[1]))



#14
from functools import reduce
words = ["cat", "elephant", "dog", "python"]
print(reduce(lambda a,b:a if len(a)>len(b) else b,words))



#15
from functools import reduce
words = ["python", "is", "very", "powerful"]
print(reduce(lambda a,b:a if len(a)<len(b) else b,words))



#16
words = ["apple", "banana", "sky", "education"]
print(list(map(lambda word:sum(1 for ch in word if ch in "aeiou"),words)))




#17
words = ["radar", "python", "level", "hello", "abcba"]
print(list(filter(lambda x:x[0]==x[-1],words)))




#18
data = [10, "hello", 25, "python", 40, "java"]
print(list(filter(lambda x:isinstance(x,int),data)))




#19
nums = [2, 3, 4, 5]
print(list(map(lambda x:f"{x}:{x*x}",nums)))




#20
nums = [121, 123, 444, 567, 909, 100]
print(list(filter(lambda x: str(x) == ''.join(reversed(str(x))), nums)))


# 21
nums=[121, 234, 343, 450, 454, 5678]
print(list(filter(lambda x: str(x)[0] == str(x)[-1],nums)))

# 22
nums = [123, 456, 89, 1001]
print(list(map(lambda x: sum(int(digit) for digit in str(x)), nums)))


# 23
words=["cat", "apple", "sky", "banana", "python", "Education"]
print(list(filter(lambda x: sum(1 for char in x if char.lower() in 'aeiouAEIOU') >= 2, words)))



# 24
words=["Ravi", "Python", "Java"]
print(list(map(lambda x: f"{x}-{len(x)}",words)))


# 25
from functools import reduce
nums=[10, 25, 8, 40, 30, 40]
print(reduce(lambda x, y: (y, x[0]) if y > x[0] else (x[0], y) if y > x[1] and y != x[0] else x,nums,
             (float('-inf'), float('-inf'))))



# 26
from functools import reduce
nums=[123, 234, 405, 99]
print(list(map(lambda x:reduce(lambda a,b:a*b,[int(digit) for digit in str(x)]),nums)))

# 27
names = ["A", "B", "C"] 
marks = [85, 72, 91]
print(dict(map(lambda name,mark:(name, mark),names,marks)))

# 28
students=[("Ravi", 22, 85), ("Amit", 17, 90), ("Priya", 21, 72), ("Neha", 19, 88)]
print(list(filter(lambda student: student[1] >= 18 and student[2] >=80, students)))

# 29
nums=[100, 250, 499.99]
print(list(map(lambda price: round(price * 1.18, 2), nums)))


# 30
nums=[-5, -2, 0, 3, 8, -11]
print(list(map(lambda x: "Zero" if x==0 else "Positive-Even" if x>0 and x%2==0 else 
               "Positive-odd" if x>0 and x%2!=0 else "Negative-even" if x<0 and x%2==0 else "Negative-odd", nums)))