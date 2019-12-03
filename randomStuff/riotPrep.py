def riot1(w, h, data):

    # create empty garden compositions
    garden = [[0 for j in range(w)] for i in range(h)]

    for pair in data:

        t = pair[0]

        row = pair[2]
        col = pair[1]

        garden[row][col] = t

    # replace 0s with 'B's
    for i in range(len(garden)):
        oneGarden = garden[i]

        for j in range(len(oneGarden)):

            if oneGarden[j] == 0:
                garden[i][j] = "B"

    return garden

w = 2
h = 2
data = [["F", 0, 1], ["W", 1, 1]]
ans1 = riot1(w, h, data)
print(ans1)