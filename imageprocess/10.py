# 2024/1/14 17:26
from PIL import Image,ImageFont,ImageDraw,ImageFilter
import string
import random

"""
random.randint(a,b)函数用于生成一个指定范围的随机整数(包括起始值和结束值)
*当范围内只有一个整数时，直接返回该整数
"""
def generator_bgcolor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def generator_font_color():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

"""
random.choice()用来从元组、字符串等序列中随机选择一个元素
字符串模块中的ascii_letters:生成全部字母，包括a-z,A-Z
字符串模块中的digits:生成数组，包括0-9
例如：
  list1 = [1,2,3,4,5]
  print(random.choice(list1))
"""
def make_rand_char():
    return random.choice(string.ascii_letters)

def producer():
    width = 60*4  #设置宽度是240
    height = 60   #设置高度是60
    """
     image.new(mode, size, color)  返回：一个图片对象，即 <class 'PIL.Image.Image'>
      1.mode：图片的模式。"1", "CMYK", "F", "HSV", "I", "L", "LAB", "P", "RGB", "RGBA", "RGBX", "YCbCr"
      2. 一个含有图片 宽，高 的元组；图片的尺寸(width, height)
      3.  图片的颜色；其默认值为0，即 黑色；
      *当设置图片的 mode 为 ‘RGBA’ 时，如果不填 color 参数的话，图片是 透明底！
    """
    image = Image.new('RGB',(width,height),(255,255,255)) #创建一个图片对象 (255,255,255)是白色
    """
    ImageFont.truetype(font, size=10, index=0, encoding='', layout_engine=None)
    返回：一个 Font 对象，这个 Font 对象可以用来将文本绘制到一个 Image 对象中
       1.font: 字体文件的文件名或文件对象、包含字体数据的字节串、字体的名字（仅在系统中安装了对应字体时）。
       2.size: 字体大小
       3.index: 字体文件中的字体编号
       4.index: 字体文件中的字体编号
       5.layout_engine: 字体布局引擎
       *支持从字节串中加载字体
       import requests
       # 从网络下载字体文件
       url = 'https://s3.amazonaws.com/python-gaming/fonts/AnotherDanger.ttf'
       response = requests.get(url)
       binary_data = response.content
   
       # 从字节串中加载字体
       font = ImageFont.truetype(binary_data, size=36)
    """
    font = ImageFont.truetype('arial.ttf',36)
    draw = ImageDraw.Draw(image) #在原图像的基础上创建绘制对象返回ImageDraw
    for x in range(width):
        for y in range(height):
            """
            ImageDraw.point(table,mode=None)函数可以对图像上的每个像素块进行处理，并将处理后的图像返回Image对象。
            1.table：一个包含256个整数或函数的列表，用于指定像素的映射表。(就是指定要处理像素块的位置，可以用整数明确位置，也可以通过函数来返回要处理的位置)
            2.mode：表示像素的格式，可选参数，当未指定时，自动从源图像中获取。
            例子：
              a.将一张图片灰度化
              from PIL import Image
              def make_grayscale(pix):
                  r, g, b = pix
                  gray_value = (r + g + b) // 3
                  return (gray_value, gray_value, gray_value)
              
              image = Image.open("test.png")
              gray_image = image.point(make_grayscale, "RGB")
              gray_image.show()
              
              b.假如有一张黑白图片，将其中黑色部分替换成其他颜色
              from PIL import Image
              def replace_black(pix):
                  r, g, b = pix
                  if r == 0 and g == 0 and b == 0:
                      return (255, 0, 0)  # 将黑色替换为蓝色
                  return pix  # 其他颜色保持不变
              
              image = Image.open("test2.png")
              new_image = image.point(replace_black, "RGB")
              new_image.show()
            """
            draw.point((x, y), fill=generator_bgcolor())

    for i in range(4):

        # ImageDraw.Draw.text(xy, text, fill=None, font=None, anchor=None, spacing=0, align=”left”)
        # 1.xy-文字的左上角。
        # 2.text-要绘制的文本。如果包含任何换行符，则文本将传递到multiline_text()
        # 3.fill-用于文本的颜色。
        # 4.font-一个ImageFont实例。(就是字体)
        # 5.spacing-如果文本传递到multiline_text()，则行之间的行间距。
        # 6.align-如果文本已传递到multiline_text()，“left”，“center”或“right”。
        # 例如：
        # from PIL import Image, ImageFont, ImageDraw
        # # creating a image object
        # image = Image.open(r'C:\Users\System-Pc\Desktop\rose.jpg')
        # draw = ImageDraw.Draw(image)
        # # specified font size
        # font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 20)
        # text = 'LAUGHING IS THE \n BEST MEDICINE'
        # # drawing text size
        # draw.text((5, 5), text, font = font, align ="left")
        # image.show()

        draw.text((i*60+10,10),make_rand_char(),font=font,fill=generator_font_color())

    #image.filter(ImageFilter.BLUR):是滤波器  ImageFilter.BLUR为模糊滤波，处理之后的图像会整体变得模糊。
    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg','jpeg')

if __name__ == '__main__':
        producer()