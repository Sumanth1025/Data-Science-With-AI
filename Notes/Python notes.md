\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_17/07/2026\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Python class notes
**Data Types**

Dictionaries : It is the collection of key value pairs.

It is a mutable data type so we can add, delete and update the data.

we can execute the dictionary in the form of {'keys':'values'}.



dict.items() To print all keys and values in the form of list

dict.keys() To print all the keys in the form of list

dict.value() To print all the values in the form of list

dict.pop() To delete the exact key and value pair



ex: a={'keys':'values'}

&#x20; \_  print(a)

ANS:{'keys':'values'}



ex:

&#x09;f={'name':'uma', 'bankid':'ICICI25674','amount':5000}

&#x09;f\['amount']+=500

&#x09;print(f)





sets:

what is a set,

the data should not contain any duplicate values in it is called as sets.

It shows in the form of {}

Union: It prints all values from both sets. Symbol: |.

Intersection: It prints common values from both sets. Symbol: \&.
Difference: Set A - Set B It prints all elements from set A and removes common elements and set B elements.

Symmetric Difference: It removes the common values from both sets and print the remaining from both sets.





\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_18/07/2026\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Set:

&#x09;set store unique values

&#x09;set store only immutable/ non changeable elements.



why the order in set does not change for number but change for characters/string. Because set store values/ objects based on their hash values.

And for numbers the hash values are themselves



dictionary:

it is also a sequence but it stores values in the form of key and value pairs.



**why the order is not changing in dictionary even through it is unordered?**

Dictionary stored the values in it the order of the keys inserted in to the dictionary.

FrozenSet:

&#x09;it is a set which cannot be changed after its creation.

Note: When do we use tuple or frozenset.

&#x20;     we use them when we want to store values which should not be changed.

&#x09;

&#x09;eg: founder of an company

&#x09;eg:  



