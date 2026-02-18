#Aim: WAP to update a given tuple. Given following tuple
tup = ("Square", "Cricle", "Triangle")
change=list(tup)
change.remove("Cricle")
change.insert(1,"rectangle")
change2=tuple(change)
print(f"updated tuple:{change2}")
