import streamlit as st
from options import options
from templates import *

st.set_page_config(page_title="Revport XML Loader Generator")
st.title("Revport XML Loader Generator")

# Dropdown Section
selection = st.selectbox("Choose Loader Type", options)

