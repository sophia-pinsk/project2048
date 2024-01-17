import pygame
import random
import sys
import os

screen_rect = (0, 0, 650, 650)

pygame.init()

pygame.display.set_caption('2048')

screen = pygame.display.set_mode((650, 650))


# Функция для загрузки изображения
def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


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
        # Цвета для различных значений на доске
        self.colors = {'2': '#8133ff', '4': '#aa33ff', '8': '#c933ff',
                       '16': '#eb33ff', '32': '#ff33eb',
                       '64': '#ff33c2', '128': '#ff337e', '256': '#ff333d',
                       '512': '#ad232a', '1024': '#ad5123', '2048': '#ff5500', '4096': '#ffe100'}
        self.score = score

    # Генерация начальной доски
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
        # Транспонирование матрицы
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
        # Отмена транспонирования и обновление доски
        self.board.clear()
        self.board = [[0] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                self.board[j][i] = new_matrix[i][j]

    # Движение кирпичей вниз
    def move_down(self):
        new_matrix = [[0] * 5 for _ in range(5)]
        # Транспонирование матрицы
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
        # Отмена транспонирования и обновление доски
        self.board.clear()
        self.board = [[0] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                self.board[j][i] = new_matrix[i][j]

    # Получение текущего счета
    def get_score(self):
        return self.score

    # Получение текущей доски
    def get_board(self):
        return self.board

    # Генерация нового блока на доске
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
        # Обновление экрана после добавления нового блока
        self.render(screen)
        pygame.display.flip()

    # Отрисовка доски на экране
    def render(self, screen):
        # Создание прозрачной поверхности для отрисовки
        s = pygame.Surface((600, 600), pygame.SRCALPHA)
        sur = pygame.Surface((108, 108), pygame.SRCALPHA)
        # Заполнение фона
        pygame.draw.rect(s, pygame.Color((20, 20, 20)), (0, 0, 600, 600), 0)
        screen.blit(s, (100, 100))
        # Отрисовка кирпичей на доске
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

    def losing(self):
        f = 0
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == 0:
                    return False
                if j != 4:
                    if self.board[i][j] == self.board[i][j + 1]:
                        f = 1
                if j != 0:
                    if self.board[i][j] == self.board[i][j - 1]:
                        f = 1
                if i != 0:
                    if self.board[i][j] == self.board[i - 1][j]:
                        f = 1
                if i != 4:
                    if self.board[i][j] == self.board[i + 1][j]:
                        f = 1
                if f == 1:
                    return False
        return True

    def winn(self):
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == self.target_score:
                    return True
        return False


class Button:
    def create_button(self, surface, color, x, y, length, height, text, text_color):
        # Отрисовка кнопки
        surface = self.draw_button(surface, color, length, height, x, y)
        surface = self.write_text(surface, text, text_color, length, height, x, y)
        self.rect = pygame.Rect(x, y, length, height)
        return surface

    def write_text(self, surface, text, text_color, length, height, x, y):
        # Отображение текста на кнопке
        myText = font2.render(text, 1, text_color)
        surface.blit(myText, ((x + length / 2) - myText.get_width() / 2, (y + height / 2) - myText.get_height() / 2))
        return surface

    def draw_button(self, surface, color, length, height, x, y):
        # Создание поверхности для кнопки и ее отрисовка
        sur = pygame.Surface((length, height), pygame.SRCALPHA)
        pygame.draw.rect(sur, pygame.Color(color), (0, 0, length, height), 0)
        screen.blit(sur, (x, y))
        return surface

    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
        return False


def start_screen():
    screen.blit(fon, (0, 0))
    font = pygame.font.SysFont('calibri', 80)
    string_rendered = font.render('2048', 1, pygame.Color('black'))
    screen.blit(string_rendered, (315, 60))
    # Создание кнопок
    button_normal = Button()
    button_normal.create_button(screen, (25, 25, 25, 127), 160, 200, 220, 80, 'Начать обычную игру', (255, 255, 255))

    button_hard = Button()
    button_hard.create_button(screen, (25, 25, 25, 127), 425, 200, 220, 80, 'Начать сложную игру', (255, 255, 255))

    button2 = Button()
    button2.create_button(screen, (25, 25, 25, 127), 250, 330, 300, 80, 'Продолжить игру', (255, 255, 255))

    button3 = Button()
    button3.create_button(screen, (25, 25, 25, 127), 250, 450, 300, 80, 'Правила игры', (255, 255, 255))

    button4 = Button()
    button4.create_button(screen, (25, 25, 25, 127), 250, 570, 300, 80, 'Таблица игроков', (255, 255, 255))

    pygame.display.flip()

    # Обработка событий
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button3.pressed(event.pos):
                    pygame.display.flip()
                    rules_window()
                    return
                if button2.pressed(event.pos):
                    pygame.display.flip()
                    game(0)
                    return
                if button_normal.pressed(event.pos):
                    pygame.display.flip()
                    new_game_window(difficulty='normal')
                    return
                if button_hard.pressed(event.pos):
                    pygame.display.flip()
                    new_game_window(difficulty='hard')
                    return
        pygame.display.flip()


# Функция завершения работы программы
def terminate():
    pygame.quit()
    sys.exit()


def rules_window():
    screen.blit(fon, (0, 0))
    intro_text = [
        'Ваша задача в этой увлекательной игре — собрать кирпич с цифрой «2048».',
        'В начале игры вам предоставляются два кирпичика с цифрой «2». Нажимая',
        'кнопки вверх, вправо, влево или вниз, все ваши кирпичи смещаются в ',
        'выбранном направлении. При столкновении клеток с одинаковым ',
        'числовым значением они объединяются, создавая сумму, вдвое большую.',
        'Игра продолжается до тех пор, пока все пустые ячейки не заполнятся,',
        'и вы больше не сможете перемещать кирпичи ни в одном из направлений.',
        'Или же, конечно, когда на одном из кирпичей появится долгожданная цифра 2048.',
        'Завершив игру, ваш результат заносится в турнирную таблицу,',
        'отражая вашу мастерство в этом увлекательном кроссворде цифр.',
        'Сможете ли вы достичь заветной цифры 2048 и войти в историю игры?',
        'Сыграйте, чтобы узнать!'
    ]
    rules_text = font.render('Правила игры', 1, pygame.Color('black'))
    screen.blit(rules_text, (250, 20))
    text_coord = 180
    for line in intro_text:
        string_rendered = font2.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    button_back.create_button(screen, (25, 25, 25, 127), 250, 650, 300, 80, 'Вернуться назад', (255, 255, 255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_back.pressed(event.pos):
                    start_screen()
                    return
        pygame.display.flip()


def new_game_window(difficulty='normal'):
    screen.blit(fon, (0, 0))
    text = font.render('Введите свое имя', 1, pygame.Color('black'))
    screen.blit(text, (255, 40))
    button_back.create_button(screen, (25, 25, 25, 127), 450, 650, 300, 80, 'Вернуться назад', (255, 255, 255))
    sur = pygame.Surface((300, 50), pygame.SRCALPHA)
    pygame.draw.rect(sur, pygame.Color(25, 25, 25), (0, 0, 300, 50), 0)
    screen.blit(sur, (250, 300))
    warning = font2.render('Максимальный размер ника - 20 символов', 1, pygame.Color('black'))
    screen.blit(warning, (220, 360))
    new_game_button = Button()
    new_game_button.create_button(screen, (25, 25, 25, 127), 50, 650, 300, 80, 'Начать игру', (255, 255, 255))
    text = ''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_back.pressed(event.pos):
                    start_screen()
                if new_game_button.pressed(event.pos) and len(text) > 1:
                    game(1, text, difficulty)
                    return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    if len(text) <= 20:
                        text += str(event.unicode)
                    else:
                        pass
                if len(text) < 21:
                    pygame.draw.rect(sur, pygame.Color(25, 25, 25), (0, 0, 300, 50), 0)
                    screen.blit(sur, (250, 300))
                    txt_surface = font2.render(text, True, pygame.Color('white'))
                    screen.blit(txt_surface, (250, 310))
                else:
                    pass
            pygame.display.flip()


def game(flag, name=False, difficulty='normal'):
    with open('save.txt') as f:
        read_data = [(i.rstrip('/n')).split() for i in f.readlines()]
    a = ([[int(j) for j in i] for i in read_data[:-2]])
    if len(a) > 1 and flag == 0:
        name = read_data[-1][0]
        score = int(read_data[-2][0])
    if flag == 1:
        f = open("save.txt", 'w')
        f.write('')
        f.close()
        a = []
        score = 0
    if (flag == 1) or (len(a) > 1 and flag == 0):
        screen.blit(fon, (0, 0))
        board = Board(a, score, difficulty)
        board.render(screen)
        score = str(board.get_score())
        font3 = pygame.font.SysFont('calibri', 30)

        # Создание прозрачных поверхностей для текста
        score_surface = pygame.Surface((200, 50), pygame.SRCALPHA)
        name_surface = pygame.Surface((200, 50), pygame.SRCALPHA)

        score_text = font3.render("Очки:" + score + ' ', True, (0, 0, 0))
        name_text = font3.render("Игрок:" + name + ' ', True, (0, 0, 0))

        score_surface.blit(score_text, (0, 0))
        name_surface.blit(name_text, (0, 0))

        screen.blit(score_surface, (185, 50))
        screen.blit(name_surface, (450, 50))

        button_menu = Button()

        button_menu.create_button(screen, (25, 25, 25, 127),
                                  160, 720, 500, 70, 'Сохранить игру и вернуться в главное меню', (255, 255, 255))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        board.move_left()
                        board.render(screen)
                        board.new_block()
                    if event.key == pygame.K_RIGHT:
                        board.move_right()
                        board.render(screen)
                        board.new_block()
                    if event.key == pygame.K_UP:
                        board.move_up()
                        board.render(screen)
                        board.new_block()
                    if event.key == pygame.K_DOWN:
                        board.move_down()
                        board.render(screen)
                        board.new_block()
                    score = str(board.get_score())
                    score_text = font3.render("Очки:" + score + ' ', True, (0, 0, 0), (255, 255, 255))
                    screen.blit(score_text, (185, 50))
                    name_text = font3.render("Игрок:" + name + ' ', True, (0, 0, 0), (250, 250, 250))
                    screen.blit(name_text, (450, 50))
                    pygame.display.flip()
                    if board.winn():
                        board.render(screen)
                        file = open("table.txt", 'a')
                        file.write(str(name) + ' ' + str(score) + '\n')
                        file.close()
                        if flag == 0:
                            f = open("save.txt", 'w')
                            f.write('')
                            f.close()
                        pygame.time.delay(2500)
                        game_over(score, 1)
                        return
                    if board.losing():
                        board.render(screen)
                        if flag == 0:
                            f = open("save.txt", 'w')
                            f.write('')
                            f.close()
                        file = open("table.txt", 'a')
                        file.write(str(name) + ' ' + str(score) + '\n')
                        file.close()
                        pygame.time.delay(2500)
                        game_over(score, 0)
                        return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_menu.pressed(event.pos):
                        remember_board = board.get_board()
                        f = open("save.txt", 'w')
                        for i in remember_board:
                            for j in i:
                                f.write(str(j) + ' ')
                            f.write('\n')
                        f.write(score)
                        f.write('\n')
                        f.write(name)
                        f.close()
                        start_screen()
                        return
            pygame.display.flip()
    else:
        start_screen()
        return


# Функция завершения игры
def game_over(score, f):
    screen.blit(fon, (0, 0))
    if f == 1:
        text = font.render('Победа!', True, (184, 134, 11))
        image = load_image("pobeda.png", -1)
        screen.blit(image, (800 // 2 - image.get_width() / 2, 0))
    else:
        text = font.render('Игра окончена', True, (255, 255, 255))
    screen.blit(text, (800 // 2 - text.get_width() / 2, 800 // 2 - text.get_height() / 2))
    text2 = font.render('Очки:' + score, True, (255, 255, 255))
    screen.blit(text2, (800 // 2 - text2.get_width() / 2, 800 // 2 - text.get_height() / 2 + 100))
    button_menu = Button()
    button_menu.create_button(screen, (25, 25, 25, 127),
                              250, 650, 300, 80, 'Вернуться в главное меню', (255, 255, 255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_menu.pressed(event.pos):
                    start_screen()
                    return
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('2048')
    size = WIDTH, HEIGHT = 800, 800
    screen = pygame.display.set_mode(size)
    fon = pygame.transform.scale(load_image('фон 2.jfif'), (WIDTH, HEIGHT))
    font2 = pygame.font.SysFont('calibri', 20)
    font = pygame.font.SysFont('calibri', 40)
    clock = pygame.time.Clock()
    button_back = Button()
    running = True
    while running:
        screen.fill((0, 0, 0))
        start_screen()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
