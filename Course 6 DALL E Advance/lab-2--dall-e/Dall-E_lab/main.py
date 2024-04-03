# libraries
import os
import openai
from PIL import Image,ImageOps,ImageFilter
from io import BytesIO
import requests

# Set API key and prompt
openai.api_key = os.getenv('OPENAI_KEY')
