# CodeJam 2022 Hackathon Beginnger Project
# Mind over Matter
# Code by: Cypress Z, Eimy L, Lauren S


## Imports ##

import sys
import tkinter as tk
import random
import pygame
from pygame.locals import *

## Variables ##

app_screen_bg = "#FECCFF"
intro_screen_bg = "#8ce2ff"
grey = "#363636"
white = "#ffffff"

sort_game_bg = 255, 255, 255
collect_game_bg = 255, 255, 255
click_game_bg = 255, 255, 255
draw_game_bg = 255, 255, 255

blue_rect = 193, 212, 227
pink_rect = 255, 204, 203
purple_rect = 190, 180, 214
yellow_rect = 204, 232, 219

yellow_coin = 250, 226, 175 
player_grey = 41, 41, 41


## App Screens ##


def app_screen():
    ''' () -> NoneType
    Displays an app screen and opens different windows
    depending on which button is pressed
    '''

    window = tk.Tk()
    window.geometry("650x700")
    
    window.configure(bg = app_screen_bg)
    
    title = tk.Label(window, text = "Mind over Matter", font =("Arial",30),
                     bg = app_screen_bg, fg = grey, width = 50, height = 2, anchor='center')
    
    subheading = tk.Label(text = "Please select a game", font = ("Arial", 20),
                     bg = app_screen_bg, fg = grey, width = 50, anchor ='center')
        
    sort_game_button = tk.Button(text = "Sort Game",
                                 font = ("Arial", 18),
                                 width = 8, height = 4,
                                 bg = grey,
                                 fg = grey,
                                 command = sort_game)
    collect_game_button = tk.Button(text = "Collect Game",
                                 font = ("Arial", 18),
                                 width = 8, height = 4,
                                 bg = grey,
                                 fg = grey,
                                 command = collect_game)
    click_game_button = tk.Button(text = "Click Game",
                                 font = ("Arial", 18),
                                 width = 8, height = 4,
                                 bg = grey,
                                 fg = grey,
                                 command = click_game)
    draw_game_button = tk.Button(text = "Draw Game",
                                 font = ("Arial", 18),
                                 width = 8, height = 4,
                                 bg = grey,
                                 fg = grey,
                                 command = draw_game)
    help_button = tk.Button(text = "Help",
                                 font = ("Arial", 18),
                                 width = 8, height = 4,
                                 bg = grey,
                                 fg = grey,
                                 command = help_page)
    info_button = tk.Button(text = "Learn More",
                                 font = ("Arial", 18),
                                 width = 8, height = 4,
                                 bg = grey,
                                 fg = grey,
                                 command = info_page)
    
    
    title.pack()
    subheading.pack()
    
    sort_game_button.place(x = 150, y = 150)
    collect_game_button.place(x = 375, y = 150)
    click_game_button.place(x = 150, y = 350)
    draw_game_button.place(x = 375, y = 350)
    help_button.place(x = 150, y = 550)
    info_button.place(x = 375, y = 550)

    window.mainloop()

## Info Screens ##

