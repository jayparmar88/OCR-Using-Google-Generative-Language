import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image

import google.generativeai as genai

#api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key='AIzaSyDCCD2Qwwo67RARzm8V7R7x4dzdTyIdbgA')

def get_gemini_response(input, image,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,image[0],prompt])
    return response.text
   

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


##streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.header("Generative AI : Business Card Reader")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""  
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    input=st.text_input("Input Prompt (optional) : ",key="input")


submit=st.button("Submit")

input_prompt = """
               You are an expert in understanding business cards.
               Input: Image of a business card
               Task: Extract and label the following information in JSON format if available:
               Labels : company_name, person_name, occupation, contact_number, email addresse, website, address, other_details (services, features, etc.)
               Constraints: Do not include missing information.
               """

if submit:
    image_data = input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data, input)
    st.subheader("Output :")
    st.write(response)
