# Google Generative AI: Business Card Reader

## Project Overview

Text Extraction project aims to leverage the power of Google Generative Language API to extract relevant text information from business cards. The solution is deployed as a Streamlit application, providing users with a user-friendly interface to upload images, input prompts, and retrieve extracted information in JSON format.

## Purpose

The primary purpose of this project is to streamline the extraction of crucial information from business cards. The application facilitates the quick and accurate retrieval of data. This can be particularly useful in scenarios where manual extraction is time-consuming or impractical.

## Requirements

- python
- streamlit
- pillow
- google-generativeai

Install the required packages using:

```bash
pip install streamlit Pillow google-generativeai
```

## Configuration

1. **Google Generative Language API**: Obtain an API key from the [Google Cloud Console](https://console.cloud.google.com/) and replace `'YOUR_API_KEY'` in the app code with your actual API key. You can also use [Google AI studios](https://aistudio.google.com/app/apikey) to get API.

```python
genai.configure(api_key='YOUR_API_KEY')
```

## Usage

1. Access the application on streamlit platform or you can deploy it on your web browser.

2. Upload a business card image (supported formats: jpg, jpeg, png).

3. Optionally, provide an input prompt relevant to the image (e.g., specific information you want to extract).

4. Click the "Submit" button.

The application will use the Google Natural Language API and Gemini Generative AI to extract text information from the uploaded image based on the provided prompt.

## How It Works

1. **Upload Image:** Users can upload an image containing a business card.

2. **Input Prompt (Optional):** Users have the option to provide a prompt that guides the extraction process, allowing customization based on specific requirements.

3. **Text Extraction:** The Google Generative Language API is employed to extract text information from the image.

4. **Output Presentation:** The extracted information is presented in JSON format, organized into relevant categories.
