import os
from config import HP
from utils import recursive_fetching
import random
import json

random.seed(HP.seed)

cls_mapper = {
    "cls2id": {"A":0, "B":1, "C":2, "Five":3, "Point":4, "V":5},
    "id2cls": {"0":"A", "1":"B", "2":"C", "3":"Five", "4":"Point", "5":"v"}
}
json.dump(cls_mapper, open(HP.cls_mapper_path, 'w'))

train_items = recursive_fetching(HP.train_data_root, ['ppm'])
test_items = recursive_fetching(HP.test_data_root, ['ppm'])
dataset = train_items + test_items
dataset_num = len(dataset)
print("Total Items: %d" % dataset_num)
random.shuffle(dataset)

dataset_dict = {}
for it in dataset:
    fn_start = os.path.split(it)[-1].split('-')[0]
    cls_id = cls_mapper["cls2id"][fn_start]
    if cls_id not in dataset_dict:
        dataset_dict[cls_id] = [it]
    else:
        dataset_dict[cls_id].append(it)

train_ratio, eval_ratio, test_ratio = 0.8, 0.1, 0.1
train_set, eval_set, test_set = [], [], []
for _, set_list in dataset_dict.items():
    length = len(set_list)
    train_num, eval_num = int(length*train_ratio), int(length*eval_ratio)
    test_num = length - train_num - eval_num
    random.shuffle(set_list)
    train_set.extend(set_list[:train_num])
    eval_set.extend(set_list[train_num:train_num+eval_num])
    test_set.extend(set_list[train_num+eval_num:])

random.shuffle(train_set)
random.shuffle(eval_set)
random.shuffle(test_set)
print("train set : eval set : test set -> ", len(train_set), len(eval_set), len(test_set))

with open(HP.metadata_train_path, 'w') as fw:
    for path in train_set:
        fn_start = os.path.split(path)[-1].split('-')[0]
        cls_id = cls_mapper["cls2id"][fn_start]
        fw.write("%d|%s\n" % (cls_id, path))

with open(HP.metadata_eval_path, 'w') as fw:
    for path in eval_set:
        fn_start = os.path.split(path)[-1].split('-')[0]
        cls_id = cls_mapper["cls2id"][fn_start]
        fw.write("%d|%s\n" % (cls_id, path))

with open(HP.metadata_test_path, 'w') as fw:
    for path in test_set:
        fn_start = os.path.split(path)[-1].split('-')[0]
        cls_id = cls_mapper["cls2id"][fn_start]
        fw.write("%d|%s\n" % (cls_id, path))

from utils import load_meta, load_image
mode_set, size_set = [], []
for _, path in load_meta(HP.metadata_train_path):
    img = load_image(path)
    mode_set.append(img.mode)
    size_set.append(img.size)

print(set(mode_set), set(size_set))






