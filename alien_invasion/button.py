# 2024/4/5 13:27
import pygame.font

class Button():
    """初始化按钮的属性"""
    def __init__(self,screen,msg):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        #设置按钮的尺寸和背景颜色，文字颜色
        self.width,self.height = 200,50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        #使用什么字体来渲染文本,None是默认字体，48指定来了文本的字号
        self.font = pygame.font.SysFont(None,48)

        #创建按钮的rect对象，使其在屏幕中居中
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        #按钮的标签只创建一次
        self.prep_msg(msg)

    def prep_msg(self,msg):
        """将msg渲染为图像，并在按钮上居中展示"""
        #render函数将存储在msg上的文本转化成图像， 还接受一个布尔实参，该实参指定开启还是关闭反锯齿功能（反锯齿让文本的边缘更平滑），另外两个实参分别时文本的颜色和文本的背景色(如果没有指定文本的背景色，pygame将以透明背景的方式渲染背景)
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制一个颜色填充按钮，再绘制一个文本
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)


