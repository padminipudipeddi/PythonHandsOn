print("MYWAY SANDWICH\n for $5")
toppings =["onion, lettuce, bell pepper, olive, tomatoes"]
print("Toppings:", toppings)
selection = [i for i in (input("Please enter 3 toppings separated by comma:").split(','))]
print("you have entered:", selection)
sandwich_count = int(input("please enter no.of sandwiches:"))
print("you have entered:", sandwich_count)
total = int((sandwich_count * 5))
print("your total is : $", total)