def help_page():
    '''() -> NoneType
    Displays a page with text
    '''
    
    window = tk.Tk()
    window.geometry("650x700")
    
    window.configure(bg = white)
    
    title = tk.Label(window, text = "Help Page", font =("Arial",30),
                     bg = app_screen_bg, fg = grey, width = 50, height = 2, anchor='center')
    
    textS = tk.Label(window, text = "Welcome to the sorting game!",
                    font =("Arial",20), bg = white, fg = grey)
    textSh = tk.Label(window, text = "Drag the correct colour square in the centre to same colour square in the corner",
                    font =("Arial",15), bg = white, fg = grey)
    
    textC = tk.Label(window, text = "Welcome to the collect game!",
                    font =("Arial",20), bg = white, fg = grey)
    textCh = tk.Label(window, text = "Using the arrow keys move your square to the yellow square",
                    font =("Arial",15), bg = white, fg = grey)
    
    textD = tk.Label(window, text = "Welcome to the drawing game!",
                    font =("Arial",20), bg = white, fg = grey)
    textDh = tk.Label(window, text = "Using the arrow keys to move around and draw. Press the button to change the colour,",
                    font =("Arial",15), bg = white, fg = grey)
    textDs = tk.Label(window, text = "and press the space bar to clear the screen.",
                    font =("Arial",15), bg = white, fg = grey)
    
    textM = tk.Label(window, text = "Welcome to the clicking game!",
                    font =("Arial",20), bg = white, fg = grey)
    textMh = tk.Label(window, text = "Using your mouse, click on the square that pops up on your screen",
                    font =("Arial",15), bg = white, fg = grey)
    
    phone_title = tk.Label(window, text = "Help Lines",
                    font =("Arial",20), bg = white, fg = grey)
    phone1 = tk.Label(window, text = "Kids Help Phone: +1 800-668-6868",
                    font =("Arial",15), bg = white, fg = grey)
    phone2 = tk.Label(window, text = "Kids Help Text Line: 686868",
                    font =("Arial",15), bg = white, fg = grey)
    phone3 = tk.Label(window, text = "Suicide Action Montreal: +1 866-277-3553",
                    font =("Arial",15), bg = white, fg = grey)
    phone4 = tk.Label(window, text = "Government of Canada: +1 866-585-0445",
                    font =("Arial",15), bg = white, fg = grey)
    
    
    
    title.pack()
    textS.place(x=50, y=100)
    textSh.place(x=50, y=140)
    
    textC.place(x=50, y=180)
    textCh.place(x=50, y=220)
    
    textD.place(x=50, y=260)
    textDh.place(x=50, y=300)
    textDs.place(x=50, y=320)
    
    textM.place(x=50, y=360)
    textMh.place(x=50, y=400)
    
    phone_title.place(x=50, y=460)
    phone1.place(x=50, y=490)
    phone2.place(x=50, y=510)
    phone3.place(x=50, y=530)
    phone4.place(x=50, y=550)
    


def info_page():
    ''' () -> NoneType
    Displays a page with text
    '''
    
    window = tk.Tk()
    window.geometry("650x700")
    
    window.configure(bg = white)
    
    title = tk.Label(window, text = "Learn More", font =("Arial",30),
                     bg = app_screen_bg, fg = grey, width = 50, height = 2, anchor='center')
    
    line1 = tk.Label(window, text = "Thank you for using Mind Over Matter!",
                    font =("Arial",20), bg = white, fg = grey)
    line2 = tk.Label(window, text = "We are so glad that you are here!",
                    font =("Arial",20), bg = white, fg = grey)
    line3 = tk.Label(window, text = "We made this app to help users calm down by focusing all",
                     font =("Arial",20), bg = white, fg = grey)
    line4 = tk.Label(window, text = "their attention on one easy task.",
                    font =("Arial",20), bg = white, fg = grey)
    line5 = tk.Label(window, text = "These simple, easy to play games help you destress and",
                     font =("Arial",20), bg = white, fg = grey)
    line6 = tk.Label(window, text = "can be played any time.",
                     font =("Arial",20), bg = white, fg = grey)
    line7 = tk.Label(window, text = "We hope you have fun! ",
                    font =("Arial",20), bg = white, fg = grey)
    


    title.pack()
    line1.place(x=50, y=100)
    line2.place(x=50, y=140)
    line3.place(x=50, y=180)
    line4.place(x=50, y=220)
    line5.place(x=50, y=260)
    line6.place(x=50, y=300)
    line7.place(x=50, y=340)    
    
## Game Helper Functions ##

def random_coords():
    ''' () -> int, int
    Generates and returns 2 random coordinates.
    '''
    
    rand_x = random.randint(0, 650-30)
    rand_y = random.randint(0, 700-30)
    
    return rand_x, rand_y

def random_colour():
    ''' () -> var
    Generates and returns a variable attached to rgb
    values
    '''
    colour_num = random.randint(0,3)
    
    if colour_num == 0:
        target_colour = yellow_rect
    elif colour_num == 1:
        target_colour = blue_rect
    elif colour_num == 2:
        target_colour = pink_rect
    else:
        target_colour = purple_rect
    
    return target_colour

## Game Functions ##

