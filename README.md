# Roblox Shirt & Pants AI Generator

This web app lets you create Roblox shirt and pants textures from a prompt using AI!

## How it works

1. Enter a description (prompt) and pick "shirt" or "pants".
2. The AI generates a Roblox template image.
3. Download the image and upload it to Roblox.

**Note:**  
The included code uses a placeholder image. To make real AI designs, connect to an image generation API (see below).

---

## Setup

1. **Install Python** (version 3.8+ recommended).

2. **Clone your repo and enter the folder:**
   ```sh
   git clone https://github.com/Sysbret/roblox-ai-shirt-generator.git
   cd roblox-ai-shirt-generator
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```sh
   python app.py
   ```
   Open `http://127.0.0.1:5000` in your browser.

---

## How to Connect a Real AI Image Generator

- Replace the `generate_image` function in `app.py` with a call to a service like:
    - [Stability AI API](https://platform.stability.ai/docs/api-reference)
    - [OpenAI DALL-E](https://platform.openai.com/docs/guides/images)
    - [Replicate.com](https://replicate.com/)

Most APIs return a PNG or JPG image. Save it to the `static/generated` folder.

---

## Roblox Template Info

Roblox shirts/pants have specific templates:
- Shirt: 585 x 559 pixels
- Pants: 585 x 559 pixels

This app uses those sizes for compatibility.

---

## Git & GitHub Basics

- **Make changes:** Edit files in your folder.
- **Stage changes:** `git add .`
- **Commit:** `git commit -m "Describe your change"`
- **Push:** `git push origin main` (or your branch name)

If you're new to GitHub, see:  
[GitHub Hello World Guide](https://docs.github.com/en/get-started/quickstart/hello-world)

---

## Credits

By Sysbret.  
Template code by GitHub Copilot.
