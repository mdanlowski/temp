# Inicjalizacja modułów pygame
import pygame
pygame.init()

# Ustawienie planszy i rozgrywki
plansza = pygame.display.set_mode([800,600])
pygame.display.set_caption('Moja pierwsza gra z pygame!')
rozgrywka = True

# Kolory RGB (Red,Green,Blue)
CZERWONY = (255,0,0) # ciekawostka - tuple, czyli "krotki"
ZIELONY = (0,255,0)
NIEBIESKI = (0,0,255)

# Główna pętla / rozgrywka
while rozgrywka:

    for zdarzenie in pygame.event.get(): 
        if zdarzenie.type == pygame.QUIT: 
            rozgrywka = False

    # pygame.draw.circe(ekran, KOLOR, gdzie?, jak?)
    pygame.draw.circle(plansza, ZIELONY, (100,100), 50)

    # update ekranu / odświeżenie obrazu w ciągłej pętli
    pygame.display.update()
   
pygame.quit()
