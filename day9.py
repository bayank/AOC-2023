def calc_diff_list(numlist):
    # Calculate differences between consecutive numbers
    newlist = [numlist[i+1] - numlist[i] for i in range(len(numlist) - 1)]
    return newlist


def check_zero_list(line):
    if type(line) == str:  # Convert string to list of integers if needed
        numlist = list(map(int, line.split(" ")))
    else:
        numlist = line
    # Base case: If all elements are 0, return True
    if all(elem == 0 for elem in numlist):
        return [numlist]

    # Recursive case: Calculate diff list and call function again
    new_diff_list = calc_diff_list(numlist)

    # Get result from recursive call and add current list to it
    result = check_zero_list(new_diff_list)
    result.append(numlist)  # Add current numlist to the result

    return result


def calc_history(line):
    new_list = check_zero_list(line)
    new_list[0].append(0)

    for i in range(1, len(new_list)):
        new_list[i].append((new_list[i][-1]) + (new_list[i - 1][-1]))
    history = new_list[-1][-1]
    return history


if __name__ == "__main__":

    with open("day9_input.txt") as f:
        lines = f.readlines()
        p1 = 0
        for line in lines:
            p1 += calc_history(line.strip())
    print(f'Part 1: {p1}')
