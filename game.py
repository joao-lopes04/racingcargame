import pygame, random, sys
#Let's import the Car Class
from car import Car



def car_racing():

    pygame.init()

    #loads road image
    road_image = pygame.image.load("img/estrada.png").convert()

    WIDTH, HEIGHT = 900, 500

    #resize screen
    road_image = pygame.transform.scale(road_image, (WIDTH, HEIGHT))

    speed = 0.6

    PlayerCar1 = Car("img/mycar.png", 60, 100, 70)
    PlayerCar1.rect.x = 160
    PlayerCar1.rect.y = HEIGHT - 100


   

    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Car Racing")

    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()


    lanes = {
    "faixa1": [180, 190, 205],
    "faixa2": [290, 305, 320],
    "faixa3": [440, 450, 465],
    "faixa4": [550, 570, 590]
}

    image_paths = ["img/carro random.png", "img/carro random2.png", "img/carro random3.png", "img/carro random4.png"]

    car1 = Car(random.choice(image_paths), 60, 100, random.randint(50, 100))
    car1_lane_start = random.choice(lanes["faixa1"])
    car1.rect.x = car1_lane_start
    car1.rect.y = -100
    car1.repaint(random.choice(image_paths))

    car2 = Car(random.choice(image_paths), 60, 100, random.randint(50, 100))
    car2_lane_start = random.choice(lanes["faixa2"])
    car2.rect.x = car2_lane_start
    car2.rect.y = -600
    car2.repaint(random.choice(image_paths))

    car3 = Car(random.choice(image_paths), 60, 100, random.randint(50, 100))
    car3_lane_start = random.choice(lanes["faixa3"])
    car3.rect.x = car3_lane_start
    car3.rect.y = -300
    car3.repaint(random.choice(image_paths))

    car4 = Car(random.choice(image_paths), 60, 100, random.randint(50, 100))
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

    all_coming_cars = pygame.sprite.Group()
    all_coming_cars.add(car1)
    all_coming_cars.add(car2)
    all_coming_cars.add(car3)
    all_coming_cars.add(car4)


    #Allowing the user to close the window...
    carryOn = True
    game_over_image = pygame.image.load("img/lostbackground.jpeg").convert()
    game_over_image = pygame.transform.scale(game_over_image, (WIDTH, HEIGHT))

    
    clock=pygame.time.Clock()

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
                if PlayerCar1.rect.x > 610:
                    PlayerCar1.rect.x = 610

            if keys[pygame.K_UP] or keys[pygame.K_w]:
                PlayerCar1.moveup(5)
                if PlayerCar1.rect.y < 0:
                     PlayerCar1.rect.y = 0
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                PlayerCar1.movedown(5)
                if PlayerCar1.rect.y > 400:
                    PlayerCar1.rect.y = 400


            #Game Logic
            for car in all_coming_cars:
                car.moveForward(speed)
                if car.rect.y > HEIGHT:
                    car.changeSpeed(random.randint(50,100))
                    
                    car.rect.y = -200

            car1.moveForward(speed)
            if car1.rect.y > HEIGHT:
                   car1_lane = random.choice(lanes["faixa1"])
                   car1.rect.x = car1_lane
                   car1.rect.y = -100

            car2.moveForward(speed)
            if car2.rect.y > HEIGHT:
                   car2_lane = random.choice(lanes["faixa2"])
                   car2.rect.x = car2_lane
                   car2.rect.y = -100

            car3.moveForward(speed)
            if car3.rect.y > HEIGHT:
                   car3_lane = random.choice(lanes["faixa3"])
                   car3.rect.x = car3_lane
                   car3.rect.y = -100

            car4.moveForward(speed)
            if car4.rect.y > HEIGHT:
                   car4_lane = random.choice(lanes["faixa4"])
                   car4.rect.x = car4_lane
                   car4.rect.y = -100
                
                
                # Check if there is a car collision
            car_collision_list = pygame.sprite.spritecollide(PlayerCar1, all_coming_cars, False)
            for car in car_collision_list:
                    print("Car crash!")
                    # End Of Game
                    carryOn = False

                

            all_sprites_list.update()

            screen.blit(road_image, (0, 0))

            #Drawing on Screen
            # Desenha a imagem de fundo
            

           


            #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
            all_sprites_list.draw(screen)

            #Refresh Screen
            pygame.display.flip()

            #Number of frames per secong e.g. 60
            clock.tick(60)

    pygame.quit()


