def give_candies(num_candies, people):
    count = 1
    # this list copy is just to keep the function pure
    li = [x for x in people]
    while num_candies >= count:
        print("Count: ", count, "index: ", (count-1) % len(li))
        li[(count-1) % len(li)] += count
        num_candies -= count
        count += 1
    li[(count-1) % len(li)] += num_candies
    return li


print(give_candies(7, [0 for i in range(4)]))
