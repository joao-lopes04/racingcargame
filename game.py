import pygame, random, sys
#Let's import the Car Class
from car import Car
from powerup import SlowPowerUp, ScoreBoostPowerUp, ShrinkPlayerPowerUp
import interface

global offset_1
offset_1 = 0

def car_racing():

    pygame.init()

    #loads road image
    road_image = pygame.image.load("img/1 (1).png").convert_alpha()

    WIDTH, HEIGHT = 800, 600

    #resize screen
    road_image = pygame.transform.scale(road_image, (WIDTH, HEIGHT))

    speed = 0.6

    PlayerCar1 = Car("img/playermap1.png", 100, 100, 70)
    PlayerCar1.rect.x = 160
    PlayerCar1.rect.y = HEIGHT - 100
    font = pygame.font.SysFont('Anton', 50)

    

    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Car Racing")

    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()

    

    lanes = {
    "faixa1": [180, 190, 205],
    "faixa2": [290, 305, 320],
    "faixa3": [440, 450, 470],
    "faixa4": [550, 570, 590]
}
    
    slowPU = SlowPowerUp("img/SlowPowerUp.png", 50, 50, 55)
    slowPU.rect.x = random.randint(135, 570-50)
    slowPU.rect.y = -3749



    plus50PU = ScoreBoostPowerUp("img/+50PowerUp.png", 50, 50, 55)
    plus50PU.rect.x = random.randint(135, 570-50)
    plus50PU.rect.y = -2382

    shrinkPU = ShrinkPlayerPowerUp("img/ShrinkPowerUp.png", 50, 50, 55)
    shrinkPU.rect.x = random.randint(135, 570-50)
    shrinkPU.rect.y = -1557

    invencibilityPU = ShrinkPlayerPowerUp("img/InvencibilityPowerUp.png", 50, 50, 55)
    invencibilityPU.rect.x = random.randint(135, 570-50)
    invencibilityPU.rect.y = -4934

    image_paths = ["img/carro random.png", "img/carro random2.png", "img/carro random3.png", "img/carro random4.png"]

    car1 = Car(random.choice(image_paths), 60, 100, random.randint(70, 115))
    car1_lane_start = random.choice(lanes["faixa1"])
    car1.rect.x = car1_lane_start
    car1.rect.y = -100
    car1.repaint(random.choice(image_paths))

    car2 = Car(random.choice(image_paths), 60, 100, random.randint(70, 115))
    car2_lane_start = random.choice(lanes["faixa2"])
    car2.rect.x = car2_lane_start
    car2.rect.y = -600
    car2.repaint(random.choice(image_paths))

    car3 = Car(random.choice(image_paths), 60, 100, random.randint(70, 115))
    car3_lane_start = random.choice(lanes["faixa3"])
    car3.rect.x = car3_lane_start
    car3.rect.y = -300
    car3.repaint(random.choice(image_paths))

    car4 = Car(random.choice(image_paths), 60, 100, random.randint(70, 115))
    car4_lane_start = random.choice(lanes["faixa4"])
    car4.rect.x = car4_lane_start
    car4.rect.y = -900
    car4.repaint(random.choice(image_paths))



    

    # Add the car to the list of objects
    all_sprites_list.add(PlayerCar1)
    all_sprites_list.add(car1)
    all_sprites_list.add(car2)
    all_sprites_list.add(car3)
    all_sprites_list.add(car4)
    all_sprites_list.add(slowPU)
    all_sprites_list.add(plus50PU)
    all_sprites_list.add(shrinkPU)
    all_sprites_list.add(invencibilityPU)


    

    powerup1_sprite_list = pygame.sprite.Group()
    powerup1_sprite_list.add(slowPU)

    powerup2_sprite_list = pygame.sprite.Group()
    powerup2_sprite_list.add(plus50PU)

    powerup3_sprite_list = pygame.sprite.Group()
    powerup3_sprite_list.add(shrinkPU)

    powerup4_sprite_list = pygame.sprite.Group()
    powerup4_sprite_list.add(invencibilityPU)

    all_coming_cars = pygame.sprite.Group()
    all_coming_cars.add(car1)
    all_coming_cars.add(car2)
    all_coming_cars.add(car3)
    all_coming_cars.add(car4)

    #Allowing the user to close the screen...
    carryOn = True
    
    scorebox = pygame.image.load("img/scorebox2.png")
    score = 0
    
    clock=pygame.time.Clock()
    enemy_hit = False
    powerup1_hit = False
    powerup2_hit = False
    powerup3_hit = False
    frame_count = 0

    while carryOn:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    carryOn=False
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x:
                         PlayerCar1.moveRight(10)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                PlayerCar1.moveLeft(5)
                # Limites horizontais para o carro do jogador
                if PlayerCar1.rect.x < 135:
                    PlayerCar1.rect.x = 135
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                PlayerCar1.moveRight(5)
                 # Limites horizontais para o carro do jogador
                if PlayerCar1.rect.x > 570:
                    PlayerCar1.rect.x = 570

            if keys[pygame.K_UP] or keys[pygame.K_w]:
                PlayerCar1.moveup(5)
                if PlayerCar1.rect.y < 0:
                     PlayerCar1.rect.y = 0
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                PlayerCar1.movedown(5)
                if PlayerCar1.rect.y > 500:
                    PlayerCar1.rect.y = 500


        
            #Game Logic
            for car in all_coming_cars:
                car.moveForward(speed)
                if car.rect.y > HEIGHT:
                    score += 1
                    car.changeSpeed(random.randint(70,115))
                    
                    car.rect.y = -200
            
            for powerup in powerup1_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -3749

            slowPU.moveForward(speed)
            if slowPU.rect.y > HEIGHT:
                 slowPU.rect.x = random.randint(135, 570-50)
                 slowPU.rect.y = -3749

            for powerup in powerup2_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -2382

            plus50PU.moveForward(speed)
            if plus50PU.rect.y > HEIGHT:
                 plus50PU.rect.x = random.randint(135, 570-50)
                 plus50PU.rect.y = -2382

            for powerup in powerup3_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -1557

            shrinkPU.moveForward(speed)
            if shrinkPU.rect.y > HEIGHT:
                 shrinkPU.rect.x = random.randint(135, 570-50)
                 shrinkPU.rect.y = -1557

            for powerup in powerup4_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -4934

            invencibilityPU.moveForward(speed)
            if invencibilityPU.rect.y > HEIGHT:
                 invencibilityPU.rect.x = random.randint(135, 570-50)
                 invencibilityPU.rect.y = -4934

            car1.moveForward(speed)
            if car1.rect.y > HEIGHT:
                   score +=1
                   car1_lane = random.choice(lanes["faixa1"])
                   car1.rect.x = car1_lane
                   car1.rect.y = -100

            car2.moveForward(speed)
            if car2.rect.y > HEIGHT:
                   score +=1
                   car2_lane = random.choice(lanes["faixa2"])
                   car2.rect.x = car2_lane
                   car2.rect.y = -100

            car3.moveForward(speed)
            if car3.rect.y > HEIGHT:
                   score +=1
                   car3_lane = random.choice(lanes["faixa3"])
                   car3.rect.x = car3_lane
                   car3.rect.y = -100

            car4.moveForward(speed)
            if car4.rect.y > HEIGHT:
                   score +=1
                   car4_lane = random.choice(lanes["faixa4"])
                   car4.rect.x = car4_lane
                   car4.rect.y = -100
                
            
                
                # Check if there is a car collision
            car_collision_list = pygame.sprite.spritecollide(PlayerCar1, all_coming_cars, False, pygame.sprite.collide_mask)
            for car in car_collision_list:
                    print("Car crash!")
                    # End Of Game
                    #carryOn = False
                    enemy_hit = True

            '''car_collision_powerup1 = pygame.sprite.spritecollide(PlayerCar1, powerup1_sprite_list, False, pygame.sprite.collide_mask)
            for powerup in car_collision_powerup1:
                powerup1_hit = True

            car_collision_powerup2 = pygame.sprite.spritecollide(PlayerCar1, powerup2_sprite_list, False, pygame.sprite.collide_mask)
            for powerup in car_collision_powerup2:
                powerup2_hit = True

            car_collision_powerup3 = pygame.sprite.spritecollide(PlayerCar1, powerup3_sprite_list, False, pygame.sprite.collide_mask)
            for powerup in car_collision_powerup3:
                powerup3_hit = True

            powerup_active = False
            powerup_duration = 300
            if powerup1_hit:
                all_sprites_list.remove(slowPU)
                #PlayerCar1 = Car("img/PowerUpYellowCarSinglePlayer.png",100,100,70)
                powerup_active = True
                
                

            if powerup_active:
                frame_count += 1
                for car in all_coming_cars:
                    car.changeSpeed(50)

                if frame_count >= powerup_duration:
                    powerup_active = False
                    all_sprites_list.add(slowPU)
                    for car in all_coming_cars:
                        car.changeSpeed(random.randint(70, 110))
                        
                    frame_count = 0

            if powerup2_hit:
                score += 50


            if powerup3_hit:
                all_sprites_list.remove(shrinkPU)
                #PlayerCar1 = Car("img/PowerUpYellowCarSinglePlayer.png",100,100,70)
                powerup_active = True
                
                

            if powerup_active:
                frame_count += 1
                for car in all_coming_cars:
                    car.changedimensions(30,50)
                    all_sprites_list.add(shrinkPU)
                if frame_count >= powerup_duration:
                    powerup_active = False
                    
                    for car in all_coming_cars:
                        car.changedimensions(60,100)
                        
                    frame_count = 0'''

           
            if enemy_hit:
                score_text = font.render(f"SCORE: {score}", 1, "black")
                play_again = pygame.image.load("img/Play Again Button.png")
                main_menu = pygame.image.load("img/Menu Button.png")
                background_lost_single = pygame.image.load("GAME OVER SAPO.png")
                
                screen.blit(background_lost_single, (0,0))
                screen.blit(play_again, (450, 400))
                screen.blit(score_text,(500,300))
                screen.blit(main_menu, (700,400))

                #updates the new screen
                pygame.display.update()


                break

                

            all_sprites_list.update()

            global offset_1

            #allowing the background to move down
            offset_1 += 2
            offset_1 %= HEIGHT

            # cleanig the screen
            screen.fill((0, 0, 0))

            # drawing the background twice, one above the other
            screen.blit(road_image, (0, offset_1))
            screen.blit(road_image, (0, offset_1 - HEIGHT))
            
            
            #Drawing on Screen
            # Desenha a imagem de fundo
            

           


            #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
            all_sprites_list.draw(screen)
            

            #Refresh Screen
            pygame.display.flip()

            #Number of frames per secong e.g. 60
            clock.tick(60)

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()  # Quit the game if the window is closed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False
                    pygame.quit()
        #checking for mouse position and clicks
        mouse_x, mouse_y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #if the button is pressed the game starts over again
        if 450  < mouse_x < 450 + play_again.get_width() and 400  < mouse_y < 400 + play_again.get_height():
            if click[0] == 1:
                '''PlayerCar1 = Car("img/PowerUpYellowCarSinglePlayer.png",100,100,70)
                for car in all_coming_cars:
                    car.changeSpeed(random.randint(70, 115))'''
                car_racing()
        # Check for mouse clicks on "Main Menu" button
        if 700  < mouse_x < 700 + main_menu.get_width() and 400  < mouse_y < 400 + main_menu.get_height():
            if click[0] == 1:
                # Return to the main menu 
                '''PlayerCar1 = Car("img/PowerUpYellowCarSinglePlayer.png",100,100,70)
                for car in all_coming_cars:
                    car.changeSpeed(random.randint(70, 115))'''
                waiting = False  # Exit the waiting loop and return to the main menu
                interface.interface()

