import i2v
from PIL import Image

import os
from os import path

def select(list, n=10):
    rounds = len(list) / n + 1
    for t in range(rounds):
        yield t+1, list[t*n: (t+1)*n]

def write_tags(file_list, tag_list):
    for file, tag in zip(file_list, tag_list):
        f = file.split('.')[0]
        t = tag['general']
        with open('tags/{}.txt'.format(f), 'w') as w:
            for k, v in t:
                w.write('{}##{}\n'.format(k, v))

illust2vec = i2v.make_i2v_with_caffe(
    'model/illust2vec_tag.prototxt',
    'model/illust2vec_tag_ver200.caffemodel',
    'model/tag_list.json')

path2date = path.join('..', 'illustrations_128')
for it, filename_list in select(os.listdir(path2date), 1000):
    image_list = []
    for filename in filename_list:
        if filename == 'false_positive': continue
        path2image = path.join(path2date, filename)
        this_img = Image.open(path2image)
        image_list.append(this_img)
    ret_tag = illust2vec.estimate_plausible_tags(image_list, threshold=0.05)
    write_tags(filename_list, ret_tag)
    print 'write', it, 'round of tags'