import pygame
from pygame.locals import *
from itertools import repeat

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
title_font = pygame.font.SysFont('Proza Libre', 80)
instruction_font = pygame.font.SysFont('Work Sans', 40)
instructionEx_font = pygame.font.SysFont('Work Sans', 30)

clock = pygame.time.Clock()
fps = 60
level = 1

screen_width = 1200
screen_height = 900
# 4 rows of 6 faces

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Guess Who')

#define game variables
tile_size = 100
size = 150
clicking = False;
right_clicking = False
listx = []
listy = []
wrongList =[]

rlistx = []
rlisty = []

black = (0,0,0)
count = 1

#load images
bg_img = pygame.image.load('images/background.png')
gameTitleText = title_font.render('Guess Who', False, (0, 0, 20))
instructionLeft = instruction_font.render('Left Click:', False, (0, 0, 20))
instructionLeftText = instructionEx_font.render('Will place an X at cursor', False, (0, 0, 20))

instructionRight = instruction_font.render('Right Click:', False, (0, 0, 20))
instructionRightText = instructionEx_font.render('Will place an O at cursor', False, (0, 0, 20))

#kaito
char1_img = pygame.image.load('images/char1.png')
char1 = pygame.transform.scale(char1_img, (size, size))
char1Label = my_font.render('1', False, (0, 0, 20))

#rollin
char2_img = pygame.image.load('images/char2.png')
char2 = pygame.transform.scale(char2_img, (size, size))
char2Label = my_font.render('2', False, (0, 0, 20))

#dinn
char3_img = pygame.image.load('images/char3.png')
char3 = pygame.transform.scale(char3_img, (size, size))
char3Label = my_font.render('3', False, (0, 0, 20))

#yomi
char4_img = pygame.image.load('images/char4.png')
char4 = pygame.transform.scale(char4_img, (size, size))
char4Label = my_font.render('4', False, (0, 0, 20))

#misa
char5_img = pygame.image.load('images/char5.png')
char5 = pygame.transform.scale(char5_img, (size, size))
char5Label = my_font.render('5', False, (0, 0, 20))

#arkam-
char6_img = pygame.image.load('images/char6.png')
char6 = pygame.transform.scale(char6_img, (size, size))
char6Label = my_font.render('6', False, (0, 0, 20))

#KP-
char7_img = pygame.image.load('images/char7.png')
char7 = pygame.transform.scale(char7_img, (size, size))
char7Label = my_font.render('7', False, (0, 0, 20))

#bear
char8_img = pygame.image.load('images/char8.png')
char8 = pygame.transform.scale(char8_img, (size, size))
char8Label = my_font.render('8', False, (0, 0, 20))

#sugar
char9_img = pygame.image.load('images/char9.png')
char9 = pygame.transform.scale(char9_img, (size, size))
char9Label = my_font.render('9', False, (0, 0, 20))

#leona
char10_img = pygame.image.load('images/char10.png')
char10 = pygame.transform.scale(char10_img, (size, size))
char10Label = my_font.render('10', False, (0, 0, 20))

#salpo-
char11_img = pygame.image.load('images/char11.png')
char11 = pygame.transform.scale(char11_img, (size, size))
char11Label = my_font.render('11', False, (0, 0, 20))

#mikey-
char12_img = pygame.image.load('images/char12.png')
char12 = pygame.transform.scale(char12_img, (size, size))
char12Label = my_font.render('12', False, (0, 0, 20))

#chief
char13_img = pygame.image.load('images/char13.png')
char13 = pygame.transform.scale(char13_img, (size, size))
char13Label = my_font.render('13', False, (0, 0, 20))

#vesper
char14_img = pygame.image.load('images/char14.png')
char14 = pygame.transform.scale(char14_img, (size, size))
char14Label = my_font.render('14', False, (0, 0, 20))

#zodiack
char15_img = pygame.image.load('images/char15.png')
char15 = pygame.transform.scale(char15_img, (size, size))
char15Label = my_font.render('15', False, (0, 0, 20))

#mitsu-
char16_img = pygame.image.load('images/char16.png')
char16 = pygame.transform.scale(char16_img, (size, size))
char16Label = my_font.render('16', False, (0, 0, 20))