def car_racing2():

    pygame.init()

    #loads road image
    road_image = pygame.image.load("img/3 (1).png").convert()

    WIDTH, HEIGHT = 800, 600

    #resize screen
    road_image = pygame.transform.scale(road_image, (WIDTH, HEIGHT))

    speed = 0.6

    PlayerCar1 = Car("img/playermap2.png", 100, 100, 70)
    PlayerCar1.rect.x = 160
    PlayerCar1.rect.y = HEIGHT - 100
    font = pygame.font.SysFont('Anton', 50)

   

    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Car Racing")

    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()


    lanes = {
    "faixa1": [180, 190, 205],
    "faixa2": [290, 305, 320],
    "faixa3": [440, 450, 470],
    "faixa4": [550, 570, 590]
}


    slowPU = SlowPowerUp("img/SlowPowerUp.png", 50, 50, 55)
    slowPU.rect.x = random.randint(135, 570-50)
    slowPU.rect.y = -3749



    plus50PU = ScoreBoostPowerUp("img/+50PowerUp.png", 50, 50, 55)
    plus50PU.rect.x = random.randint(135, 570-50)
    plus50PU.rect.y = -2382

    shrinkPU = ShrinkPlayerPowerUp("img/ShrinkPowerUp.png", 50, 50, 55)
    shrinkPU.rect.x = random.randint(135, 570-50)
    shrinkPU.rect.y = -1557

    invencibilityPU = ShrinkPlayerPowerUp("img/InvencibilityPowerUp.png", 50, 50, 55)
    invencibilityPU.rect.x = random.randint(135, 570-50)
    invencibilityPU.rect.y = -4934

    image_paths = ["img/enemymap2.png"]

    car1 = Car(random.choice(image_paths), 60, 100, random.randint(70, 115))
    car1_lane_start = random.choice(lanes["faixa1"])
    car1.rect.x = car1_lane_start
    car1.rect.y = -100
    car1.repaint(random.choice(image_paths))

    car2 = Car(random.choice(image_paths), 60, 100, random.randint(70, 115))
    car2_lane_start = random.choice(lanes["faixa2"])
    car2.rect.x = car2_lane_start
    car2.rect.y = -600
    car2.repaint(random.choice(image_paths))

    car3 = Car(random.choice(image_paths), 60, 100, random.randint(70, 115))
    car3_lane_start = random.choice(lanes["faixa3"])
    car3.rect.x = car3_lane_start
    car3.rect.y = -300
    car3.repaint(random.choice(image_paths))

    car4 = Car(random.choice(image_paths), 60, 100, random.randint(70, 115))
    car4_lane_start = random.choice(lanes["faixa4"])
    car4.rect.x = car4_lane_start
    car4.rect.y = -900
    car4.repaint(random.choice(image_paths))





    # Add the car to the list of objects
    all_sprites_list.add(PlayerCar1)
    all_sprites_list.add(car1)
    all_sprites_list.add(car2)
    all_sprites_list.add(car3)
    all_sprites_list.add(car4)
    all_sprites_list.add(slowPU)
    all_sprites_list.add(plus50PU)
    all_sprites_list.add(shrinkPU)
    all_sprites_list.add(invencibilityPU)


    

    powerup1_sprite_list = pygame.sprite.Group()
    powerup1_sprite_list.add(slowPU)

    powerup2_sprite_list = pygame.sprite.Group()
    powerup2_sprite_list.add(plus50PU)

    powerup3_sprite_list = pygame.sprite.Group()
    powerup3_sprite_list.add(shrinkPU)

    powerup4_sprite_list = pygame.sprite.Group()
    powerup4_sprite_list.add(invencibilityPU)


    all_coming_cars = pygame.sprite.Group()
    all_coming_cars.add(car1)
    all_coming_cars.add(car2)
    all_coming_cars.add(car3)
    all_coming_cars.add(car4)


    #Allowing the user to close the screen...
    carryOn = True
    game_over_image = pygame.image.load("img/lostbackground.jpeg").convert()
    game_over_image = pygame.transform.scale(game_over_image, (WIDTH, HEIGHT))
    scorebox = pygame.image.load("img/scorebox2.png")
    score = 0
    
    clock=pygame.time.Clock()
    enemy_hit = False

    while carryOn:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    carryOn=False
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x:
                         PlayerCar1.moveRight(10)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                PlayerCar1.moveLeft(5)
                # Limites horizontais para o carro do jogador
                if PlayerCar1.rect.x < 135:
                    PlayerCar1.rect.x = 135
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                PlayerCar1.moveRight(5)
                 # Limites horizontais para o carro do jogador
                if PlayerCar1.rect.x > 560:
                    PlayerCar1.rect.x = 560

            if keys[pygame.K_UP] or keys[pygame.K_w]:
                PlayerCar1.moveup(5)
                if PlayerCar1.rect.y < 0:
                     PlayerCar1.rect.y = 0
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                PlayerCar1.movedown(5)
                if PlayerCar1.rect.y > 500:
                    PlayerCar1.rect.y = 500


            #Game Logic
            for car in all_coming_cars:
                car.moveForward(speed)
                if car.rect.y > HEIGHT:
                    score += 1
                    car.changeSpeed(random.randint(70,115))
                    
                    car.rect.y = -200

            for powerup in powerup1_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -3749

            slowPU.moveForward(speed)
            if slowPU.rect.y > HEIGHT:
                 slowPU.rect.x = random.randint(135, 570-50)
                 slowPU.rect.y = -3749

            for powerup in powerup2_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -2382

            plus50PU.moveForward(speed)
            if plus50PU.rect.y > HEIGHT:
                 plus50PU.rect.x = random.randint(135, 570-50)
                 plus50PU.rect.y = -2382

            for powerup in powerup3_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -1557

            shrinkPU.moveForward(speed)
            if shrinkPU.rect.y > HEIGHT:
                 shrinkPU.rect.x = random.randint(135, 570-50)
                 shrinkPU.rect.y = -1557

            for powerup in powerup4_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -4934

            invencibilityPU.moveForward(speed)
            if invencibilityPU.rect.y > HEIGHT:
                 invencibilityPU.rect.x = random.randint(135, 570-50)
                 invencibilityPU.rect.y = -4934



            car1.moveForward(speed)
            if car1.rect.y > HEIGHT:
                   score +=1
                   car1_lane = random.choice(lanes["faixa1"])
                   car1.rect.x = car1_lane
                   car1.rect.y = -100

            car2.moveForward(speed)
            if car2.rect.y > HEIGHT:
                   score +=1
                   car2_lane = random.choice(lanes["faixa2"])
                   car2.rect.x = car2_lane
                   car2.rect.y = -100

            car3.moveForward(speed)
            if car3.rect.y > HEIGHT:
                   score +=1
                   car3_lane = random.choice(lanes["faixa3"])
                   car3.rect.x = car3_lane
                   car3.rect.y = -100

            car4.moveForward(speed)
            if car4.rect.y > HEIGHT:
                   score +=1
                   car4_lane = random.choice(lanes["faixa4"])
                   car4.rect.x = car4_lane
                   car4.rect.y = -100
                
                
                # Check if there is a car collision
            car_collision_list = pygame.sprite.spritecollide(PlayerCar1, all_coming_cars, False, pygame.sprite.collide_mask)
            for car in car_collision_list:
                    print("Car crash!")
                    # End Of Game
                    #carryOn = False
                    enemy_hit = True
            if enemy_hit:
                score_text = font.render(f"SCORE: {score}", 1, "black")
                play_again = pygame.image.load("img/Play Again Button.png")
                main_menu = pygame.image.load("img/Menu Button.png")
                background_lost_single = pygame.image.load("GAME OVER SAPO.png")
                
                screen.blit(background_lost_single, (0,0))
                screen.blit(play_again, (450, 400))
                screen.blit(score_text,(500,300))
                screen.blit(main_menu, (700,400))
                #updates the new screen
                pygame.display.update()


                break

                

            all_sprites_list.update()

            global offset_1

            #allowing the background to move down
            offset_1 += 2
            offset_1 %= HEIGHT

            # cleanig the screen
            screen.fill((0, 0, 0))

            # drawing the background twice, one above the other
            screen.blit(road_image, (0, offset_1))
            screen.blit(road_image, (0, offset_1 - HEIGHT))
            
            #Drawing on Screen
            # Desenha a imagem de fundo
            

           


            #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
            all_sprites_list.draw(screen)

            #Refresh Screen
            pygame.display.flip()

            #Number of frames per secong e.g. 60
            clock.tick(60)

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()  # Quit the game if the window is closed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False
                    pygame.quit()
        #checking for mouse position and clicks
        mouse_x, mouse_y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #if the button is pressed the game starts over again
        if 450  < mouse_x < 450 + play_again.get_width() and 400  < mouse_y < 400 + play_again.get_height():
            if click[0] == 1:
                car_racing2()
        # Check for mouse clicks on "Main Menu" button
        if 700  < mouse_x < 700 + main_menu.get_width() and 400  < mouse_y < 400 + main_menu.get_height():
            if click[0] == 1:
                # Return to the main menu 
                waiting = False  # Exit the waiting loop and return to the main menu
                interface.interface2()


