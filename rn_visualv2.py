import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(num_points=100000)

    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(figsize=(10, 6))

    x_values = rw.x_values
    y_values = rw.y_values

    point_numbers = list(range(rw.num_points))
    plt.scatter(x_values, y_values, c=point_numbers, cmap=plt.cm.Blues, 
        edgecolor='none', s=1)
    
    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(x_values[-1], y_values[-1], c='red', edgecolor='none', s=100)
    
    #Remove the axes.
    plt.axes().get_xaxis().set_visible(True)
    plt.axes().get_yaxis().set_visible(True)
    
    plt.show()

    #Keep running? 
    keep_running = input("Make another walk? (press 'n' to quit) ")
    if keep_running == 'n':
        break
