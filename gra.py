import pygame as pg
pg.init()
# stworzenie planszy
plansza = pg.display.set_mode( [800,600] )
pg.display.set_caption("Moja Pierwsza Gra w Okienku")
rozgrywka = True
dirt = pg.image.load("dirt.jpg")

kolor_nieb = (0,255,0)

while rozgrywka:
    for zdarzenie in pg.event.get():
        if zdarzenie.type == pg.QUIT:
            rozgrywka = False

    #pg.draw.circle(plansza, kolor_nieb, (100,100), 50)
    #plansza.blit(dirt, (300,300))
    for x in range(0,8):
        for y in range(0,6):
            plansza.blit(dirt, (x*100,y*100))

            
    pg.display.update()

pg.quit()
