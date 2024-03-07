from utils import load_lora_info
import os
import requests

def download_file(url, filename):
    response = requests.get(url, stream=True)
    print(f"Status code: {response.status_code}")  # Check the status code

    if response.history:
        print("Request was redirected")
        for resp in response.history:
            print(f"Redirected from {resp.url}")

    print(f"Final URL: {response.url}")  # Check the final URL
    print(f"Content-Type: {response.headers.get('Content-Type')}")  # Check the content type

    if response.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=128):
                f.write(chunk)
        print(f"Downloaded '{filename}' from '{url}'")
    else:
        print(f"Error: Unable to download file from '{url}'")

def download_loras(style: str):
    os.makedirs("models/lora", exist_ok=True)
    os.makedirs(f"models/lora/{style}", exist_ok=True)

    lora_info = load_lora_info(style)

    for element in list(lora_info.keys()):
        for lora in lora_info[element]:
            lora_id = lora["id"]
            lora_weight_url = lora["weight_url"]
            download_file(lora_weight_url, f"models/lora/{style}/{lora_id}.safetensors")

if __name__ == "__main__":
    download_loras("reality")