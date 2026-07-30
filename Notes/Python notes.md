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







\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_20/07/2026\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_





# **Data Type conversion VS Data Type casting:**





### Type Conversion:

&#x09;The automatic assigning of data type when we perform operation between two different data types is called Type Conversion. Type conversion only possible between supportive data type.

&#x09;



### Type Casting:

&#x09;Here the user change the data type of an object manually. We use data type function to type cast one data object into another data object.

&#x09;Here also type casting can happen only between supportive objects.









### Dynamically Typed :

&#x09;Here we don't have to mention the type of the value we are passing them into our program, we can just pass the values and python automatically assigns data type to the based on the values.







### range() and len() functions:

#### &#x09;range():

&#x09;		It is used to generate numbers. It takes three values start, stop and step.

&#x09;	Syntax: range(start, stop, step)

&#x09;	Start: From which number to generate.

&#x09;	Stop: Until which number to generate.

&#x09;	Step: How many values to jump.





\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_21/07/2026\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



## Mutable/changable and Immutable/non changable

### Object:

##### Mutable Object:

&#x09;Object which can be edited after they created.

##### Immutable Object:

&#x09;Object which can't be edited after they created.



Immutable:					Mutable:

Integer						List

float						set

complex						dictionary

tuple

string





Logical

Identity

Membership

Bitwise

warlus





Note:

&#x09;Operator we use to check Immutable and Mutable is +=.

&#x09;

Input() function:

&#x09;This function is used to pass the values into my program after the execution of the program.



\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_22/07/2026\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



Operators:

&#x09;operator is a symbol that performs some action between one or more then one objects.

Types of operators:



Arithmetic:

&#x09;These operator are used to perform mathematical operations in our program.

&#x09;operators:+,-,\*,/,//,%,\*\*.



Assignment:

&#x09;This are used to assign a value to a variable.



Comparison/relational:

&#x09;Two compare values of two objects and they return Boolen value as an output.



\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_23/07/2026\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_





## Logical Operators:

&#x09;			It is used to evaluate one or more than one condition at once.

&#x09;			Operators: and, or, not

### AND True Table:



con1	con2	result

True	True	True

True	False	False

False	True	False

False	False	False









### OR True Table:



con1	con2	result

True	True	True

True	False	True

False	True	True

False	False	False





### NOT True Table:



con1	result

True	False

False	True





## Identity operator:

&#x09;				These operators are used to check wheather two variables are pointing to the same object or not.

&#x09;				operator: is, is not







## Membership operator:





&#x09;				These are used to check whether an object is a member of sequence or not.

&#x09;				Operations: in, in not.







\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_27/07/2026\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



## Binary Operator:

&#x09;



number			binary

&#x20; 1			 0001

&#x20; 2			 0010

&#x20; 3			 0011

&#x20; 4			 0100

&#x20; 5			 0101

&#x20; 6			 0110

&#x20; 7			 0111

&#x20; 8			 1000

&#x20; 9			 1001

&#x20; 10			 1010







Bitwise \&(AND):

&#x09;It comperes two binary values and return 1 when both binary values are 1.

Bitwise |(OR):

&#x09;It compare two binary values and return 1 when atleast 1 of the binary values is 1.



Bitwise <<(left shift):

&#x09;Number << n



formula : number\*2\*\*n





Bitwise >>(right shift):

&#x09;Number >> n



formula : number//2\*\*2



Bitwise Not(\~):

&#x09;-6 = 2'compliment of (6).

&#x09;2'compliment = 1's compliment + 1.



formula = -(n+1)





Tasks:

3<<3

4<<6







6>>2

2>>2





\~9,\~8,\~-4





Bitwise (XOR)(^):

&#x09;It return 1 when the both the bits are different, otherwise 0.

eg: 5^6



5 = 0101

6 = 0110

ANs=0011

ans=3









walrus operator:

&#x09;It is used to assign an object and pass it into an operations in the same line.

Symbol: (:=)



\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_28/07/2026\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



Indexing and Slicing:



Index numbers: For an ordered sequence, each elemet in the seq is assigned with a number based on it position, while we run the program.



since the index numbers of any ordered seq are starting from 0 so we can python does zero based indexing.



For n elements the possible index values are 0 to n-1.



Accessing or editing elements in a sequence using index number is called indexing



Indexing done by using positive numbers is called positive indexing.



Here the indexing is done using -ve numbers and the elements are accessed from the end.



It is using of nested indexing inside sequence of sequence.



Slicing:It is used to access or edit multiple



\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_29/07/2026\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



### Tuple packing and unpacking:



&#x09;Packing: When we pass multiple objects to a variable, python by default packs them into a tuple.



&#x09;Unpacking: Using multiple variables to access elements from a sequence.





### String Concatenation and Replication:



&#x09;String Concatenation:

&#x09;	Joining two strings together using + operator.

&#x09;String Replication:

&#x09;	we can repeat a string multiply times using \* operator.





### Decision making statement:

Here the if statement takes a condition and make one decision if the condition is true else make another decision.



Syntax:(Rules to write a program)

if condition:

&#x09;#code

else:

&#x09;#code







































