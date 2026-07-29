# #index numbers
# # accessing 
# name= 'uma'
# print(name[2])

# #Using indexing we have accessed and edited a list 
# marks=[45,54,65 ,64,49,90]

# print(marks[2])


# fruits=['guava','apple','banana','mango']
# print(fruits[-3])
# print(fruits[-1])

#double indexing

# kalakaarulu=['vyshu','koustish']
# print(kalakaarulu[1][1])

# # fixed nested list syntax and corrected indexes
# bio = ['Uma Maheswararao', 'MSc Computer Science', 'Tech Trainer', ['Python', 'Machine Learning', 'Artificial Intelligence']]

# print(bio[1][0])        # first character of the second item
# print(bio[3][1][0])     # first character of the second skill
# print(bio[3][2][0])     # first character of the third skill

# #Slicing

# toppers=[8.7,8.57,8.5,8.43,8.32]

# print(toppers[0:3])

# backbenchers=[6.4,6.5,6.23,5.66,4.90]
# backbenchers[2:5]=[9.0,9.5,9.99]
# print(backbenchers) 

#omitted values in slicing

tuple1=(1,2,3,5,6,7,8,9,10)
print(tuple1[6:10])
print(tuple1[6:])
print(tuple1[:5])
print(tuple1[:])
print(tuple1[::3])

tech = 'Machine Learning'

print(tech[::-1])#negative step, to jump on element fro last