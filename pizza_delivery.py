availableToppings = ["olive","chicken","cheese","pineapple"]
availableFlavours = ["fajita","afghani","tikka","pineapple"]
usertoppings = []
flag = True
pizza_size = input("Enter Pizza size: ")
uflavour = input("Enter flavour: ")

while flag:

    utopping = input("Enter topping :")


    if utopping == "q":
        break
    elif(utopping in availableToppings):
        
        
        
        if utopping in usertoppings:
            print("Topping already added")
            
        else:
            usertoppings.append(utopping)
            
        
    else:
        print("Topping is not avaible")
        

print(f"Your order of  {uflavour}  {pizza_size}  Pizza is ready with these toppings " ) 
print(*usertoppings, sep = ", ")