def car_racing3():

    pygame.init()

    #loads road image
    road_image = pygame.image.load("img/2 (1).png").convert()

    WIDTH, HEIGHT = 800, 600

    #resize screen
    road_image = pygame.transform.scale(road_image, (WIDTH, HEIGHT))

    speed = 0.6

    PlayerCar1 = Car("img/playermap3.png", 100, 100, 70)
    PlayerCar1.rect.x = 160
    PlayerCar1.rect.y = HEIGHT - 100
    font = pygame.font.SysFont('Anton', 50)

    

    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Car Racing")

    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()


    lanes = {
    "faixa1": [180, 190, 205],
    "faixa2": [290, 305, 320],
    "faixa3": [440, 450, 470],
    "faixa4": [550, 570, 590]
}

    slowPU = SlowPowerUp("img/SlowPowerUp.png", 50, 50, 55)
    slowPU.rect.x = random.randint(135, 570-50)
    slowPU.rect.y = -3749



    plus50PU = ScoreBoostPowerUp("img/+50PowerUp.png", 50, 50, 55)
    plus50PU.rect.x = random.randint(135, 570-50)
    plus50PU.rect.y = -2382

    shrinkPU = ShrinkPlayerPowerUp("img/ShrinkPowerUp.png", 50, 50, 55)
    shrinkPU.rect.x = random.randint(135, 570-50)
    shrinkPU.rect.y = -1557

    invencibilityPU = ShrinkPlayerPowerUp("img/InvencibilityPowerUp.png", 50, 50, 55)
    invencibilityPU.rect.x = random.randint(135, 570-50)
    invencibilityPU.rect.y = -4934


    image_paths = ["img/enemymap3.png"]

    car1 = Car(random.choice(image_paths), 60, 100, random.randint(70, 115))
    car1_lane_start = random.choice(lanes["faixa1"])
    car1.rect.x = car1_lane_start
    car1.rect.y = -100
    car1.repaint(random.choice(image_paths))

    car2 = Car(random.choice(image_paths), 60, 100, random.randint(70,115))
    car2_lane_start = random.choice(lanes["faixa2"])
    car2.rect.x = car2_lane_start
    car2.rect.y = -600
    car2.repaint(random.choice(image_paths))

    car3 = Car(random.choice(image_paths), 60, 100, random.randint(70,115))
    car3_lane_start = random.choice(lanes["faixa3"])
    car3.rect.x = car3_lane_start
    car3.rect.y = -300
    car3.repaint(random.choice(image_paths))

    car4 = Car(random.choice(image_paths), 60, 100, random.randint(70,115))
    car4_lane_start = random.choice(lanes["faixa4"])
    car4.rect.x = car4_lane_start
    car4.rect.y = -900
    car4.repaint(random.choice(image_paths))





    # Add the car to the list of objects
    all_sprites_list.add(PlayerCar1)
    all_sprites_list.add(car1)
    all_sprites_list.add(car2)
    all_sprites_list.add(car3)
    all_sprites_list.add(car4)
    all_sprites_list.add(slowPU)
    all_sprites_list.add(plus50PU)
    all_sprites_list.add(shrinkPU)
    all_sprites_list.add(invencibilityPU)


    

    powerup1_sprite_list = pygame.sprite.Group()
    powerup1_sprite_list.add(slowPU)

    powerup2_sprite_list = pygame.sprite.Group()
    powerup2_sprite_list.add(plus50PU)

    powerup3_sprite_list = pygame.sprite.Group()
    powerup3_sprite_list.add(shrinkPU)

    powerup4_sprite_list = pygame.sprite.Group()
    powerup4_sprite_list.add(invencibilityPU)

    all_coming_cars = pygame.sprite.Group()
    all_coming_cars.add(car1)
    all_coming_cars.add(car2)
    all_coming_cars.add(car3)
    all_coming_cars.add(car4)


    #Allowing the user to close the screen...
    carryOn = True
    game_over_image = pygame.image.load("GAME OVER SAPO.png").convert_alpha()
    game_over_image = pygame.transform.scale(game_over_image, (WIDTH, HEIGHT))
    scorebox = pygame.image.load("img/scorebox2.png")
    score = 0
    
    clock=pygame.time.Clock()
    enemy_hit = False

    while carryOn:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    carryOn=False
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x:
                         PlayerCar1.moveRight(10)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                PlayerCar1.moveLeft(5)
                # Limites horizontais para o carro do jogador
                if PlayerCar1.rect.x < 135:
                    PlayerCar1.rect.x = 135
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                PlayerCar1.moveRight(5)
                 # Limites horizontais para o carro do jogador
                if PlayerCar1.rect.x > 570:
                    PlayerCar1.rect.x = 570

            if keys[pygame.K_UP] or keys[pygame.K_w]:
                PlayerCar1.moveup(5)
                if PlayerCar1.rect.y < 0:
                     PlayerCar1.rect.y = 0
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                PlayerCar1.movedown(5)
                if PlayerCar1.rect.y > 500:
                    PlayerCar1.rect.y = 500


            #Game Logic
            for car in all_coming_cars:
                car.moveForward(speed)
                if car.rect.y > HEIGHT:
                    score += 1
                    car.changeSpeed(random.randint(70, 115))
                    
                    car.rect.y = -200


            for powerup in powerup1_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -3749

            slowPU.moveForward(speed)
            if slowPU.rect.y > HEIGHT:
                 slowPU.rect.x = random.randint(135, 570-50)
                 slowPU.rect.y = -3749

            for powerup in powerup2_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -2382

            plus50PU.moveForward(speed)
            if plus50PU.rect.y > HEIGHT:
                 plus50PU.rect.x = random.randint(135, 570-50)
                 plus50PU.rect.y = -2382

            for powerup in powerup3_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -1557

            shrinkPU.moveForward(speed)
            if shrinkPU.rect.y > HEIGHT:
                 shrinkPU.rect.x = random.randint(135, 570-50)
                 shrinkPU.rect.y = -1557

            for powerup in powerup4_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -4934

            invencibilityPU.moveForward(speed)
            if invencibilityPU.rect.y > HEIGHT:
                 invencibilityPU.rect.x = random.randint(135, 570-50)
                 invencibilityPU.rect.y = -4934

            car1.moveForward(speed)
            if car1.rect.y > HEIGHT:
                   score +=1
                   car1_lane = random.choice(lanes["faixa1"])
                   car1.rect.x = car1_lane
                   car1.rect.y = -100

            car2.moveForward(speed)
            if car2.rect.y > HEIGHT:
                   score +=1
                   car2_lane = random.choice(lanes["faixa2"])
                   car2.rect.x = car2_lane
                   car2.rect.y = -100

            car3.moveForward(speed)
            if car3.rect.y > HEIGHT:
                   score +=1
                   car3_lane = random.choice(lanes["faixa3"])
                   car3.rect.x = car3_lane
                   car3.rect.y = -100

            car4.moveForward(speed)
            if car4.rect.y > HEIGHT:
                   score +=1
                   car4_lane = random.choice(lanes["faixa4"])
                   car4.rect.x = car4_lane
                   car4.rect.y = -100
                
                
                # Check if there is a car collision
            car_collision_list = pygame.sprite.spritecollide(PlayerCar1, all_coming_cars, False, pygame.sprite.collide_mask)
            for car in car_collision_list:
                    print("Car crash!")
                    # End Of Game
                    #carryOn = False
                    enemy_hit = True
            if enemy_hit:
                score_text = font.render(f"SCORE: {score}", 1, "black")
                play_again = pygame.image.load("img/Play Again Button.png")
                main_menu = pygame.image.load("img/Menu Button.png")
                background_lost_single = pygame.image.load("GAME OVER SAPO.png")
                
                screen.blit(background_lost_single, (0,0))
                screen.blit(play_again, (450, 400))
                screen.blit(score_text,(500,300))
                screen.blit(main_menu, (700,400))

                #updates the new screen
                pygame.display.update()


                break

                

            all_sprites_list.update()

            global offset_1

            #allowing the background to move down
            offset_1 += 2
            offset_1 %= HEIGHT

            # cleanig the screen
            screen.fill((0, 0, 0))

            # drawing the background twice, one above the other
            screen.blit(road_image, (0, offset_1))
            screen.blit(road_image, (0, offset_1 - HEIGHT))
            
            screen
            #Drawing on Screen
            # Desenha a imagem de fundo
            

           


            #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
            all_sprites_list.draw(screen)

            #Refresh Screen
            pygame.display.flip()

            #Number of frames per secong e.g. 60
            clock.tick(60)

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()  # Quit the game if the window is closed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False
                    pygame.quit()
        #checking for mouse position and clicks
        mouse_x, mouse_y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #if the button is pressed the game starts over again
        if 450  < mouse_x < 450 + play_again.get_width() and 400  < mouse_y < 400 + play_again.get_height():
            if click[0] == 1:
                car_racing3()
        # Check for mouse clicks on "Main Menu" button
        if 700  < mouse_x < 700 + main_menu.get_width() and 400  < mouse_y < 400 + main_menu.get_height():
            if click[0] == 1:
                # Return to the main menu 
                waiting = False  # Exit the waiting loop and return to the main menu
                interface.interface3()


