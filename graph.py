all_nodes = []

for x in range(20):
    for y in range(10):
        all_nodes.append([x, y])


def neighbors(node):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for dir in dirs:
        neighbor = [node[0] + dir[0], node[1] + dir[1]]
        if neighbor in all_nodes:
            result.append(neighbor)
    return result

sample_neighbors = neighbors(all_nodes[0])
sample_neighbors2 = neighbors(all_nodes[1])
print(sample_neighbors)
print(sample_neighbors2)
print(all_nodes[0])
print(all_nodes[1])
