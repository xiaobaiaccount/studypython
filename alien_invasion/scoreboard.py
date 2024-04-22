# 2024/4/8 7:05
import pygame.font
from ship import Ship
from pygame.sprite import Group
class GameScore():
    """游戏得分类"""
    def __init__(self,screen,ai_setting,stats):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.ai_setting = ai_setting
        self.stats = stats

        #设置字体
        self.textcolor = (0,0,0)
        #None表示默认字体
        self.font = pygame.font.SysFont(None,48)

        #使得创建对象的时候就调用这个函数
        self.prep_image()

    def prep_image(self):
        """创建得分，最高等分，等级，飞船的函数"""
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """将字体转换成图图像"""
        round_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(round_score)
        #还接受一个布尔实参，该实参指定开启还是关闭反锯齿功能（反锯齿让文本的边缘更平滑）
        self.text_image = self.font.render(score_str,True,self.textcolor,self.ai_setting.bg_color)

        #设置图像的初始位置
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.right = self.screen_rect.right - 20
        self.text_image_rect.top = 20

    def prep_high_score(self):
        """将最高得分转换成图像"""
        #将最高得分转换成10的倍数
        high_score = int(round(self.stats.game_high_score,-1))
        #将最高得分以3位一分割的方式转换成字符的形式
        self.hight_score = "{:,}".format(high_score)
        #将得分字符串转换成图像形式(字体的背景颜色是游戏界面的颜色)
        self.text_high_image = self.font.render(self.hight_score,True,self.textcolor,self.ai_setting.bg_color)
        self.text_high_image_rect = self.text_high_image.get_rect()
        #设置最高分字体的初始位置
        self.text_high_image_rect.top = 20
        self.text_high_image_rect.centerx = self.screen_rect.centerx

    def prep_level(self):
        """重置等级"""
        self.level_image = self.font.render(str(self.stats.level),True,self.textcolor,self.ai_setting.bg_color)
        #初始化等级的位置
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.top = self.text_image_rect.bottom + 10
        self.level_image_rect.right = self.screen_rect.right - 20


    def prep_ships(self):
        """显示有几艘飞船"""
        self.ships = Group()
        for i in range(self.stats.ships_left):
            ship = Ship(self.screen,self.ai_setting)
            #优化飞船的位置
            ship.rect.y = 10
            ship.rect.x = 10 + i*ship.rect.width
            self.ships.add(ship)


    def show_score(self):
        """将字体绘制出来"""
        self.screen.blit(self.text_image,self.text_image_rect)
        #将最高分绘制出来
        self.screen.blit(self.text_high_image,self.text_high_image_rect)
        #将等级绘画出来
        self.screen.blit(self.level_image,self.level_image_rect)
        #绘制飞船（必须要在这里写，因为update_screen会每次重刷界面，然后飞船就没了）
        #在别的函数中画出飞船，再使用pygame.display.flip()刷新页面也不行，因为update_screen()是每时每刻都在重新刷新，而别的函数只有在调用的时候可画飞船再重刷界面
        #所以还是在update_screen()中画出飞船比较好
        self.ships.draw(self.screen)






