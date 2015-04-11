def travel(travels):
    counter = 0

    for travel in travels:
        if travel >= 23:
            counter += 23
        else:
            counter += travel * 1

        if counter >= 50:
            return 50

    return counter