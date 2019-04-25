import pygame
pygame.init()
pygame.display.set_caption('2 pic 1 word')
#MENU_SCREEN
screen = pygame.display.set_mode((1280, 720))
bg = pygame.image.load('Picture/bg.png')
bg = pygame.transform.scale(bg, (1280, 720))
bg = bg.convert()
clock = pygame.time.Clock()
credit_bg = pygame.image.load('Picture/credit_bg.png')
credit_bg = pygame.transform.scale(credit_bg,(1280,720))
win = pygame.image.load('Picture/win_bg.png')
win = pygame.transform.scale(win,(1280,720))
#SOUND
menu_sound = False
play_sound = False
win_sound = False
#BUTTON
start = pygame.image.load('Picture/Button/start.png')
start = pygame.transform.scale(start,(200,100))
start_click = pygame.image.load('Picture/Button/start_click.png')
start_click = pygame.transform.scale(start_click,(200,100))
exit_n = pygame.image.load('Picture/Button/exit.png')
exit_n = pygame.transform.scale(exit_n,(200,100))
exit_click = pygame.image.load('Picture/Button/exit_click.png')
exit_click = pygame.transform.scale(exit_click,(200,100))
credit = pygame.image.load('Picture/Button/credit.png')
credit = pygame.transform.scale(credit,(200,100))
credit_click = pygame.image.load('Picture/Button/credit_click.png')
credit_click = pygame.transform.scale(credit_click,(200,100))
#GAME_PIC
'''pic1 = ['sun.jpg','egg.jpg','butter.jpg','sun.jpg','rain.jpg','pan.jpg','ear.png',
        'snow.jpg','cat.jpg','wall.jpg','book.png','cheese.jpg','bird.jpg','skate.jpg',
        'jelly.jpg','basket.jpg','wheel.jpg','lady.jpg','hand.jpg','rain.jpg','pill.jpg',
        'home.jpg','down.jpg','sun.jpg','arm.jpg','light.jpg','tea.jpg','scare.jpg',
        'cork.jpg','book.png','tooth.png','water.jpg','road.jpg','pig.png','dragon.png',
        'grape.jpg','lip.jpg','air.jpg','dish.jpg','cup.jpg','hand.jpg','star.png',
        'cow.jpg','sheet.jpg','back.jpg','honey.jpg','bag.jpg','hose.jpg','pop.jpg',
        'drum.jpg']'''
pic1 = ['sun.jpg','egg.jpg','butter.jpg']
'''pic2 = ['flower.jpg','plant.png','fly.jpg','set.png','coat.jpg','cake.jpg','ring.png','man.jpg',
        'fish.jpg','paper.jpg','shelf.jpg','cake.jpg','bath.jpg','board.jpg','fish.jpg',
        'ball.jpg','chair.jpg','bug.jpg','ball.jpg','bow.jpg','box.jpg','work.jpg',
        'stairs.jpg','glasses.jpg','chair.jpg','house.jpg','pot.jpg','crow.jpg','screw.jpg',
        'worm.png','brush.jpg','melon.jpg','runner.jpg','tail.png','fly.jpg','fruit.jpg',
        'stick.jpg','port.jpg','washer.png','cake.jpg','shake.jpg','fish.jpg','boy.jpg',
        'cloth.jpg','stroke.jpg','moon.jpg','pipe.jpg','pipe.jpg','corn.jpg','stick.jpg']'''
pic2 = ['flower.jpg','plant.png','fly.jpg']
plus = pygame.image.load('Picture/plus.png')
equal = pygame.image.load('Picture/equal.png')
question = pygame.image.load('Picture/question.png')
bg_game = pygame.image.load('Picture/bg_game.png')
bg_game = pygame.transform.scale(bg_game,(1280,720))
#ANSWER#
answer = []
integer = ['1','2','3','4','5','6','7','8','9','0']
for a in range(len(pic1)): 
    res = pic1[a][:-4] + pic2[a][:-4]
    ans = '.'.join(str(ord(c)) for c in res)
    answer.append(ans)

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
                pygame.K_o,pygame.K_p,pygame.K_q,pygame.K_r,pygame.K_s,pygame.K_t,pygame.K_u,pygame.K_v,pygame.K_w,pygame.K_x,pygame.K_y,pygame.K_z,pygame.K_BACKSPACE,pygame.K_SPACE,13]
    menu_sound.stop()
    global play_sound
    if not play_sound:
        play_sound = pygame.mixer.Sound('Sound/Chibi Ninja.wav')
        play_sound.set_volume(.3)
        play_sound.play(loops=-1)
    #GAME
    while True:
        for event in pygame.event.get():
            pygame.display.update()
            screen.fill(0)
            screen.blit(bg_game,(0,0))
            picture1 = pygame.image.load('Picture/pics1/'+pic1[i])
            picture2 = pygame.image.load('Picture/pics2/'+pic2[i])
            picture1 = pygame.transform.scale(picture1,(220,220))
            picture2 = pygame.transform.scale(picture2,(220,220))
            screen.blit(picture1,(230,200))
            screen.blit(picture2,(600,200))
            screen.blit(plus,(330,200))
            screen.blit(equal,(720,200))
            screen.blit(question,(850,200))
            if i == len(answer)-1 and input_ == answer[i]:
                winner()
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
                        i += 1
                        if input_ != '':
                            output = input_.split('.')
                            for a in output:
                                a = int(a) - 97
                                show_input += set_letter[a]
                                correct_sound = pygame.mixer.Sound('Sound/correct.wav')
                                correct_sound.set_volume(.2)
                                correct_sound.play()
                                show_input = ''
                        input_ = ''
                    else:
                        wrong_sound = pygame.mixer.Sound('Sound/wrong.wav')
                        wrong_sound.set_volume(.5)
                        wrong_sound.play()
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
            show_text(show_input,70,(640,550),(255, 255, 255),'fonts//Nawabiat.ttf')
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
            if order == 'credit':
                credit_background()
    else:
        if p:
            screen.blit(icon,(x,y))
        else:
            screen.blit(icon,(x,y))

def credit_background():
    slide = 40
    click = pygame.mouse.get_pressed()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu()
            if slide < 255:
                slide += 10
                credit_bg.set_alpha(slide)
                screen.blit(credit_bg,(0,0))
                pygame.time.delay(10)
            screen.blit(credit_bg,(0,0))
            pygame.display.update()
            clock.tick(30)

def winner():
    slide = 40
    play_sound.stop()
    global win_sound,menu_sound
    if not win_sound:
        win_sound = pygame.mixer.Sound('Sound/MHW behemoth.wav')
        win_sound.set_volume(.6)
        win_sound.play(loops = -1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    win_sound.stop()
                    menu_sound = False
                    menu()
        if slide < 255:
            slide += 10
            win.set_alpha(slide)
            screen.blit(win,(0,0))
            pygame.time.delay(100)
        screen.blit(win,(0,0))
        pygame.display.update()
        clock.tick(30)

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
            screen.blit(bg, (0,0))
            pygame.time.delay(70)
        screen.blit(bg,(0,0))
        button(exit_n,exit_click,80,460,100,100,'exit')
        button(start,start_click,80,250,100,100,'start')
        button(credit,credit_click,80,360,100,100,'credit')
        pygame.display.update()
        clock.tick(30)
pygame.init()
menu()
