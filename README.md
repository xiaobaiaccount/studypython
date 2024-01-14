# studypython
### 学习python的小例子

1.图像处理(imageprocess)

```
string.ascii_letters #生成全部字母，包括a-z,A-Z
string.digits #生成数组，包括0-9

random.randint(a,b) #函数用于生成一个指定范围的随机整数(包括起始值和结束值)
random.choice() #用来从元组、字符串等序列中随机选择一个元素

image.new(mode, size, color) #创建一个图片对象

ImageFont.truetype(binary_data, size=36) #返回一个Font

ImageDraw.Draw(image) #在原图像的基础上创建绘制对象返回ImageDraw
ImageDraw.point(table,mode=None) #函数可以对图像上的每个像素块进行处理，并将处理后的图像返回Image对象。
ImageDraw.Draw.text(xy, text, fill=None, font=None, anchor=None, spacing=0, align=”left”) #在图片上面写字

image.filter(ImageFilter.BLUR):是滤波器   ImageFilter.BLUR为模糊滤波，处理之后的图像会整体变得模糊。对图片进行样式处理
```



