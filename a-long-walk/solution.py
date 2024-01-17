def solution(input):
    # Convert string to 2D char array. idc if it takes long just for sanity
    char_array = [list(line) for line in input.split('\n')]
    visited = [[False for i in range(len(char_array[0]))] for j in range(len(char_array))]

    # Find start column
    startCol = 0
    for i in range(len(char_array[0])):
        char = char_array[0][1]
        if char == '.':
            startCol = i

    return maxPathLen(input, visited, 0, startCol, 0)


def maxPathLen(input, visited, row, col, currLen):

    return 0

def main():
    input0 = '''#.###########################################################################################################################################
    #.............#...#...###...#...#.......#...###...#...#...#.....#...#...#...###...#...#...#.....###...#.....#...#####...#...#...............#
    #############.#.#.#.#.###.#.#.#.#.#####.#.#.###.#.#.#.#.#.#.###.#.#.#.#.#.#.###.#.#.#.#.#.#.###.###.#.#.###.#.#.#####.#.#.#.#.#############.#
    #.............#.#...#.#...#.#.#...#.....#.#...#.#.#.#.#.#.#.#...#.#.#.#.#.#.#...#.#.#.#.#.#.#...#...#.#...#...#...#...#.#.#.#.......#.......#
    #.#############.#####.#.###.#.#####.#####.###.#.#.#.#.#.#.#.#.###.#.#.#.#.#.#.###.#.#.#.#.#.#.###.###.###.#######.#.###.#.#.#######.#.#######
    #.............#.....#.#...#.#.#.....#...#.#...#.#.#.#.#.#...#...#.#...#.#.#.#...#.#.#.#.#.#.#...#...#.###.....#...#...#...#...#...#.#.......#
    #############.#####.#.###.#.#.#.#####.#.#.#.###.#.#.#.#.#######.#.#####.#.#.###.#.#.#.#.#.#.###.###.#.#######.#.#####.#######.#.#.#.#######.#
    #.............#...#.#.#...#.#.#...>.>.#.#.#.###.#.#.#...#.......#.....#.#.#.###.#.#.#.#.#...#...#...#.#...#...#.#...#.....#...#.#.#.#.....#.#
    #.#############.#.#.#.#.###.#.#####v###.#.#.###.#.#.#####.###########.#.#.#.###.#.#.#.#.#####.###.###.#.#.#.###.#.#.#####.#.###.#.#.#.###.#.#
    #.........#...#.#.#.#.#...#...#...#.#...#.#.###.#.#.#.....#...#####...#.#.#...#.#.#.#.#.....#...#...#...#.#...#.#.#.#...#.#...#.#.#.#...#.#.#
    #########.#.#.#.#.#.#.###.#####.#.#.#.###.#.###.#.#.#.#####.#.#####.###.#.###.#.#.#.#.#####.###.###.#####.###.#.#.#.#.#.#.###.#.#.#.###.#.#.#
    #.........#.#.#.#...#...#.#...#.#.#.#.#...#.#...#.#.#.....#.#.#.>.>.#...#.#...#.#.#.#.###...#...###.....#.....#.#.#...#.#.#...#.#...#...#...#
    #.#########.#.#.#######.#.#.#.#.#.#.#.#.###.#.###.#.#####.#.#.#.#v###.###.#.###.#.#.#.###.###.#########.#######.#.#####.#.#.###.#####.#######
    #.#.......#.#.#...#.....#...#...#.#.#...###.#.###.#.....#...#.#.#.###.....#...#.#...#...#.#...#...#...#.......#...#...#.#.#...#.#...#...#...#
    #.#.#####.#.#.###.#.#############.#.#######.#.###.#####.#####.#.#.###########.#.#######.#.#.###.#.#.#.#######.#####.#.#.#.###.#.#.#.###.#.#.#
    #.#.#.....#.#.###.#...#...#.....#.#.....###.#.###.#...#.#.....#.#.#.....#.....#.....#...#.#.###.#.#.#.###...#.......#.#.#...#...#.#...#...#.#
    #.#.#.#####.#.###.###.#.#.#.###.#.#####.###.#.###.#.#.#.#.#####.#.#.###.#.#########.#.###.#.###.#.#.#.###.#.#########.#.###.#####.###.#####.#
    #...#.#.....#.#...#...#.#.#...#.#.#...#...#...###.#.#...#.......#...#...#.>.>...#...#.#...#...#.#...#.>.>.#.#.....#...#...#.#.....###...#...#
    #####.#.#####.#.###v###.#.###.#.#.#.#.###.#######.#.#################.#####v###.#.###.#.#####.#.#######v###.#.###.#.#####.#.#.#########.#.###
    ###...#.....#...###.>.#.#.....#...#.#...#.......#.#.###...###.........#.....#...#.#...#.....#.#.....###...#.#...#.#.....#...#.....#...#.#...#
    ###.#######.#######v#.#.###########.###.#######.#.#.###.#.###.#########.#####.###.#.#######.#.#####.#####.#.###.#.#####.#########.#.#.#.###.#
    #...#...#...#.......#...#...........###.........#...#...#.....#...#...#.....#.....#.....#...#...#...#.....#.#...#.......#.......#...#.#.#...#
    #.###.#.#.###.###########.###########################.#########.#.#.#.#####.###########.#.#####.#.###.#####.#.###########.#####.#####.#.#.###
    #.#...#.#.###...###...###.#.................#.....#...#.....#...#...#.###...###...#...#...#####.#.###.....#.#.....#...#...#...#.......#...###
    #.#.###.#.#####.###.#.###.#.###############.#.###.#.###.###.#.#######.###.#####.#.#.#.#########.#.#######.#.#####.#.#.#.###.#.###############
    #.#.###...#...#.....#...#...#...............#.#...#.#...#...#.#.......#...#...#.#.#.#.#...###...#.....#...#.......#.#.#.....#.......#.......#
    #.#.#######.#.#########.#####.###############.#.###.#.###.###.#.#######.###.#.#.#.#.#.#.#.###.#######.#.###########.#.#############.#.#####.#
    #.#...#.....#.....#...#.....#.................#...#...#...#...#.....#...#...#...#.#.#...#...#.........#.....#...#...#.#...###.......#.#.....#
    #.###.#.#########.#.#.#####.#####################.#####.###.#######.#.###.#######.#.#######.###############.#.#.#.###.#.#.###.#######.#.#####
    #.#...#.....#...#.#.#.......###.....#...#.......#.#...#...#.#...#...#...#.#.......#.....#...###...#...###...#.#.#...#.#.#...#.........#.....#
    #.#.#######.#.#.#.#.###########.###.#.#.#.#####.#.#.#.###.#.#.#.#.#####.#.#.###########.#.#####.#.#.#.###v###.#.###.#.#.###.###############.#
    #...#...###...#.#...###.....#...###...#...#####...#.#.###...#.#.#.#...#...#.......#...#.#.#...#.#.#.#.#.>.>.#.#...#.#.#...#.#...#...#...#...#
    #####.#.#######v#######.###.#.#####################.#.#######.#.#.#.#.###########.#.#.#.#.#.#.#.#.#.#.#.#v#.#.###.#.#.###.#.#.#.#v#.#.#.#.###
    #...#.#.#...###.>.#...#...#.#.###...#####...###...#.#.#.......#...#.#.#...#.......#.#...#...#.#.#.#.#...#.#...#...#.#...#.#...#.>.#...#...###
    #.#.#.#.#.#.###v#.#.#.###.#.#v###.#.#####.#.###.#.#.#.#.###########.#.#.#.#.#######.#########.#.#.#.#####.#####.###.###.#.#######v###########
    #.#...#...#...#.#.#.#.#...#.>.>.#.#...#...#...#.#.#.#.#...........#.#.#.#.#.......#.........#.#.#.#.#.....#...#...#...#.#.#.....#...#...#####
    #.###########.#.#.#.#.#.#####v#.#.###.#.#####.#.#.#.#.###########.#.#.#.#.#######v#########.#.#.#.#.#.#####.#.###.###.#.#.#.###.###.#.#.#####
    #.......#...#.#.#...#.#.#.....#.#.#...#.....#.#.#.#.#.#...###...#.#.#.#.#.#.....>.>.#...#...#...#.#.#.......#...#.#...#.#.#...#.###...#.....#
    #######.#.#.#.#.#####.#.#.#####.#.#.#######.#.#.#.#.#.#.#.###.#.#.#.#.#.#.#.#####v#.#.#.#.#######.#.###########.#.#.###.#.###.#.###########.#
    #.....#...#.#.#...###.#.#.....#...#...#...#.#.#.#.#.#.#.#.###.#.#.#.#.#.#...#.....#.#.#.#.......#...#...........#...#...#...#.#.............#
    #.###.#####.#.###.###.#.#####.#######.#.#.#.#.#.#.#.#.#.#.###.#.#v#.#.#.#####.#####.#.#.#######.#####.###############.#####.#.###############
    #...#.....#.#.#...#...#.#.....#...###.#.#.#.#...#.#.#.#.#.#...#.>.>.#...#...#.....#...#...#...#.#.....#.........#...#...#...#...#...........#
    ###.#####.#.#.#.###.###.#.#####.#.###.#.#.#.#####.#.#.#.#.#.#####v#######.#.#####.#######.#.#.#.#.#####.#######.#.#.###.#.#####.#.#########.#
    #...#...#.#.#...###.....#.#.....#...#.#.#.#.#.....#.#...#.#.#.....#.....#.#.....#.......#...#...#.......#####...#.#.###.#.#.....#.#.........#
    #.###.#.#.#.#############.#.#######.#.#.#.#.#.#####.#####.#.#.#####.###.#.#####.#######.#####################.###.#.###.#.#.#####.#.#########
    #.....#.#.#.###.......###...#...#...#.#.#...#.....#.....#...#.......#...#.....#...#...#.#...#...#...#...#.....#...#...#...#.......#.........#
    #######.#.#.###.#####.#######.#.#.###.#.#########.#####.#############.#######.###.#.#.#.#.#.#.#.#.#.#.#.#.#####.#####.#####################.#
    #.......#.#.....#.....#.......#...###...###...#...#.....###...#...#...#...#...###.#.#...#.#...#.#.#...#.#...#...#...#.....#...###...........#
    #.#######.#######.#####.###################.#.#.###.#######.#.#.#.#.###.#.#.#####.#.#####.#####.#.#####.###.#.###.#.#####.#.#.###.###########
    #.......#.......#.....#...............#...#.#.#.....#...#...#...#...###.#.#.....#.#...###.#.....#...#...###...#...#.......#.#.#...#.........#
    #######.#######.#####.###############.#.#.#.#.#######.#.#.#############.#.#####.#.###.###.#.#######.#.#########.###########.#.#.###.#######.#
    #.......#.....#.#...#.#...#...#.......#.#.#.#...#.....#.#...........#...#.......#.#...#...#...#...#.#...#.....#.............#.#...#.#.......#
    #.#######.###.#.#.#.#.#.#.#.#.#.#######.#.#.###.#.#####.###########.#.###########.#.###.#####.#.#.#.###.#.###.###############.###.#.#.#######
    #.......#.#...#...#...#.#...#.#...#####.#.#.#...#.....#.......#.....#...#.......#.#...#.....#.#.#...#...#...#...#.............###...#...#...#
    #######.#.#.###########.#####.###.#####.#.#.#.#######v#######.#.#######.#.#####.#.###.#####.#.#.#####.#####.###.#.#####################.#.#.#
    #.......#.#.###.........#...#.....#.....#.#.#.#.....>.>.#...#.#...#.....#.#.....#.....#...#.#.#.....#.#...#.#...#.#...#.......#.....###...#.#
    #.#######.#v###.#########.#.#######.#####.#.#.#.#####v#.#.#.#.###.#.#####.#.###########.#.#.#.#####.#.#.#.#.#.###v#.#.#.#####.#.###.#######.#
    #.#.......#.>.#...........#.......#.....#.#.#.#.#...#.#.#.#.#.....#.......#...#...###...#.#.#.#.....#...#...#...>.>.#.#.#.....#...#.........#
    #.#.#######v#.###################.#####.#.#.#.#.#.#.#.#.#.#.#################.#.#.###.###.#.#.#.#################v###.#.#.#######.###########
    #...#...#...#...###.....#.........#.....#.#.#...#.#.#.#...#...#...#...........#.#.#...###.#.#.#.#...............#.#...#.#.#.....#...........#
    #####.#.#.#####.###.###.#.#########.#####.#.#####.#.#.#######.#.#.#.###########.#.#.#####.#.#.#.#.#############.#.#.###.#.#.###.###########.#
    #...#.#.#...#...#...#...#.........#.....#.#...#...#...#.....#...#.#.........#...#.#.....#.#.#.#.#...#.........#...#.....#.#.#...###...#...#.#
    #.#.#.#.###.#.###.###.###########.#####.#.###.#.#######.###.#####.#########.#.###.#####.#.#.#.#.###.#.#######.###########.#.#.#####.#.#.#.#.#
    #.#...#.....#...#...#.#...###...#.#...#.#.....#.........#...#.....#...#####.#...#.......#...#...###...#.......#...#.......#.#.#...#.#.#.#.#.#
    #.#############.###.#.#.#.###.#.#v#.#.#.#################.###.#####.#.#####v###.#######################.#######.#.#.#######.#.#.#.#.#.#v#.#.#
    #.............#...#.#.#.#...#.#.>.>.#...###...............###...#...#...#.>.>.#.#...###...###...###...#.....###.#.#.....#...#.#.#.#.#.>.#...#
    #############.###.#.#.#.###.#.###v#########.###################.#.#####.#.#v#.#.#.#.###.#.###.#.###.#.#####.###.#.#####.#.###.#.#.#.###v#####
    #.............###.#.#.#...#.#...#...###...#...#...#.......###...#.#.....#.#.#...#.#...#.#.#...#.#...#.......#...#...###...#...#.#.#.#...#...#
    #.###############.#.#.###.#.###.###.###.#.###.#.#.#.#####.###.###.#.#####.#.#####.###.#.#.#.###.#.###########.#####.#######.###.#.#.#.###.#.#
    #...............#.#.#.#...#.#...###...#.#.###...#...#...#...#.#...#.#...#.#...###.#...#.#.#...#.#.......###...#.....#...###.....#...#.....#.#
    ###############.#.#.#.#.###.#.#######.#.#.###########.#.###.#.#.###.#.#.#.###.###.#.###.#.###.#.#######.###.###.#####.#.###################.#
    ###.............#...#...###.#.#.......#.#.....#.......#.....#...###...#...###.#...#.....#...#.#.#.....#...#...#...#...#.#...#...#...###...#.#
    ###.#######################.#.#.#######.#####.#.#############################.#.###########.#.#.#.###.###.###.###.#.###.#.#.#.#.#.#.###.#.#.#
    #...#...#.....#.......#...#...#.......#.#.....#.........###...#...###...#...#...###...#.....#.#.#...#.#...###.#...#.#...#.#.#.#.#.#.#...#.#.#
    #.###.#.#.###.#.#####.#.#.###########.#.#.#############.###.#.#.#.###.#.#.#.#######.#.#v#####.#.###.#.#v#####.#.###.#.###.#.#.#.#.#.#v###.#.#
    #...#.#.#.#...#.#.....#.#.....#.......#.#...#...........#...#.#.#.#...#.#.#...#...#.#.>.>.#...#.#...#.>.>.....#.....#.#...#.#.#...#.>.###...#
    ###.#.#.#.#.###.#v#####.#####.#.#######.###.#.###########.###.#.#.#.###.#.###.#.#.#.###v#.#.###.#.#####v#############.#.###.#.#######v#######
    ###...#...#.....#.>.#...#.....#.......#.#...#...........#.#...#.#.#...#.#.###.#.#.#.#...#...###...#.....#.....#...###.#...#...#.......###...#
    #################v#.#.###.###########.#.#.#############.#.#.###.#.###.#.#.###.#.#.#.#.#############.#####.###.#.#.###.###.#####.#########.#.#
    #.................#.#.#...###.......#...#.....#...###...#.#.###.#.#...#...###.#.#...#.....#.........#...#.###...#...#.#...#...#.......#...#.#
    #.#################.#.#.#####.#####.#########.#.#.###.###.#.###.#.#.#########.#.#########.#.#########.#.#.#########.#.#.###.#.#######.#.###.#
    #.#.........#.....#...#.#...#.#.....#...#.....#.#.#...#...#.#...#.#.....###...#...#.......#...#...#...#.#.#.........#...###.#.........#.#...#
    #.#.#######.#.###.#####.#.#.#.#.#####.#.#.#####.#.#.###.###.#.###.#####.###.#####.#.#########.#.#.#.###.#.#.###############.###########.#.###
    #.#.#.......#.#...###...#.#...#...#...#...###...#.#...#.#...#.#...#...#...#...#...#.........#.#.#.#.#...#.#...............#.........#...#...#
    #.#.#.#######.#.#####.###.#######.#.#########.###.###.#.#.###.#.###.#.###.###.#.###########.#.#.#.#.#.###.###############.#########.#.#####.#
    #...#.........#.....#.#...#.......#.........#...#.###.#.#.#...#...#.#...#...#.#.#...........#...#.#.#...#.#...............#.........#.#.....#
    ###################.#.#.###.###############.###.#.###v#.#.#.#####.#.###.###.#.#.#.###############.#.###.#.#.###############.#########.#.#####
    #...#...#...........#...#...#...#...#...#...###.#...>.>.#...#...#.#...#.#...#...#.........###...#...#...#.#...............#.....#.....#.....#
    #.#.#.#.#.###############.###.#.#.#.#.#.#v#####.#####v#######.#.#.###.#.#.###############.###.#.#####.###.###############.#####.#.#########.#
    #.#...#.#...#...........#...#.#.#.#.#.#.>.>...#.#...#.........#.#.....#.#.#...#.........#.....#.....#.#...#.....#...#.....#####...#.........#
    #.#####.###.#.#########.###.#.#.#.#.#.###v###.#.#.#.###########.#######.#.#.#.#.#######.###########.#.#.###.###.#.#.#.#############.#########
    #.....#...#...#.....#...###...#.#.#.#.#...###...#.#.#.......#...###...#...#.#.#.......#.............#.#...#...#...#...#####.........#...#...#
    #####.###.#####.###.#.#########.#.#.#.#.#########.#.#.#####.#.#####.#.#####.#.#######.###############.###.###.#############.#########.#.#.#.#
    #####...#.#...#.###...###...###...#...#.......#...#...#...#...#...#.#.#...#.#.#.....#...........#...#.....###.............#...........#...#.#
    #######.#.#.#.#.#########.#.#################.#.#######.#.#####.#.#.#.#.#.#.#.#.###.###########.#.#.#####################.#################.#
    ###...#.#.#.#.#.....#...#.#.#...###...###.....#.......#.#.#...#.#.#.#.#.#.#.#.#.#...#.......#...#.#.#.....#...............#.................#
    ###.#.#.#.#.#.#####.#.#.#.#.#.#.###.#.###.###########.#.#.#.#.#.#.#.#.#.#.#.#.#.#.###.#####.#.###.#.#.###.#.###############.#################
    #...#...#...#.......#.#.#.#.#.#...#.#.#...#.......###...#.#.#.#.#.#.#.#.#...#.#.#...#.....#.#.#...#.#.#...#...............#.#...............#
    #.###################.#.#.#.#.###.#.#.#.###.#####.#######.#.#.#.#.#.#.#.#####.#.###.#####.#.#.#.###.#.#.#################.#.#.#############.#
    #.......#...#.....###.#.#.#.#.#...#.#.#...#.....#...#.....#.#.#.#.#.#.#...#...#.#...#...#.#...#.#...#.#.#...#...........#.#...#.......#.....#
    #######.#.#.#.###.###.#.#.#.#.#.###.#.###v#####.###.#.#####.#.#.#.#.#.###.#.###.#.###.#.#v#####.#.###.#.#.#.#.#########.#.#####.#####.#.#####
    #.......#.#...#...#...#...#...#.#...#...>.>.#...#...#...###.#.#.#.#.#.#...#.#...#.#...#.>.>.###.#.#...#...#.#.........#.#.#...#.....#.#.....#
    #.#######.#####v###.###########.#.#######v#.#.###.#####v###.#.#.#.#.#.#.###.#.###.#.#####v#.###.#.#.#######.#########.#.#.#.#.#####v#.#####.#
    #.........#...#.>...#...#...###...#...#...#...#...#...>.>...#...#...#.#...#.#.###.#...#...#...#.#.#.......#.#...#.....#...#.#.#...>.#.#.....#
    ###########.#.#v#####.#.#.#.#######.#.#.#######.###.###v#############.###.#.#.###.###.#.#####.#.#.#######.#.#.#.#.#########.#.#.###v#.#.#####
    #...........#.#.......#...#.....#...#.#.......#...#.#...###...#...###...#.#.#.#...#...#.....#.#.#.#...###.#.#.#.#.###.....#.#.#.#...#...#...#
    #.###########.#################.#.###.#######.###.#.#.#####.#.#.#.#####.#.#.#.#.###.#######.#.#.#.#.#.###.#.#.#.#v###.###.#.#.#.#.#######.#.#
    #.#.........#.#.....#.....#.....#...#...#.....###...#.....#.#.#.#.#####.#.#.#.#...#.#.......#.#.#.#.#...#.#.#.#.>.>.#...#.#.#.#.#.#...###.#.#
    #.#.#######.#.#.###.#.###.#.#######.###.#.###############.#.#.#.#.#####.#.#.#.###.#.#.#######.#.#.#.###.#.#.#.###v#.###.#.#.#.#.#.#.#.###.#.#
    #.#.#.....#.#...###.#.#...#.#...###.#...#.........#...###...#...#.....#.#.#...#...#.#.......#...#.#.#...#.#.#.###.#.#...#.#.#.#.#.#.#.....#.#
    #.#.#.###.#.#######.#.#.###.#.#.###.#.###########.#.#.###############.#.#.#####.###.#######.#####.#.#.###.#.#.###.#.#.###.#.#.#.#.#.#######.#
    #...#...#.#.#...###...#...#.#.#.....#...#...#...#.#.#.................#.#...###...#.#.......#...#.#.#...#.#.#.#...#...#...#.#.#.#.#.#.......#
    #######.#.#.#.#.#########.#.#.#########.#.#.#.#.#.#.###################.###.#####.#.#.#######.#.#.#.###.#.#.#.#.#######.###.#.#.#.#.#.#######
    ###...#.#.#...#.........#...#...#.....#.#.#.#.#...#...................#...#.....#...#.........#.#...###...#...#.......#...#.#...#...#...#...#
    ###.#.#.#.#############.#######.#.###.#.#.#.#.#######################.###.#####.###############.#####################.###.#.###########.#.#.#
    #...#...#...#...#.....#.###...#...###.#.#.#.#.#.....#.................###...#...#.............#.#...#...#####...#...#...#.#...#...#...#...#.#
    #.#########.#.#.#.###.#.###.#.#######.#.#.#.#.#.###.#.#####################.#.###.###########.#.#.#.#.#.#####.#.#.#.###.#.###.#.#.#.#.#####.#
    #.........#.#.#.#.###...#...#...###...#...#...#.#...#.........###...#...###...###.........###...#.#...#...#...#.#.#.#...#.#...#.#...#.......#
    #########.#.#.#.#.#######.#####.###.###########.#.###########.###.#.#.#.#################.#######.#######.#.###.#.#.#.###.#.###.#############
    #.........#...#.#.....#...#...#.....#...#...#...#...#...#...#.....#...#.......#.....#...#.......#.......#.#.###...#...###.#.###.............#
    #.#############.#####.#.###.#.#######.#.#.#.#.#####.#.#.#.#.#################.#.###.#.#.#######.#######.#.#.#############.#.###############.#
    #.............#.......#.....#.......#.#.#.#.#...#...#.#.#.#.#.................#...#...#.#.......###.....#.#.......#...###...#...#...........#
    #############.#####################.#.#.#.#.###.#.###.#.#.#.#v###################.#####.#.#########v#####.#######.#.#.#######.#.#.###########
    #.......#.....#...#...#...###.......#.#.#.#.#...#...#.#.#.#.>.>.....#...###...###.....#...###...#.>.>...#.........#.#.#...###.#.#...........#
    #.#####.#.#####.#.#.#.#.#.###.#######.#.#.#.#.#####.#.#.#.#########.#.#.###.#.#######.#######.#.#.#####.###########.#.#.#.###.#.###########.#
    #.....#.#...###.#.#.#...#...#.....#...#...#.#.....#.#.#.#.#...#.....#.#.#...#.#.....#.......#.#...#.....#...#.....#.#...#.#...#...#...#.....#
    #####.#.###.###.#.#.#######.#####.#.#######.#####.#.#.#.#.#.#.#.#####.#.#.###.#.###.#######.#.#####.#####.#.#.###.#.#####.#.#####.#.#.#.#####
    #.....#.....#...#.#.#.......#...#.#.......#.#...#.#.#.#.#.#.#.#.....#.#.#...#.#...#...#.....#.#.....#...#.#.#.#...#.#.....#.....#...#.#.....#
    #.###########.###.#.#.#######.#.#v#######.#.#.#.#.#.#.#.#.#.#.#####.#.#.###.#.###.###.#.#####.#.#####.#.#.#.#.#.###.#.#########.#####.#####.#
    #.#...#.....#...#.#.#.#.....#.#.>.>...#...#.#.#.#.#...#...#.#.......#.#.###.#.###...#.#...#...#.#...#.#...#.#.#.###.#.#.......#.....#.###...#
    #.#.#.#.###.###.#.#.#.#.###.#.#######.#.###.#.#.#.#########.#########.#.###.#.#####.#.###v#.###.#.#.#.#####.#.#.###.#.#.#####.#####.#.###.###
    #...#...#...###.#...#...###.#.#.......#.###...#.#.#.........#...#...#.#.#...#...#...#.#.>.>.#...#.#.#.#...#...#...#.#.#.#.....#...#.#.#...###
    #########.#####.###########.#.#.#######.#######.#.#.#########.#.#.#.#.#.#.#####.#.###.#.#####.###.#.#.#.#.#######.#.#.#.#.#####.#.#.#.#.#####
    #.........#.....#...###...#.#.#...#...#.......#.#.#...#.....#.#.#.#.#.#.#...###.#.###...#.....#...#.#.#.#.........#.#.#.#.#...#.#.#.#.#...###
    #.#########.#####.#.###.#.#.#.###.#.#.#######.#.#.###.#.###.#.#.#.#.#.#.###.###.#.#######.#####.###.#.#.###########.#.#.#.#.#.#.#.#.#.###v###
    #.........#.......#.....#.#.#.#...#.#.....#...#.#.###...###...#.#.#.#.#.#...#...#.......#.....#...#...#.#...#.....#.#.#.#.#.#.#.#.#.#.#.>.###
    #########.###############.#.#.#.###.#####.#.###.#.#############.#.#.#.#.#.###.#########.#####.###.#####.#.#.#.###.#.#.#.#.#.#.#.#.#.#.#.#v###
    #.........#...#...#...#...#.#.#...#.....#.#...#.#.#.............#.#.#.#.#.###...#.....#.....#.#...#.....#.#.#.#...#.#.#.#.#.#.#.#.#.#.#.#.###
    #.#########.#.#.#.#.#.#.###.#.###.#####.#.###.#.#.#.#############.#.#.#.#.#####.#.###.#####.#.#.###.#####.#.#.#.###.#.#.#.#.#.#.#.#.#.#.#.###
    #...........#...#...#...###...###.......#.....#...#...............#...#...#####...###.......#...###.......#...#.....#...#...#...#...#...#...#
    ###########################################################################################################################################.#'''
    input1 = '''#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#'''

    print(solution(input1))




if __name__ == "__main__":
    main()