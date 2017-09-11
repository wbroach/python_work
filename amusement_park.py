age = 3
admission_underage4 = 0.00
admission_between4and18 = 5.00
admission_18andup = 10.00

if age < 4:
    print("Your admission cost is " + "$" + str(admission_underage4))
elif age < 18:
    print("Your admission cost is " + "$" + str(admission_between4and18))
else:
    print("Your admission cost is " + "$" + str(admission_18andup))
