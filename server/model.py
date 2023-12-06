#Based on neural network
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

#Scaling Data down
train_images,test_images = train_images/255.0, test_images/255.0

#Definig Class name list
#images are of low res
class_names=['Plane','Car','Bird','Cat','Deer','Dog','Frog','Horse','Ship','Truck']

#Visualising image
for i in range(16):
    plt.subplot(4,4,i+1)
    plt.xticks([]) #To remove cordinates
    plt.yticks([]) #To remove cordinates
    plt.imshow(train_images[i],cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i][0]])

# plt.show()


#reducing amount of data for fast operation
'''train_images=train_images[:20000]
train_labels=train_labels[:20000]
test_images=test_images[:4000]
test_labels=test_labels[:4000]'''

#model
#convolutional layer takes detail like truck bigger than car
#pooling layer reduces image to essential information
model=models.Sequential()
model.add(layers.Conv2D(32,(3,3),activation='relu',input_shape=(32,32,3)))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64,(3,3),activation='relu'))
model.add(layers.MaxPooling2D(2,2))
model.add(layers.Conv2D(64,(3,3),activation='relu'))
model.add(layers.Flatten()) #Making it 1D
model.add(layers.Dense(64,activation='relu'))
model.add(layers.Dense(10,activation='softmax'))


model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(train_images,train_labels,epochs=11,validation_data=(test_images,test_labels)) #how often data is repeated to model (epochs)

loss,accuracy=model.evaluate(test_images,test_labels)
print(f"Loss:{loss},accuracy:{accuracy}")

model.save('image_classifier.model')

