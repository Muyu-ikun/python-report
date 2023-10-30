def find_outlier(integers):

    first_three_paritys = [n % 2 for n in integers[:3]]

    if sum(first_three_paritys) < 2:
        for n in integers:
            if n % 2 == 1 :
                return n

    else:
        for n in integers:
            if n % 2 == 0:
                return n

    return None