# 1. Find the size of a Tuple in Python
Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
Tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))
print('The size of tuple1',Tuple1.__sizeof__())
print('The size of tuple2',Tuple2.__sizeof__())
print('The size of tuple3',Tuple3.__sizeof__())
# 2. Python – Maximum and Minimum K elements in Tuple
test_tup = (5, 20, 3, 7, 6, 8)
#3.Python program to create a list of tuples from given list having number and its cube in each tuple
list1 = [1, 2, 5, 6]
res= [(val ,val**3) for val in list1]
print(res)
# 4. Python – Adding Tuple to List and vice – versa
test_list = [5, 6, 7]
test_tup = (10,12,15)
res = tuple(list(test_tup) + test_list)
print('The tuple after additiion is',res)
# 5. Python – Sum of tuple elements
def summation(test_tup):
    test = list(test_tup)
    count = 0
    for i in test:
        count = count +i
    return count
test_tup = (5, 20, 3, 7, 6, 8)
print('The sum is',summation(test_tup))
# 6. Python – Modulos of tuple elements
test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)

res = []
for i in range(0,len(test_tup1)):
    res.append(test_tup1[i] % test_tup2[i])
print(res)
# 7. Python – Row-wise element Addition in Tuple Matrix
test_list = [[('Gfg', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]
#8. Python | Update each element in tuple list
test_list = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
add_ele = 10
res = [tuple(i + add_ele for i in sub) for sub in test_list]
print(res)
# 9. Python | Multiply Adjacent elements
test_tup = (1, 5, 7, 8, 10)
res = tuple(map(lambda x,y: x * y,test_tup[1:],test_tup[:-1] ))
print('The new tuple is',res)
# 10 Python – Join Tuples if similar initial element
# 11 Python – All pair combinations of 2 tuples
test_tuple1 = (4, 5)
test_tuple2 = (7, 8)

res = [(a,b) for a in test_tuple1 for b in test_tuple2]
res = res + [(a,b) for a in test_tuple2 for b in test_tuple1]
print('The maximum combination are',res)
# 12. Python – Remove Tuples of Length K
test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
k = 3

res = [i for i in test_list if len(i) != k]
print(res)
# 13.Python – Remove Tuples from the List having every element as None
test_list = [(None, None), (None, None), (3, 4), (12, 3), (None, )]
res = []
for i in test_list:
    if not(i.count(None) == len(i)):
        res.append(i)
print('The new tuple',res)
# 14. Python program to sort a list of tuples by second Item
tup = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)]
tuples = [('for', 24), ('Geeks', 8), ('Geeks', 30)]
def sort_tuple(tup):
    tup.sort(key = lambda x: x[1])
    return tup
print(sort_tuple(tup))
print(sort_tuple(tuples))
# 15. Python – Sort Tuples by Total digits
# 16. Python – Elements frequency in Tuple
from collections import Counter
test_tup = (4, 5, 4, 5, 6, 6, 5, 5, 4)
res = dict(Counter(test_tup))
print(res)
# 17 Python – Filter Range Length Tuples
# 18 Python – Assign Frequency to Tuples
# 19 Python | Test if tuple is distinct
test_tup = (1, 4, 5, 6)
res = len(set(test_tup)) == len(test_tup)
print(res)


