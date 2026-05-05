#sorted() and sort(): In python sorted() function is used to sort all items of list in an ascending order and create a new list.
#in list numbers are sorted numerically and string items are sorted in alphabetical order. The sort() method is used to sort the list in place, meaning it modifies the original list and does not return a new list.
num = [1,3,2,6,5,4]
print("The Original list num is:", num)
num2 = sorted(num)
print("The sorted list num2 is:", num2)
print("The sorted list num2 is:",sorted(num))
print("The Original list num is:", num)
print("The sorted list num2 is descending order using sorted is:", sorted(num, reverse=True))
print ("The sort list num returning NOne: ", num.sort())
print("The original updated sorted list using sort function is:", num)
num.sort(reverse=True)
print("The original updated sorted list in descending order using sort function is:", num)