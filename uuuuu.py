import numpy as np
from PIL import Image
from numpy import asarray, zeros
from matplotlib import pyplot

image = Image.open("616467.jpg")
data = asarray (image)
print("data array size:", data.shape)
print(data[1: 10, 1: 10, 1])


image2 = Image.fromarray(data[:, :, 1])
data2 = data//8
#print(data2[0:10, 0:10])
data3 = data
data3[:, :, 1] = zeros(data.shape())
data3[:, :, 2] = 0
image3 = Image.fromarray(data2)
image4 = Image.fromarray(data3)
#print(image2.mode)
#print(image2.size)
image2.save("outP1.jpg")
pyplot.imshow(image4)
pyplot.show()
