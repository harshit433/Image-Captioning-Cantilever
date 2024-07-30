from flask import Flask, request, render_template, redirect, url_for
from PIL import Image
import prediction

app = Flask(__name__)


def generate_caption(image_path):
    raw_image = Image.open(image_path).convert('RGB')
    text = "a photography of"
    inputs = processor(raw_image, text, return_tensors="pt")

    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            file_path = f'static/media/{file.filename}'
            file.save(file_path)
            caption = prediction.predict_caption(file_path)
            return render_template('index.html', file_path=file_path, caption=caption)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
