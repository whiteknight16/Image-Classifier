from flask import Flask, request
from flask_cors import CORS
from tensorflow.keras import models
import numpy as np
from PIL import Image
import io
import requests

app = Flask(__name__)
CORS(app)

@app.route('/model', methods=['POST'])
def modelCall():
    try:
        url = request.json['url']
        response = requests.get(url)
        img = Image.open(io.BytesIO(response.content))
        img = img.resize((32,32))

        img_array = np.array(img) / 255.0  # Convert the image to a numpy array and scale the pixel values

        class_names=['Plane','Car','Bird','Cat','Deer','Dog','Frog','Horse','Ship','Truck']
        model = models.load_model("../server/image_classifier.model")

        prediction=model.predict(np.array([img_array]))
        index=np.argmax(prediction) #argmax give index of highest value
        return {"class": class_names[index]}
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)