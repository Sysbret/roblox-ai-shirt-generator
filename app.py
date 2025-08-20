from flask import Flask, render_template, request, send_from_directory
import requests
import os
from datetime import datetime

app = Flask(__name__)
GENERATED_FOLDER = "static/generated"
os.makedirs(GENERATED_FOLDER, exist_ok=True)

# Dummy image generator - replace with real API like Stability, OpenAI, etc.
def generate_image(prompt, template="shirt"):
    # Example: use a placeholder image for now
    # Replace this with an actual call to an image generation API
    url = "https://placehold.co/585x559/png?text=" + template.capitalize()
    img_data = requests.get(url).content
    filename = f"{template}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
    filepath = os.path.join(GENERATED_FOLDER, filename)
    with open(filepath, "wb") as f:
        f.write(img_data)
    return filename

@app.route("/", methods=["GET", "POST"])
def index():
    image_url = None
    if request.method == "POST":
        prompt = request.form.get("prompt")
        template = request.form.get("template", "shirt")
        filename = generate_image(prompt, template)
        image_url = f"/{GENERATED_FOLDER}/{filename}"
    return render_template("index.html", image_url=image_url)

@app.route("/static/generated/<path:filename>")
def download_file(filename):
    return send_from_directory(GENERATED_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)