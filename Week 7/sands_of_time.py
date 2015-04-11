def sands_of_time(n):

    number_dots = 1
    number_stars = n

    star = "*"
    dot = "."

    clock = False

    for a in range(0, n):
        print((number_dots * dot) + (star * number_stars) + (number_dots * dot))

        if clock:
            number_stars += 2
            number_dots -= 1
        else:
            number_dots += 1
            number_stars -= 2

        if number_stars == 1:
            clock = True

sands_of_time(11)