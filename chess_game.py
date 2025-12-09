import pygame
import sys

# Constants
WIDTH, HEIGHT = 640, 640
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
WHITE = (232, 235, 239)
BLACK = (125, 135, 150)


def draw_board(win):
    win.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            if (row + col) % 2 == 1:
                pygame.draw.rect(win, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_pieces(win, board):
        for row in range(ROWS):
            for col in range(COLS):
                piece = board[row][col]
                if piece == 0:
                    continue
                color = (0, 0, 0) if piece < 0 else (255, 255, 255)
                pygame.draw.circle(
                    win,
                    color,
                    (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                    SQUARE_SIZE // 3
                )


def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))

    # Simple board: 1=white, -1=black, 0=empty
    # Pawns (1 row), Rooks, Knights, Bishops, Queen, King
    board = [
        [-2, -3, -4, -5, -6, -4, -3, -2],
        [-1]*8,
        [0]*8,
        [0]*8,
        [0]*8,
        [0]*8,
        [1]*8,
        [2, 3, 4, 5, 6, 4, 3, 2]
    ]
    selected = None

    pygame.display.set_caption('Chess Game')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_board(win)
        pygame.display.flip()


if __name__ == "__main__":
    main()
