from tools.get_dr_txt import *
from tools.get_gt_txt import *
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('config',type=str)
parser.add_argument('surfix',type=int)
parser.add_argument('--year',type=int,default=2020)
parser.add_argument('--classes_path',type=str,default='model_data/imo_classes.txt')
args = parser.parse_args()

centernet = mAP_CenterNet(edge=args.surfix,model_path=args.config,classes_path=args.classes_path)
image_ids = open(f'VOCdevkit/VOC{args.year}/ImageSets/Main/test.txt').read().strip().split()

surfix = str(args.surfix)

if not os.path.exists("./input"):
    os.makedirs("./input")
if not os.path.exists("./input/detection-results_"+surfix):
    os.makedirs("./input/detection-results_"+surfix)
if not os.path.exists("./input/images-optional"):
    os.makedirs("./input/images-optional")

for image_id in tqdm(image_ids):
    image_path = f"./VOCdevkit/VOC{args.year}/JPEGImages/" + image_id + ".jpg"
    image = Image.open(image_path)
    # image.save("./inputWav/images-optional/"+image_id+".jpg")
    centernet.detect_image(image_id, image ,"./input/detection-results_"+surfix)

print("Conversion completed!")

image_ids = open(f'VOCdevkit/VOC{args.year}/ImageSets/Main/test.txt').read().strip().split()

if not os.path.exists("./input"):
    os.makedirs("./input")
if not os.path.exists("./input/ground-truth_"+surfix):
    os.makedirs("./input/ground-truth_"+surfix)

for image_id in image_ids:
    with open("./input/ground-truth_"+surfix+"/"+image_id+".txt", "w") as new_f:
        root = ET.parse(f"VOCdevkit/VOC{args.year}/Annotations/"+image_id+".xml").getroot()
        for obj in root.findall('object'):
            difficult_flag = False
            if obj.find('difficult')!=None:
                difficult = obj.find('difficult').text
                if int(difficult)==1:
                    difficult_flag = True
            obj_name = obj.find('name').text
            '''
            ！！！！！！！！！！！！注意事项！！！！！！！！！！！！
            # 这一部分是当xml有无关的类的时候，可以取消下面代码的注释
            # 利用对应的classes.txt来进行筛选！！！！！！！！！！！！
            '''
            # classes_path = 'model_data/voc_classes.txt'
            # class_names = get_classes(classes_path)
            # if obj_name not in class_names:
            #     continue

            bndbox = obj.find('bndbox')
            left = bndbox.find('xmin').text
            top = bndbox.find('ymin').text
            right = bndbox.find('xmax').text
            bottom = bndbox.find('ymax').text

            if difficult_flag:
                new_f.write("%s %s %s %s %s difficult\n" % (obj_name, left, top, right, bottom))
            else:
                new_f.write("%s %s %s %s %s\n" % (obj_name, left, top, right, bottom))

print("Conversion completed!")


subprocess.run('python tools/get_map.py --surfix '+str(surfix))