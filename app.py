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
import string
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import joblib


# ============================================== PATH SETTINGS ==============================================
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

# ============================================ GENERAL SETTINGS =============================================

# The title and icon showed on the browser tab
PAGE_TITLE = "Fake News Classifier"
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
st.title("Fake news Classifier")
st.write("By Irene Burresi")


# -------------------------------------------- NAVIGATION MENU ---------------------------------------------
selected = option_menu(
    menu_title=None,
    options=["Fake news classifier", "Data Visualisation"],
    #icons=["emoji-smile", "mortarboard", "code-slash", "paperclip"],
    orientation="horizontal",
)

# --------------------------------------------- FAKE PREDICTOR ---------------------------------------------



model = joblib.load('model/nb_model.pkl')

fake_data = pd.read_csv("./data/Fake.csv")
true_data = pd.read_csv("./data/True.csv")
to_classify = "pippo"
if selected == "Fake news classifier":
    st.subheader("Classifier")
    st.write("---")
    st.write("Use sample articles:")
    col1, col2 = st.columns(2)
    with col1:
        preset_fake = st.button("Sample fake article")
    with col2:
        preset_true = st.button("Sample real article")
    aux_title = ""
    aux_text = ""

    if preset_fake:
        aux_article = fake_data.sample().iloc[0]
        aux_title = str(aux_article.title)
        aux_text = str(aux_article.text)
    if preset_true:
        aux_article = true_data.sample().iloc[0]
        aux_title = str(aux_article.title)
        aux_text = str(aux_article.text)

    st.write("Or try your own:")
    title = st.text_input("Paste the title here:", value=aux_title, max_chars=None)
    art_text = st.text_area("Paste the article here:", value=aux_text, height=None, max_chars=None, key=None, help=None)

    to_classify = art_text + " " + title

    stop = set(stopwords.words('english'))
    punctuation = list(string.punctuation)
    stop.update(punctuation)

    def remove_stopwords(text):
        final_text = []
        for i in text.split():
            if i.strip().lower() not in stop:
                final_text.append(i.strip())
        return " ".join(final_text)

    def text_cleaning(text):
        # Remove urls
        text = BeautifulSoup(text, "html.parser").get_text()
        text = re.sub('\[[^]]*\]', '', text)
        text = re.sub(r'http\S+', '', text)
        text = remove_stopwords(text)
        # .lower() - convert all strings to lowercase
        text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text.lower())
        # Remove all non-ascii characters
        text = re.sub(r'[^\x00-\x7f]', r' ', text)
        return text

    to_classify = text_cleaning(to_classify)
    data = [to_classify]
    df = pd.Series(data)
    if model.predict(df)[0] == 0:
        pippo = 0
        st.write("This news is fake")
    elif model.predict(df)[0] == 1:
        pippo = 1
        st.write("This news is not fake")

elif selected == "Data Visualisation":
    st.write("Coming soon")



