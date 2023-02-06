# curses package, control the terminal
import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


# print the maze
def print_maze(maze, stdscr, path=[]):
    # path , path i wanna draw in the maze
    BLUE = curses.color_pair(1)
    MAGENTA = curses.color_pair(2)

    # loop everything in the maze
    for i, row in enumerate(maze):  # row is list
        for j, value in enumerate(row):  # then numerate over the list
            # make it path in diff color
            if (i, j) in path:
                stdscr.addstr(i, j*2, "X", MAGENTA)
            # then draw to the screen
            else:
                stdscr.addstr(i, j*2, value, BLUE)
            # i row, j column


def find_start(maze, start):  # algorithm
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None


def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)  # start position

    # setup queue and setup iteration, finding neighbor etc
    q = queue.Queue()
    # first in first out
    q.put((start_pos, [start_pos]))  # current position and the path as list
    # has two element -> keep track the current position

    visited = set()  # contain position, currently visited

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()  # clear entire screen
        print_maze(maze, stdscr, path)
        time.sleep(0.3)
        stdscr.refresh()

        # fund end node
        if maze[row][col] == end:
            return path

        # continue branching out, find neighbour in find_neighbors
        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == '#':
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))

            visited.add(neighbor)


def find_neighbors(maze, row, col):
    neighbors = []

    if row > 0:  # up
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  # down
        neighbors.append((row + 1, col))
    if col > 0:  # left
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):  # right
        neighbors.append((row, col + 1))

    return neighbors


def main(stdscr):  # standard output sreen

    # add a color
    # initialize
    # ID, foreground, background
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    # use the color
    blue_and_black = curses.color_pair(1)
    magenta_and_black = curses.color_pair(2)

    # this screen override and takeover our terminal
    # stdscr.clear()  # clear entire screen
    # have to pass position, text, and color
    # stdscr.addstr(5, 5, "Hello world!", blue_and_black)
    # print_maze(maze, stdscr)
    # first val is vertical value, second one is horizonal value
    # stdscr.refresh()
    find_path(maze, stdscr)
    stdscr.getch()  # get character, similiar to input statement in py. wait user hit


# initialized module curses, and call function main
wrapper(main)
