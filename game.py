# Making a Platformer Game in Python
import sys
import pygame
from settings import *
from player import Player


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Platformer")

        self.all_sprites = pygame.sprite.Group()

        self.player = Player(500, 500, self.all_sprites)

        self.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((0, 0, 0))

            self.all_sprites.draw(self.screen)
            self.all_sprites.update()

            pygame.display.update()


game = Game()
