#-------------------------------------#
#   调用摄像头或者视频进行检测
#   调用摄像头直接运行即可
#   调用视频可以将cv2.VideoCapture()指定路径
#   视频的保存并不难，可以百度一下看看
#-------------------------------------#
import time

import cv2
import numpy as np
from PIL import Image

from tools.centernet import CenterNet

centernet = CenterNet()
#-------------------------------------#
#   调用摄像头
#   capture=cv2.VideoCapture("1.mp4")
#-------------------------------------#
# capture=cv2.VideoCapture(0)
# capture=cv2.VideoCapture("rtmp://183.234.189.126:1935/big/test")
# capture=cv2.VideoCapture("rtmp://183.234.189.126:1935/live/cctv2")
# capture=cv2.VideoCapture("img//hyd.mp4")
capture=cv2.VideoCapture("img/Video23.mp4")
# capture=cv2.VideoCapture("img//sourcecode.mp4")
# fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')
# out = cv2.VideoWriter('output.mp4',fourcc, 20.0,(640,480))
fps = 0.0
while(True):
    t1 = time.time()
    # 读取某一帧
    for i in range(10):
        ref,frame=capture.read()
    ref,frame=capture.read()
    # 格式转变，BGRtoRGB

    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    # 转变成Image
    frame = Image.fromarray(np.uint8(frame))
    # 进行检测
    frame = np.array(centernet.detect_image(frame))
    print(frame.shape)
    fps  = ( fps + (1./(time.time()-t1)) ) / 2
    print("fps= %.2f"%(fps))
    frame = cv2.putText(frame, "fps= %.2f"%(fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # RGBtoBGR满足opencv显示格式
    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    # out.write(frame)
    cv2.imshow("video",frame)
    c= cv2.waitKey(30) & 0xff 
    if c==27:
        capture.release()
        # out.release()
        break
capture.release()
# out.release()
