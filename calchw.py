

def find_solution(x):
    equation = (x**3 - (15 * x) +1)
    print("Solution to " + "f(" + str(x) + "): = " + str(equation))
    

point_set = [value for value in range(-4, 5)]

for i in point_set:
    find_solution(i)
