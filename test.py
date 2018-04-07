import i2v
from PIL import Image

illust2vec = i2v.make_i2v_with_caffe(
    'model/illust2vec_tag.prototxt',
    'model/illust2vec_tag_ver200.caffemodel',
    'model/tag_list.json')

img = Image.open('images/dora.jpg')
ret = illust2vec.estimate_plausible_tags([img], threshold=0.1)
print ret[0]

