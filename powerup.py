import pygame
import random
import time
from abc import ABC, abstractmethod

'''class PowerUp(ABC):
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
        @abstractmethod
        def affect_player():
            pass

        @abstractmethod
        def affect_traffic():
            pass
        
        @abstractmethod
        def moveForward(self, speed):
            self.rect.y += self.speed * speed / 20'''


class SlowPowerUp(pygame.sprite.Sprite):

  """
    Represents a power-up that slows down elements in the game.

    This class extends the Pygame Sprite class to create and manage a power-up that affects players or traffic.
    It includes methods to alter its behavior and movement.

    Args:
        image (str): The file path to the image of the power-up.
        width (int): The width of the power-up.
        height (int): The height of the power-up.
        speed (int): The speed of the power-up.

    Attributes:
        image (pygame.Surface): The image of the power-up.
        rect (pygame.Rect): The rectangle defining the position and size of the power-up.
        width (int): The width of the power-up.
        height (int): The height of the power-up.
        speed (int): The speed of the power-up.

    Methods:
        affect_player(): A method to define the effect of the power-up on players.
        affect_traffic(): A method to define the effect of the power-up on traffic.
        moveForward(speed): Moves the power-up forward based on the given speed.
    """

    # Rest of your class code...  

  def __init__(self, image, width, height, speed):
    super().__init__()
    self.image = pygame.image.load(image)
    self.image = pygame.image.load(image).convert_alpha()
    self.image = pygame.transform.scale(self.image, (width,height))
    self.rect = self.image.get_rect()
    self.width = width
    self.height = height
    self.speed = speed


  def affect_player():
    pass
  
  def affect_traffic():
    pass
  def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20

class ScoreBoostPowerUp(pygame.sprite.Sprite):

  """
  Represents a power-up that boosts the player's score or affects traffic.

  This class extends the Pygame Sprite class to create and manage a power-up that can impact the player's score or traffic behavior.
  It includes methods to define the effects on players and traffic, along with movement control.

  Args:
      image (str): The file path to the image of the power-up.
      width (int): The width of the power-up.
      height (int): The height of the power-up.
      speed (int): The speed of the power-up.

  Attributes:
      image (pygame.Surface): The image of the power-up.
      rect (pygame.Rect): The rectangle defining the position and size of the power-up.
      width (int): The width of the power-up.
      height (int): The height of the power-up.
      speed (int): The speed of the power-up.

  Methods:
      affect_player(): A method to define the effect of the power-up on players.
      affect_traffic(): A method to define the effect of the power-up on traffic.
      moveForward(speed): Moves the power-up forward based on the given speed.
  """

  def __init__(self, image, width, height, speed):
    super().__init__()
    self.image = pygame.image.load(image)
    self.image = pygame.image.load(image).convert_alpha()
    self.image = pygame.transform.scale(self.image, (width, height))
    self.rect = self.image.get_rect()
    self.width = width
    self.height = height
    self.speed = speed

  def affect_player():
    pass
  
  def affect_traffic():
    pass

  def moveForward(self, speed):
    self.rect.y += self.speed * speed / 20

class ShrinkPlayerPowerUp(pygame.sprite.Sprite):
    
    """
    Represents a power-up that shrinks the player or affects traffic.

    This class extends the Pygame Sprite class to create and manage a power-up that can shrink the player or affect traffic behavior.
    It includes methods to define the effects on players and traffic, along with movement control.

    Args:
        image (str): The file path to the image of the power-up.
        width (int): The width of the power-up.
        height (int): The height of the power-up.
        speed (int): The speed of the power-up.

    Attributes:
        image (pygame.Surface): The image of the power-up.
        rect (pygame.Rect): The rectangle defining the position and size of the power-up.
        width (int): The width of the power-up.
        height (int): The height of the power-up.
        speed (int): The speed of the power-up.

    Methods:
        affect_player(): A method to define the effect of the power-up on players.
        affect_traffic(): A method to define the effect of the power-up on traffic.
        moveForward(speed): Moves the power-up forward based on the given speed.
    """

    def __init__(self, image, width, height, speed):
      super().__init__()
      self.image = pygame.image.load(image)
      self.image = pygame.image.load(image).convert_alpha()
      self.image = pygame.transform.scale(self.image, (width, height))
      self.rect = self.image.get_rect()
      self.width = width
      self.height = height
      self.speed = speed

    def affect_player():
      pass
  
    def affect_traffic():
      pass
    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20



class InvencibilityPowerUp(pygame.sprite.Sprite):

  """
    Represents a power-up that grants invincibility to the player or affects traffic.

    This class extends the Pygame Sprite class to create and manage a power-up that provides invincibility to the player or affects traffic behavior.
    It includes methods to define the effects on players and traffic, along with movement control.

    Args:
        image (str): The file path to the image of the power-up.
        width (int): The width of the power-up.
        height (int): The height of the power-up.
        speed (int): The speed of the power-up.

    Attributes:
        image (pygame.Surface): The image of the power-up.
        rect (pygame.Rect): The rectangle defining the position and size of the power-up.
        width (int): The width of the power-up.
        height (int): The height of the power-up.
        speed (int): The speed of the power-up.

    Methods:
        affect_player(): A method to define the effect of the power-up on players.
        affect_traffic(): A method to define the effect of the power-up on traffic.
        moveForward(speed): Moves the power-up forward based on the given speed.
    """

  def __init__(self, image, width, height, speed):
    super().__init__()
    self.image = pygame.image.load(image)
    self.image = pygame.image.load(image).convert_alpha()
    self.image = pygame.transform.scale(self.image, (width, height))
    self.rect = self.image.get_rect()
    self.width = width
    self.height = height
    self.speed = speed

  def affect_player():
    pass
  
  def affect_traffic():
    pass
  def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20


class SuperSpeedPowerUp(pygame.sprite.Sprite):

  """
    Represents a power-up that grants super speed to the player or affects traffic.

    This class extends the Pygame Sprite class to create and manage a power-up that provides super speed to the player or affects traffic behavior.
    It includes methods to define the effects on players and traffic, along with movement control.

    Args:
        image (str): The file path to the image of the power-up.
        width (int): The width of the power-up.
        height (int): The height of the power-up.
        speed (int): The speed of the power-up.

    Attributes:
        image (pygame.Surface): The image of the power-up.
        rect (pygame.Rect): The rectangle defining the position and size of the power-up.
        width (int): The width of the power-up.
        height (int): The height of the power-up.
        speed (int): The speed of the power-up.

    Methods:
        affect_player(): A method to define the effect of the power-up on players.
        affect_traffic(): A method to define the effect of the power-up on traffic.
        moveForward(speed): Moves the power-up forward based on the given speed.
    """

  def __init__(self, image, width, height, speed):
    super().__init__()
    self.image = pygame.image.load(image)
    self.image = pygame.image.load(image).convert_alpha()
    self.image = pygame.transform.scale(self.image, (width, height))
    self.rect = self.image.get_rect()
    self.width = width
    self.height = height
    self.speed = speed

  def affect_player():
    pass
  
  def affect_traffic():
    pass
  def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20