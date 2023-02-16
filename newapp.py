import streamlit as st
from datetime import *
from PIL import Image
img=Image.open('IMG_20230107_232922_505.jpg')
page_title='HAPPY BIRTHDAY AARU'
page_icon=':cake:'
layout='centered'
st.set_page_config(page_title=page_title,page_icon=page_icon,layout=layout)
st.title(page_title+" "+page_icon)
st.image(img)