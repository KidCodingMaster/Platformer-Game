import pygame
import os


class Player(pygame.sprite.Sprite):
    VEL = 1

    def __init__(self, x, y, group):
        super().__init__(group)

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

        self.speed = pygame.Vector2()

        self.image = self.standing
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        keys = pygame.key.get_pressed()

        self.speed.x = int(keys[pygame.K_RIGHT] or keys[pygame.K_d]) - int(keys[pygame.K_LEFT] or keys[pygame.K_a])
        self.speed.y = int(keys[pygame.K_DOWN] or keys[pygame.K_s]) - int(keys[pygame.K_UP] or keys[pygame.K_w])

        self.rect.center += self.speed
