import pygame

#classe pour le joueur

class Player(pygame.sprite.Sprite):         #sprite pour que ça soit un composant du jeu

    def __init__(self, game):
        super().__init__()          #initialiser le sprite
        self.game = game
        self.health = 100
        self.max_health = 100


        self.velocity = 5               #vitesse
        self.image = pygame.image.load('perso.png')
        self.image = pygame.transform.scale(self.image, (60, 80))
        self.rect = self.image.get_rect()           #recup les coordonnées pour pouvoir bouger le perso
        self.rect.x = 100                           #abcisses
        self.rect.y = 200                           #ordonées


    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

    def update_health_bar(self, surface):
        bar_color = (255, 247, 0)
        bar_position = [970, 10, self.max_health, 10]
        black_bar = (0, 0, 0)
        black_bar_position = [970, 10, self.health, 10]
        pygame.draw.rect(surface, black_bar, bar_position)
        pygame.draw.rect(surface, bar_color, black_bar_position)


    def damage(self, amount):
        self.health -= amount
        if self.health == 0:
            self.game.game_over()

    def senzu(self, amount):
        while not self.health == self.max_health:
            self.health += amount