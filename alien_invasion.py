import sys

import pygame
from pygame.constants import FULLSCREEN
from settings import settings
from ship import Ship, Ship
from bullet import Bullet
from alien import Alien

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

        #Clock
        self.clock = pygame.time.Clock()
 
        #ship
        self.ship = Ship(self)
        



        #bullets

        self.bullets = pygame.sprite.Group()

        #alien
        self.aliens = pygame.sprite.Group()


        self._create_fleet()
        
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

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        
        pygame.display.update()  
        pygame.display.flip()
         

    def _check_keydown_events(self,event):
        """Repsond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # Press Q to quit the game    
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False   

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)    

    def _create_fleet(self):
        """Create a fleet of aliens"""
        #Create an alien and find the number of aliens in a row.
        #Spacing between each alien is euqal to one alien width
        alien = Alien(self)
        
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #Create thge first row of aliens.
        for row_number in range(number_rows):
            for alien_number in range (number_aliens_x):
                self._create_alien(alien_number,row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    #Main game run
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:          
            self._check_events() 
            self.ship.update()   
            self.bullets.update()  
            self._update_screen() 
            self.clock.tick(15)

            # get rid of bullets that have disappeared.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            
            

             

    #play background music        
    settings.music_play()       

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
    