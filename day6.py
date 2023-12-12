"""
Puzzle Input:
Time:        56     97     78     75
Distance:   546   1927   1131   1139
"""


def ways_to_win(race_time, record_dist):
    num_ways_to_win = 0
    for hold_time in range(race_time):
        speed = hold_time
        travel_time = race_time - hold_time
        total_distance = speed * travel_time
        if total_distance > record_dist:
            num_ways_to_win += 1
    return num_ways_to_win


def join_list_elements(list_elements):
    return int(''.join(map(str, list_elements)))


if __name__ == '__main__':
    times = [56, 97, 78, 75]
    record_dists = [546, 1927, 1131, 1139]

    total_ways_to_win = 1
    for i in range(len(times)):
        total_ways_to_win *= ways_to_win(times[i], record_dists[i])

    print(f'Part 1: {total_ways_to_win}')

    part2 = ways_to_win(join_list_elements(times),join_list_elements(record_dists))
    print(f'Part 2: {part2}')
