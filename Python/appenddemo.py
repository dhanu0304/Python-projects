#append() : In python, append() method adds an item to the end of th elist
my_list=[1,2,3]
another_list=[4,5,6]
#append with an element
my_list.append(8)
#append with a list
my_list.append(another_list)
print(my_list)
#append with a tuple
my_list.append((7,8))
print(my_list)
#append with a string
my_list.append("abc")
print(my_list)