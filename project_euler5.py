from math import factorial

stuffs = []
upper = factorial(20)

for value in range(0, upper, 20):
    if value % 1 == 0:
        if value % 2 == 0:
            if value % 3 == 0:
                if value % 4 == 0:
                    if value % 5 == 0:
                        if value % 6 == 0:
                            if value % 7 == 0:
                                if value % 8 == 0:
                                    if value % 9 == 0:
                                        if value % 10 == 0:
                                            if value % 11 == 0:
                                                if value % 12 == 0:
                                                    if value % 13 == 0:
                                                        if value % 14 == 0:
                                                            if value % 15 == 0:
                                                                if value % 16 == 0:
                                                                    if value % 17 == 0:
                                                                        if value % 18 == 0:
                                                                            if value % 19 == 0:
                                                                                if value % 20 == 0:
                                                                                    stuffs.append(value)
print(stuffs[1])


