from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Webpage",page_icon=":tada:",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# use locall csss
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
local_css("style/style.css")
    
# LOAD ASSETS(upload json file here)
lottie_coding = "https://lottie.host/5ab081e6-15ef-4a2a-b845-ac9379d386ef/M8DQ2gO1CK.json"
img_contact_form = Image.open("images/I1.png")
img_lottie_animation = Image.open("images/I2.png")
# HEADER SECTION
with st.container():
    st.subheader("Hi , I am Yash Aggarwal")
    st.title("A B.Tech Student at VGU Jaipur")
    st.write("I am passionate about learning and builting new techs. Everyday !")
    st.write("[Know More >](www.linkedin.com/in/yash-aggarwal-183741359)")

# What I Do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        st.write("##")
        st.write(
            """
            I'm Yash Aggarwal, a dedicated engineering student with a strong interest in technology, 
            software development, and practical problem-solving. I focus on building efficient,
            user-centric digital solutions and continuously work on enhancing my technical skills 
            through hands-on projects and learning. With a disciplined approach and a commitment to growth,
            
            I aim to contribute to impactful technical work and develop solutions that create real value.
            """
        )
        st.write("[Know More >](www.linkedin.com/in/yash-aggarwal-183741359)")

    with right_column:
        st_lottie(lottie_coding, height=350, key="coding")

# PROJECTS
with st.container():
    st.write("---")
    st.header("MY PROJECTS 📽️")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("PROJECT 1️⃣")
        st.write(
            """
                Project discription here
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=hEPoto5xp3k&pp=ugUEEgJlbg%3D%3D)")
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Enter Project 2")
        st.write(
            """
                Project discription here
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=hEPoto5xp3k&pp=ugUEEgJlbg%3D%3D)")
    

    











 # contact 
with st.container():
    st.write("---")
    st.header("Get In Touch with me!")
    # st.write("##")  

    contact_form = """
    <form action="https://formsubmit.co/yashaggarwal668@gmail.com" method="POST">
     <import type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
""" 
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()