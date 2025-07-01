---
title: Solar AI Assistant

colorFrom: yellow
colorTo: blue
sdk: streamlit
app_file: app.py
pinned: false
---


# Solar Industry AI Assistant

This project is an AI-powered rooftop analysis tool that uses satellite imagery to assess solar installation potential, as part of an internship assessment.

## Overview

The system takes a satellite image of a rooftop, along with the property's location and electricity cost, and provides a detailed analysis including:
- Rooftop characteristics (usable area, orientation, shading)
- A recommended solar panel system size
- An estimated ROI and payback period

## Project Structure
```
.
├── .env                  # Stores secret API keys (DO NOT COMMIT)
├── .gitignore            # Specifies files for Git to ignore
├── README.md             # This documentation file
├── app.py                # The main Streamlit web application
├── prompt.py             # Contains the master prompt for the AI
├── requirements.txt      # Python dependencies for the project
├── solar_analyzer.py     # Backend logic for calling the AI API
└── venv/                 # Python virtual environment
```

## Project Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone (https://github.com/pc-expertgamer/solar-ai-assistant)
    cd solar-ai-assistant
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your API Key:**
    - Sign up at [OpenRouter.ai](https://openrouter.ai/) to get an API key.
    - Create a file named `.env` in the root directory.
    - Add your key to the file like this:
      `OPENROUTER_API_KEY="your-api-key-here"`

5.  **Run the application:**
    ```bash
    streamlit run app.py
    ```
    Open your browser to the URL provided by Streamlit (usually `http://localhost:8501`).

## Implementation Documentation

-   **AI Integration:** The core logic resides in `solar_analyzer.py`. It uses the `requests` library to call the OpenRouter API, specifically targeting a vision-capable model (`anthropic/claude-3-haiku`). The image is base64-encoded and sent along with a detailed text prompt.
-   **Prompt Engineering:** The prompt, located in `prompt.py`, is dynamically generated to include user-provided context (location, electricity cost). It explicitly instructs the AI to return a structured JSON object, which makes the response reliable and easy to parse. This addresses the "Structured Output Extraction" requirement.
-   **Web Interface:** The user interface is built with Streamlit in `app.py`. It provides widgets for file upload and text input, and displays the final analysis in a clean, user-friendly format using columns and metric cards.
-   **Error Handling:** The API call in `solar_analyzer.py` is wrapped in a `try...except` block to gracefully handle network errors or malformed responses from the AI. The UI in `app.py` displays these errors to the user.

## Example Use Cases

1.  **Homeowner Assessment:** A homeowner can upload a satellite picture of their house, input their location and average electricity bill, and get a preliminary estimate of solar potential and savings without needing a site visit.
2.  **Solar Professional Triage:** A solar sales consultant can quickly analyze multiple properties to identify the most promising leads before investing time in a detailed, manual proposal.

## Future Improvement Suggestions

-   **Automated Image Fetching:** Integrate with an API like Google Maps Static API to automatically fetch a satellite image based on an address, removing the need for manual uploads.
-   **Advanced ROI Calculation:** Incorporate a database or API for local, state, and federal solar incentives (e.g., tax credits, SRECs) to provide a more accurate financial analysis.
-   **3D Shading Analysis:** Use more advanced geospatial data (like LiDAR, if available) to perform a more precise, hour-by-hour shading analysis throughout the year.
-   **Model Comparison:** Allow the user to select from different AI models (e.g., GPT-4o, Gemini Pro Vision) to compare results and costs.
-   **Performance Metrics:** Log the response time and confidence scores from the AI to track performance and identify potential issues with image quality or prompt design.
