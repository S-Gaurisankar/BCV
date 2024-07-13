import os
import sys
import streamlit as st

sys.path.append(os.path.abspath(r"C:\Users\gauri\OneDrive\Desktop\BusinessContractValidation\BCV2\scripts"))

from compare import highlight_differences

st.title("Business Contract Validation")

# api_key = st.text_input("Enter your API Key", type="password")
api_key = "AIzaSyD9BWdDpADSUichoSLnzJvjh5c3TTdM9mA"

pdf1 = st.file_uploader("Upload the first PDF", type="pdf")
pdf2 = st.file_uploader("Upload the second PDF", type="pdf")

if pdf1 and pdf2 and api_key:
    os.makedirs("data/samples", exist_ok=True)
    
    with open("data/samples/temp1.pdf", "wb") as f:
        f.write(pdf1.getbuffer())

    with open("data/samples/temp2.pdf", "wb") as f:
        f.write(pdf2.getbuffer())

    output_path = "data/samples/highlighted_diff.pdf"

    if st.button("Generate Differences PDF"):
        highlight_differences("data/samples/temp1.pdf", "data/samples/temp2.pdf", output_path, api_key)
        st.success("Differences highlighted successfully!")
        with open(output_path, "rb") as f:
            st.download_button("Download Highlighted PDF", f, file_name="highlighted_diff.pdf")

