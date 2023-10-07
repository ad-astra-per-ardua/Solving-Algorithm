import sys
mod = 999

def dijkstra(wall_dict, source, dest):
    visited_list = [source]
    to_visit_list = [(node, wall_dict[source]["connections"][node]) for node in wall_dict[source]["connections"]]
    total_cost = mod
    done = False

    while not done:
        short_edge = min(to_visit_list, key=lambda x: x[1])
        node_to_visit, cost = short_edge
        visited_list.append(node_to_visit)
        to_visit_list = [x for x in to_visit_list if x[0] != node_to_visit]
        new_visits = [x for x in wall_dict[node_to_visit]["connections"] if x not in visited_list]

        for location in new_visits:
            if location == dest:
                done = True
                total_cost = wall_dict[node_to_visit]["connections"][dest] + cost
            else:
                new_cost = cost + wall_dict[node_to_visit]["connections"][location]
                to_visit_list.append((location, new_cost))

    return total_cost

def connection(wall_dict, height, width):
    top = {"connections": {}}
    bottom = {"connections": {}}

    for x, y in wall_dict:
        this_block = wall_dict[(x, y)]

        if x == 0:
            top["connections"][(x, y)] = 1
        if x == height - 1:
            this_block["connections"]["bottom"] = 0
        else:
            below_block = wall_dict[(x + 1, y)]
            cost = 0 if this_block["letter"] == below_block["letter"] else 1
            this_block["connections"][(x + 1, y)] = cost
            below_block["connections"][(x, y)] = cost

        if y < width - 1:
            right_block = wall_dict[(x, y + 1)]
            cost = 0 if this_block["letter"] == right_block["letter"] else 1
            this_block["connections"][(x, y + 1)] = cost
            right_block["connections"][(x, y)] = cost

    wall_dict["top"] = top
    wall_dict["bottom"] = bottom

if __name__ == "__main__":
    dataset_count = int(sys.stdin.readline())
    for _ in range(dataset_count):
        height, width = map(int, sys.stdin.readline().split())
        wall_dict = {}

        for i in range(height):
            row = sys.stdin.readline().strip()
            if len(row) != width:
                sys.exit(f"ERROR: Invalid width of line '{row}' (should be {width})!")
            for j in range(width):
                wall_dict[(i, j)] = {"letter": row[j], "connections": {}}

        connection(wall_dict, height, width)
        print(dijkstra(wall_dict, "top", "bottom"))
