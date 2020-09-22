import pygame
import sys
import Tank
import Bullet
from pygame.sprite import Group


def score_change(bullets1,bullets2,tank1,tank2):
    for i in bullets1.copy():
        if tank2.rect.collidepoint(i.rect.center):
            bullets1.remove(i)
            print("tank1击中了tank2")
            break

    # print(len(bullets2))

    for i in bullets2.copy():
        if tank1.rect.collidepoint(i.rect.center):

            bullets2.remove(i)
            print("tank2击中了tank1")
            break



def rungame():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("xx游戏")
    pos1 = 1
    pos2 = 1
    tank1 = Tank.Tank1(screen)
    tank2 = Tank.Tank2(screen)
    tank1_bullts = Group()
    tank2_bullts = Group()
    screen.fill((230, 230, 230))
    while True:
        screen.fill((230, 230, 230))
        tank1.draw_tank()
        tank2.draw_tank()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        mykeylist = pygame.key.get_pressed()
        if mykeylist[pygame.K_UP]:
            pos1 = 1
            tank1.rect.centery -= 1
            tank1.img = pygame.image.load("picture/坦克1.png")
        elif mykeylist[pygame.K_RIGHT]:
            pos1 = 2
            tank1.rect.centerx += 1
            tank1.img = pygame.image.load("picture/坦克2.png")
        elif mykeylist[pygame.K_DOWN]:
            pos1 = 3
            tank1.rect.centery += 1
            tank1.img = pygame.image.load("picture/坦克3.png")
        elif mykeylist[pygame.K_LEFT]:
            pos1 = 4
            tank1.rect.centerx -= 1
            tank1.img = pygame.image.load("picture/坦克4.png")
        elif mykeylist[pygame.K_SPACE]:
            if tank1_bullts.__len__() < 5:
                newbullet = Bullet.Bullet(screen, tank1, pos1)
                tank1_bullts.add(newbullet)


        if mykeylist[pygame.K_w]:
            pos2 = 1
            tank2.rect.centery -= 1
            tank2.img = pygame.image.load("picture/坦克_1.png")
        elif mykeylist[pygame.K_d]:
            pos2 = 2
            tank2.rect.centerx += 1
            tank2.img = pygame.image.load("picture/坦克_2.png")
        elif mykeylist[pygame.K_s]:
            pos2 = 3
            tank2.rect.centery += 1
            tank2.img = pygame.image.load("picture/坦克_3.png")
        elif mykeylist[pygame.K_a]:
            pos2 = 4
            tank2.rect.centerx -= 1
            tank2.img = pygame.image.load("picture/坦克_4.png")
        elif mykeylist[pygame.K_x]:
            if tank2_bullts.__len__() < 5:
                newbullet = Bullet.Bullet(screen, tank2, pos2)
                tank2_bullts.add(newbullet)

        if tank1.rect.centery < 0:
            tank1.rect.centery = 0
        if tank1.rect.centery > 600:
            tank1.rect.centery = 600
        if tank1.rect.centerx < 0:
            tank1.rect.centerx = 0
        if tank1.rect.centerx > 800:
            tank1.rect.centerx = 800
        tank1_bullts.update()
        for i in tank1_bullts.sprites():
            i.draw_bullet()

        for i in tank1_bullts.copy():
            if i.rect.centerx <= 0 or i.rect.centerx >= 800:
                tank1_bullts.remove(i)
            elif i.rect.centery >= 600 or i.rect.centery <= 0:
                tank1_bullts.remove(i)

        if tank2.rect.centery < 0:
            tank2.rect.centery = 0
        if tank2.rect.centery > 600:
            tank2.rect.centery = 600
        if tank2.rect.centerx < 0:
            tank2.rect.centerx = 0
        if tank2.rect.centerx > 800:
            tank2.rect.centerx = 800
        tank2_bullts.update()
        for i in tank2_bullts.sprites():
            i.draw_bullet()

        for i in tank2_bullts.copy():
            if i.rect.centerx <= 0 or i.rect.centerx >= 800:
                tank2_bullts.remove(i)
            elif i.rect.centery >= 600 or i.rect.centery <= 0:
                tank2_bullts.remove(i)
        score_change(tank1_bullts,tank2_bullts,tank1,tank2)
        pygame.display.flip()


rungame()


