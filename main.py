import pygame
import numpy

pygame.init()
size = width, height =600, 600#the size of the screen
screen = pygame.display.set_mode(size)
board = numpy.zeros((3 ,3))
screen.fill((28, 170, 156))
the_title = pygame.display.set_caption('TIC TAC TOE')
running = True
player = 1

def mark_square(row, col, player): #take the position and make the move
    board[row][col] = player
    return board

def draw_lines():# creating the lines of the board
    pygame.draw.line(screen, (23, 145,135), (0,200), (600,200), 15)
    pygame.draw.line(screen, (23, 145,135), (0, 400), (600, 400), 15)
    pygame.draw.line(screen, (23, 145,135), (200, 0), (200, 600), 15)
    pygame.draw.line(screen, (23, 145,135), (400, 0), (400, 600), 15)


def available(row, col):#check the square
    return board[row][col] == 0


def is_board_full():
    for r in range(3):
        for c in range(3):
            if board[r][c] == 0:
                return False
    return True


def draw_fiqures():
    for row in range(3):
        for col in range(3):
            if board [row][col] == 1:
                pygame.draw.circle(screen,(239,231,200), (int(col*200+200/2), int(row*200+200/2)), 60, 10)
            elif board [row][col] == 2:
                pygame.draw.line(screen,(66,66,66),(col*200+55,row*200+200-55),(col*200+200-55,row*200+55),25)
                pygame.draw.line(screen,(66, 66, 66),(col * 200 + 55,row * 200 +55),(col * 200 + 200 - 55, row * 200+200 - 55), 25)


def final_draw_fiqures():
    for row in range(3):
        for col in range(3):
            if board [row][col] == 1:
                pygame.draw.circle(screen,(28, 170, 156), (int(col*200+200/2), int(row*200+200/2)), 60, 10)
            elif board [row][col] == 2:
                pygame.draw.line(screen,(28, 170, 156),(col*200+55,row*200+200-55),(col*200+200-55,row*200+55),25)
                pygame.draw.line(screen,(28, 170, 156),(col * 200 + 55,row * 200 +55),(col * 200 + 200 - 55, row * 200+200 - 55), 25)


def check_win():
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        print(str(player)+' Win')
        return True
    if board[0][0] == board[0][1] == board[0][2] == player or board[1][0] == board[1][1] == board[1][2] == player or \
            board[2][0] == board[2][1] == board[2][2] == player:
        print(str(player) + ' Win')
        return True
    if board[0][0] == board[1][0] == board[2][0] == player or board[0][1] == board[1][1] == board[2][1] == player or board[0][2] == board[1][2] == board[2][2] == player:
       print(str(player)+' Win')
       return True




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:# this check if you have used the mouse
            mouseX = int(event.pos[1]//200)#x
            mouseY = (event.pos[0]//200)#y
            check = available(mouseX, mouseY) #this function chek the if the square is empty or not
            if check:
                if player == 1:
                    mark_square(mouseX, mouseY, 1)
                    player = 2
                elif player == 2:
                    mark_square(mouseX, mouseY, 2)
                    player = 1
                draw_fiqures()
                if check_win():
                   final_draw_fiqures()
                   board = numpy.zeros((3, 3))
                end = is_board_full()
                if end :
                    final_draw_fiqures()
                    board = numpy.zeros((3,3))
    draw_lines()
    pygame.display.update()


