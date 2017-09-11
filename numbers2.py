#~ digits = list(range(1,11))
#~ digits.append(0)
#~ print(min(digits))
#~ print(max(digits))
#~ print(sum(digits))

cubes = [value**3 for value in range(1,11)]

for cube in cubes:
    print(cube)

print(cubes[0:3])
