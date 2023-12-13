def find_steps(instructions, graph):
    node = "AAA"
    steps = 0
    instructions = instructions*len(graph)
    for i in instructions:
        steps += 1
        if i == "L":
            node = graph[node][0]
        else:
            node = graph[node][1]
        if node == "ZZZ":
            break
    return steps

def read_file(filename):
    graph = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        # Extract instructions
        instructions = lines[0].strip()
        # Extract graph
        for line in lines[1:]:
            data = line.strip().split(' = ')
            if len(data) == 2:
                node, nodes = data
                left_node, right_node = nodes.strip('()').split(', ')
                graph[node] = (left_node, right_node)
            else:
                print(f"Can't parse line: {line}")
    return instructions, graph



if __name__ == '__main__':
    graph1 = {
        "AAA": ("BBB", "CCC"),
        "BBB": ("DDD", "EEE"),
        "CCC": ("ZZZ", "GGG"),
        "DDD": ("DDD", "DDD"),
        "EEE": ("EEE", "EEE"),
        "GGG": ("GGG", "GGG"),
        "ZZZ": ("ZZZ", "ZZZ")
    }

    graph2 = {
        "AAA": ("BBB", "BBB"),
        "BBB": ("AAA", "ZZZ"),
        "ZZZ": ("ZZZ", "ZZZ")
    }

    #print(find_steps("RL", graph1))
    #print(find_steps("LLR", graph2))

    instructions, graph = read_file('/Users/bayank/PycharmProjects/AOC2023/day8_input.txt')
    print("Instructions:", instructions)
    print("Graph:", graph)
    print(find_steps(instructions, graph))