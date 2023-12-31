import pygame
import sys
from game import car_racing, car_racing_multi, car_racing2, car_racing3, car_racing_multi2, car_racing_multi3


# Creating a function that creates the GUI
def interface():

    """
    Displays the main menu interface.

    This function initializes the Pygame environment and renders the main menu screen.
    It handles user input for different menu options such as single player, multiplayer,
    settings, maps selection, and exit. Based on user clicks, it navigates to various
    screens or triggers specific actions.

    Notes:
    - The function waits for user input indefinitely until a specific action is triggered.
    - Clicks on different buttons navigate to respective functionalities.

    Modules Used:
    - Pygame: Handles GUI rendering, mouse input, and screen updates.
    - SysFont from Pygame: Generates text labels for menu options.
    - Mixer from Pygame: Controls sound effects for button clicks.

    Characteristics:
    - Waits for user input and processes clicks on menu buttons.
    - Renders the main menu interface with various buttons.
    - Provides options to navigate to different screens or trigger specific game actions.
    - Handles quitting the game when the exit button is clicked.

    """

    # initiating pygames
    pygame.init()
    #initiating sound player
    pygame.mixer.init
    # creating the screen 900x500 pixels
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # saving the screen sizes
    width = screen.get_width()
    height = screen.get_height()
    # creating some textlabels
    font = pygame.font.SysFont('Anton', 50)
    #creating some images
    menu_background = pygame.image.load("img/menubackground.png")
    singleplayerbutton = pygame.image.load("img/singleplayerbutton.png")
    multiplayerbutton = pygame.image.load("img/multiplayerbutton.png")
    settingsbutton = pygame.image.load("img/settingsbutton.png")
    mapsbutton = pygame.image.load("img/mapsbutton.png")
    exitbutton = pygame.image.load("img/exitbutton.png")
    button_sound = pygame.mixer.Sound("sounds/click.wav")

    # interface loop
    while True:
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            # press on quit button
        #drawing in the screen
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
                
                car_racing_multi()
                pass
        #checks if there was a click in the area of this coordinates and if so, opens the maps screen
        if 270 < mouse_x < 270 + mapsbutton.get_width() \
                and 117< mouse_y < 117 + mapsbutton.get_height():
            if click[0] == 1:
                button_sound.play()
                draw_map_selection()
                


        #checks if there was a click in the area of this coordinates and if so, opens the settings screen
        if 50  < mouse_x < 50 + settingsbutton.get_width() \
                and 117 < mouse_y < 117 + settingsbutton.get_height():
            if click[0] == 1:
                button_sound.play()
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


def interface2():
    # initiating pygames
    pygame.init()
    #initiating sound player
    pygame.mixer.init()
    # creating the screen 900x500 pixels
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # saving the screen sizes
    width = screen.get_width()
    height = screen.get_height()
    # creating some textlabels
    font = pygame.font.SysFont('Anton', 50)
    #creating some images
    menu_background = pygame.transform.scale(pygame.image.load("img/menubackground2.jpg"), (WIDTH, HEIGHT))
    singleplayerbutton = pygame.image.load("img/singleplayerbutton.png")
    multiplayerbutton = pygame.image.load("img/multiplayerbutton.png")
    settingsbutton = pygame.image.load("img/settingsbutton.png")
    mapsbutton = pygame.image.load("img/mapsbutton.png")
    exitbutton = pygame.image.load("img/exitbutton.png")
    button_sound = pygame.mixer.Sound("sounds/click.wav")
    # interface loop
    while True:
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            # press on quit button
        #drawing in the screen
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
                
                car_racing_multi2()
                pass
        #checks if there was a click in the area of this coordinates and if so, opens the maps screen
        if 270 < mouse_x < 270 + mapsbutton.get_width() \
                and 117< mouse_y < 117 + mapsbutton.get_height():
            if click[0] == 1:
                button_sound.play()
                draw_map_selection()
                


        #checks if there was a click in the area of this coordinates and if so, opens the settings screen
        if 50  < mouse_x < 50 + settingsbutton.get_width() \
                and 117 < mouse_y < 117 + settingsbutton.get_height():
            if click[0] == 1:
                button_sound.play
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
                car_racing2()

