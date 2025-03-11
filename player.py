import pygame
import os


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.walking_right = [
            pygame.image.load(os.path.join("./assets", "images", "playerright", i))
            for i in os.listdir(os.path.join("./assets", "images", "playerright"))
        ]
        self.walking_right = [
            pygame.image.load(os.path.join("./assets", "images", "playerleft", i))
            for i in os.listdir(os.path.join("assets", "images", "playerleft"))
        ]

        self.standing = pygame.image.load(
            os.path.join("assets", "images", "standing.png")
        )

        self.image = self.standing

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
