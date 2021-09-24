import sys

import pygame

from settings import settings
from ship import Ship, Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Iitialize the game, and create game resources"""
        pygame.init()
        self.settings = settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def _check_events(self):
        """Respond to Keypresses and mouse events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        #move ship to the right
                        self.ship.rect.x += 1

    def _update_screen(self):
        """Update Images on the screen, and flip to the new screen"""
        self.screen.blit(self.settings.background_image,(0,0))
        self.ship.blitme()  
        pygame.display.flip() 

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()      
            self._update_screen()   

            

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()