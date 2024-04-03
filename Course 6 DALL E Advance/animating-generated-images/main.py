# WRITE YOUR CODE HERE
import os
import openai
from PIL import Image, ImageOps,ImageChops
from io import BytesIO
import requests

# Set environment variables
openai.api_key =  os.getenv('OPENAI_KEY')

# Generate the base image
def generate_base_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']

def download_image(image_url,x):
    response = requests.get(image_url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    with open(x+'.jpg', 'wb') as handler:
      handler.write(img_data)
    return img

angles = range(0, 360, 10)
image_filenames = [f"earth_{angle}_degrees.jpg" for angle in angles]

resized_earth_images = []
for filename in image_filenames:
    img = Image.open(filename)
    resized_img = img.resize((256, 256), Image.ANTIALIAS)
    resized_earth_images.append(resized_img)

output_gif = "rotating_earth.gif"
resized_earth_images[0].save(
    output_gif,
    save_all=True,
    append_images=resized_earth_images[1:],
    duration=100,
    loop=0
)