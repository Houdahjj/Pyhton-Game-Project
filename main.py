import pygame
import math
from game import Game

pygame.init()

pygame.display.set_caption("Jeu d'évitement")
screen = pygame.display.set_mode((1080,620))


background = pygame.image.load('sunset.jpg')
background = pygame.transform.scale(background, (1080, 620))

#charger baniere

banner = pygame.image.load("banniere.png")
banner = pygame.transform.scale(banner,(410,460)) #redimensionner image
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/1.8)
banner_rect.y = math.ceil(screen.get_width()/10.5)

#bouton play
play_button = pygame.image.load("play.png")
play_button = pygame.transform.scale(play_button,(200,100))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 1.52)
play_button_rect.y = math.ceil(screen.get_height() / 1.3)

#charger le jeu

game = Game()


running = True

compteur = 0
score = 0

police = pygame.font.Font(None,72)
compteur = 0

#boucle du jeu
while running:

    #arrière-plan image
    screen.blit(background,(0,0))



    #le jeu a commencé?
    if game.is_playing:
        compteur+=1
        score = compteur
        #declancher les instructions
        game.update(screen) #parametre de la fenetre pour qu'elle soit récupérée dans game
        texte = police.render(str(compteur), True, pygame.Color("#FFFF00"))
        screen.blit(texte, [0, 0])



    if not game.is_playing:
        texte = police.render(str(score), True, pygame.Color("#FFFF00"))
        screen.blit(texte, [10, 10])
        compteur=0
        #texte2 = police.render(str(score), True, pygame.Color("#FFFF00"))
        #screen.blit(texte2, [0, 0])

        #ecran de bienvenue
        screen.blit(banner,banner_rect)
        screen.blit(play_button,play_button_rect)


    # application
    pygame.display.flip()


    for event in pygame.event.get():
        # si le joueur ferme la fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # voir si le joueur lache une touche du clavier
        # verifier quelle touche a été actionée, 2/ fluidité déplacement
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #savoir si la souris touche le bouton
            if play_button_rect.collidepoint(event.pos):
                game.is_playing = True




