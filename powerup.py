import pygame
import random
import time

class PowerUp:
  def __init__(self, image, pu_duration):
    self.image = image
    self.pu_duration = pu_duration


class PUslow(PowerUp):
  def __init__():
    super().__init__()
    self.image = pygame.image.load("img/SlowPowerUp")
    self.pu_duration = 420
    
  def apply(self, ):
    self.enemy_velocity = 2


class PU50(PowerUp):
  def __init__():
    super().__init__()
    self.image = pygame.image.load("img/+50PowerUp")


class PUshrink(PowerUp):
  def __init__():
    super().__init__()
    self.image = pygame.image.load("img/ShrinkPowerUp")
    self.pu_duration = 420


class PUinvencibility(PowerUp):
  def __init__():
    super().__init__()
    self.image = pygame.image.load("img/InvencibilityPowerUp")
    self.pu_duration = 420
