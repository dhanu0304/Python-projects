#union(|) Operator: The union of two sets are caluclated by using the union or (|) operator. The union of two sets A and B is the set of all elements that are in A, or in B, or in both A and B. The union of two sets is denoted by A ∪ B.
days1={"Mon" ,"Tue" ,"Wed" ,"Sat"}
days2={"Thr" ,"Fri" ,"Sat" ,"Sun","Mon"}
print("Days1 union Days2 is : ",days1 | days2 )
print("Days2 union Days1 is : ",days1.union(days2) )