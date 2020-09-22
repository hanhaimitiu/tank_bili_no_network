import pygame


class Tank1():
    def __init__(self,screen):
        self.screen = screen
        self.img = pygame.image.load("picture/坦克1.png")
        self.rect = self.img.get_rect()
        self.rect.center = (600,400)
        self.rect.centerx = 600
        self.rect.centery = 400

    def draw_tank(self):
        self.screen.blit(self.img,self.rect)


class Tank2():
    def __init__(self,screen):
        self.screen = screen
        self.img = pygame.image.load("picture/坦克_1.png")
        self.rect = self.img.get_rect()
        self.rect.center = (600,400)
        self.rect.centerx = 600
        self.rect.centery = 400

    def draw_tank(self):
        self.screen.blit(self.img,self.rect)
