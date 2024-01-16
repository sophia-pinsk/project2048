import pygame
import random


class Board:
    def __init__(self, list, score=0, difficulty='normal'):
        if difficulty == 'normal':
            self.target_score = 2048
        elif difficulty == 'hard':
            self.target_score = 4096
        # Инициализация доски
        if len(list) > 1:
            self.board = list
        else:
            self.board = self.gen_board()
        self.colors = {'2': '#8133ff', '4': '#aa33ff', '8': '#c933ff',
                       '16': '#eb33ff', '32': '#ff33eb',
                       '64': '#ff33c2', '128': '#ff337e', '256': '#ff333d',
                       '512': '#ad232a', '1024': '#ad5123', '2048': '#ff5500', '4096': '#ffe100'}
        self.score = score

    def gen_board(self):
        board = [[0] * 5 for _ in range(5)]
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        x1 = random.randint(0, 4)
        y1 = random.randint(0, 4)
        if (x == x1) and (y == y1):
            if x != 0:
                x -= 1
            else:
                x += 1
        board[x][y] = 2
        board[x1][y1] = 2
        return board

    # Движение кирпичей влево
    def move_left(self):
        for i in self.board:
            while 0 in i:
                i.remove(0)
            while len(i) != 5:
                i.append(0)
        for i in range(5):
            for j in range(4):
                if self.board[i][j] == self.board[i][j + 1] and self.board[i][j] != 0:
                    self.board[i][j] *= 2
                    self.score += self.board[i][j]
                    self.board[i].pop(j + 1)
                    self.board[i].append(0)

    # Движение кирпичей вправо
    def move_right(self):
        for i in self.board:
            while 0 in i:
                i.remove(0)
            while len(i) != 5:
                i.insert(0, 0)
        for i in range(5):
            for j in range(4, 0, -1):
                if self.board[i][j] == self.board[i][j - 1] and self.board[i][j] != 0:
                    self.board[i][j] *= 2
                    self.score += self.board[i][j]
                    self.board[i].pop(j - 1)
                    self.board[i].insert(0, 0)

    # Движение кирпичей вверх
    def move_up(self):
        new_matrix = [[0] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                new_matrix[j][i] = self.board[i][j]
        for i in new_matrix:
            while 0 in i:
                i.remove(0)
            while len(i) != 5:
                i.append(0)
        for i in range(5):
            for j in range(4):
                if new_matrix[i][j] == new_matrix[i][j + 1] and new_matrix[i][j] != 0:
                    new_matrix[i][j] *= 2
                    self.score += new_matrix[i][j]
                    new_matrix[i].pop(j + 1)
                    new_matrix[i].append(0)
        self.board.clear()
        self.board = [[0] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                self.board[j][i] = new_matrix[i][j]

    # Движение кирпичей вниз
    def move_down(self):
        new_matrix = [[0] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                new_matrix[j][i] = self.board[i][j]
        for i in new_matrix:
            while 0 in i:
                i.remove(0)
            while len(i) != 5:
                i.insert(0, 0)
        for i in range(5):
            for j in range(4, 0, -1):
                if new_matrix[i][j] == new_matrix[i][j - 1] and new_matrix[i][j] != 0:
                    new_matrix[i][j] *= 2
                    self.score += new_matrix[i][j]
                    new_matrix[i].pop(j - 1)
                    new_matrix[i].insert(0, 0)
        self.board.clear()
        self.board = [[0] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                self.board[j][i] = new_matrix[i][j]

    # Новый блок на доске
    def new_block(self):
        f = False
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == 0:
                    f = True
        while f:
            x, y = random.randint(0, 4), random.randint(0, 4)
            if self.board[x][y] == 0:
                f = False
                self.board[x][y] = random.choice([2, 4])
        self.render(screen)
        pygame.display.flip()

    def render(self, screen):
        s = pygame.Surface((600, 600), pygame.SRCALPHA)
        sur = pygame.Surface((108, 108), pygame.SRCALPHA)
        pygame.draw.rect(s, pygame.Color((20, 20, 20)), (0, 0, 600, 600), 0)
        screen.blit(s, (100, 100))
        for i in range(5):
            for j in range(5):
                x = 10 * (j + 1) + 108 * j + 100
                y = 10 * (i + 1) + 108 * i + 100
                if self.board[i][j] == 0:
                    text = ''
                    color = (25, 25, 25)
                else:
                    color = self.colors[str(self.board[i][j])]
                    text = str(self.board[i][j])
                pygame.draw.rect(sur, pygame.Color(color), (0, 0, 108, 108), 0)
                screen.blit(sur, (x, y))
                if text:
                    font_size = 108 // 3
                    font = pygame.font.SysFont('calibri', font_size)
                    myText = font.render(text, 1, pygame.Color('white'))
                    screen.blit(myText, (x + 54 - myText.get_width() / 2, y + 54 - myText.get_height() / 2))
