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
if __name__ == '__main__':
    part1 = (
            (ways_to_win(56,546))
             * (ways_to_win(97, 1927))
             * (ways_to_win(78, 1131))
             * (ways_to_win(75,1139))
    )
    print(f'Part 1: {part1}')

    part2 = ways_to_win(56977875,546192711311139)
    print(f'Part 2: {part2}')