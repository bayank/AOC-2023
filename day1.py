import re


def calibrate_values(input_string):
    # Dictionary to map the words to digits
    word_to_digit = {
    'one': 'on1ne',
    'two': 'tw2wo',
    'three': 'thr3ree',
    'four': 'fou4our',
    'five': 'fiv5ive',
    'six': 'si6ix',
    'seven': 'sev7ven',
    'eight': 'eig8ght',
    'nine': 'nin9ine'
    }

    # Replaces word with digits in the input string
    for word, digit in word_to_digit.items():
        input_string = input_string.replace(word, digit)

    # Find all matches in the input string
    numbers = re.findall(r'\d+', input_string)

    # Extract the first and last numbers
    if numbers:
        first_number = numbers[0]
        last_number = numbers[-1]
        return int(first_number[0] + last_number[-1])
    else:
        return None


if __name__ == '__main__':

    sum = 0

    with open("day1_input.txt", "r") as f:
        for line in f:
            line = line.strip()
            sum += calibrate_values(line)

    print(f"Answer: {sum}")



