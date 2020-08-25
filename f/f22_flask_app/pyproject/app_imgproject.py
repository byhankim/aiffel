from flask import Flask, render_template, request
import os
from PIL import Image

app = Flask(__name__)

# image processing
def img_grayscale(image):
    return image.convert('L')

def img_resize(image):
    return image.resize((1980, 1080))

# flask
@app.route("/")
def index():
    return render_template("imgproject.html")

@app.route("/image_preprocess", methods=["POST"])
def preprocessing():
    if request.method == "POST":
        file = request.files['uploaded_image']
        if not file: return render_template('imgproject.html', label="No Files")
        
        img = Image.open(file)
        img = img_grayscale(img)
        img = img_resize(img)

        img.save("result_img.png")
        src_dir = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(src_dir, "result_img.png")

        # result return
        return render_template("imgproject.html",label=img_path)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=os.environ.get("PORT", 5000))