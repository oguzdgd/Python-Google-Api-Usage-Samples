import pathlib
import textwrap

import google.generativeai as genai
import PIL.Image


img = PIL.Image.open('image.png') 

# Used to securely store your API key

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

GOOGLE_API_KEY='WRITE YOUR APİ KEY HERE'
genai.configure(api_key=GOOGLE_API_KEY)


for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')

#İf you want to use gemini-pro-vision use below code
"""
model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(img)
print(response.text)
"""

response = model.generate_content("Say Hello for Yıldız Ai")
print(response.text)