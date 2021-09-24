import pygame
from pygame import mixer



class settings:
    """A clas to store all the settings for Alien Invasion"""
    def __init__(self) -> None:
        """Initialize the game's settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 1000
        self.bg_colour = (230,230,230)
        self.background_image = pygame.image.load('images/background.png')
        self.font = pygame.font.Font('freesansbold.ttf',32)
        self.game_title = self.font.render('Alien Invasion Version 1',True,(240,20,100))
        
        
        #ship settings
        self.ship_speed = 1.5

    def music_play():
            mixer.init()
            mixer.music.load('music/GameMusicLoop.ogg') 
            mixer.music.play(loops = -1)
    


    
