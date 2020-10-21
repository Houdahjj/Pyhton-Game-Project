import pygame
import random


class Senzu(pygame.sprite.Sprite):

    def __init__(self, senzu_event):
        super().__init__()
        self.image = pygame.image.load('Senzu_Bean.png')
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1200, 1800)
        self.rect.y = random.randint(0, 650)
        self.velocity = 5
        self.senzu_event = senzu_event

    def remove(self):
        self.senzu_event.all_senzu.remove(self)



    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def fall(self):
            self.rect.x -= self.velocity
            if self.rect.x < 0:
                self.remove()
            if self.check_collision(
                    self, self.senzu_event.game.all_player):
                print("joueur touché")
                self.remove()

                #subir dégats
                self.senzu_event.game.player.senzu(20)


