#adjacency_list = {
#    "A" : ["B","S"],
#    "B" : ["A"],
#    "C" : ["D","E","F","S"],
#    "D" : ["C"],
#    "E" : ["C","H"],
#    "F" : ["C","G"],
#    "G" : ["F","S"],
#    "H" : ["E"],
#    "S" : ["A","C","G"]
#}

adjacency_list = {
    "5": ["3", "7"],
    "3": ["2", "4"],
    "7": ["8"],
    "2": [],
    "4": ["8"],
    "8": []
}

#maze = [
#    [1, 0, 1, 1, 1],
#    [0, 0, 0, 0, 1],
#    [0, 1, 1, 0, 1],
#    [0, 0, 0, 0, 1],
#    [1, 1, 1, 0, 1],
#]


def can_i(x, y):
    print("x, y", x, y)


def solve():
    rows = len(maze)
    cols = len(maze[0])

    for x in range(rows):
        for y in range(cols):
            if maze[x][y] == 0:
                can_i(x, y)


solve()
