import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk()

    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(figsize=(10, 6))

    x_values = rw.x_values
    y_values = rw.y_values

    plt.plot(x_values, y_values, linewidth=.1, c='blue')

    # Set chart title and label axes.
    plt.title("Random Walk", fontsize=15)
    plt.xlabel("X", fontsize=10)
    plt.ylabel("Y", fontsize=10)

    # Set size of tick labels.
    plt.tick_params(axis='both', labelsize=14)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolor='none', s=50)
    plt.scatter(x_values[-1], y_values[-1], c='red', edgecolor='none', s=50)
    
    #Remove the axes.
    plt.axes().get_xaxis().set_visible(True)
    plt.axes().get_yaxis().set_visible(True)
    
    plt.show()

    #Keep running? 
    keep_running = input("Make another walk? (press 'n' to quit) ")
    if keep_running == 'n':
        break
