import pygame

class settings:
    """A clas to store all the settings for Alien Invasion"""
    def __init__(self) -> None:
        """Initialize the game's settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 1000
        self.bg_colour = (230,230,230)
        self.background_image = pygame.image.load('images/background.png')