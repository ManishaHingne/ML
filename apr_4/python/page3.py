from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
import numpy as np
import cv2 as cv

def createAndSaveModel():
    classifier = Sequential()

    # add convolution
    classifier.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))

    # add max pooling
    classifier.add(MaxPooling2D(pool_size=(2, 2)))

    # add flattening
    classifier.add(Flatten())

    # full connection

    # hidden layer
    classifier.add(Dense(units=128, activation='relu'))

    # output layer
    classifier.add(Dense(units=1, activation='sigmoid'))

    # compile the layers
    # create the model
    classifier.compile(optimizer='adam', loss='mean_squared_error')

    from keras.preprocessing.image import ImageDataGenerator

    # 0 - 1
    # RGB = 255, 0, 0 => 1, 0, 0
    x_train_generator = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
    x_test_generator = ImageDataGenerator(rescale=1./255)

    # generate train and test data
    x_train = x_train_generator.flow_from_directory('images/training_set', target_size=(64, 64), batch_size=32, class_mode='binary')
    x_test = x_test_generator.flow_from_directory('images/test_set', target_size=(64, 64), batch_size=32, class_mode='binary')

    # fit the images to the model
    classifier.fit_generator(x_train, steps_per_epoch=8000, epochs=20, validation_data=x_test, validation_steps=1000)

    # save the model
    json = classifier.to_json()
    file = open('my_model.json', 'w')
    file.write(json)
    file.close()

    # save the weights
    classifier.save_weights('weights.h5', True)


# createAndSaveModel()

def classify(testImageFile):
    from keras.models import model_from_json

    # read the json model
    file = open('my_model.json', 'r')
    data = file.read()
    print(data)

    file.close()

    # classifier will load the model from the data
    # data -> contents of the my_model.json file
    classifier = model_from_json(data)

    # load waits
    classifier.load_weights('weights.h5')

    # load the test image
    from keras.preprocessing import image

    test_image = image.load_img(testImageFile, target_size=(64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)

    classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    result = classifier.predict(test_image)

    filename = ''
    if result[0][0] == 1:
        prediction = 'dog'
        filename = 'images/training_set/dogs/dog.1.jpg'
    else:
        prediction = 'cat'
        filename = 'images/training_set/cats/cat.1.jpg'

    print('prediction: {}'.format(prediction))

    # visualize
    image = cv.imread(filename)
    cv.imshow('result', image)
    cv.waitKey(0)

# classify('images/single_prediction/cat_or_dog_1.jpg')
classify('images/single_prediction/cat_or_dog_2.jpg')













