fruits=["Apple","Mango","Banana"] 
vegetables=["Carrot","Potato","Tomato"]
beverages=["Tea","Coffee","Lemonade"]
fruits.append("Pineapple")
vegetables.insert(1,"Broccoli")
beverages.pop()
inventory=fruits+vegetables+beverages
print(fruits[:2])
print(vegetables[-1])
lengths = [len(fruit) for fruit in fruits]
print(lengths)
if "water" in beverages:
    print("water in beverages")
tuple_1=(fruits[0],vegetables[0],beverages[0])
print(tuple_1)