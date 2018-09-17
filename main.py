import sys, pygame
from extras import *

pygame.init()

size = (1500,844)

screen = pygame.display.set_mode(size)

init(screen, size)

img = pygame.image.load("0.png")

clock = pygame.time.Clock()

imgs = []
for i in range(0,11):
    stri = str(i) + '.png'
    imgs.append(pygame.image.load(stri))

test = sprite(img, (1,0), 0.7)
test.display(screen)
direc = (0,0)
test.moveTo((200,75), 3)
test.canAnimate = False
mouse = pygame.Rect(0, 0, 2, 2)
while True:
    xm, ym = pygame.mouse.get_pos()
    mouse.center = (xm,ym)

    fps = clock.get_fps()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #test.display(screen)
    #pygame.draw.rect(screen, (255,255,255), test.rect)
    test.move(direc)
    direc = (0,0)
    test.display(screen)
    pygame.display.flip()
    screen.fill((0,0,0))

    if pygame.mouse.get_pressed()[0] == 1 and test.moveing[0] == False:
        test.moveTo((xm,ym), 2)
        ## moveTo has issue when moving where the vlaues multiplied are negative
        ## IE: Up and to the right results in +X -Y which is negative, the same with down and to the left
        ## While Right and Down works, and Up and Left Works
        print(test.pos, (xm,ym))

    test.update(imgs)

    




    for key in getKeys():
        if key == 'd':
            test.update(imgs)
            if test.rect.right < size[0]:
                test.flip = (False, False)
                direc = (1,0)
        if key == 'a':
            test.update(imgs)
            if test.rect.left > 0:
                test.flip = (True, False)
                direc = (-1,0)
         

    #clock.tick(100)