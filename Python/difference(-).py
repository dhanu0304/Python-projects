#The Difference of two sets can be calculated by using the subtraction(-) operator.
#The resulting set will be obtained by removing all the elements from set 1 that are present in set 2
days1={"Mon","Tue","Wed","Sat"}
days2={"Thr","Fri","Sat","Sun","Mon"}
print("days1-days2:",days1-days2)
print("days2-days1:",days2-days1)
print("Days1-Days2:",days1.difference(days2))
print("Days2-Days1:",days2.difference(days1))
