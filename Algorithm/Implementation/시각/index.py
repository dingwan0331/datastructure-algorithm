def find_three_in_time(h):
    count = 0 

    for hour in range(h+1):
        for min in range(60):
            for sec in range(60):
                count += 1
                if '3' in str(h) + str(min) + str(sec):
                    count += 1
    return count