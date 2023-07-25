'''
predict.py有几个注意点
1、该代码无法直接进行批量预测，如果想要批量预测，可以利用os.listdir()遍历文件夹，利用Image.open打开图片文件进行预测。
具体流程可以参考get_dr_txt.py，在get_dr_txt.py即实现了遍历还实现了目标信息的保存。
2、如果想要进行检测完的图片的保存，利用r_image.save("img.jpg")即可保存，直接在predict.py里进行修改即可。 
3、如果想要获得预测框的坐标，可以进入detect_image函数，在绘图部分读取top，left，bottom，right这四个值。
4、如果想要利用预测框截取下目标，可以进入detect_image函数，在绘图部分利用获取到的top，left，bottom，right这四个值
在原图上利用矩阵的方式进行截取。
5、如果想要在预测图上写额外的字，比如检测到的特定目标的数量，可以进入detect_image函数，在绘图部分对predicted_class进行判断，
比如判断if predicted_class == 'car': 即可判断当前目标是否为车，然后记录数量即可。利用draw.text即可写字。
'''
from tools.centernet import CenterNet
import os
import numpy as np

centernet = CenterNet()

# while True:
#     img = input('Input image filename:')
#     try:
#         image = Image.open(img)
#     except:
#         print('Open Error! Try again!')
#         continue
#     else:
#         r_image,_ = centernet.detect_image(image)
#         # r_image.save("img.jpg")
#         r_image.show()

for root, dirs, files in os.walk("img500", topdown=False):
    scoreList=[]
    for name in files:
        imgpath=os.path.join(root, name)
        try:
            # image = Image.open(imgpath)
            _, maxscore = centernet.detect_image(imgpath)
        except:
            print(imgpath)
            # print('Open Error! Try again!')
            continue
        else:

            scoreList.append(maxscore)
            # r_image.save("img.jpg")
            # image=image.convert('L')
            # image.show()
            # r_image.show()
            print(maxscore)
print(sum(scoreList)/len(scoreList))
print(len(scoreList))

E=sum(scoreList)/len(scoreList)
print(sum(scoreList)/len(scoreList))
print(len(scoreList))
scorenp =np.asarray(scoreList)
print(np.median(scorenp))
print(np.mean(scorenp))
print(np.var(scorenp))
print(np.std(scorenp))
