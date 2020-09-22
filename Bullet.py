from pygame.sprite import Sprite
import pygame


class Bullet(Sprite):
    def __init__(self,screen,tank,pos):
        super().__init__()
        self.screen = screen
        self.tank = tank
        self.pos = int(pos)
        self.color=(0,0,0)
        self.rect = pygame.Rect(0,0,2,2)
        self.rect.center = self.tank.rect.center

    def update(self):
        if self.pos==1:
            self.rect.centery-=1
        elif self.pos==2:
            self.rect.centerx+= 1
        elif self.pos==3:
            self.rect.centery+= 1
        elif self.pos==4:
            self.rect.centerx-= 1

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)