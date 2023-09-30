import os
import sys
import msvcrt

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_labyrinth(labyrinth, player_pos):
    clear_console()
    for i, row in enumerate(labyrinth):
        for j, cell in enumerate(row):
            if (i, j) == player_pos:
                print("P", end=" ")
            else:
                print(cell, end=" ")
        print()

def main():
    labyrinth = [
        "##########",
        "#P.......#",
        "#.##.###.#",
        "#.#.....#.#",
        "#.#.#####.#",
        "#.#.#...#.#",
        "#...#.#.#.#",
        "#.##.#.#..#",
        "#....#....#",
        "##########"
    ]

    labyrinth = [list(row) for row in labyrinth]
    
    player_pos = (1, 1)

    while True:
        print_labyrinth(labyrinth, player_pos)

        key = msvcrt.getch().decode('utf-8')

        if key == 'w' and player_pos[0] > 0 and labyrinth[player_pos[0] - 1][player_pos[1]] != '#':
            player_pos = (player_pos[0] - 1, player_pos[1])
        elif key == 's' and player_pos[0] < len(labyrinth) - 1 and labyrinth[player_pos[0] + 1][player_pos[1]] != '#':
            player_pos = (player_pos[0] + 1, player_pos[1])
        elif key == 'a' and player_pos[1] > 0 and labyrinth[player_pos[0]][player_pos[1] - 1] != '#':
            player_pos = (player_pos[0], player_pos[1] - 1)
        elif key == 'd' and player_pos[1] < len(labyrinth[0]) - 1 and labyrinth[player_pos[0]][player_pos[1] + 1] != '#':
            player_pos = (player_pos[0], player_pos[1] + 1)

if __name__ == "__main__":
    main()
