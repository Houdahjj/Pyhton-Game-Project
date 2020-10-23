import pygame
from projectile import Projectile

class ProjectileEvent:

#instancie la vitesse des projectiles, pour les initialiser dans le jeu ainsi que le groupe de projectiles
    def __init__(self, game):
        self.percent = 100
        self.percent_speed = 20
        #groupe de projectiles
        self.all_projectiles = pygame.sprite.Group()
        self.a = 0
        self.b = 3
        self.game = game

 #nombre de projectiles qui vont être lancés en fonction d'un nombre a et b 
    def meteor_fall(self):
        for i in range(self.a, self.b):
            self.all_projectiles.add(Projectile(self))
        # Pour accelerer l'apparition des boules
        self.percent_speed += 3
        # Pour augmenter le nombre de boules
        self.b += 1
        
 #reinitialiser les poucentages
    def reset_percent(self):
        self.percent = 0

#si les pourcentages dépassent un quota (100), les projectiles sont lancés, les pourcentages servent de base pour que les projectiles se lancent, donc on remet à 0 à chaque fois
    def attempt_fall(self):
        if self.loaded():
            self.meteor_fall()
            self.reset_percent()
            
#on actualise pour boucler le cycle pourcentage/lancement de projectiles
    def update(self):
        self.add_percent()
        self.attempt_fall()

#vitesse d'évolution des pourcents
    def add_percent(self):
        self.percent += self.percent_speed / 100

    def loaded(self):
        return self.percent >= 100
