import pygame
WHITE = (255, 255, 255)

class Car(pygame.sprite.Sprite):


    """
    Represents a car in the game.

    This class extends the functionality of the Pygame Sprite class to create and manage car objects.
    It includes methods to move the car in different directions, alter its speed, dimensions, and repaint it.

    Args:
        image_path (str): The file path to the image of the car.
        width (int): The width of the car.
        height (int): The height of the car.
        speed (int): The speed of the car.

    Attributes:
        image (pygame.Surface): The image of the car.
        rect (pygame.Rect): The rectangle that defines the position and size of the car.
        width (int): The width of the car.
        height (int): The height of the car.
        speed (int): The speed of the car.

    Methods:
        moveRight(pixels): Moves the car to the right by a certain number of pixels.
        moveLeft(pixels): Moves the car to the left by a certain number of pixels.
        moveup(pixels): Moves the car up by a certain number of pixels.
        movedown(pixels): Moves the car down by a certain number of pixels.
        moveForward(speed): Moves the car forward based on the given speed.
        moveBackward(speed): Moves the car backward based on the given speed.
        changeSpeed(speed): Changes the speed of the car.
        changedimensions(width, height): Changes the dimensions (width and height) of the car.
        repaint(image_path): Repaints the car with a new image specified by the image_path.
    """
    #This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, image_path, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        
        


        #Initialise attributes of the car.
        self.width=width
        self.height=height
        self.speed = speed

        # Instead we could load a proper picture of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveup(self, pixels):
        self.rect.y -= pixels

    def movedown(self, pixels):
        self.rect.y += pixels

    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20

    def moveBackward(self, speed):
        self.rect.y -= self.speed * speed / 20

    def changeSpeed(self, speed):
        self.speed = speed

    def changedimensions(self, width, height):
        self.width = width
        self.height = height

    def repaint(self, image_path):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height)) 