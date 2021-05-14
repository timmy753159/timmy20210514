import numpy as np
from PIL import Image
from numpy import asarray
from matplotlib import pyplot

image = Image.open("616467.jpg")
w, h = image.size
image_new = image.resize((w, h * 2))
imagex1 = Image.new("RGB", (256, 256), color=(255, 0, 0))

data = asarray (image)
datax1 = asarray(imagex1)
datax1.setflags(write=1)
for i in range(256):
    datax1[:, i, 0] = i


print("data array size:", data.shape)
print(data[1: 10, 1: 10, 1])

image2 = Image.fromarray(data[:, :, 1])
data2 = data//8
#print(data2[0:10, 0:10])
data3 = data
image3 = Image.fromarray(data2)
imagex2 = Image.fromarray(datax1)

#print(image2.mode)
#print(image2.size)
image2.save("outP1.jpg")
pyplot.imshow(image2)
pyplot.show()
