import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.magma,
    edgecolor='none', s=40)

plt.title("Y = X Cubed", fontsize=24)
plt.xlabel("X Factor", fontsize=14)
plt.ylabel("Y Factor", fontsize=14)


plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
plt.axis([1, 5100, 0, 100000000000])

plt.show()
