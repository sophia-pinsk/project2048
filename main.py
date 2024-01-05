import pygame
from random import choice


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        pygame.draw.rect(screen, pygame.Color(100, 100, 100),
                         (self.left, self.top, self.cell_size * 4, self.cell_size * 4))
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(10, 10, 10), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 9)


class SquareSprite2(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (223, 231, 255)
        self.font = pygame.font.Font(None, size // 2)
        self.update2()

    def update2(self):
        self.image.fill(self.color)  # Заполнение цветом
        number = self.font.render('2', True, (0, 0, 0))  # Рендеринг цифры "2"
        number_rect = number.get_rect(center=self.image.get_rect().center)
        self.image.blit(number, number_rect)
        screen.blit(self.image, self.rect)


class SquareSprite4(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (213, 221, 255)
        self.font = pygame.font.Font(None, size // 2)
        self.update4()

    def update4(self):
        self.image.fill(self.color)
        number = self.font.render('4', True, (0, 0, 0))
        number_rect = number.get_rect(center=self.image.get_rect().center)
        self.image.blit(number, number_rect)
        screen.blit(self.image, self.rect)


class SquareSprite8(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (203, 211, 255)
        self.font = pygame.font.Font(None, size // 2)
        self.update8()

    def update8(self):
        self.image.fill(self.color)
        number = self.font.render('8', True, (0, 0, 0))
        number_rect = number.get_rect(center=self.image.get_rect().center)
        self.image.blit(number, number_rect)
        screen.blit(self.image, self.rect)


class SquareSprite16(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (193, 201, 255)
        self.font = pygame.font.Font(None, size // 2)
        self.update16()

    def update16(self):
        self.image.fill(self.color)
        number = self.font.render('16', True, (0, 0, 0))
        number_rect = number.get_rect(center=self.image.get_rect().center)
        self.image.blit(number, number_rect)
        screen.blit(self.image, self.rect)


class SquareSprite32(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (183, 191, 255)
        self.font = pygame.font.Font(None, size // 2)
        self.update32()

    def update32(self):
        self.image.fill(self.color)
        number = self.font.render('32', True, (0, 0, 0))
        number_rect = number.get_rect(center=self.image.get_rect().center)
        self.image.blit(number, number_rect)
        screen.blit(self.image, self.rect)


class SquareSprite64(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (173, 191, 255)
        self.font = pygame.font.Font(None, size // 2)
        self.update64()

    def update64(self):
        self.image.fill(self.color)
        number = self.font.render('64', True, (0, 0, 0))
        number_rect = number.get_rect(center=self.image.get_rect().center)
        self.image.blit(number, number_rect)
        screen.blit(self.image, self.rect)


class SquareSprite128(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (163, 191, 255)
        self.font = pygame.font.Font(None, size // 2)
        self.update128()

    def update128(self):
        self.image.fill(self.color)
        number = self.font.render('128', True, (0, 0, 0))
        number_rect = number.get_rect(center=self.image.get_rect().center)
        self.image.blit(number, number_rect)
        screen.blit(self.image, self.rect)


class SquareSprite256(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (153, 181, 255)
        self.font = pygame.font.Font(None, size // 2)
        self.update256()

    def update256(self):
        self.image.fill(self.color)
        number = self.font.render('256', True, (0, 0, 0))
        number_rect = number.get_rect(center=self.image.get_rect().center)
        self.image.blit(number, number_rect)
        screen.blit(self.image, self.rect)


class SquareSprite512(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (143, 171, 255)
        self.font = pygame.font.Font(None, size // 2)
        self.update512()

    def update512(self):
        self.image.fill(self.color)
        number = self.font.render('512', True, (0, 0, 0))
        number_rect = number.get_rect(center=self.image.get_rect().center)
        self.image.blit(number, number_rect)
        screen.blit(self.image, self.rect)


class SquareSprite1024(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (133, 161, 255)
        self.font = pygame.font.Font(None, size // 2)
        self.update1024()

    def update1024(self):
        self.image.fill(self.color)
        number = self.font.render('1024', True, (0, 0, 0))
        number_rect = number.get_rect(center=self.image.get_rect().center)
        self.image.blit(number, number_rect)
        screen.blit(self.image, self.rect)


class SquareSprite2048(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (123, 151, 255)
        self.font = pygame.font.Font(None, size // 2)
        self.update2048()

    def update2048(self):
        self.image.fill(self.color)
        number = self.font.render('2048', True, (0, 0, 0))
        number_rect = number.get_rect(center=self.image.get_rect().center)
        self.image.blit(number, number_rect)
        screen.blit(self.image, self.rect)

def move(direction, screen):
    if direction == "w":
        return moveUp(screen)
    if direction == "s":
        return moveDown(screen)
    if direction == "a":
        return moveLeft(screen)
    if direction == "d":
        return moveRight(screen)


def moveLeft(board):
    shiftLeft(board)
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1] and board[i][j] != 0:
                board[i][j] *= 2
                board[i][j + 1] = 0
                j = 0
    shiftLeft(board)
    return board


def moveUp(board):
    board = rotateLeft(board)
    board = moveLeft(board)
    board = rotateRight(board)
    return board


def moveRight(board):
    shiftRight(board)
    for i in range(4):
        for j in range(3, 0, -1):
            if board[i][j] == board[i][j - 1] and board[i][j] != 0:
                board[i][j] *= 2
                board[i][j - 1] = 0
                j = 0

    # final shift
    shiftRight(board)
    return board


def moveDown(board):
    board = rotateLeft(board)
    board = moveLeft(board)
    shiftRight(board)
    board = rotateRight(board)
    return board


def shiftLeft(board):
    for i in range(4):
        nums, count = [], 0
        for j in range(4):
            if board[i][j] != 0:
                nums.append(board[i][j])
                count += 1
        board[i] = nums
        board[i].extend([0] * (4 - count))


def shiftRight(board):
    for i in range(4):
        nums, count = [], 0
        for j in range(4):
            if board[i][j] != 0:
                nums.append(board[i][j])
                count += 1
        board[i] = [0] * (4 - count)
        board[i].extend(nums)


def rotateLeft(board):
    b = [[board[j][i] for j in range(4)] for i in range(3, -1, -1)]
    return b


def rotateRight(board):
    b = rotateLeft(board)
    b = rotateLeft(b)
    return rotateLeft(b)

pygame.init()
size = 1200, 600

w1 = [(415, 165, 115), (545, 165, 115), (675, 165, 115), (805, 165, 115),
      (415, 295, 115), (545, 295, 115), (675, 295, 115), (805, 295, 115),
      (415, 425, 115), (545, 425, 115), (675, 425, 115), (805, 425, 115),
      (415, 555, 115), (545, 555, 115), (675, 555, 115), (805, 555, 115)]

horizontal1 = [(415, 165, 115), (545, 165, 115), (675, 165, 115), (805, 165, 115)] # создаю координаты горизонтали
horizontal2 = [(415, 295, 115), (545, 295, 115), (675, 295, 115), (805, 295, 115)]
horizontal3 = [(415, 425, 115), (545, 425, 115), (675, 425, 115), (805, 425, 115)]
horizontal4 = [(415, 555, 115), (545, 555115), (675, 555, 115), (805, 555, 115)]
upright1 = [(415, 165, 115), (415, 295, 115), (415, 425, 115), (415, 555, 115)] # создаю координаты вертикали
upright2 = [(545, 165, 115), (545, 295, 115), (545, 425, 115), (545, 555, 115)]
upright3 = [(675, 165, 115), (675, 295, 115), (675, 425, 115), (675, 555, 115)]
upright4 = [(805, 165, 115), (805, 295, 115), (805, 425, 115), (805, 555, 115)]

screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption('Инициализация игры')
board = Board(4, 4)
board.set_view(350, 100, 130)
running = True
s1 = choice(w1)
s2 = choice(w1)
while s2 == s1:
    s2 = choice(w1)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.K_UP:
            s3 = choice(w1)
            while s3 == s1 or s3 == s2:
                s3 = choice(w1)
            SquareSprite4(s3[0], s3[1], s3[2])
            pygame.display.flip()
    screen.fill((30, 30, 30))
    board.render(screen)
    SquareSprite2(s1[0], s1[1], s1[2])
    SquareSprite2(s2[0], s2[1], s2[2])
    pygame.display.flip()
pygame.quit()
