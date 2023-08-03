import requests
from colorthief import ColorThief
import matplotlib.pyplot as plt 

API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
headers = {"Authorization": f"Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("C:/Users/verys/Downloads/gerson-repreza-cpmZ9WkkYGE-unsplash.jpg")
ct=ColorThief("C:/Users/verys/Downloads/gerson-repreza-cpmZ9WkkYGE-unsplash.jpg")

print(output, ct.get_color(quality=1))

from gradio_client import Client

client = Client("https://huggingfaceh4-falcon-chat.hf.space/")
result = client.predict(
				"Howdy!",	# str  in 'Click on any example and press Enter in the input textbox!' Dataset component
				fn_index=0
)
print(result)