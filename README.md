# Instagram_Caption_Generator-IGC

This project leverages an AI model from Hugging Face to generate captions for images and identify the dominant color using ColorThief. Combining the caption and color is then used to create Instagram-ready captions with an interactive Gradio interface.

## Features
### Image Captioning: 
Uses the ViT-GPT2 model from Hugging Face to generate captions for uploaded images.
### Color Detection: 
Extracts the dominant color from the image using ColorThief and converts it to a human-readable color name.
### Interactive Caption Generator: 
Integrates with Gradio to generate Instagram captions based on the image description and dominant color.
## Requirements
You will need the following Python packages:

requests
colorthief
matplotlib
scipy
webcolors
gradio_client
### Install the required packages using:
pip install requests colorthief matplotlib scipy webcolors gradio_client
## How to Use
### Clone the repository:
git clone https://github.com/BaRaj/image-caption-color.git
cd image-caption-color
### Set up API Access:
Replace the Authorization header in the script with your Hugging Face API token:
headers = {"Authorization": "Bearer your_huggingface_token"}
### Insert Image File:
Modify the output = query(" ") and ct=ColorThief(" ") lines with the correct path to your image file.
### Run the script
To generate an Instagram caption based on your image, run: python generate_caption.py
## Example Output
![amazing-landscape-with-mountains-forest-sunset-sky-is-ablaze-with-color-trees-are-silhouetted-against-horizon_36682-200883](https://github.com/user-attachments/assets/04b123a9-bf12-4668-a235-54509e9554c1)
Generated Caption: A breathtaking view of mountains at sunset.
Dominant Color: Cornflower Blue Instagram Caption: Generate an Instagram caption for a photo of a breathtaking view of mountains at sunset with the major color being Cornflower Blue.
## How It Works
### Image Captioning: 
The ViT-GPT2 model from Hugging Face analyzes the image and generates captions based on visual features.
### Color Extraction: 
The dominant color is extracted using ColorThief and mapped to a CSS3 color name via the KDTree algorithm.
### Caption Generation: 
A Gradio-based API takes the image caption and color and outputs 4 Instagram-ready captions.