def interface3():
    # initiating pygames
    pygame.init()
    #initiating sound player
    pygame.mixer.init()
    # creating the screen 900x500 pixels
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # saving the screen sizes
    width = screen.get_width()
    height = screen.get_height()
    # creating some textlabels
    font = pygame.font.SysFont('Anton', 50)
    #creating some images
    menu_background = pygame.transform.scale(pygame.image.load("img/menubackground3.jpg"), (WIDTH, HEIGHT))
    singleplayerbutton = pygame.image.load("img/singleplayerbutton.png")
    multiplayerbutton = pygame.image.load("img/multiplayerbutton.png")
    settingsbutton = pygame.image.load("img/settingsbutton.png")
    mapsbutton = pygame.image.load("img/mapsbutton.png")
    exitbutton = pygame.image.load("img/exitbutton.png")
    button_sound = pygame.mixer.Sound("sounds/click.wav")
    # interface loop
    while True:
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            # press on quit button
        #drawing in the screen
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
                car_racing_multi3()
                pass
        #checks if there was a click in the area of this coordinates and if so, opens the maps screen
        if 270 < mouse_x < 270 + mapsbutton.get_width() \
                and 117< mouse_y < 117 + mapsbutton.get_height():
            if click[0] == 1:
                button_sound.play()
                
                draw_map_selection()
                


        #checks if there was a click in the area of this coordinates and if so, opens the settings screen
        if 50  < mouse_x < 50 + settingsbutton.get_width() \
                and 117 < mouse_y < 117 + settingsbutton.get_height():
            if click[0] == 1:
                button_sound.play()
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
                car_racing3()

def credits():
    res = (800, 600) #setting width and height
    screen = pygame.display.set_mode(res)
    settings_background = pygame.image.load("img/Settings (3).png")
    run_instructions = True
    #handeling the setting window loop event
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

def draw_map_selection():
    #initiating sound player
    pygame.mixer.init()
    res = (800,600) #setting widht and heigth
    screen = pygame.display.set_mode(res)
    playbuttonmaps = pygame.image.load("img/playbuttonmaps.png")
    mapsbackground = pygame.transform.scale(pygame.image.load("img/Maps.png"), (res))
    button_sound = pygame.mixer.Sound("sounds/click.wav")
    #handles the settings window event
    run_map_selection = True
    while run_map_selection:
        #quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #go back to the menu if "esc" is pressed
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run_map_selection = False

        #draw the diferent maps and a play button on them
        screen.blit(mapsbackground,(0,0))
        screen.blit(playbuttonmaps, (92,330))
        screen.blit(playbuttonmaps, (358, 330))
        screen.blit(playbuttonmaps, (628, 330))




        #updating the screen
        pygame.display.update()


        #checking the mouse position and clicks
        mouse_x, mouse_y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Check for mouse clicks on each map option

        #if there is a click in the area of this coordinates open the highway menu and adjust the background sounds
        if 92  < mouse_x < 92 + playbuttonmaps.get_width() \
                and  330  < mouse_y <  330 + playbuttonmaps.get_height():
            if click[0] == 1:
                button_sound.play()
                interface()
                
        #if there is a click in the area of this coordinates open the ocean menu and adjust the background sounds
        if 357 - playbuttonmaps.get_width() < mouse_x < 357 + playbuttonmaps.get_width() \
                and  330  < mouse_y <  330 + playbuttonmaps.get_height():
            if click[0] == 1:
                button_sound.play()
                interface2()
                
        #if there is a click in the area of this coordinates open the space menu and adjust the background sounds
        if 627 - playbuttonmaps.get_width() < mouse_x < 627 +  playbuttonmaps.get_width() \
                and  330 < mouse_y <  330 + playbuttonmaps.get_height():
            if click[0] == 1:
                button_sound.play()
                interface3()
                




          