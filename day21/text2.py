import pygame

EMPTY = 0
BLACK = 1
WHITE = 2

black_color = (0, 0, 0)
white_color = (255, 255, 255)




class RenjuBoard(object):


    def __init__(self):
        self._board = [[]] * 15
        self.reset()


    def reset(self):
        for row in range(len(self._board)):
            self._board[row] = [EMPTY] * 15

    def move(self, row, col, is_black):
        if self._board[row][col] == EMPTY:
            self._board[row][col] = BLACK if is_black else WHITE
            return True
        return False

    def draw(self, screen):
        for index in range(1, 16):
            pygame.draw.line(screen, black_color, (40, 40 * index), (600, 40 * index), 1)
            pygame.draw.line(screen, black_color, (40 * index, 40), (40 * index, 600), 1)
        pygame.draw.rect(screen, black_color, [36, 36, 568, 568], 4)
        pygame.draw.circle(screen, black_color, [320, 320], 5, 0)
        pygame.draw.circle(screen, black_color, [480, 480], 5, 0)
        pygame.draw.circle(screen, black_color, [160, 160], 5, 0)
        pygame.draw.circle(screen, black_color, [160, 480], 5, 0)
        pygame.draw.circle(screen, black_color, [480, 160], 5, 0)
        for row in range(len(self._board)):
            for col in range(len(self._board[row])):
                if self._board[row][col] != EMPTY:
                    ccolor = black_color if self._board[row][col] == BLACK else white_color
                    pos = [40 * (col + 1), 40 * (row + 1)]
                    pygame.draw.circle(screen, ccolor, pos, 18, 0)

    def game_over1(self):
        count1 = 0
        for row in range(1, 16):
            for col in range(1, 16):
                if self._board[row][col] == BLACK:
                    count1 += 1
                elif self._board[row][col] != BLACK:
                    count1 = 0
            if count1 == 5:
                break
        return True

    def game_over2(self):
        count2 = 0
        for row in range(1, 16):
            for col in range(1, 16):
                if self._board[row][col] == WHITE:
                    count2 += 1
                elif self._board[row][col] != WHITE:
                    count2 = 0
            if count2 == 5:
                break
        return True


def main():
    board = RenjuBoard()
    is_black = True
    pygame.init()
    pygame.display.set_caption('五子棋')
    screen = pygame.display.set_mode([640, 640])
    screen.fill([255, 255, 0])
    board.draw(screen)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                board.reset()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if 20 <= x <= 620 and 20 <= y <= 620:
                    row = round((y - 40) / 40)
                    col = round((x - 40) / 40)
                    if board.move(row, col, is_black):
                        is_black = not is_black
                        board.draw(screen)
                        pygame.display.flip()
                        if board.game_over1():
                            print('黑棋赢')
                        if board.game_over2():
                            print('白棋赢')
    pygame.quit()


if __name__ == '__main__':
    main()