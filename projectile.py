import pygame
import random


class Projectile(pygame.sprite.Sprite):

#instance des caracteristiques des projectiles : image, redimensions, vitesse, position des projectiles (aléatoire) 
    def __init__(self, projectile_event):
        super().__init__()
        self.image = pygame.image.load('comete.png')
        self.image = pygame.transform.scale(self.image, (40,30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1200, 1800)
        self.rect.y = random.randint(0, 650)
        self.velocity = 5
        self.projectile_event = projectile_event

#suppression d'un projectile (en cas de collisions)
    def remove(self):
        self.projectile_event.all_projectiles.remove(self)

#detecter collision
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

#fonction qui lance les projectiles en fonction de la vitesse calculée, et les supprime à chaque collision avec le personnage
    def fall(self):
            self.rect.x -= self.velocity
            if self.rect.x < 0:
                self.remove()
            if self.check_collision(
                    self, self.projectile_event.game.all_player):
                print("joueur touché")
                self.remove()

                #subir dégats
                self.projectile_event.game.player.damage(20)


