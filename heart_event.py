import pygame
from heart import Heart

class HeartEvent:

    def __init__(self, game):

        self.all_heart = pygame.sprite.Group()
        self.a = 0
        self.b = 5
        self.game = game


    def heart_fall(self):
        #for i in range(self.a, self.b):
            #self.all_heart.add(Heart(self))
        return 0

    def attempt_fall(self):
        self.heart_fall()



    def update(self):
        self.attempt_fall()

