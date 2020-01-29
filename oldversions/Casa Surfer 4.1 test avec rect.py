import pygame as pg

pg.init()
white = (255,255,255)
taxi_sprite = pg.image.load ('./img/obstacle.png')
bus_sprite = pg.image.load ('./img/bus.png')
gameDisplay = pg.display.set_mode(pg.display.list_modes()[1], pg.FULLSCREEN)
gameDisplay.fill(white)
taxi_rect = taxi_sprite.get_rect()
bus_rect = bus_sprite.get_rect()
taxi_rect = pg.Rect((100,150), (267,200))
bus_rect = pg.Rect((500,150), (300,200))
taxi_rect.x = 100
taxi_rect.y = 150
bus_rect.x = 500
bus_rect.y = 150

while True:
    for event in pg.event.get ( ):
        # print(background)
        if event.type == pg.QUIT:
            pg.quit ( )
            quit ( )
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                taxi_rect.x += 5
            if event.key == pg.K_LEFT:
                bus_rect.x -= 5
            if event.key == pg.K_ESCAPE:
                pg.quit ( )
                quit ( )

    gameDisplay.fill (white)
    gameDisplay.blit(taxi_sprite,taxi_rect)
    gameDisplay.blit(bus_sprite, bus_rect)
    pg.draw.rect(gameDisplay,(0,0,0),taxi_rect,10)
    pg.draw.rect (gameDisplay, (0, 0, 0), bus_rect, 10)
    pg.display.update()



