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
        self.walking_left = [
            pygame.image.load(os.path.join("./assets", "images", "playerleft", i))
            for i in os.listdir(os.path.join("assets", "images", "playerleft"))
        ]

        self.standing = [
            pygame.image.load(os.path.join("assets", "images", "standing.png"))
        ]

        self.speed = pygame.Vector2()

        self.animation_count = 0

        self.curr_animation = self.standing
        self.image = self.curr_animation[self.animation_count]
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        keys = pygame.key.get_pressed()

        self.speed.x = int(keys[pygame.K_RIGHT] or keys[pygame.K_d]) - int(
            keys[pygame.K_LEFT] or keys[pygame.K_a]
        )
        self.speed.y = int(keys[pygame.K_DOWN] or keys[pygame.K_s]) - int(
            keys[pygame.K_UP] or keys[pygame.K_w]
        )

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.curr_animation = self.walking_right
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.curr_animation = self.walking_left
        else:
            self.curr_animation = self.standing

        if self.animation_count < len(self.curr_animation) - 1:
            self.animation_count += 0.05
        else:
            self.animation_count = 0

        self.image = self.curr_animation[int(self.animation_count)]
        self.rect.center += self.speed