x_img = pygame.image.load('images/wrong.png')
wrong_img = pygame.transform.scale(x_img, (size, size))
wrongList.extend(repeat(wrong_img, 24))

o_img = pygame.image.load('images/correct.png')
correct_img = pygame.transform.scale(o_img, (size, size))

class World():
    def __init__(self, data):
        self.tile_list = []
    def draws(self):
        count = 1

        for x in range(10):
            xcor = x * tile_size
            ycor = x * tile_size 
            if x >= 0:
                if x % 2 == 1:
                    pygame.draw.rect(screen, black, pygame.Rect(100, ycor, size, size), 6)    
                    #pygame.draw.rect(screen, black, pygame.Rect(xcor, 100, size, size), 6)    

                    pygame.draw.rect(screen, black, pygame.Rect(300, ycor, size, size), 6)    
                    #pygame.draw.rect(screen, black, pygame.Rect(xcor, 300, size, size), 6)    

                    pygame.draw.rect(screen, black, pygame.Rect(500, ycor, size, size), 6)    
                    #pygame.draw.rect(screen, black, pygame.Rect(xcor, 500, size, size), 6)    

                    pygame.draw.rect(screen, black, pygame.Rect(700, ycor, size, size), 6)    
                    #pygame.draw.rect(screen, black, pygame.Rect(xcor, 700, size, size), 6)      
            

world_data = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 13, 0, 14, 0, 15, 0, 16, 0, 17, 0, 18, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 19, 0, 20, 0, 21, 0, 22, 0, 23, 0, 24, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

world = World(world_data)

run = True

clickNum = 0
rclickNum = 0

while run:
    
    screen.blit(bg_img, (0, 0))
    screen.blit(gameTitleText, (350, 20))
    screen.blit(instructionLeft, (900, 355))
    screen.blit(instructionLeftText, (900, 385))
    screen.blit(instructionRight, (900, 425))
    screen.blit(instructionRightText, (900, 455))

    screen.blit(char1, (100,100))    
    screen.blit(char1Label, (140,250))

    screen.blit(char2, (300,100))
    screen.blit(char2Label, (330,250))

    screen.blit(char3, (500,100))
    screen.blit(char3Label, (540,250))
    
    screen.blit(char4, (700,100))
    screen.blit(char4Label, (725,250))

    screen.blit(char5, (100,300))
    screen.blit(char5Label, (140,450))

    screen.blit(char6, (300,300))
    screen.blit(char6Label, (325,450))
    
    screen.blit(char7, (500,300))
    screen.blit(char7Label, (520,450))

    screen.blit(char8, (700,300))
    screen.blit(char8Label, (715,450))

    screen.blit(char9, (100,500))
    screen.blit(char9Label, (135,650))

    screen.blit(char10, (300,500))
    screen.blit(char10Label, (335,650))

    screen.blit(char11, (500,500))
    screen.blit(char11Label, (535,650))

    screen.blit(char12, (700,500))
    screen.blit(char12Label, (735,650))

    screen.blit(char13, (100,700))
    screen.blit(char13Label, (135,850))

    screen.blit(char14, (300,700))
    screen.blit(char14Label, (325,850))
    
    screen.blit(char15, (500,700))
    screen.blit(char15Label, (480,850))

    screen.blit(char16, (700,700))
    screen.blit(char16Label, (745,850))

    world.draws()   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                clicking = True;
                mx, my = pygame.mouse.get_pos()  
                mousex = mx-75
                mousey = my-75
                clickNum += 1

            if event.button == 3:
                right_clicking = True;
                rx, ry = pygame.mouse.get_pos()  
                rmousex = rx-75
                rmousey = ry-75
                rclickNum += 1

        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                clicking = False;       
                listx.append(mousex)
                listy.append(mousey)
                
            if event.button == 3:
                right_clicking = False;
                rlistx.append(rmousex)
                rlisty.append(rmousey)

    if rclickNum >= 1:
        screen.blit(correct_img, (rmousex, rmousey))

    if clickNum == 1:
        screen.blit(wrong_img, (mousex, mousey))

    if clickNum >= 2:
        for i in range(clickNum):
            screen.blit(wrong_img, (listx[i-1], listy[i-1]))
        screen.blit(wrong_img, (mousex, mousey))
    
    pygame.display.update()

pygame.quit()