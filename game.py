import pygame
from projectile_event import ProjectileEvent
from senzu_event import SenzuEvent
from player import Player


#classe pour le jeu
class Game:

    def __init__(self):
        #le jeu a commencé ?
        self.is_playing = False
        # charger joueur
        self.player = Player(self)
        #sprite de joueur pour collision
        self.all_player = pygame.sprite.Group()
        self.all_player.add(self.player)
        #instance de l'évenement des projectiles et des haricots magiques
        self.projectile_event = ProjectileEvent(self)
        self.senzu_event = SenzuEvent(self)
        self.pressed = {} # coordonées qui saffichent quand on actionne une touche

        #si le joueur n'as plus de vie, la partie est terminé
    def game_over(self):
        self.player.health = self.player.max_health
        self.is_playing = False
        #projectiles qui augmentent leurs vitesses
        self.projectile_event.all_projectiles = pygame.sprite.Group()
        self.projectile_event.percent = 100
        self.projectile_event.b = 3
        self.projectile_event.percent_speed = 20


    #mises à jour : lancements des projectiles, des haricots magiques, barre de vie
    def update(self,screen):
        self.player.update_health_bar(screen)
        # application image
        screen.blit(self.player.image, self.player.rect)
        self.projectile_event.update()
        self.senzu_event.update()

        for senzu in self.senzu_event.all_senzu:
            senzu.fall()
        #self.heart_event.update()
        for projectile in self.projectile_event.all_projectiles:
            projectile.fall()
        # appliquer groupe de projectiles
        self.projectile_event.all_projectiles.draw(screen)

        self.senzu_event.all_senzu.draw(screen)

        # Verifier si le joueur veux aller en haut ou en bas
        # fluidité du déplacement !! -> On verifie où il veux aller et on actionne la fonction bouger
        if self.pressed.get(pygame.K_UP) and self.player.rect.y > 10:
            self.player.move_up()
        elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y + 90 < screen.get_height():
            self.player.move_down()





