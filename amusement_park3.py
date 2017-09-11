age = 66


if age < 4:
    price = 0.00
elif age < 18:
    price = 5.00
elif age < 65:
    price = 10.00
elif age >= 65:
    price = 5.00
print("Your admission cost is " + "$" + str(price) + ".\n")
