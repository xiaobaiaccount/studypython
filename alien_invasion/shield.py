# 2024/4/13 15:34
import pygame.image
from pygame.sprite import Sprite
class Shield(Sprite):
    def __init__(self,screen,ai_setting,ship):
        """创建盾牌"""
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_setting = ai_setting
        self.ship = ship


        self.image = pygame.image.load('images/shield.png')
        #初始化盾牌的位置
        self.rect = self.image.get_rect()
        self.rect.y = self.ai_setting.screen_height - 4*self.rect.height
        self.rect.centerx = self.screen_rect.centerx

    def blitme(self):
        self.screen.blit(self.image,self.rect)