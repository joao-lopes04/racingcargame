import pygame
import random
import time
from abc import ABC, abstractclassmethod
from car import Car


class PowerUp(ABC):
  def __init__(self, image_path, width, height, speed, pu_duration):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()


    #Initialise attributes of the PowerUp.
        self.width=width
        self.height=height
        self.speed = speed

    

    # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        @abstractclassmethod
        def affect_player():
            pass

        @abstractclassmethod
        def affect_traffic():
            pass
        
        @abstractclassmethod
        def moveForward(self, speed):
            self.rect.y += self.speed * speed / 20




class SlowPowerUp(PowerUp):
    def __init__(self, image_path, width, height, speed, pu_duration):
       super().__init__(image_path, width, height, speed, pu_duration)
       self.image = pygame.image.load(image_path)
       self.width = width
       self.height =  height
       self.speed = speed
       self.pu_duration = pu_duration
       self.rect = self.image.get_rect()




    def affect_player(self, player):
        
        # Implement slowing down the player
        pass

    def affect_traffic(self, speed):
        # Implement slowing down the traffic
        self.speed = speed
    
    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20
    

class InvincibilityPowerUp(PowerUp):
    def __init__(self, image, width, height, speed, pu_duration):
       super().__init__(image, width, height, speed, pu_duration)
       self.image = pygame.image.load("img/SlowPowerUp.png")
       self.width = width
       self.height =  height
       self.speed = speed
       self.pu_duration = pu_duration
       self.rect = self.image.get_rect()

    
    def affect_player(self, player):
        # Implement invincibility for player
        pass

    def affect_traffic(self, traffic):
        # No effect on traffic
        pass
    
    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20



class ScoreBoostPowerUp(PowerUp):
    def __init__(self, image, width, height, speed, pu_duration):
       super().__init__(image, width, height, speed, pu_duration)
       self.image = pygame.image.load("img/SlowPowerUp.png")
       self.width = width
       self.height =  height
       self.speed = speed
       self.pu_duration = pu_duration
       self.rect = self.image.get_rect()

    
    def affect_score(self, score):
        # Implement a boost in the score
        pass
    
    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20



class ShrinkPlayerPowerUp(PowerUp):
    def __init__(self, image, width, height, speed, pu_duration):
       super().__init__(image, width, height, speed, pu_duration)
       self.image = pygame.image.load("img/SlowPowerUp.png")
       self.width = width
       self.height =  height
       self.speed = speed
       self.pu_duration = pu_duration
       self.rect = self.image.get_rect()

    def affect_player(self, player):
        # Implement shrinking the player
        pass

    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20
    

