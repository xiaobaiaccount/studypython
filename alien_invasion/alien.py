# 2024/3/25 7:06
import pygame.image
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,screen,ai_setting):
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_setting = ai_setting

        #加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        #初始化外星人的位置，在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = 0

        #存储外形人的精确位置
        self.x = float(self.rect.x)

    def update(self):
         self.x += (self.ai_setting.alien_speed_factor * self.ai_setting.fleet_direction)
         self.rect.x = self.x

# rect.right是图片的右边缘坐标(rect.x+rect.width = rect.right)
# 当我们新增rect.right的时候，为了保证rect.right的值不发生改变，会减小rect.x的值并新增rect.width的值
# Initial x: 50, width: 100, right: 150
# After increasing right by 10(rect.width增加10): x=40, width=110, right=150
#通常rect.x是用来改变位置的  rect.right用来判断是否超出边缘

    def check_edges(self):
        """判断外星人是否走到边缘"""
        if self.rect.right >= self.screen.get_rect().right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        #在指定位置绘制外星人
        self.screen.blit(self.image,self.rect)
