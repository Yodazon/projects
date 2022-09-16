from pickletools import optimize
from telnetlib import SE
import numpy as np
import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from keras.utils import to_categorical


train_images = mnist.train_images()
train_labels = mnist.train_labels()

test_images = mnist.test_images()
test_labels = mnist.test_labels()

#Normalize the images
train_images = (train_images/255) - 0.5
test_images = (test_images/255) - 0.5

#Flatten the images
train_images = train_images.reshape((-1,784))
test_images = test_images.reshape((-1,784))

print (train_images.shape)
print (test_images.shape)


#Build the model
model = Sequential([

    Dense(64, activation='relu',input_shape = (784,)),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax'),
])

#Compile the model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'],
)

#Train the model
model.fit(
    train_images,
    to_categorical(train_labels),
    epochs=5,
    batch_size=32,
)

model.evaluate(
    test_images,
    to_categorical(test_labels)
)


# Load the model's saved weights
model.save_weights('model.h5')

#predict on the first 5 test images
predictions = model.predict(test_images[:5])

#print our model's predictions
print (np.argmax(predictions, axis =1))

print (test_labels[:5])
