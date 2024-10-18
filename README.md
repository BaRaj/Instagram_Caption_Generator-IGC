# Instagram_Caption_Generator-IGC
This project leverages an AI model from Hugging Face to generate captions for images and identify the dominant color using ColorThief. The combination of the caption and color is then used to create Instagram-ready captions with an interactive Gradio interface.

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
### Clone the repository
git clone https://github.com/your-username/image-caption-color.git
cd image-caption-color
### Set up API Access:
Replace the Authorization header in the script with your Hugging Face API token:
headers = {"Authorization": "Bearer your_huggingface_token"}
### Insert Image File: 
Modify output = query(" ") and ct=ColorThief(" ") lines with the correct path to your image file.

### Run the script: 
To generate an Instagram caption based on your image, run:
python generate_caption.py

### Interactive Captioning: 
The script sends the generated prompt to the Gradio interface, which can augment your caption. You can see the output caption directly in the terminal.

## Example Output
For an image of a landscape:
