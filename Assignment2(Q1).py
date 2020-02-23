'''
Given a list of words, determine whether the words can be chained to form a circle. 
A word X can be placed in front of another word Y in a circle if the last character 
of X is same as the first character of Y.

For example, 
the words ['chair', 'height', 'racket', touch', 'tunic'] 
can form the following circle: 

chair --> racket --> touch --> height --> tunic --> chair 

list is entered by user directly in the form of list of words

sample input
['chair', 'height', 'racket', touch', 'tunic']

sample output
['chair', 'racket', 'touch', 'height', 'tunic']

'''

lst1 = [i for i in input().split()]
n = len(lst1)
lst2 = []
lst2.append(lst1[0])
str2 = lst1[0]
for i in range(0,n):
    for j in range(1,n):
        str1 = lst1[j]
        p = len(str2)
        if str2[p-1] == str1[0]:
            lst2.append(lst1[j])
            str2 = str1
            lst1[j] = '*&'
            break
print(lst2)        
