import os
count = 0
with open(r"C:\Users\user\Desktop\pythonTrain\capstone project\object detection\weekly offers detection\Tensorflow\workspace\images\collectedimages\offers_only_dataset\train.txt") as t:
    imagesPath = t.readlines()
for path in imagesPath:
    path = path[:-1]  # remove \n
    path = path.replace("jpg", "txt").replace("JPEG", "txt")
    print(path)
    path = os.path.join(
        r"C:\Users\user\Desktop\pythonTrain\capstone project\object detection\weekly offers detection\Tensorflow\workspace\images\collectedimages\offers_only_dataset", path)
    with open(path)as t:
        boxes = t.readlines()
    count += len(boxes)
print(count)
