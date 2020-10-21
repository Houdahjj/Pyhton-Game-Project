
import pygame

class Heart(pygame.sprite.Sprite):

    def __init__(self, heart_event):
        super().__init__()
        self.image = pygame.image.load('coeur.png')
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.heart_event = heart_event

    def placement(self):
        self.rect.x = 800
        self.rect.y = 0

    def remove(self):
        self.heart_event.all_heart.remove(self)