def car_racing_multi():
    pygame.init()
    font = pygame.font.SysFont('Anton', 50)
    # Carrega a imagem da estrada
    road_image = pygame.image.load("img/1 (1).png").convert()

    WIDTH, HEIGHT = 800, 600

# Redimensiona a imagem para o tamanho da tela
    road_image = pygame.transform.scale(road_image, (WIDTH, HEIGHT)) 

    GREEN = (20, 255, 140)
    GREY = (210, 210 ,210)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    PURPLE = (255, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    BLUE = (100, 100, 255)

    speed = 0.6
    colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)

    PlayerCar1 = Car("img/player1map1.png", 100, 100, 70)
    PlayerCar1.rect.x = 160
    PlayerCar1.rect.y = HEIGHT - 100

    PlayerCar2 = Car("img/player2map1.png", 100, 100, 70)
    PlayerCar2.rect.x = 450
    PlayerCar2.rect.y = HEIGHT - 100

   

    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Car Racing")

    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()


    lanes = {
    "faixa1": [180, 190, 205],
    "faixa2": [290, 305, 320],
    "faixa3": [440, 450, 470],
    "faixa4": [550, 570, 590]
}


    slowPU = SlowPowerUp("img/SlowPowerUp.png", 50, 50, 55)
    slowPU.rect.x = random.randint(135, 570-50)
    slowPU.rect.y = -3749



    plus50PU = ScoreBoostPowerUp("img/+50PowerUp.png", 50, 50, 55)
    plus50PU.rect.x = random.randint(135, 570-50)
    plus50PU.rect.y = -2382

    shrinkPU = ShrinkPlayerPowerUp("img/ShrinkPowerUp.png", 50, 50, 55)
    shrinkPU.rect.x = random.randint(135, 570-50)
    shrinkPU.rect.y = -1557

    invencibilityPU = ShrinkPlayerPowerUp("img/InvencibilityPowerUp.png", 50, 50, 55)
    invencibilityPU.rect.x = random.randint(135, 570-50)
    invencibilityPU.rect.y = -4934

    image_paths = ["img/carro random.png", "img/carro random2.png", "img/carro random3.png", "img/carro random4.png"]

    car1 = Car(random.choice(image_paths), 60, 100, random.randint(70,115))
    car1_lane_start = random.choice(lanes["faixa1"])
    car1.rect.x = car1_lane_start
    car1.rect.y = -100
    car1.repaint(random.choice(image_paths))

    car2 = Car(random.choice(image_paths), 60, 100, random.randint(70,115))
    car2_lane_start = random.choice(lanes["faixa2"])
    car2.rect.x = car2_lane_start
    car2.rect.y = -600
    car2.repaint(random.choice(image_paths))

    car3 = Car(random.choice(image_paths), 60, 100, random.randint(70,115))
    car3_lane_start = random.choice(lanes["faixa3"])
    car3.rect.x = car3_lane_start
    car3.rect.y = -300
    car3.repaint(random.choice(image_paths))

    car4 = Car(random.choice(image_paths), 60, 100, random.randint(70,115))
    car4_lane_start = random.choice(lanes["faixa4"])
    car4.rect.x = car4_lane_start
    car4.rect.y = -900
    car4.repaint(random.choice(image_paths))





    # Add the car to the list of objects
    all_sprites_list.add(PlayerCar1)
    all_sprites_list.add(PlayerCar2)
    all_sprites_list.add(car1)
    all_sprites_list.add(car2)
    all_sprites_list.add(car3)
    all_sprites_list.add(car4)
    all_sprites_list.add(slowPU)
    all_sprites_list.add(plus50PU)
    all_sprites_list.add(shrinkPU)
    all_sprites_list.add(invencibilityPU)


    

    powerup1_sprite_list = pygame.sprite.Group()
    powerup1_sprite_list.add(slowPU)

    powerup2_sprite_list = pygame.sprite.Group()
    powerup2_sprite_list.add(plus50PU)

    powerup3_sprite_list = pygame.sprite.Group()
    powerup3_sprite_list.add(shrinkPU)

    powerup4_sprite_list = pygame.sprite.Group()
    powerup4_sprite_list.add(invencibilityPU)

    all_coming_cars = pygame.sprite.Group()
    all_coming_cars.add(car1)
    all_coming_cars.add(car2)
    all_coming_cars.add(car3)
    all_coming_cars.add(car4)


    #Allowing the user to close the screen...
    carryOn = True
    game_over_image = pygame.image.load("img/lostbackground.jpeg").convert()
    game_over_image = pygame.transform.scale(game_over_image, (WIDTH, HEIGHT))

    
    score = 0
    
    clock=pygame.time.Clock()
    enemy_hit1 = False
    enemy_hit2 = False

    while carryOn:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    carryOn=False
                
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                PlayerCar1.moveLeft(5)
                # Limites horizontais para o carro do jogador
                if PlayerCar1.rect.x < 135:
                    PlayerCar1.rect.x = 135
            if keys[pygame.K_RIGHT]:
                PlayerCar1.moveRight(5)
                 # Limites horizontais para o carro do jogador
                if PlayerCar1.rect.x > 570:
                    PlayerCar1.rect.x = 570

            if keys[pygame.K_UP]:
                PlayerCar1.moveup(5)
                if PlayerCar1.rect.y < 0:
                     PlayerCar1.rect.y = 0
            if keys[pygame.K_DOWN]:
                PlayerCar1.movedown(5)
                if PlayerCar1.rect.y > 500:
                    PlayerCar1.rect.y = 500

            if keys[pygame.K_a]:
                PlayerCar2.moveLeft(5)
                # Limites horizontais para o carro do jogador
                if PlayerCar2.rect.x < 135:
                    PlayerCar2.rect.x = 135
            if keys[pygame.K_d]:
                PlayerCar2.moveRight(5)
                 # Limites horizontais para o carro do jogador
                if PlayerCar2.rect.x > 570:
                    PlayerCar2.rect.x = 570

            if keys[pygame.K_w]:
                PlayerCar2.moveup(5)
                if PlayerCar2.rect.y < 0:
                     PlayerCar2.rect.y = 0
            if keys[pygame.K_s]:
                PlayerCar2.movedown(5)
                if PlayerCar2.rect.y > 500:
                    PlayerCar2.rect.y = 500


            #Game Logic
            for car in all_coming_cars:
                car.moveForward(speed)
                if car.rect.y > HEIGHT:
                    score += 1
                    car.changeSpeed(random.randint(70, 115))
                    
                    car.rect.y = -200


            for powerup in powerup1_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -3749

            slowPU.moveForward(speed)
            if slowPU.rect.y > HEIGHT:
                 slowPU.rect.x = random.randint(135, 570-50)
                 slowPU.rect.y = -3749

            for powerup in powerup2_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -2382

            plus50PU.moveForward(speed)
            if plus50PU.rect.y > HEIGHT:
                 plus50PU.rect.x = random.randint(135, 570-50)
                 plus50PU.rect.y = -2382

            for powerup in powerup3_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -1557

            shrinkPU.moveForward(speed)
            if shrinkPU.rect.y > HEIGHT:
                 shrinkPU.rect.x = random.randint(135, 570-50)
                 shrinkPU.rect.y = -1557

            for powerup in powerup4_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -4934

            invencibilityPU.moveForward(speed)
            if invencibilityPU.rect.y > HEIGHT:
                 invencibilityPU.rect.x = random.randint(135, 570-50)
                 invencibilityPU.rect.y = -4934

            car1.moveForward(speed)
            if car1.rect.y > HEIGHT:
                   score += 1
                   car1_lane = random.choice(lanes["faixa1"])
                   car1.rect.x = car1_lane
                   car1.rect.y = -100

            car2.moveForward(speed)
            if car2.rect.y > HEIGHT:
                   score += 1
                   car2_lane = random.choice(lanes["faixa2"])
                   car2.rect.x = car2_lane
                   car2.rect.y = -100

            car3.moveForward(speed)
            if car3.rect.y > HEIGHT:
                   score += 1
                   car3_lane = random.choice(lanes["faixa3"])
                   car3.rect.x = car3_lane
                   car3.rect.y = -100

            car4.moveForward(speed)
            if car4.rect.y > HEIGHT:
                   score += 1
                   car4_lane = random.choice(lanes["faixa4"])
                   car4.rect.x = car4_lane
                   car4.rect.y = -100
                
                
                # Check if there is a car collision
            car_collision_list = pygame.sprite.spritecollide(PlayerCar1, all_coming_cars, False, pygame.sprite.collide_mask)
            for car in car_collision_list:
                    print("Car crash!")
                    # End Of Game
                    enemy_hit1 = True
            if enemy_hit1:
                
                score_text = font.render(f"SCORE: {score}", 1, "black")
                play_again = pygame.image.load("img/Play Again Button.png")
                main_menu = pygame.image.load("img/Menu Button.png")
                background_lost_multi = pygame.image.load("GREEN WINS.png")
                
                screen.blit(background_lost_multi, (0,0))
                
                screen.blit(play_again, (630, 350))
                screen.blit(score_text,(600,270))
                screen.blit(main_menu, (630,450))


                #updates the new screen
                pygame.display.update()

                break

            car_collision_list = pygame.sprite.spritecollide(PlayerCar2, all_coming_cars, False, pygame.sprite.collide_mask)
            for car in car_collision_list:
                    print("Car crash!")
                    # End Of Game
                    #carryOn = False
                    enemy_hit2 = True
            if enemy_hit2:
                
                score_text = font.render(f"SCORE: {score}", 1, "black")
                play_again = pygame.image.load("img/Play Again Button.png")
                main_menu = pygame.image.load("img/Menu Button.png")
                background_lost_multi = pygame.image.load("RED WINS.png")
                
                screen.blit(background_lost_multi, (0,0))
                
                screen.blit(play_again, (630, 350))
                screen.blit(score_text,(600,270))
                screen.blit(main_menu, (630,450))

                #updates the new screen
                pygame.display.update()


                break

                

            all_sprites_list.update()

            global offset_1

            #allowing the background to move down
            offset_1 += 2
            offset_1 %= HEIGHT

            # cleanig the screen
            screen.fill((0, 0, 0))

            # drawing the background twice, one above the other
            screen.blit(road_image, (0, offset_1))
            screen.blit(road_image, (0, offset_1 - HEIGHT))

            #Drawing on Screen
            # Desenha a imagem de fundo
            

           


            #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
            all_sprites_list.draw(screen)

            #Refresh Screen
            pygame.display.flip()

            #Number of frames per secong e.g. 60
            clock.tick(60)

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()  # Quit the game if the window is closed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False
                    pygame.quit()
        #checking for mouse position and clicks
        mouse_x, mouse_y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #if the button is pressed the game starts over again
        if 630  < mouse_x < 630 + play_again.get_width() and 350  < mouse_y < 350 + play_again.get_height():
            if click[0] == 1:
                car_racing_multi()
        # Check for mouse clicks on "Main Menu" button
        if 630  < mouse_x < 630 + main_menu.get_width() and 450  < mouse_y < 450 + main_menu.get_height():
            if click[0] == 1:
                # Return to the main menu 
                waiting = False  # Exit the waiting loop and return to the main menu
                interface.interface()

