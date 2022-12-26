import pygame, sys, random


def main():
    pygame.init()
    screen = pygame.display.set_mode((450, 550))
    pygame.display.set_caption("2048")
    font = pygame.font.SysFont('', 50)
    clock = pygame.time.Clock()
    fps = 10

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
            exitSceen(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    pass
                if event.key == pygame.K_s:
                    pass
                if event.key == pygame.K_a:
                    pass
                if event.key == pygame.K_d:
                    pass
        screen.fill(pygame.color.Color('white'))
        pygame.draw.rect(screen, pygame.color.Color('green'), pygame.Rect(20, 125, 410, 410))
        for block in blocks:
            pygame.draw.rect(screen, block[1], block[0])
        pygame.display.flip()


def exitSceen(event):
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


if __name__ == "__main__":
    main()