def car_racing_mutli():
    pygame.init()

    # Carrega a imagem da estrada
    road_image = pygame.image.load("img/estrada.png").convert()

    WIDTH, HEIGHT = 900, 500

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

    PlayerCar1 = Car("img/mycar.png", 60, 100, 70)
    PlayerCar1.rect.x = 160
    PlayerCar1.rect.y = HEIGHT - 100

    PlayerCar2 = Car("img/playermap1.png", 60, 100, 100)
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
    "faixa3": [440, 450, 465],
    "faixa4": [550, 570, 590]
}

    image_paths = ["img/carro random.png", "img/carro random2.png", "img/carro random3.png", "img/carro random4.png"]

    car1 = Car(random.choice(image_paths), 60, 100, random.randint(50, 100))
    car1_lane_start = random.choice(lanes["faixa1"])
    car1.rect.x = car1_lane_start
    car1.rect.y = -100
    car1.repaint(random.choice(image_paths))

    car2 = Car(random.choice(image_paths), 60, 100, random.randint(50, 100))
    car2_lane_start = random.choice(lanes["faixa2"])
    car2.rect.x = car2_lane_start
    car2.rect.y = -600
    car2.repaint(random.choice(image_paths))

    car3 = Car(random.choice(image_paths), 60, 100, random.randint(50, 100))
    car3_lane_start = random.choice(lanes["faixa3"])
    car3.rect.x = car3_lane_start
    car3.rect.y = -300
    car3.repaint(random.choice(image_paths))

    car4 = Car(random.choice(image_paths), 60, 100, random.randint(50, 100))
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

    all_coming_cars = pygame.sprite.Group()
    all_coming_cars.add(car1)
    all_coming_cars.add(car2)
    all_coming_cars.add(car3)
    all_coming_cars.add(car4)


    #Allowing the user to close the window...
    carryOn = True
    game_over_image = pygame.image.load("img/lostbackground.jpeg").convert()
    game_over_image = pygame.transform.scale(game_over_image, (WIDTH, HEIGHT))

    
    clock=pygame.time.Clock()

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
                if PlayerCar1.rect.x > 610:
                    PlayerCar1.rect.x = 610

            if keys[pygame.K_UP]:
                PlayerCar1.moveup(5)
                if PlayerCar1.rect.y < 0:
                     PlayerCar1.rect.y = 0
            if keys[pygame.K_DOWN]:
                PlayerCar1.movedown(5)
                if PlayerCar1.rect.y > 400:
                    PlayerCar1.rect.y = 400

            if keys[pygame.K_a]:
                PlayerCar2.moveLeft(5)
                # Limites horizontais para o carro do jogador
                if PlayerCar2.rect.x < 135:
                    PlayerCar2.rect.x = 135
            if keys[pygame.K_d]:
                PlayerCar2.moveRight(5)
                 # Limites horizontais para o carro do jogador
                if PlayerCar2.rect.x > 610:
                    PlayerCar2.rect.x = 610

            if keys[pygame.K_w]:
                PlayerCar2.moveup(5)
                if PlayerCar2.rect.y < 0:
                     PlayerCar2.rect.y = 0
            if keys[pygame.K_s]:
                PlayerCar2.movedown(5)
                if PlayerCar2.rect.y > 400:
                    PlayerCar2.rect.y = 400


            #Game Logic
            for car in all_coming_cars:
                car.moveForward(speed)
                if car.rect.y > HEIGHT:
                    car.changeSpeed(random.randint(50,100))
                    
                    car.rect.y = -200

            car1.moveForward(speed)
            if car1.rect.y > HEIGHT:
                   car1_lane = random.choice(lanes["faixa1"])
                   car1.rect.x = car1_lane
                   car1.rect.y = -100

            car2.moveForward(speed)
            if car2.rect.y > HEIGHT:
                   car2_lane = random.choice(lanes["faixa2"])
                   car2.rect.x = car2_lane
                   car2.rect.y = -100

            car3.moveForward(speed)
            if car3.rect.y > HEIGHT:
                   car3_lane = random.choice(lanes["faixa3"])
                   car3.rect.x = car3_lane
                   car3.rect.y = -100

            car4.moveForward(speed)
            if car4.rect.y > HEIGHT:
                   car4_lane = random.choice(lanes["faixa4"])
                   car4.rect.x = car4_lane
                   car4.rect.y = -100
                
                
                # Check if there is a car collision
            car_collision_list = pygame.sprite.spritecollide(PlayerCar1, all_coming_cars, False)
            for car in car_collision_list:
                    print("Car crash!")
                    # End Of Game
                    carryOn = False

            car_collision_list = pygame.sprite.spritecollide(PlayerCar2, all_coming_cars, False)
            for car in car_collision_list:
                    print("Car crash!")
                    # End Of Game
                    carryOn = False

                

            all_sprites_list.update()

            screen.blit(road_image, (0, 0))

            #Drawing on Screen
            # Desenha a imagem de fundo
            

           


            #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
            all_sprites_list.draw(screen)

            #Refresh Screen
            pygame.display.flip()

            #Number of frames per secong e.g. 60
            clock.tick(60)

    pygame.quit()
