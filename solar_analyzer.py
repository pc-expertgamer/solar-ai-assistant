# solar_analyzer.py
import os
import base64
import requests
import json
from dotenv import load_dotenv
from prompt import get_solar_analysis_prompt

load_dotenv() # Loads the .env file

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# We choose a model that supports vision. Claude 3 Haiku is fast and cheap.
# Other options: "google/gemini-pro-vision", "openai/gpt-4o"
MODEL_NAME = "anthropic/claude-3-haiku" 

def encode_image(image_bytes):
    """Encodes the image bytes to a base64 string."""
    return base64.b64encode(image_bytes).decode('utf-8')

def analyze_rooftop_image(image_bytes, location, electricity_cost):
    """
    Analyzes a rooftop image using a vision model via OpenRouter.
    This addresses "LLM Integration" and "Response Accuracy".
    """
    base64_image = encode_image(image_bytes)
    analysis_prompt = get_solar_analysis_prompt(location, electricity_cost)

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": analysis_prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "response_format": {"type": "json_object"} # Ask for JSON output
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status() # Raises an HTTPError for bad responses (4xx or 5xx)
        
        # Extract the JSON content from the response
        response_data = response.json()
        json_content_string = response_data['choices'][0]['message']['content']
        
        # Parse the JSON string into a Python dictionary
        analysis_result = json.loads(json_content_string)
        return analysis_result

    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return {"error": f"API request failed: {e}"}
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        print(f"Failed to parse API response: {e}")
        print(f"Raw response: {response.text}") # Log the raw response for debugging
        return {"error": f"Failed to parse API response. The model may have returned an invalid format. Raw response: {response.text}"}