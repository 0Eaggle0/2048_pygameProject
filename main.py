import pygame, sys, random


pygame.init()
screen = pygame.display.set_mode((450, 550))
pygame.display.set_caption("2048")
font = pygame.font.SysFont('', 50)
clock = pygame.time.Clock()
fps = 10


def main():
    board = []
    for i in range(4):
        board += [["0"] * 4]
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
        name_a_game = font.render("2048", True, pygame.color.Color('orange'))
        screen.blit(name_a_game, (180, 50))
        pygame.draw.rect(screen, pygame.color.Color('purple'), pygame.Rect(20, 125, 410, 410))
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
                    return False
                if checkCell(board, i, j):
                    return False
    return True


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
    screen.fill(pygame.color.Color('black'))
    label = font.render("GAME OVER", True, pygame.color.Color('red'))
    labelRect = label.get_rect()
    labelRect.centerx = screen.get_rect().centerx
    labelRect.centery = screen.get_rect().centery
    screen.blit(label, labelRect)
    event = pygame.event.wait()
    exit(event)


def win():
    screen.fill(pygame.color.Color('black'))
    label = font.render("!!!!! WIN !!!!!", True, pygame.color.Color(0, 255, 0))
    labelRect = label.get_rect()
    labelRect.centerx = screen.get_rect().centerx
    labelRect.centery = screen.get_rect().centery
    screen.blit(label, labelRect)
    event = pygame.event.wait()
    exit(event)


def text_builder(board, i, j):
    if board[j][i] == "0":
        text = font.render(" ", True, pygame.color.Color(227, 219, 51))
    else:
        text = font.render(board[j][i], True, pygame.color.Color(227, 219, 51))
    textRect = text.get_rect()
    textRect.centerx = i * 100 + 75
    textRect.centery = j * 100 + 180
    return text, textRect


def move_manager(board, user_input):
    if not check_lose(board) and not check_win(board):
        move = pushDirection(board, user_input)
        if move != 0:
            new_num(board, 1)
    return board


def pushDirection(board, user_input):
    move = 0
    if user_input == "w":
        i_list, j_list = range(1, 4), range(4)
        i_direction, j_direction = -1, 0
    elif user_input == "s":
        i_list, j_list = range(2, -1, -1), range(4)
        i_direction, j_direction = 1, 0
    elif user_input == "a":
        i_list, j_list = range(4), range(1, 4)
        i_direction, j_direction = 0, -1
    elif user_input == "d":
        i_list, j_list = range(4), range(2, -1, -1)
        i_direction, j_direction = 0, 1

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


if __name__ == "__main__":
    main()