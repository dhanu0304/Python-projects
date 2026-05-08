Months = {"Jan","Feb","Mar","Apr"}
print("\n Printing the original set ...")
print(Months)
Months.discard("Apr")
print("\n Printing the modified set ...");
print(Months)
Months.discard("May") #doesn't give error
print("\n Printing the modified set ...");
print(Months)