def sort_game():
    ''' () -> NoneType
    Opens a new window and for the user to play
    the sort game in
    '''
     
    pygame.init()
    pygame.display.set_caption('Sort Game')
     
    fps = 60
    fpsClock = pygame.time.Clock()
     
    width, height = 600, 750
    screen = pygame.display.set_mode((width, height))
    
    x,y = 260, 340
    rectangle = pygame.rect.Rect(x, y , 100, 100)

    rectangle1 = pygame.rect.Rect(460, 610, 125, 125) 
    rectangle2 = pygame.rect.Rect(20, 20, 125, 125) 
    rectangle3 = pygame.rect.Rect(20, 610, 125, 125) 
    rectangle4 = pygame.rect.Rect(460, 20, 125, 125) 
        

    colourChange = True
    running = True
    rectangle_draging = False
    
    while running:
        screen.fill((sort_game_bg))
        
        #dragging square
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:            
                    if rectangle.collidepoint(event.pos):
                        rectangle_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = rectangle.x - mouse_x
                        offset_y = rectangle.y - mouse_y 

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:            
                    rectangle_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if rectangle_draging:
                    mouse_x, mouse_y = event.pos
                    rectangle.x = mouse_x + offset_x
                    rectangle.y = mouse_y + offset_y
                    
        #border
        if rectangle.top <= 0:
            rectangle.y = rectangle.y +10
        if rectangle.bottom >= 700:
            rectangle.y = rectangle.y -10
        if rectangle.right >= 650:
            rectangle.x = rectangle.x - 10
        if rectangle.left <= 0:
            rectangle.x = rectangle.x + 10
                    
        #colour change of centre rectangle
        if colourChange == True:
            colour_num = random.randint(0,4)
                
            if colour_num == 0:
                rand_colour = yellow_rect
                target = 'yel'
            elif colour_num == 1:
                rand_colour = pink_rect
                target = 'pin'
            elif colour_num == 2:
                rand_colour = blue_rect
                target = 'blu'
            else:
                rand_colour = purple_rect
                target = 'pup'
            
            colourChange = False
        
        #shows the rectangles
        pygame.draw.rect(screen, (blue_rect), rectangle1)
        pygame.draw.rect(screen, (pink_rect), rectangle2)
        pygame.draw.rect(screen, (yellow_rect), rectangle3)
        pygame.draw.rect(screen, (purple_rect), rectangle4)
        
        pygame.draw.rect(screen, (rand_colour), rectangle)
        
        #setting a target and collision
        if target == 'yel':
            collide = pygame.Rect.colliderect(rectangle, rectangle3)
            if collide:
                colourChange = True
                rectangle_draging = False
                rectangle.x = 260
                rectangle.y = 340
                
        if target == 'pin':
            collide = pygame.Rect.colliderect(rectangle, rectangle2)
            if collide:
                colourChange = True
                rectangle_draging = False
                rectangle.x = 260
                rectangle.y = 340
                
        if target == 'blu':
            collide = pygame.Rect.colliderect(rectangle, rectangle1)
            if collide:
                colourChange = True
                rectangle_draging = False
                rectangle.x = 260
                rectangle.y = 340

        if target == 'pup':
            collide = pygame.Rect.colliderect(rectangle, rectangle4)
            if collide:
                colourChange = True
                rectangle_draging = False
                rectangle.x = 260
                rectangle.y = 340
            
        pygame.display.flip()
        
    pygame.quit()


