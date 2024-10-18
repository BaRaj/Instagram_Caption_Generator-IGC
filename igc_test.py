from colorthief import ColorThief
import matplotlib.pyplot as plt 
from scipy.spatial import KDTree
from webcolors import CSS3_HEX_TO_NAMES
from webcolors import hex_to_rgb

API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
headers = {"Authorization": f"Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

def convert_rgb_to_names(rgb_tuple):
    
    # a dictionary of all the hex and their respective names in css3
    css3_db = CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))
    
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return f'{names[index]}'

output = query(" ") 			
			#insert file here
ct=ColorThief(" ")	

color_name=convert_rgb_to_names(ct.get_color())

prompt = f"Generate an instagram caption for a photo of {output} with the major color being {color_name}. "

from gradio_client import Client

client = Client("https://luohy-sail-7b.hf.space/")
result = client.predict(
				prompt,	# str representing input in 'Input' Textbox component
			True,	# bool representing input in 'Search Augmentation' Checkbox component
				fn_index=0
)

print(result)

