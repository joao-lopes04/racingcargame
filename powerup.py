import pygame
import random
import time
from abc import ABC, abstractclassmethod
from car import Car





class SlowPowerUp(pygame.sprite.Sprite):
    def __init__(self, image_path, width, height, speed):
       super().__init__()
       self.image = pygame.transform.scale(pygame.image.load(image_path), (width, height))
       self.width = width
       self.height =  height
       self.speed = speed
       
       self.rect = self.image.get_rect()




    def affect_player(self, player):
        
        # Implement slowing down the player
        pass

    def affect_traffic(self, speed):
        # Implement slowing down the traffic
        self.speed = speed
    
    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20
    

class InvincibilityPowerUp(pygame.sprite.Sprite):
    def __init__(self, image, width, height, speed):
       super().__init__()
       self.image = pygame.image.load("img/SlowPowerUp.png")
       self.width = width
       self.height =  height
       self.speed = speed
       
       self.rect = self.image.get_rect()

    
    def affect_player(self, player):
        # Implement invincibility for player
        pass

    def affect_traffic(self, traffic):
        # No effect on traffic
        pass
    
    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20 



class ScoreBoostPowerUp(pygame.sprite.Sprite):
    def __init__(self, image_path, width, height, speed):
       super().__init__()
       self.image = pygame.image.load(image_path)
       self.width = width
       self.height =  height
       self.speed = speed
       
       self.rect = self.image.get_rect()

    
    def affect_score(self, score):
        # Implement a boost in the score
        score += score
    
    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20



class ShrinkPlayerPowerUp(pygame.sprite.Sprite):
    def __init__(self, image, width, height, speed):
       super().__init__()
       self.image = pygame.image.load(image)
       self.width = width
       self.height =  height
       self.speed = speed
       
       self.rect = self.image.get_rect()

    def affect_player(self, width, height):
        self.width
        pass

    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20
    

