import pygame,time
from pygame.locals import *
pygame.init()
pygame.display.set_caption('2 pic 1 word')
#MENU_SCREEN
screen = pygame.display.set_mode((1280, 720))
bg = pygame.image.load('Picture/bg.gif')
bg = pygame.transform.scale(bg, (1280, 720))
bg = bg.convert()
clock = pygame.time.Clock()
logo = pygame.image.load('Picture/logo.jpg')
font = pygame.font.SysFont('Arial',30)
word = font.render('FUCK                            YOU',True,(0,0,0))
icon_game = pygame.image.load('Picture/logo.jpg')
icon_game = pygame.transform.scale(icon_game,(100,100))
#SOUND
menu_sound = False
play_sound = False
game_over_sound = False
#BUTTON
start = pygame.image.load('Picture/Button/start.png')
start = pygame.transform.scale(start,(170,90))
start_click = pygame.image.load('Picture/Button/start_click.png')
start_click = pygame.transform.scale(start_click,(170,90))
exit_n = pygame.image.load('Picture/Button/exit.png')
exit_click = pygame.image.load('Picture/Button/exit_click.png')
#GAME_PIC
pic1 = ['sun.jpg','egg.jpg','butter.jpg','sun.jpg','rain.jpg','pan.jpg','ear.png',
        'snow.jpg','cat.jpg','wall.jpg','book.jpg','cheese.jpg','bird.jpg','skate.jpg',
        'jelly.jpg','basket.jpg','wheel.jpg','lady.jpg','hand.jpg','rain.jpg','pill.jpg',
        'home.jpg','down.jpg','sun.jpg','arm.jpg','light.jpg','tea.jpg','scare.jpg',
        'cork.jpg','book.jpg','tooth.png','water.jpg','road.jpg','pig.jpeg','dragon.jpeg',
        'grape.jpg','lip.jpg','air.jpg','dish.jpg','cup.jpg','hand.jpg','star.png',
        'cow.jpg','sheet.jpg','back.jpg','honey.jpg','bag.jpg','hose.jpg','pop.jpg',
        'drum.jpg']
pic2 = ['flower.jpg','plant.png','fly.jpg','set.png','coat.jpg','cake.jpg','ring.png','man.jpg',
        'fish.jpg','paper.jpg','shelf.jpg','cake.jpg','bath.jpg','board.jpg','fish.jpg',
        'ball.jpg','chair.jpg','bug.jpg','ball.jpg','bow.jpg','box.jpg','work.jpg',
        'stairs.jpg','glasses.jpg','chair.jpg','house.jpg','pot.jpg','crow.jpg','screw.jpg',
        'worm.png','brush.jpg','melon.jpg','runner.jpg','tail.png','fly.jpg','fruit.jpg',
        'stick.jpg','port.jpg','washer.png','cake.jpg','shake.jpg','fish.jpg','boy.jpg',
        'cloth.jpg','stroke.jpg','moon.jpg','pipe.jpg','pipe.jpg','corn.jpg','stick.jpg']
plus = pygame.image.load('Picture/plus.jpg')
bg_game = pygame.image.load('Picture/bg_game.png')
bg_game = pygame.transform.scale(bg_game,(1280,720))
#ANSWER#
answer = []
integer = ['1','2','3','4','5','6','7','8','9','0']

for a in range(len(pic1)):
    if pic1[a][-1] in integer:
        pic1[a] = pic1[a][:-1]
    if pic2[a][-1] in integer:
        pic2[a] = pic2[a][:-1]
    res = pic1[a][:-4] + pic2[a][:-4]
    answer.append(res)

def text_objects(text,font,color=None):
    if not color:
        color = (0,0,0)
    textsurface = font.render(text,True,color)
    return textsurface, textsurface.get_rect()
def show_text(text,size,position,color=None,fontfam=None):
    if not color:
        color = (0,0,0)
    if not fontfam:
        fontfam = 'fonts/FIPPS___.ttf'
    sizetext = pygame.font.Font(fontfam,size)
    textsurface,textrec = text_objects(text,sizetext,color)
    textrec.center = position
    screen.blit(textsurface,textrec)

