import pygame
from projectile import Projectile

class ProjectileEvent:

    def __init__(self, game):
        self.percent = 100
        self.percent_speed = 20
        #groupe de projectile
        self.all_projectiles = pygame.sprite.Group()
        self.a = 0
        self.b = 3
        self.game = game

    def meteor_fall(self):
        for i in range(self.a, self.b):
            self.all_projectiles.add(Projectile(self))
        # Pour accelerer l'apparition des boules
        self.percent_speed += 3
        # Pour augmenter le nombre de boules
        self.b += 1

    def reset_percent(self):
        self.percent = 0

    def attempt_fall(self):
        if self.loaded():
            self.meteor_fall()

            # ICI QUE JE DOIS AUGMENTER LA VELOCITY
            self.reset_percent()

    def update(self):
        self.add_percent()
        self.attempt_fall()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def loaded(self):
        return self.percent >= 100