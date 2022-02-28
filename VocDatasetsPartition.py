# Voc数据集划分,生成对应的txt文件
import os
import random

# root_dir = r'./Own_data/VOC2007/'
root_dir = r"./datasets/VOCdevkitnb/VOC2007/"
if not os.path.exists(root_dir):
    os.makedirs(root_dir)

## 0.9train 0.1val 0.2test
trainval_percent = 0.925  # 训练集+验证集 占 所有数据集比例
train_percent = 1.0  #训练集占  训练集+验证集 比例
xmlfilepath = root_dir + 'Annotations'
if not os.path.exists(xmlfilepath):
    os.makedirs(xmlfilepath)
txtsavepath = root_dir + 'ImageSets/Main'
if not os.path.exists(txtsavepath):
    os.makedirs(txtsavepath)
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open(root_dir + 'ImageSets/Main/trainval.txt', 'w')
ftest = open(root_dir + 'ImageSets/Main/test.txt', 'w')
ftrain = open(root_dir + 'ImageSets/Main/train.txt', 'w')
fval = open(root_dir + 'ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()