def car_racing_multi2():
    pygame.init()
    font = pygame.font.SysFont('Anton', 50)
    # Carrega a imagem da estrada
    road_image = pygame.image.load("img/3 (1).png").convert()

    WIDTH, HEIGHT = 800, 600

# Redimensiona a imagem para o tamanho da tela
    road_image = pygame.transform.scale(road_image, (WIDTH, HEIGHT)) 

    GREEN = (20, 255, 140)
    GREY = (210, 210 ,210)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    PURPLE = (255, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    BLUE = (100, 100, 255)

    speed = 0.6
    colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)

    PlayerCar1 = Car("img/player1map2.png", 100, 100, 70)
    PlayerCar1.rect.x = 160
    PlayerCar1.rect.y = HEIGHT - 100

    PlayerCar2 = Car("img/player2map2.png", 100, 100, 70)
    PlayerCar2.rect.x = 450
    PlayerCar2.rect.y = HEIGHT - 100

   

    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Car Racing")

    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()


    lanes = {
    "faixa1": [180, 190, 205],
    "faixa2": [290, 305, 320],
    "faixa3": [440, 450, 470],
    "faixa4": [550, 570, 590]
}
    

    slowPU = SlowPowerUp("img/SlowPowerUp.png", 50, 50, 55)
    slowPU.rect.x = random.randint(135, 570-50)
    slowPU.rect.y = -3749



    plus50PU = ScoreBoostPowerUp("img/+50PowerUp.png", 50, 50, 55)
    plus50PU.rect.x = random.randint(135, 570-50)
    plus50PU.rect.y = -2382

    shrinkPU = ShrinkPlayerPowerUp("img/ShrinkPowerUp.png", 50, 50, 55)
    shrinkPU.rect.x = random.randint(135, 570-50)
    shrinkPU.rect.y = -1557

    invencibilityPU = ShrinkPlayerPowerUp("img/InvencibilityPowerUp.png", 50, 50, 55)
    invencibilityPU.rect.x = random.randint(135, 570-50)
    invencibilityPU.rect.y = -4934

    image_paths = ["img/enemymap2.png"]

    car1 = Car(random.choice(image_paths), 60, 100, random.randint(70,115))
    car1_lane_start = random.choice(lanes["faixa1"])
    car1.rect.x = car1_lane_start
    car1.rect.y = -100
    car1.repaint(random.choice(image_paths))

    car2 = Car(random.choice(image_paths), 60, 100, random.randint(70,115))
    car2_lane_start = random.choice(lanes["faixa2"])
    car2.rect.x = car2_lane_start
    car2.rect.y = -600
    car2.repaint(random.choice(image_paths))

    car3 = Car(random.choice(image_paths), 60, 100, random.randint(70,115))
    car3_lane_start = random.choice(lanes["faixa3"])
    car3.rect.x = car3_lane_start
    car3.rect.y = -300
    car3.repaint(random.choice(image_paths))

    car4 = Car(random.choice(image_paths), 60, 100, random.randint(70,115))
    car4_lane_start = random.choice(lanes["faixa4"])
    car4.rect.x = car4_lane_start
    car4.rect.y = -900
    car4.repaint(random.choice(image_paths))





    # Add the car to the list of objects
    all_sprites_list.add(PlayerCar1)
    all_sprites_list.add(PlayerCar2)
    all_sprites_list.add(car1)
    all_sprites_list.add(car2)
    all_sprites_list.add(car3)
    all_sprites_list.add(car4)
    all_sprites_list.add(slowPU)
    all_sprites_list.add(plus50PU)
    all_sprites_list.add(shrinkPU)
    all_sprites_list.add(invencibilityPU)


    

    powerup1_sprite_list = pygame.sprite.Group()
    powerup1_sprite_list.add(slowPU)

    powerup2_sprite_list = pygame.sprite.Group()
    powerup2_sprite_list.add(plus50PU)

    powerup3_sprite_list = pygame.sprite.Group()
    powerup3_sprite_list.add(shrinkPU)

    powerup4_sprite_list = pygame.sprite.Group()
    powerup4_sprite_list.add(invencibilityPU)

    all_coming_cars = pygame.sprite.Group()
    all_coming_cars.add(car1)
    all_coming_cars.add(car2)
    all_coming_cars.add(car3)
    all_coming_cars.add(car4)


    #Allowing the user to close the screen...
    carryOn = True
    game_over_image = pygame.image.load("img/lostbackground.jpeg").convert()
    game_over_image = pygame.transform.scale(game_over_image, (WIDTH, HEIGHT))

    
    score = 0
    
    clock=pygame.time.Clock()
    enemy_hit1 = False
    enemy_hit2 = False

    while carryOn:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    carryOn=False
                
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                PlayerCar1.moveLeft(5)
                # Limites horizontais para o carro do jogador
                if PlayerCar1.rect.x < 135:
                    PlayerCar1.rect.x = 135
            if keys[pygame.K_RIGHT]:
                PlayerCar1.moveRight(5)
                 # Limites horizontais para o carro do jogador
                if PlayerCar1.rect.x > 560:
                    PlayerCar1.rect.x = 560

            if keys[pygame.K_UP]:
                PlayerCar1.moveup(5)
                if PlayerCar1.rect.y < 0:
                     PlayerCar1.rect.y = 0
            if keys[pygame.K_DOWN]:
                PlayerCar1.movedown(5)
                if PlayerCar1.rect.y > 500:
                    PlayerCar1.rect.y = 500

            if keys[pygame.K_a]:
                PlayerCar2.moveLeft(5)
                # Limites horizontais para o carro do jogador
                if PlayerCar2.rect.x < 135:
                    PlayerCar2.rect.x = 135
            if keys[pygame.K_d]:
                PlayerCar2.moveRight(5)
                 # Limites horizontais para o carro do jogador
                if PlayerCar2.rect.x > 560:
                    PlayerCar2.rect.x = 560

            if keys[pygame.K_w]:
                PlayerCar2.moveup(5)
                if PlayerCar2.rect.y < 0:
                     PlayerCar2.rect.y = 0
            if keys[pygame.K_s]:
                PlayerCar2.movedown(5)
                if PlayerCar2.rect.y > 500:
                    PlayerCar2.rect.y = 500


            #Game Logic
            for car in all_coming_cars:
                car.moveForward(speed)
                if car.rect.y > HEIGHT:
                    score += 1
                    car.changeSpeed(random.randint(70, 115))
                    
                    car.rect.y = -200


            for powerup in powerup1_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -3749

            slowPU.moveForward(speed)
            if slowPU.rect.y > HEIGHT:
                 slowPU.rect.x = random.randint(135, 570-50)
                 slowPU.rect.y = -3749

            for powerup in powerup2_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -2382

            plus50PU.moveForward(speed)
            if plus50PU.rect.y > HEIGHT:
                 plus50PU.rect.x = random.randint(135, 570-50)
                 plus50PU.rect.y = -2382

            for powerup in powerup3_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -1557

            shrinkPU.moveForward(speed)
            if shrinkPU.rect.y > HEIGHT:
                 shrinkPU.rect.x = random.randint(135, 570-50)
                 shrinkPU.rect.y = -1557

            for powerup in powerup4_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -4934

            invencibilityPU.moveForward(speed)
            if invencibilityPU.rect.y > HEIGHT:
                 invencibilityPU.rect.x = random.randint(135, 570-50)
                 invencibilityPU.rect.y = -4934

            car1.moveForward(speed)
            if car1.rect.y > HEIGHT:
                   score += 1
                   car1_lane = random.choice(lanes["faixa1"])
                   car1.rect.x = car1_lane
                   car1.rect.y = -100

            car2.moveForward(speed)
            if car2.rect.y > HEIGHT:
                   score += 1
                   car2_lane = random.choice(lanes["faixa2"])
                   car2.rect.x = car2_lane
                   car2.rect.y = -100

            car3.moveForward(speed)
            if car3.rect.y > HEIGHT:
                   score += 1
                   car3_lane = random.choice(lanes["faixa3"])
                   car3.rect.x = car3_lane
                   car3.rect.y = -100

            car4.moveForward(speed)
            if car4.rect.y > HEIGHT:
                   score += 1
                   car4_lane = random.choice(lanes["faixa4"])
                   car4.rect.x = car4_lane
                   car4.rect.y = -100
                
                
                # Check if there is a car collision
            car_collision_list = pygame.sprite.spritecollide(PlayerCar1, all_coming_cars, False, pygame.sprite.collide_mask)
            for car in car_collision_list:
                    print("Car crash!")
                    # End Of Game
                    enemy_hit1 = True
            if enemy_hit1:
                
                score_text = font.render(f"SCORE: {score}", 1, "black")
                play_again = pygame.image.load("img/Play Again Button.png")
                main_menu = pygame.image.load("img/Menu Button.png")
                background_lost_multi = pygame.image.load("img/GREENWINS_sea (1).png")
                
                screen.blit(background_lost_multi, (0,0))
                
                screen.blit(play_again, (630, 350))
                screen.blit(score_text,(600,270))
                screen.blit(main_menu, (630,450))


                #updates the new screen
                pygame.display.update()

                break

            car_collision_list = pygame.sprite.spritecollide(PlayerCar2, all_coming_cars, False, pygame.sprite.collide_mask)
            for car in car_collision_list:
                    print("Car crash!")
                    # End Of Game
                    #carryOn = False
                    enemy_hit2 = True
            if enemy_hit2:
                
                score_text = font.render(f"SCORE: {score}", 1, "black")
                play_again = pygame.image.load("img/Play Again Button.png")
                main_menu = pygame.image.load("img/Menu Button.png")
                background_lost_multi = pygame.image.load("img/REDWINS_sea.png")
                
                screen.blit(background_lost_multi, (0,0))
                
                screen.blit(play_again, (630, 350))
                screen.blit(score_text,(600,270))
                screen.blit(main_menu, (630,450))

                #updates the new screen
                pygame.display.update()


                break

                

            all_sprites_list.update()

            global offset_1

            #allowing the background to move down
            offset_1 += 2
            offset_1 %= HEIGHT

            # cleanig the screen
            screen.fill((0, 0, 0))

            # drawing the background twice, one above the other
            screen.blit(road_image, (0, offset_1))
            screen.blit(road_image, (0, offset_1 - HEIGHT))

            #Drawing on Screen
            # Desenha a imagem de fundo
            

           


            #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
            all_sprites_list.draw(screen)

            #Refresh Screen
            pygame.display.flip()

            #Number of frames per secong e.g. 60
            clock.tick(60)

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()  # Quit the game if the window is closed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False
                    pygame.quit()
        #checking for mouse position and clicks
        mouse_x, mouse_y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #if the button is pressed the game starts over again
        if 630  < mouse_x < 630 + play_again.get_width() and 350  < mouse_y < 350 + play_again.get_height():
            if click[0] == 1:
                car_racing_multi2()
        # Check for mouse clicks on "Main Menu" button
        if 630  < mouse_x < 630 + main_menu.get_width() and 450  < mouse_y < 450 + main_menu.get_height():
            if click[0] == 1:
                # Return to the main menu 
                waiting = False  # Exit the waiting loop and return to the main menu
                interface.interface2()


