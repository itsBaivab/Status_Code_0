import os  
import requests  
from dotenv import load_dotenv  
  
# Load environment variables from .env file  
load_dotenv()  
  
def generate_qr_code(fileURL,positive_prompt,Seed):  
    # Define the payload  
    payload = {  
        "functions": None,  
        "variables": None,  
        "qr_code_data": fileURL,  
        "qr_code_input_image": None,  
        "qr_code_vcard": None,  
        "qr_code_file": None,  
        "use_url_shortener": True,  
        "text_prompt": positive_prompt,  
        "negative_prompt": "ugly, disfigured, low quality, blurry, nsfw, text, words, multiple limbs, extra fingers, extra limbs, saturated colors",  
        "image_prompt": None,  
        "image_prompt_controlnet_models": [  
            "sd_controlnet_canny",  
            "sd_controlnet_depth",  
            "sd_controlnet_tile",  
        ],  
        "image_prompt_strength": 0.3,  
        "image_prompt_scale": 1,  
        "image_prompt_pos_x": 0.5,  
        "image_prompt_pos_y": 0.5,  
        "selected_model": "dream_shaper",  
        "selected_controlnet_model": ["control_v1p_sd15_qrcode_monster_v2"],  
        "output_width": 768,  
        "output_height": 768,  
        "guidance_scale": 8,  
        "controlnet_conditioning_scale": [2],  
        "num_outputs": 1,  
        "quality": 60,  
        "scheduler": "multistep_dpm_solver",  
        "seed": Seed,  
        "obj_scale": 0.65,  
        "obj_pos_x": 0.5,  
        "obj_pos_y": 0.5,  
    }  
  
    try:  
        response = requests.post(  
            "https://api.gooey.ai/v2/art-qr-code/?example_id=ql5yj7qd",  
            headers={  
                "Authorization": f"Bearer {os.getenv('GOOEY_API_KEY')}",  
            },  
            json=payload,  
        )  
  
        # Check if the response is successful  
        response.raise_for_status()  
  
        result = response.json()  
        print(response.status_code, result['output']['output_images'])  
  
    except requests.exceptions.HTTPError as http_err:  
        print(f"HTTP error occurred: {http_err}")  
    except Exception as err:  
        print(f"Other error occurred: {err}")  
   
    return result['output']['output_images']
 
