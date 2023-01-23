import os

import pygame, sys, random


pygame.init()
width, height = 450, 550
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2048")
font = pygame.font.SysFont('', 50)
clock = pygame.time.Clock()
col_blocks = 4
fps = 10


def start():
    start_screen()
    game()


def game():
    board = []
    for i in range(col_blocks):
        board += [["0"] * col_blocks]
    new_num(board, 2)
    blocks = []

    for i in range(4):
        for j in range(4):
            blocks.append([pygame.Rect((i * 100) + 30, (j * 100) + 135, 90, 90), pygame.color.Color('white')])

    while True:
        for event in pygame.event.get():
            exit(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    board = move_manager(board, "w")
                if event.key == pygame.K_s:
                    board = move_manager(board, "s")
                if event.key == pygame.K_a:
                    board = move_manager(board, "a")
                if event.key == pygame.K_d:
                    board = move_manager(board, "d")
        screen.fill(pygame.color.Color('white'))
        fon = pygame.transform.scale(load_image('bg.jpg'), (width, height))
        screen.blit(fon, (0, 0))
        name_a_game = font.render("2048", True, pygame.color.Color('orange'))
        screen.blit(name_a_game, (180, 50))
        for block in blocks:
            pygame.draw.rect(screen, block[1], block[0])
        for i in range(4):
            for j in range(4):
                screen.blit(text_builder(board, i, j)[0], text_builder(board, i, j)[1])
        if check_lose(board):
            gameOver()
        elif check_win(board):
            win()
        pygame.display.flip()
        clock.tick(fps)


def exit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


def new_num(board, n):
    for i in range(n):
        newNum = str(random.choice([2, 4]))
        randomx = random.randrange(4)
        randomy = random.randrange(4)
        while board[randomy][randomx] != "0":
            randomx = random.randrange(4)
            randomy = random.randrange(4)
        board[randomy][randomx] = newNum


def check_win(board):
    win = False
    for line in board:
        for num in line:
            if num == "2048":
                win = True
    return win


def check_lose(board):
    no_0 = False

    for element in board:
        no_0 = no_0 or ("0" in element)

    if not no_0:
        board_size = len(board)
        for i in range(board_size):
            for j in range(board_size):
                if board[i][j] == 0:
                    return True
                if checkCell(board, i, j):
                    return True
    return False


def checkCell(board, i, j):
    move_i = []
    move_j = []
    board_size = len(board)
    if i > 0:
        move_i.append(-1)
        move_j.append(0)
    if i < (board_size - 1):
        move_i.append(1)
        move_j.append(0)
    if j > 0:
        move_j.append(-1)
        move_i.append(0)
    if j < (board_size - 1):
        move_j.append(1)
        move_i.append(0)
    for k in range(len(move_i)):
        if board[i + move_i[k]][j + move_j[k]] == board[i][j]:
            return True
    return False


def gameOver():
    text_coord = 50
    while True:
        fon = pygame.transform.scale(load_image('lose.jpg'), (width, height))
        screen.blit(fon, (0, 0))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 310 <= mouse[0] <= 460 and 5 <= 45:
                    start()
        pygame.draw.rect(screen, pygame.Color('purple'), [310, 5, 150, 40])
        string_rendered = font.render('заново', True, pygame.Color('green'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = 5
        intro_rect.x = 320
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

        pygame.display.flip()
        clock.tick(fps)


def win():
    text_coord = 50
    while True:
        fon = pygame.transform.scale(load_image('win.png'), (width, height))
        screen.blit(fon, (0, 0))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 310 <= mouse[0] <= 460 and 5 <= 45:
                    start()
        string_rendered = font.render('заново', True, pygame.Color('green'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = 5
        intro_rect.x = 320
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

        pygame.display.flip()
        clock.tick(fps)


def text_builder(board, i, j):
    if board[j][i] == "0":
        text = font.render(" ", True, pygame.color.Color(227, 219, 51))
    else:
        if board[j][i] == '2':
            text = font.render(board[j][i], True, pygame.color.Color(227, 219, 51))
        elif board[j][i] == '4':
            text = font.render(board[j][i], True, pygame.color.Color(227, 00, 51))
        elif board[j][i] == '8':
            text = font.render(board[j][i], True, pygame.color.Color(154, 197, 0))
        elif board[j][i] == '16':
            text = font.render(board[j][i], True, pygame.color.Color(154, 0, 255))
        elif board[j][i] == '32':
            text = font.render(board[j][i], True, pygame.color.Color(0, 0, 255))
        elif board[j][i] == '64':
            text = font.render(board[j][i], True, pygame.color.Color(255, 0, 255))
        elif board[j][i] == '128':
            text = font.render(board[j][i], True, pygame.color.Color(255, 124, 0))
        elif board[j][i] == '256':
            text = font.render(board[j][i], True, pygame.color.Color(0, 255, 255))
        elif board[j][i] == '512':
            text = font.render(board[j][i], True, pygame.color.Color(154, 205, 50))
        elif board[j][i] == '1024':
            text = font.render(board[j][i], True, pygame.color.Color(47, 79, 79))
        elif board[j][i] == '2048':
            text = font.render(board[j][i], True, pygame.color.Color(0, 255, 0))
        else:
            text = font.render(board[j][i], True, pygame.color.Color(0, 0, 0))
    textRect = text.get_rect()
    textRect.centerx = i * 100 + 75
    textRect.centery = j * 100 + 180
    return text, textRect


def move_manager(board, user_input):
    if not check_lose(board) and not check_win(board):
        move = checkDirection(board, user_input)
        if move != 0:
            new_num(board, 1)
    return board


def checkDirection(board, user_input):
    if user_input == "w":
        i_list, j_list = range(1, 4), range(4)
        i_direction, j_direction = -1, 0
        return pushDirection(i_list, j_list, i_direction, j_direction, board)
    elif user_input == "s":
        i_list, j_list = range(2, -1, -1), range(4)
        i_direction, j_direction = 1, 0
        return pushDirection(i_list, j_list, i_direction, j_direction, board)
    elif user_input == "a":
        i_list, j_list = range(4), range(1, 4)
        i_direction, j_direction = 0, -1
        return pushDirection(i_list, j_list, i_direction, j_direction, board)
    elif user_input == "d":
        i_list, j_list = range(4), range(2, -1, -1)
        i_direction, j_direction = 0, 1
        return pushDirection(i_list, j_list, i_direction, j_direction, board)


def pushDirection(i_list, j_list, i_direction, j_direction, board):
    move = 0
    for i in range(4):
        move += push(board, i_list, j_list, i_direction, j_direction)
    move += add(board, i_list, j_list, i_direction, j_direction)
    for i in range(4):
        move += push(board, i_list, j_list, i_direction, j_direction)
    return move


def add(board, i_list, j_list, i_direction, j_direction):
    move = 0
    for i in i_list:
        for j in j_list:
            if board[i][j] == board[i + i_direction][j + j_direction]:
                board[i + i_direction][j + j_direction] = str(
                    int(board[i][j]) + int(board[i + i_direction][j + j_direction]))
                if board[i][j] != 0:
                    move += 1
                board[i][j] = "0"
    return move


def push(board, i_list, j_list, i_direction, j_direction):
    move = 0
    for i in i_list:
        for j in j_list:
            if board[i + i_direction][j + j_direction] == "0":
                board[i + i_direction][j + j_direction] = board[i][j]
                if board[i][j] != 0:
                    move += 1
                board[i][j] = "0"
    return move


def start_screen():
    fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    text_coord = 50
    intro_text = ['PLAY', 'Об игре']
    text_cor = [180, 315, 345, 10]

    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 175 <= mouse[0] <= 275 and 340 <= 380:
                    return
                elif 310 <= mouse[0] <= 460 and 5 <= 45:
                    info()
        pygame.draw.rect(screen, pygame.Color('purple'), [175, 340, 100, 40])
        pygame.draw.rect(screen, pygame.Color('purple'), [310, 5, 150, 40])
        for i in range(2):
            text(intro_text[i], text_coord, text_cor[i], text_cor[i + 2])
        pygame.display.flip()
        clock.tick(fps)


def text(text, text_coord, x, y):
    string_rendered = font.render(text, True, pygame.Color('green'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = y
    intro_rect.x = x
    text_coord += intro_rect.height
    screen.blit(string_rendered, intro_rect)


def info():
    font = pygame.font.SysFont('', 40)
    screen = pygame.display.set_mode((1500, 600))
    text1 = ['Приветствую тебя в игре 2048!',
              '',
              'Основное управление в игре:',
                  'Вверх - W',
                  'Вниз - S',
                  'Влево - A',
                  'Вправо - D',
              '',
              'Правила:',
                  'С помощью клавиш передвижения (смотреть выше) передвигать блоки.',
                  'Цель — объединить клетки с одинаковым номиналом. Таким образом растет их «вес»: например,',
                  'сначала он составляет 2, на следующем шаге 4, потом — 32, 64, 256. Так нужно дойти до числа 2048.',
                  'Если игроку удается дойти до этой цифры, то игра окончена.',
                  'Игра будет считаться проигранной только тогда когда на поле не останется ни одной пустой клетки!']
    screen.fill(pygame.Color('black'))
    while True:
        text_coord = 50
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 1450 <= mouse[0] <= 1490 and 5 <= mouse[1] <= 45:
                    font = pygame.font.SysFont('', 50)
                    screen = pygame.display.set_mode((width, height))
                    screen.fill(pygame.Color('black'))
                    start()
        for line in text1:
            string_rendered = font.render(line, True, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        pygame.draw.rect(screen, pygame.Color('purple'), [1450, 5, 40, 40])
        text('X', 50, 1458, 10)
        pygame.display.flip()
        clock.tick(fps)


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print(f'В папке отсутствует файл: {name}')
        raise SystemExit(message)
    if color_key == -1:
        color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


if __name__ == "__main__":
    start()
