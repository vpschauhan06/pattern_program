import streamlit as st
from datetime import *
from PIL import Image
img=Image.open('IMG_20230107_232922_505.jpg')
page_title='HAPPY BIRTHDAY AARU'
page_icon=':cake:'
layout='centered'
Partner='Vinu'
st.set_page_config(page_title=page_title,page_icon=page_icon,layout=layout)
st.title(page_title+" "+page_icon)
st.image(img)
st.header('To Love of My Life: Aarti Gola :heart:')
st.text('My dear girlfriend, you are the single most incredible person I know ')
st.text('and I am so lucky and grateful to have you in my life. ')
st.text('Nobody even comes close to how kind, thoughtful and caring you are.')
st.text('You could’ve chosen anybody to share your life with and I am so ')
st.text('thankful that you chose me!')
st.text('Wishing you the very happiest birthday Aaru with all my love and lots of big kisses!')
st.text('I Love You So Much AARU')
st.header(':heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart:')

'------'
from playsound import playsound
playsound('Birthday.mp3')