def game():
    i = 0
    input_ = ''
    show_input = ''
    set_letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    set_keyboard = [pygame.K_a,pygame.K_b,pygame.K_c,pygame.K_d,pygame.K_e,pygame.K_f,pygame.K_g,pygame.K_h,pygame.K_i,pygame.K_j,pygame.K_k,pygame.K_l,pygame.K_m,pygame.K_n,
                pygame.K_o,pygame.K_p,pygame.K_q,pygame.K_r,pygame.K_s,pygame.K_t,pygame.K_u,pygame.K_v,pygame.K_w,pygame.K_x,pygame.K_y,pygame.K_z,pygame.K_BACKSPACE,pygame.K_SPACE,13,pygame.K_RETURN]
    menu_sound.stop()
    global play_sound,game_over_sound
    if not play_sound:
        play_sound = pygame.mixer.Sound('Sound/Chibi Ninja.wav')
        play_sound.set_volume(.5)
        play_sound.play(loops=-1)
    #GAME
    while True:
        screen.fill(0)
        screen.blit(bg_game,(0,0))
        picture1 = pygame.image.load('Picture/pics1/'+pic1[i])
        picture2 = pygame.image.load('Picture/pics2/'+pic2[i])
        picture1 = pygame.transform.scale(picture1,(500,300))
        picture2 = pygame.transform.scale(picture2,(500,300))
        screen.blit(picture1,(300,200))
        screen.blit(picture2,(900,200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key in set_keyboard:
                if event.key == pygame.K_BACKSPACE:
                    input_ = input_.split('.')
                    del input_[-1]
                    input_ = '.'.join(input_)
                    continue
                elif event.key == pygame.K_SPACE or event.key == 13:
                    #CORRECT
                    if answer[i] == input_:
                        if input_ != '':
                            output = input_.split('.')
                            for a in output:
                                a = int(a) - 97
                                show_input += set_letter[a]
                                show_input = ''
                        input_ = ''
                    else:
                        pygame.display.update()
                        input_ = ''
                else:
                    if input_ == '':
                        input_ += str(event.key)
                    else:
                        input_ += '.' + str(event.key)
            #WRONG
            if input_ != '':
                output = input_.split('.')
                for a in output:
                    a = int(a) - 97
                    show_input += set_letter[a]
            #SHOW_INPUT
            show_text(show_input,30,(640,600),(248,248,255),'fonts//FIPPS___.ttf')
            show_input = ''
            pygame.display.update()
            clock.tick(30)

def button(icon,icon_click,x,y,w,h,order=None,p=None):
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    if p:
        x1 = x+w+10
        x2 = x-10
        y1 = y+h
        y2 = y-10
    else:
        x1 = x+w+10
        x2 = x-10
        y1 = y+h-10
        y2 = y-10
    if (x1>mouse[0]>x2) and (y1>mouse[1]>y2):
        screen.blit(icon_click,(x,y))
        if click[0] == 1 and order is not None:
            if order == 'exit':
                pygame.quit()
                quit()
            if order == 'start':
                pygame.display.update()
                game()
    else:
        if p:
            screen.blit(icon,(x,y))
        else:
            screen.blit(icon,(x,y))

def menu():
    global menu_sound,play_sound
    if not menu_sound:
        menu_sound = pygame.mixer.Sound('Sound/Arpanuats.wav')
        menu_sound.set_volume(.5)
        menu_sound.play(loops=-1)
    slide = 40
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if slide < 255:
            slide += 10
            bg.set_alpha(slide)
            screen.blit(bg, (0, 0))
            pygame.time.delay(100)
        screen.blit(bg,(0,0))
        screen.blit(icon_game,(600,100))
        screen.blit(word,(500,100))
        #button(exit_n,exit_click,570,360,100,100,'exit')
        button(start,start_click,570,250,100,100,'start')
        pygame.display.update()
        clock.tick(30)
pygame.init()
menu()
