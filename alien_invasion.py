import sys
import pygame

class AlienInvasion:
    """Over class to manage game assets and behaviour"""
    def __init__(self):
        """Initialize the game, and create game resource"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

if __name__ == '__Main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game
