# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

PINK = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'RIGHT'

while True: # the main game loop
    DISPLAYSURF.fill(PINK)

    if direction == 'RIGHT':
        catx += 5
        if catx == 280:
            direction = 'DOWN'
    #elif direction == 'DOWN':
        caty += 5
        if caty == 220:
            direction = 'LEFT'
    elif direction == 'LEFT':
        catx -= 5
        if catx == 10:
            direction = 'UP'
    #elif direction == 'UP':
        caty -= 5
        if caty == 10:
            direction = 'RIGHT'

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
