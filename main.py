import pygame


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
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(0, 0, 0), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 9)

class SquareSprite2(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (223, 231, 255)
        self.font = pygame.font.Font(None, size//2)
        self.update()

    def update(self):
        self.image.fill(self.color)  # Заполнение цветом
        number = self.font.render('2', True, (0, 0, 0))  # Рендеринг цифры "2"
        number_rect = number.get_rect(center=self.image.get_rect().center)
        self.image.blit(number, number_rect)  # Отрисовка цифры на поверхности

class SquareSprite4(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (213, 221, 255)
        self.font = pygame.font.Font(None, size//2)
        self.update()

    def update(self):
        self.image.fill(self.color)
        number = self.font.render('4', True, (0, 0, 0))
        number_rect = number.get_rect(center=self.image.get_rect().center)
        self.image.blit(number, number_rect) 
        
        
class SquareSprite8(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (203, 211, 255)
        self.font = pygame.font.Font(None, size//2)
        self.update()

    def update(self):
        self.image.fill(self.color)
        number = self.font.render('8', True, (0, 0, 0))
        number_rect = number.get_rect(center=self.image.get_rect().center)
        self.image.blit(number, number_rect)
        
        
class SquareSprite16(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (193, 201, 255)
        self.font = pygame.font.Font(None, size//2)
        self.update()

    def update(self):
        self.image.fill(self.color)
        number = self.font.render('16', True, (0, 0, 0))
        number_rect = number.get_rect(center=self.image.get_rect().center)
        self.image.blit(number, number_rect)

class SquareSprite32(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (183, 191, 255)
        self.font = pygame.font.Font(None, size//2)
        self.update()

    def update(self):
        self.image.fill(self.color)
        number = self.font.render('32', True, (0, 0, 0))
        number_rect = number.get_rect(center=self.image.get_rect().center)
        self.image.blit(number, number_rect)

class SquareSprite64(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (173, 191, 255)
        self.font = pygame.font.Font(None, size//2)
        self.update()

    def update(self):
        self.image.fill(self.color)
        number = self.font.render('64', True, (0, 0, 0))
        number_rect = number.get_rect(center=self.image.get_rect().center)
        self.image.blit(number, number_rect)

class SquareSprite128(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (163, 191, 255)
        self.font = pygame.font.Font(None, size//2)
        self.update()

    def update(self):
        self.image.fill(self.color)
        number = self.font.render('128', True, (0, 0, 0))
        number_rect = number.get_rect(center=self.image.get_rect().center)
        self.image.blit(number, number_rect)

class SquareSprite256(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (153, 181, 255)
        self.font = pygame.font.Font(None, size//2)
        self.update()

    def update(self):
        self.image.fill(self.color)
        number = self.font.render('256', True, (0, 0, 0))
        number_rect = number.get_rect(center=self.image.get_rect().center)
        self.image.blit(number, number_rect)

class SquareSprite512(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (143, 171, 255)
        self.font = pygame.font.Font(None, size//2)
        self.update()

    def update(self):
        self.image.fill(self.color)
        number = self.font.render('512', True, (0, 0, 0))
        number_rect = number.get_rect(center=self.image.get_rect().center)
        self.image.blit(number, number_rect)

class SquareSprite1024(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (133, 161, 255)
        self.font = pygame.font.Font(None, size//2)
        self.update()

    def update(self):
        self.image.fill(self.color)
        number = self.font.render('1024', True, (0, 0, 0))
        number_rect = number.get_rect(center=self.image.get_rect().center)
        self.image.blit(number, number_rect)

class SquareSprite2048(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.color = (123, 151, 255)
        self.font = pygame.font.Font(None, size//2)
        self.update()

    def update(self):
        self.image.fill(self.color)
        number = self.font.render('2048', True, (0, 0, 0)) 
        number_rect = number.get_rect(center=self.image.get_rect().center)
        self.image.blit(number, number_rect)

pygame.init()
size = 1200, 600
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption('Инициализация игры')
board = Board(4, 4)
board.set_view(350, 100, 130)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((250, 250, 250))
    board.render(screen)
    pygame.display.flip()
pygame.quit()
