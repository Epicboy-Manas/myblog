import os
import openai
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

date_str = datetime.now().strftime('%Y-%m-%d')
title = "Why Don't Birds Get Electrocuted on Power Lines?"
filename = f"content/posts/{date_str}-birds-electrocution.md"

prompt = (
    "Write a curiosity-sparking technical blog post for electrical engineering students titled "
    f"'{title}'. Explain why birds don't get electrocuted when they sit on power lines, "
    "include real-world examples, and be engaging. End with a takeaway. Use markdown formatting."
)

response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

content = response['choices'][0]['message']['content']

os.makedirs("content/posts", exist_ok=True)

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"---\ntitle: \"{title}\"\ndate: {date_str}\ndraft: false\n---\n\n")
    f.write(content)

import openai
import requests

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    
    # Download the image locally (required for Hugo)
    img_data = requests.get(image_url).content
    with open("static/images/generated_diagram.png", "wb") as f:
        f.write(img_data)
    
    return "/images/generated_diagram.png"  # Hugo static path

