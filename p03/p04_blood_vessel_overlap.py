# create blood vessel dictionary, defined like the following:
# vessel: [x1,y1,x2,y2]

blood_vessels = {
    1: [0, 9, 5, 9],
    2: [8, 0, 0, 8],
    3: [9, 4, 3, 4],
    4: [2, 2, 2, 1],
    5: [7, 0, 7, 4],
    6: [6, 4, 2, 0],
    7: [0, 9, 2, 9],
    8: [3, 4, 1, 4],
    9: [0, 0, 8, 8],
    10: [5, 5, 8, 2]
}

for x in blood_vessels.values():
    print(x)