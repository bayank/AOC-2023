import re

"""Determine which games would have been possible if the bag had been loaded with only
12 red cubes, 13 green cubes, and 14 blue cubes.
What is the sum of the IDs of those games?"""


"""Test Data:
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


def string_parser(input_string, r=12, g=13, b=14):
    # Extract Game ID
    match_game_id = re.match(r"Game (\d+):", input_string)
    game_id = int(match_game_id.group(1)) if match_game_id else None

    # Define the possible colors
    possible_colors = ['red', 'green', 'blue']

    # Extract color data for each set
    sets_raw = re.split(r';\s*', input_string.split(":")[1])  # Split sets using ';'

    # Initialize the maximum quantity dictionary with 0 for all possible colors
    max_quantity_per_color = {color: 0 for color in possible_colors}

    # Store color data for each set in a list of dictionaries
    color_data_sets = []
    for set_raw in sets_raw:
        color_data_matches = re.findall(r"(\d+) (\w+)", set_raw)
        color_data = {color: int(quantity) for quantity, color in color_data_matches}
        color_data_sets.append(color_data)

        # Calculate the maximum quantity for each color across all sets
        for color, quantity in color_data.items():
            max_quantity_per_color[color] = max(max_quantity_per_color[color], quantity)

    # Check if any color exceeds the limit
    exceed_limits = any(max_quantity_per_color[color] > limit for color, limit in zip(possible_colors, [r, g, b]))

    # Return 0 if any color exceeds the limit
    if exceed_limits:
        return 0

    # Return the game ID if all quantities are within limits
    return game_id

if __name__ == '__main__':

    count = 0
    with open("day2_input.txt", "r") as f:
        for line in f:
            line = line.strip()
            count += string_parser(line)

    print(f"Answer part 1: {count}")