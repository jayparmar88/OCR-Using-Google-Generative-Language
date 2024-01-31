import streamlit as st
import easyocr
import re
import pandas as pd
import tldextract

reader = easyocr.Reader(['en'])

st.title("Extract and Segregate Information from Business Cards")

uploaded_files = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

def segregate_info(text):
    name_pattern = re.compile(r'\b(?:[A-Z][a-z]+(?: [A-Z][a-z]+)+(?: [A-Z][a-z]+)?)\b')
    phone_pattern = re.compile(r'\b(?:\+\d{1,4}[-.\s]?)?(?:\d[-.\s]?){8,}\b')
    email_pattern = re.compile(r'\b(?:[A-Za-z0-9._%+-]+)@(?:[A-Za-z0-9.-]+\.[A-Z|a-z]{2,})\b')
    company_pattern = re.compile(r'\b[a-zA-Z]+\.[a-zA-Z]+\b')
    address_pattern = re.compile(r'\b\d+[ ](?:[A-Za-z0-9.-]+[ ]?)+(?:Avenue|Lane|Road|Boulevard|Drive|Street|Ave|Dr|Rd|Blvd|Ln|St)\.?\b')
    website_pattern = re.compile(r'\b(?:www\.)?[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    pattern = ['@', '.', ',', '-', '+']

    name = None
    phone_numbers = []
    email = None
    company_name = None
    address = ""
    website = None
    other_info = []

    name_match = name_pattern.search(text)
    if name_match:
        name = name_match.group()

    # phone_matches = phone_pattern.findall(text)
    # phone_numbers.extend(phone_matches)

    lines = text.split('\n')
    for line in lines:

        email_match = email_pattern.search(line)
        if email_match:
            email = line.replace(" ", ".")

        phone_matches = phone_pattern.findall(line)
        phone_numbers.extend(phone_matches)

        website_matches = website_pattern.search(line)
        if(website_matches):
            if("@" in line):
                continue
            else:
                website = line.replace(" ", ".")
                extracted = tldextract.extract(website)
                company_name = extracted.domain


        flag = True
        for patter in pattern:
            if patter in line:
                flag = False
                break

        if flag:
            other_info.append(line)

        if ',' in line:
            address = address + line


    st.write("Segregated Information:")
    st.write(f"Name: {name}")
    st.write(f"Phone Numbers: {', '.join(phone_numbers)}")
    st.write(f"Email: {email}")
    st.write(f"Company Name: {company_name}")
    st.write(f"Address: {address}")
    st.write(f"Website: {website}")
    st.write(f"Other info: {other_info}")


    return {
        'Name': name,
        'Phone Numbers': phone_numbers,
        'Email': email,
        'Company Name': company_name,
        'Address': address,
        'Website': website,
        'Other Info':other_info,
        'Total Extracted Text': text
    }

all_extracted_details = []

for uploaded_file in uploaded_files:
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image")

        image_bytes = uploaded_file.read()

        result = reader.readtext(image_bytes)

        st.write("Extracted Text:")
        extracted_text = ""
        for (bbox, text, prob) in result:
            st.write(text)
            extracted_text += text + "\n"

        details = segregate_info(extracted_text)
        all_extracted_details.append(details)

df_all_extracted_details = pd.DataFrame(all_extracted_details)
df_all_extracted_details.to_excel('all_extracted_details.xlsx', index=False)

if st.button("Download All Extracted Details Excel File"):
    with open('all_extracted_details.xlsx', 'rb') as f:
        file_content = f.read()
        st.download_button(label='Download Excel File', data=file_content, file_name='all_extracted_details.xlsx', key='excel_download')
