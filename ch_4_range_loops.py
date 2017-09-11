#for value in range(1,1000001):
	#print(value)
#millions = list(range(1,1000001))
#print(min(millions))
#print(max(millions))
#print(sum(millions))
#odds = list(range(1,21,2))
#for odd in odds:
	#print(odd)
#multiples = list(range(3,31,3))
#for multiple in multiples:
	#print(multiple)
#cubes = list(range(1,11))
#for cube in cubes:
	#print(cube**3)
#cubes2 = []
#for value in range(1,11):
	#cube_int = value**3
	#cubes2.append(cube_int)
#print(cubes2)
cubes = [value**3 for value in range(1,11)]
print(cubes)