def collect_game():
    ''' () -> NoneType
    Opens a new window for the user to play
    the collect game in.
    '''
    
    pygame.init()
    pygame.display.set_caption('Collect Game')

    screen = pygame.display.set_mode((650,700))

    x = 260
    y = 340
    width = 40
    height = 60
    vel = 10
    colour = random_colour()
    
    rectangle = pygame.rect.Rect(x, y , 30, 30) 

    run = True
    is_coin = False
    
    while run:
        pygame.time.delay(100)
        screen.fill((collect_game_bg))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        #border
        if rectangle.top <= 0:
            rectangle.y = rectangle.y +10
        if rectangle.bottom >= 700:
            rectangle.y = rectangle.y -10
        if rectangle.right >= 650:
            rectangle.x = rectangle.x - 10
        if rectangle.left <= 0:
            rectangle.x = rectangle.x + 10
        
        #movements
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            rectangle.x -= vel

        if keys[pygame.K_RIGHT]:
            rectangle.x += vel

        if keys[pygame.K_UP]:
            rectangle.y -= vel

        if keys[pygame.K_DOWN]:
            rectangle.y += vel
        
        #shows the player
        pygame.draw.rect(screen, (player_grey), rectangle)
        
        #coin generation, makes a new coin if collision happens
        if not is_coin:
            rand_x, rand_y = random_coords()
            colour = random_colour()
            coin = pygame.rect.Rect(rand_x, rand_y, 20, 20)
            
            pygame.draw.rect(screen, (colour), coin)
            
            is_coin = True
            
        else:
            pygame.draw.rect(screen, (colour), coin)
            
        collide = pygame.Rect.colliderect(rectangle, coin)
        
        if collide:
            is_coin = False
        
        pygame.display.flip() 
    
    pygame.quit()

def click_game():
    ''' () -> NoneType
    Opens a new window for the user to
    play the click game in
    '''
    colourChange = True 
    pygame.init()

    screen = pygame.display.set_mode((650,700))

    x = 260
    y = 340
    width = 40
    height = 60
    vel = 10
     
    old_colour = 0
    colour_num = 0


    run = True
    is_point = False
    
    while run:
        pygame.time.delay(100)
        screen.fill((click_game_bg))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            if point.collidepoint(mousepos):
                mouse_x, mouse_y = mousepos
                offset_x = point.x - mouse_x
                offset_y = point.y - mouse_y
                is_point = False
                colourChange = True
                
        if colourChange == True:
            while old_colour == colour_num:
                colour_num = random.randint(0,3)
            old_colour = colour_num
                    
            if colour_num == 0:
                target_colour = yellow_rect
            elif colour_num == 1:
                target_colour = blue_rect
            elif colour_num == 2:
                target_colour = pink_rect
            else:
                target_colour = purple_rect
            
            colourChange = False

                          
        if not is_point:
            rand_x, rand_y = random_coords()
            point = pygame.rect.Rect(rand_x, rand_y, 45, 45)
            pygame.draw.rect(screen, (target_colour), point)

            is_point = True
            
        else:
            pygame.draw.rect(screen, (target_colour), point)
    
        
        pygame.display.flip() 
    
    pygame.quit()


def draw_game():
    ''' () -> NoneType
    Opens a new window for the user
    to play the draw game in
    '''
    
    pygame.init()
    pygame.display.set_caption('Draw Game')

    screen = pygame.display.set_mode((650,700))
    screen.fill((draw_game_bg))
    
    #drawing rectangle
    x = 260
    y = 340
    width = 40
    height = 60
    vel = 10
    rectangle = pygame.rect.Rect(x, y , 15, 15)
    
    button = pygame.Rect(535, 40, 60, 20)
    colour = random_colour()
    
    #text
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('Change Colour', True, (player_grey))
    textRect = text.get_rect()
    textRect.center = (560,20)

    run = True
    
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            #when change colour button is pressed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button.collidepoint(event.pos):
                        colour = random_colour()
                        print(colour)
                        
        #border
        if rectangle.top <= 0:
            rectangle.y = rectangle.y +10
        if rectangle.bottom >= 700:
            rectangle.y = rectangle.y -10
        if rectangle.right >= 650:
            rectangle.x = rectangle.x - 10
        if rectangle.left <= 0:
            rectangle.x = rectangle.x + 10


        keys = pygame.key.get_pressed()
        
        #movement and erasing
        if keys[pygame.K_LEFT]:
            rectangle.x -= vel

        if keys[pygame.K_RIGHT]:
            rectangle.x += vel

        if keys[pygame.K_UP]:
            rectangle.y -= vel

        if keys[pygame.K_DOWN]:
            rectangle.y += vel
            
        if keys[pygame.K_SPACE]:
            screen.fill((draw_game_bg))
            
        #showing the rectangles/text
        pygame.draw.rect(screen, (colour), rectangle)
        pygame.draw.rect(screen, (player_grey), button)
        screen.blit(text, textRect)
        pygame.display.flip()
        
    
    pygame.quit()
    
## Start ###
app_screen()

