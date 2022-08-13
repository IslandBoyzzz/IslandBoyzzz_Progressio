
from PIL import Image
import requests 
import streamlit as st
from streamlit_lottie import st_lottie




st.set_page_config(page_title = "My webpage", page_icon = ":tada:", layout = "wide")






def load_lottieurl2(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

local_css("style/style.css")
lottie_animation = load_lottieurl2("https://assets4.lottiefiles.com/packages/lf20_ljotbiif.json")
image_contact_form = Image.open("Images/IMG_2464.jpg")

with st.container():
    st.subheader("Helllo, we are the ISLANDDDDD BOYZZZZZZ")
    st.title("WELCOME TO OUR PROJECT")
    st.write("Done by - Siddharth, Parth, aashish and Aditya ")
    #st.write("[Learn more >](https:/mygiis.org)")#

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About us?")
        st.write("##")
        st.write("We are just kids just trying to have fun without passing out from stress of IB ")
    with right_column:
        st_lottie(lottie_animation, height = 300, key="climate change")


with st.container():
    st.write("---")
    st.header("Photos")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
         st.image(image_contact_form)
    with text_column:
        st.subheader("ITS US ")
        st.write("ISLANDDDD BOYZZZZZZ")
        
with st.container():
    st.write("---")
    st.header("Get in touch with us")
    st.write("##")

    contact_form = """ 
        <form action="https://formsubmit.co/siddothekiddo12345@gmail.com" method="POST">
            <input type ="hidden" name = "_captcha" value ="false">
            <input type="text" name="name" placeholder ="Your Name" required>
            <input type="email" name="email" placeholder ="Your email" required>
            <textarea name ="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form> """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html = True)
    with right_column:
        st.empty()