# ===========================================================================================================
#                                               FAKE NEWS CLASSIFIER
# ===========================================================================================================
import re
# ================================================= IMPORTS =================================================
from pathlib import Path
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import streamlit.components.v1 as components
import joblib


# ============================================== PATH SETTINGS ==============================================
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

# ============================================ GENERAL SETTINGS =============================================

# The title and icon showed on the browser tab
PAGE_TITLE = "Videogames Sales"
PAGE_ICON = ":wave:"

# Social media
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/ireneburresi",
    "GitHub": "https://github.com/IreneBurresi",
}

github_link = 'https://github.com/IreneBurresi'
github_image = 'https://img.icons8.com/ios-glyphs/30/000000/github.png'

linkedin_link = "https://www.linkedin.com/in/ireneburresi"
linkedin_image = "https://img.icons8.com/ios/30/000000/linkedin-2--v1.png"


# Method to show social media links as clickable images
def add_social_media_links():
    st.write('[![Github](' + github_image + ')](' + github_link + ')'
             + ' [![Linkedin](' + linkedin_image + ')](' + linkedin_link + ')')


# ================================================ WEBSITE =================================================
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Loading css
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# ------------------------------------------------- HEADER -------------------------------------------------
st.title("Videogames Sales")
st.write("By Irene Burresi")


# -------------------------------------------- NAVIGATION MENU ---------------------------------------------
selected = option_menu(
    menu_title=None,
    options=["Fake news classifier", "Data Visualisation"],
    #icons=["emoji-smile", "mortarboard", "code-slash", "paperclip"],
    orientation="horizontal",
)

# --------------------------------------------- FAKE PREDICTOR ---------------------------------------------
if selected == "Fake news classifier":
    st.subheader("Classifier")
    st.write("---")
    title = st.text_input("Title:", value="", max_chars=None, key=None, type="default", placeholder=None, disabled=False, label_visibility="visible")
    art_text = st.text_area("Paste the article here:", value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None,
                 abel_visibility="visible")

    to_classify = art_text + " " + title


    def text_cleaning(text):
        # Remove all numbers with letters attached to them
        text = re.sub('\w*\d\w*', ' ', text)
        # .lower() - convert all strings to lowercase
        text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text.lower())
        # Remove all '\n' in the string and replace it with a space
        text = re.sub("\n", " ", text)
        # Remove all non-ascii characters
        text = re.sub(r'[^\x00-\x7f]', r' ', text)
        return text

    to_classify = text_cleaning(to_classify)

    submit = st.button("Predict")
    if submit:
        data = {'Text': to_classify}
        features = pd.DataFrame(data, index=[0])
        classification = model.predict(features)[0]
        if classification == 1:
            str_clf = "fake"
        else: str_clf = "not fake"
        st.write("This news is " + str_clf)
elif selected == "Data Visualisation":
    st.write("### Pandas Profile")
    st.write("---")
    #st.markdown(source_code, unsafe_allow_html=True)
    components.html(source_code, height = 2000)


