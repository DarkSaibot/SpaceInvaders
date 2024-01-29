import pygame
import random

class Laser(pygame.sprite.Sprite):
    def __init__(self,pos, speed, screen_height):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.laser_colors = ["blue", "red"]
        self.image.fill(random.choice(self.laser_colors))
        self.rect = self.image.get_rect(center = pos)
        self.speed = speed
        self.heigt_y_constraint = screen_height

    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.heigt_y_constraint + 50:
            self.kill()

    def update(self):
        self.rect.y += self.speed
        self.destroy()
