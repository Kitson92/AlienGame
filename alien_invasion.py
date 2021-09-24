import sys

import pygame
from pygame.constants import FULLSCREEN
from settings import settings
from ship import Ship, Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Iitialize the game, and create game resources"""
        pygame.init()
        self.settings = settings()

        #Full screen settings
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        #Game Title
        pygame.display.set_caption("Alien Invasion")
 
        

        #ship
        self.ship = Ship(self)
        
    def _check_events(self):
        """Respond to Keypresses and mouse events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)                    
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _update_screen(self):
        """Update Images on the screen, and flip to the new screen"""
        self.screen.blit(self.settings.background_image,(0,0))
        self.screen.blit(self.settings.game_title,(0,0))
        self.ship.blitme()
        pygame.display.update()  
        pygame.display.flip()
         

    def _check_keydown_events(self,event):
        """Repsond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
            print(event.key)
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
            print(event.key)
        # Press Q to quit the game    
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False   

    

    #Main game run
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:          
            self._check_events()      
            self._update_screen()   
            self.ship.update()

    #play background music        
    settings.music_play()       

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
    