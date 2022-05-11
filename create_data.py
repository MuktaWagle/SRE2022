import random
import shutil, os

with open('image_list.txt') as f:
    lines = f.readlines()

f.close()

splitlines = []

for l in lines:
    splitlines.append(l.split(' '))

folders = {'aeroplane': [], 'bicycle': [], 'bus': [], 'car': [],
 'horse': [], 'knife': [], 'motorcycle': [],'person': [],'plant': [],
 'skateboard': [],'train': [],'truck': []
}

classes = list(folders.keys())

for a in splitlines:
    i = int(a[1])
    folders[classes[i]].append(a)

for key in classes:
    random.shuffle(folders[key])
    folders[key] = folders[key][:206]
    path = os.path.join('validation1',key)
    os.mkdir(path)

path1 = os.path.join('validation1',"label_target.txt")
f1 = open(path1,"a")

for key in classes:
    path = os.path.join('validation1',key)
    for p in folders[key]:
        shutil.copy(p[0], path)
        f1.write(p[0]+" "+p[1])
f1.close()

print(len(folders['bus']))
