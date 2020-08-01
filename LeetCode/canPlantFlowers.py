def canPlaceFlowers(flowerbed, n):

    canPlantN = True
    for i in range(0, len(flowerbed)):
        if flowerbed[i] == 1:
            if i > 0:
                # check both sides
                if flowerbed[i+1] > 0 or flowerbed[i-1] > 0:
                    return False

            # check only front
            else:
                if i == len(flowerbed)-1:
                    if flowerbed[i-1] > 0:
                        return False

                if flowerbed[i+1] > 0:
                    return False


def test():
    flowerBed = [1, 0, 0, 0, 1]
    n = 1
    canPlaceFlowers(flowerBed, 1)


test()
