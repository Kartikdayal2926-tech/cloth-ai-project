import os
from flask import Flask, render_template, request
from model.recommender import get_recommendation
import requests

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
HEADERS = {"Authorization": f"Bearer {os.environ.get('HF_TOKEN')}"}

def generate_image(prompt):
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})

    if response.status_code == 200:
        image_path = "static/output.png"
        with open(image_path, "wb") as f:
            f.write(response.content)
        return image_path

    print(response.text)
    return None


@app.route("/", methods=["GET", "POST"])
def index():
    outfit = None
    image = None
    uploaded_image = None
    ai_tip = None

    if request.method == "POST":
        gender = request.form["gender"]
        occasion = request.form["occasion"]
        color = request.form["color"]
        season = request.form["season"]

        photo = request.files.get("photo")

        if photo and photo.filename != "":
            uploaded_image = os.path.join(UPLOAD_FOLDER, photo.filename)
            photo.save(uploaded_image)

            ai_tip = "Based on your outfit, try contrast colors and accessories."

        outfit = get_recommendation(gender, occasion, color, season)

        prompt = f"{outfit}, full body fashion model, premium clothing, realistic"
        image = generate_image(prompt)

    return render_template(
        "index.html",
        outfit=outfit,
        image=image,
        uploaded_image=uploaded_image,
        ai_tip=ai_tip
    )


if __name__ == "__main__":
    app.run(debug=True)