def car_racing_multi3():
    pygame.init()
    font = pygame.font.SysFont('Anton', 50)
    # Carrega a imagem da estrada
    road_image = pygame.image.load("img/2 (1).png").convert()

    WIDTH, HEIGHT = 800, 600

# Redimensiona a imagem para o tamanho da tela
    road_image = pygame.transform.scale(road_image, (WIDTH, HEIGHT)) 

    GREEN = (20, 255, 140)
    GREY = (210, 210 ,210)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    PURPLE = (255, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    BLUE = (100, 100, 255)

    speed = 0.6
    colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)

    PlayerCar1 = Car("img/player1map3.png", 100, 100, 70)
    PlayerCar1.rect.x = 160
    PlayerCar1.rect.y = HEIGHT - 100

    PlayerCar2 = Car("img/player2map3.png", 100, 100, 70)
    PlayerCar2.rect.x = 450
    PlayerCar2.rect.y = HEIGHT - 100

   

    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Car Racing")

    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()


    lanes = {
    "faixa1": [180, 190, 205],
    "faixa2": [290, 305, 320],
    "faixa3": [440, 450, 470],
    "faixa4": [550, 570, 590]
}

    slowPU = SlowPowerUp("img/SlowPowerUp.png", 50, 50, 55)
    slowPU.rect.x = random.randint(135, 570-50)
    slowPU.rect.y = -3749



    plus50PU = ScoreBoostPowerUp("img/+50PowerUp.png", 50, 50, 55)
    plus50PU.rect.x = random.randint(135, 570-50)
    plus50PU.rect.y = -2382

    shrinkPU = ShrinkPlayerPowerUp("img/ShrinkPowerUp.png", 50, 50, 55)
    shrinkPU.rect.x = random.randint(135, 570-50)
    shrinkPU.rect.y = -1557

    invencibilityPU = ShrinkPlayerPowerUp("img/InvencibilityPowerUp.png", 50, 50, 55)
    invencibilityPU.rect.x = random.randint(135, 570-50)
    invencibilityPU.rect.y = -4934

    image_paths = ["img/enemymap3.png"]

    car1 = Car(random.choice(image_paths), 60, 100, random.randint(70,115))
    car1_lane_start = random.choice(lanes["faixa1"])
    car1.rect.x = car1_lane_start
    car1.rect.y = -100
    car1.repaint(random.choice(image_paths))

    car2 = Car(random.choice(image_paths), 60, 100, random.randint(70,115))
    car2_lane_start = random.choice(lanes["faixa2"])
    car2.rect.x = car2_lane_start
    car2.rect.y = -600
    car2.repaint(random.choice(image_paths))

    car3 = Car(random.choice(image_paths), 60, 100, random.randint(70,115))
    car3_lane_start = random.choice(lanes["faixa3"])
    car3.rect.x = car3_lane_start
    car3.rect.y = -300
    car3.repaint(random.choice(image_paths))

    car4 = Car(random.choice(image_paths), 60, 100, random.randint(70,115))
    car4_lane_start = random.choice(lanes["faixa4"])
    car4.rect.x = car4_lane_start
    car4.rect.y = -900
    car4.repaint(random.choice(image_paths))





    # Add the car to the list of objects
    all_sprites_list.add(PlayerCar1)
    all_sprites_list.add(PlayerCar2)
    all_sprites_list.add(car1)
    all_sprites_list.add(car2)
    all_sprites_list.add(car3)
    all_sprites_list.add(car4)
    all_sprites_list.add(slowPU)
    all_sprites_list.add(plus50PU)
    all_sprites_list.add(shrinkPU)
    all_sprites_list.add(invencibilityPU)


    

    powerup1_sprite_list = pygame.sprite.Group()
    powerup1_sprite_list.add(slowPU)

    powerup2_sprite_list = pygame.sprite.Group()
    powerup2_sprite_list.add(plus50PU)

    powerup3_sprite_list = pygame.sprite.Group()
    powerup3_sprite_list.add(shrinkPU)

    powerup4_sprite_list = pygame.sprite.Group()
    powerup4_sprite_list.add(invencibilityPU)

    all_coming_cars = pygame.sprite.Group()
    all_coming_cars.add(car1)
    all_coming_cars.add(car2)
    all_coming_cars.add(car3)
    all_coming_cars.add(car4)


    #Allowing the user to close the screen...
    carryOn = True
    game_over_image = pygame.image.load("img/lostbackground.jpeg").convert()
    game_over_image = pygame.transform.scale(game_over_image, (WIDTH, HEIGHT))

    
    score = 0
    
    clock=pygame.time.Clock()
    enemy_hit1 = False
    enemy_hit2 = False

    while carryOn:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    carryOn=False
                
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                PlayerCar1.moveLeft(5)
                # Limites horizontais para o carro do jogador
                if PlayerCar1.rect.x < 135:
                    PlayerCar1.rect.x = 135
            if keys[pygame.K_RIGHT]:
                PlayerCar1.moveRight(5)
                 # Limites horizontais para o carro do jogador
                if PlayerCar1.rect.x > 570:
                    PlayerCar1.rect.x = 570

            if keys[pygame.K_UP]:
                PlayerCar1.moveup(5)
                if PlayerCar1.rect.y < 0:
                     PlayerCar1.rect.y = 0
            if keys[pygame.K_DOWN]:
                PlayerCar1.movedown(5)
                if PlayerCar1.rect.y > 500:
                    PlayerCar1.rect.y = 500

            if keys[pygame.K_a]:
                PlayerCar2.moveLeft(5)
                # Limites horizontais para o carro do jogador
                if PlayerCar2.rect.x < 135:
                    PlayerCar2.rect.x = 135
            if keys[pygame.K_d]:
                PlayerCar2.moveRight(5)
                 # Limites horizontais para o carro do jogador
                if PlayerCar2.rect.x > 570:
                    PlayerCar2.rect.x = 570

            if keys[pygame.K_w]:
                PlayerCar2.moveup(5)
                if PlayerCar2.rect.y < 0:
                     PlayerCar2.rect.y = 0
            if keys[pygame.K_s]:
                PlayerCar2.movedown(5)
                if PlayerCar2.rect.y > 500:
                    PlayerCar2.rect.y = 500


            #Game Logic
            for car in all_coming_cars:
                car.moveForward(speed)
                if car.rect.y > HEIGHT:
                    score += 1
                    car.changeSpeed(random.randint(70, 115))
                    
                    car.rect.y = -200

            for powerup in powerup1_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -3749

            slowPU.moveForward(speed)
            if slowPU.rect.y > HEIGHT:
                 slowPU.rect.x = random.randint(135, 570-50)
                 slowPU.rect.y = -3749

            for powerup in powerup2_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -2382

            plus50PU.moveForward(speed)
            if plus50PU.rect.y > HEIGHT:
                 plus50PU.rect.x = random.randint(135, 570-50)
                 plus50PU.rect.y = -2382

            for powerup in powerup3_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -1557

            shrinkPU.moveForward(speed)
            if shrinkPU.rect.y > HEIGHT:
                 shrinkPU.rect.x = random.randint(135, 570-50)
                 shrinkPU.rect.y = -1557

            for powerup in powerup4_sprite_list:
                 powerup.moveForward(speed)
                 if powerup.rect.y > HEIGHT:
                      powerup.rect.y = -4934

            invencibilityPU.moveForward(speed)
            if invencibilityPU.rect.y > HEIGHT:
                 invencibilityPU.rect.x = random.randint(135, 570-50)
                 invencibilityPU.rect.y = -4934

            car1.moveForward(speed)
            if car1.rect.y > HEIGHT:
                   score += 1
                   car1_lane = random.choice(lanes["faixa1"])
                   car1.rect.x = car1_lane
                   car1.rect.y = -100

            car2.moveForward(speed)
            if car2.rect.y > HEIGHT:
                   score += 1
                   car2_lane = random.choice(lanes["faixa2"])
                   car2.rect.x = car2_lane
                   car2.rect.y = -100

            car3.moveForward(speed)
            if car3.rect.y > HEIGHT:
                   score += 1
                   car3_lane = random.choice(lanes["faixa3"])
                   car3.rect.x = car3_lane
                   car3.rect.y = -100

            car4.moveForward(speed)
            if car4.rect.y > HEIGHT:
                   score += 1
                   car4_lane = random.choice(lanes["faixa4"])
                   car4.rect.x = car4_lane
                   car4.rect.y = -100
                
                
                # Check if there is a car collision
            car_collision_list = pygame.sprite.spritecollide(PlayerCar1, all_coming_cars, False, pygame.sprite.collide_mask)
            for car in car_collision_list:
                    print("Car crash!")
                    # End Of Game
                    enemy_hit1 = True
            if enemy_hit1:
                
                score_text = font.render(f"SCORE: {score}", 1, "black")
                play_again = pygame.image.load("img/Play Again Button.png")
                main_menu = pygame.image.load("img/Menu Button.png")
                background_lost_multi = pygame.image.load("img/GREENWINS_space.png")
                
                screen.blit(background_lost_multi, (0,0))
                
                screen.blit(play_again, (630, 350))
                screen.blit(score_text,(600,270))
                screen.blit(main_menu, (630,450))


                #updates the new screen
                pygame.display.update()

                break

            car_collision_list = pygame.sprite.spritecollide(PlayerCar2, all_coming_cars, False, pygame.sprite.collide_mask)
            for car in car_collision_list:
                    print("Car crash!")
                    # End Of Game
                    #carryOn = False
                    enemy_hit2 = True
            if enemy_hit2:
                
                score_text = font.render(f"SCORE: {score}", 1, "black")
                play_again = pygame.image.load("img/Play Again Button.png")
                main_menu = pygame.image.load("img/Menu Button.png")
                background_lost_multi = pygame.image.load("img/REDWINS_space.png")
                
                screen.blit(background_lost_multi, (0,0))
                
                screen.blit(play_again, (630, 350))
                screen.blit(score_text,(600,270))
                screen.blit(main_menu, (630,450))

                #updates the new screen
                pygame.display.update()


                break

                

            all_sprites_list.update()

            global offset_1

            #allowing the background to move down
            offset_1 += 2
            offset_1 %= HEIGHT

            # cleanig the screen
            screen.fill((0, 0, 0))

            # drawing the background twice, one above the other
            screen.blit(road_image, (0, offset_1))
            screen.blit(road_image, (0, offset_1 - HEIGHT))

            #Drawing on Screen
            # Desenha a imagem de fundo
            

           


            #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
            all_sprites_list.draw(screen)

            #Refresh Screen
            pygame.display.flip()

            #Number of frames per secong e.g. 60
            clock.tick(60)

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()  # Quit the game if the window is closed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False
                    pygame.quit()
        #checking for mouse position and clicks
        mouse_x, mouse_y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #if the button is pressed the game starts over again
        if 630  < mouse_x < 630 + play_again.get_width() and 350  < mouse_y < 350 + play_again.get_height():
            if click[0] == 1:
                car_racing_multi3()
        # Check for mouse clicks on "Main Menu" button
        if 630  < mouse_x < 630 + main_menu.get_width() and 450  < mouse_y < 450 + main_menu.get_height():
            if click[0] == 1:
                # Return to the main menu 
                waiting = False  # Exit the waiting loop and return to the main menu
                interface.interface3()


