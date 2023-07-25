# 1.Example 推流摄像头视频数据
import subprocess as sp
import cv2
from tools.centernet import CenterNet
import time
import numpy as np
from PIL import Image

centernet = CenterNet()
rtmpUrl = "rtmp://183.234.189.126:1935/live/czb"
camera_path = ""
# cap = cv.VideoCapture("imgs\\videodata.ddm")
# cap = cv.VideoCapture("imgs\\sourcecode.mp4")
cap = cv2.VideoCapture("rtmp://183.234.189.126:1935/big/test")
# cap = cv.VideoCapture(0)
# Get video information
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(str(fps))
# ffmpeg command
command = ['ffmpeg',
        '-re','-y',
        '-f', 'rawvideo',
        '-vcodec','rawvideo',
        '-pix_fmt', 'bgr24',
        '-s', "{}x{}".format(width, height),
        '-r', str(fps),
        '-i', '-',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-preset', 'ultrafast',
        '-f', 'flv',
        rtmpUrl]

# 管道配置
p = sp.Popen(command, stdin=sp.PIPE)

# read webcamera
while(cap.isOpened()):
    # ret, frame = cap.read()
    # if not ret:
    #     print("Opening camera is failed")
    #     break

    # process frame
    # your code
    t1 = time.time()
    # 读取某一帧
    # for i in range(3):
    #     ref, frame = cap.read()
    ref, frame = cap.read()
    # 格式转变，BGRtoRGB
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    # 转变成Image
    frame = Image.fromarray(np.uint8(frame))
    # 进行检测
    frame = np.array(centernet.detect_image(frame))

    fps = (fps + (1. / (time.time() - t1))) / 2
    print("fps= %.2f" % (fps))
    frame = cv2.putText(frame, "fps= %.2f" % (fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # RGBtoBGR满足opencv显示格式
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    # cv2.imshow("video", frame)
    c = cv2.waitKey(30) & 0xff
    if c == 27:
        cap.release()
        break
    # process frame

    # write to pipe
    p.stdin.write(frame.tostring())