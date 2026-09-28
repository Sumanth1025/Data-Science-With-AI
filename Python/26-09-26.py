# #write a set comprehension to genetate a set with each character of my string
# str1='education'
# uniquechar={char for char in str1}
# print(uniquechar)

# vowels={char for char in str1 if char in 'aeiou'}
# print(vowels)



# Note: In order to pass multiple line as paragraph as one single string, we can use either three single quotes or three double quotes
# str1='''My name is Mopidevi Sumanth Teja and I have a cold and cough nat able to take
# class but still taking class because i want salary'''
# uniword={i for i in str1.split()}
# print(uniword)




                                            #Dictionary comprehension

#write a dict comprehension to generate a dictionary of each number fron the list mapping to which cube

# nums=[4,7,9,2,-1,3]
# cubed={num: num**3 for num in nums}
# print(cubed)




#generate a dict where length of each word is mapping to its word
# words=['Python','Aritificial Intelligence','Machine Learning','Java','D22 Class']
# wordlen={len(word): word for word in words}
# print(wordlen)
# wordlen={len(word): word for word in words if len(word) > 5}
# print(wordlen)




#write a comprehension to generate dict where each cel temp is mapping to its euivalent farenheit
# temps=(34,56,23,55,12,-4)
# convert={cel:(cel*9/5)+32 for cel in temps} #  formula cel*(9/5)+32
# print(convert)




#generate an result dict where marks >35 generate pass and others fail
# marks={'ipsitha':72,'benjaminu':32,'lankesh':66,'doritha':99,'eeston':21,'jadal':12.5,'peddi':100}
# result={name:'pass' if mark>35 else 'fail' for name,mark in marks.items()}
# print(result)




#write a comprehension to generate dict where each char is mapping to its number of occurrences in the string
# str1='Sylvester Stallone'
# occurrences={i:str1.count(i) for i in str1}
# print(occurrences)