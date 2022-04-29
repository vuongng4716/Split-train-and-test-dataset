
import os
import numpy as np
import shutil
import random
root_dir = 'D:\\pathdir\\'
classes_dir = ['0', '1']

test_ratio = 0.4


src = 'D:\\pathdir\\'

allFileNames = os.listdir(src)
np.random.shuffle(allFileNames)
train_FileNames, test_FileNames = np.split(np.array(allFileNames),
                                                          [int(len(allFileNames)* (1 - test_ratio))])


train_FileNames = [src + name for name in train_FileNames.tolist()]
test_FileNames = [src + name for name in test_FileNames.tolist()]

print("*****************************")
print('Total images: ', len(allFileNames))
print('Training: ', len(train_FileNames))
print('Testing: ', len(test_FileNames))


for name in train_FileNames:
    shutil.copy(name, root_dir + 'train\\')

for name in test_FileNames:
    shutil.copy(name, root_dir + 'test\\')