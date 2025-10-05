from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.9)

st.header("Research tool ")

paper_input = st.selectbox("select the paper", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("select the style", ["Explain like I'm 5", "Technical Explanation", "Use Analogies", "Provide Examples"])

length_input = st.selectbox("select the length", ["Short (1-2 sentences)", "Medium (1-2 paragraphs)", "Long (1-2 pages)"])

template = load_prompt('template.json')

if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(result.content)

