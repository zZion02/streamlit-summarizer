import streamlit as st
from transformers import pipeline

#Load summarization model(download on first run)
summarizer = pipeline("summarization")

#Streamlit app UI
st.title("Text Summarizer ✏️")

st.write("Paste your text below and click **Summarize**")

#Text input
inputtext = st.text_area("Enter your text here:", height=300)

#Summarize button
if st.button("Summarize"):
    if input_text:
        with st.spinner("Summarizing"):
            summary = summarizer(inputtext, max_length=130, min_length=30, do_sample=False)
            st.subheader("Summary")
            st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter your text")
    
