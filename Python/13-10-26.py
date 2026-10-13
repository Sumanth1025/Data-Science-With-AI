import random

# #random() module is used to generate from 0.0 to 1.0
# print(random.random())


# #randint():
# #it takes two argument and generate integer between the given argument
# print(random.randint(1,5))


# #uniform()
# #it generate an random float value, here it take two arguments as range
# print(f'{random.uniform(1,10):.2f}')


#choice():
#It is used to choose an object from a seq of objects
name=['uma','sai','teja']
selectedname=random.choice(name)
print(selectedname)


#choices():
#it used to select multiples duplicates object feom a seq
#and k is the predefine attribute for the choices



#sample():
