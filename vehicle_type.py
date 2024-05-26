import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.preprocessing import image  # type: ignore
from tensorflow.keras.applications.efficientnet import preprocess_input  # type: ignore
from keras.models import load_model

# Load your trained model
model = load_model("my_model.keras")


def predict_and_display(image_path, model, class_labels):

    img = image.load_img(image_path, target_size=(240, 240))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)

    predicted_class_label = class_labels[predicted_class_index]

    return predicted_class_label


# images = "Egyptain Cars\\Before Cropping\\0055.jpg"

# Define your class labels (e.g., ['car', 'truck', ...])
class_labels = ["Bus", "Car", "Minibus", "Motorcycle", "Truck"]


def Get_vehicle_type(image):
    # Loop through images and display predictions
    predicted_class_label = predict_and_display(image, model, class_labels)

    return predicted_class_label


# x = Get_vehicle_type(images)
# print (x)
