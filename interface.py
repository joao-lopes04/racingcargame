import pygame
import sys
from game import car_racing, car_racing_mutli


# Creating a function that creates the GUI
def interface():
    # initiating pygames
    pygame.init()
    # creating the screen 900x500 pixels
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # saving the screen sizes
    width = screen.get_width()
    height = screen.get_height()
    # creating some textlabels
    font = pygame.font.SysFont('Anton', 50)
    
    menu_background = pygame.image.load("menubackground.png")
    singleplayerbutton = pygame.image.load("img/singleplayerbutton.png")
    multiplayerbutton = pygame.image.load("img/multiplayerbutton.png")
    settingsbutton = pygame.image.load("img/settingsbutton.png")
    mapsbutton = pygame.image.load("img/mapsbutton.png")
    exitbutton = pygame.image.load("img/exitbutton.png")
    # interface loop
    while True:
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            # press on quit button
        screen.blit(menu_background, (0,0))
        screen.blit(singleplayerbutton,(50,37))
        screen.blit(multiplayerbutton,(270,37))
        screen.blit(settingsbutton,(50,117))
        screen.blit(mapsbutton, (270,117))
        screen.blit(exitbutton,(50, 197))
        
        #updating the screen
        pygame.display.update()


        #checking for the mouse position and clicks
        mouse_x, mouse_y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Check for mouse clicks on each option
        
            
        #checks if there was a click in the area of this coordinates and if so, starts the multiplayer game
        if 270 < mouse_x < 270 + multiplayerbutton.get_width() \
                and 37 < mouse_y < 37 + multiplayerbutton.get_height():
            if click[0] == 1:
                #menu_sound.stop()
                car_racing_mutli()
                pass
        #checks if there was a click in the area of this coordinates and if so, opens the maps screen
        if 270 < mouse_x < 270 + mapsbutton.get_width() \
                and 117< mouse_y < 117 + mapsbutton.get_height():
            if click[0] == 1:
                
                #draw_map_selection()
                pass


        #checks if there was a click in the area of this coordinates and if so, opens the settings screen
        if 50  < mouse_x < 50 + settingsbutton.get_width() \
                and 117 < mouse_y < 117 + settingsbutton.get_height():
            if click[0] == 1:
                credits()

        
        #checks if there was a click in the area of this coordinates and if so, closes the game
        if 50  < mouse_x < 50 + exitbutton.get_width() \
                and 197  < mouse_y < 197 + exitbutton.get_height():
            if click[0] == 1:
                pygame.quit()
                quit()
                
        #checks if there was a click in the area of this coordinates and if so, starts the singleplayer game
        if 50 < mouse_x < 50 + singleplayerbutton.get_width() \
                and 37 < mouse_y < 37 + singleplayerbutton.get_height():
            if click[0] == 1: 
                car_racing()


def credits():
    res = (800, 600)
    screen = pygame.display.set_mode(res)
    settings_background = pygame.image.load("Settings (1).png")
    run_instructions = True
    while run_instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #if the key "esc" is pressed go back to the menu
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run_instructions = False

        
        
        #draw a settings background with some info on it
        screen.blit(settings_background, (0,0))
        
        #update the screen
        pygame.display.update()
