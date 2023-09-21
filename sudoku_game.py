import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_SIZE = 540
GRID_SIZE = 9
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Sudoku puzzle (0 represents empty cells)
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Create the game window
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Sudoku")

# Function to draw the Sudoku grid
def draw_grid():
    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, WINDOW_SIZE), 2)
        pygame.draw.line(screen, BLACK, (0, x), (WINDOW_SIZE, x), 2)

# Function to draw the numbers on the board
def draw_numbers(board):
    font = pygame.font.Font(None, 36)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] != 0:
                text = font.render(str(board[row][col]), True, BLACK)
                x = col * CELL_SIZE + CELL_SIZE // 2 - text.get_width() // 2
                y = row * CELL_SIZE + CELL_SIZE // 2 - text.get_height() // 2
                screen.blit(text, (x, y))

# Function to get the clicked cell based on mouse coordinates
def get_clicked_cell(mouse_pos):
    x, y = mouse_pos
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    return row, col

# Function to clear the selected cell
def clear_cell(board, row, col):
    if board[row][col] != 0:
        board[row][col] = 0

# Function to check if a number can be placed in a cell
def is_valid_move(board, row, col, num):
    # Check the row for duplicates
    if num in board[row]:
        return False

    # Check the column for duplicates
    if num in [board[i][col] for i in range(GRID_SIZE)]:
        return False

    # Check the 3x3 subgrid (box) for the same number.
    box_start_row, box_start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_start_row, box_start_row + 3):
        for j in range(box_start_col, box_start_col + 3):
            if board[i][j] == num:
                return False

    return True

# Main game loop
selected_cell = None  # Store the selected cell (row, col)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            selected_cell = get_clicked_cell(mouse_pos)
        elif event.type == pygame.KEYDOWN:
            if selected_cell:
                row, col = selected_cell
                if event.key in (pygame.K_1, pygame.K_KP1):
                    number = 1
                elif event.key in (pygame.K_2, pygame.K_KP2):
                    number = 2
                elif event.key in (pygame.K_3, pygame.K_KP3):
                    number = 3
                elif event.key in (pygame.K_4, pygame.K_KP4):
                    number = 4
                elif event.key in (pygame.K_5, pygame.K_KP5):
                    number = 5
                elif event.key in (pygame.K_6, pygame.K_KP6):
                    number = 6
                elif event.key in (pygame.K_7, pygame.K_KP7):
                    number = 7
                elif event.key in (pygame.K_8, pygame.K_KP8):
                    number = 8
                elif event.key in (pygame.K_9, pygame.K_KP9):
                    number = 9
                elif event.key == pygame.K_BACKSPACE:  # Backspace key clears the cell
                    clear_cell(puzzle, row, col)
                    number = 0
                else:
                    number = 0  # Clear the cell if another key is pressed
                
                if number != 0:
                    if is_valid_move(puzzle, row, col, number):
                        puzzle[row][col] = number

    # Draw the Sudoku grid and numbers
    screen.fill(WHITE)
    draw_grid()
    draw_numbers(puzzle)

    # Highlight the selected cell
    if selected_cell:
        row, col = selected_cell
        pygame.draw.rect(screen, (200, 200, 200), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()