<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://ireneburresi-fake-news-classifier-app-loquc2.streamlitapp.com">
    <img src="./assets/icona-news.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">FAKE NEWS CLASSIFIER</h3>

  <p align="center">
   A simple web app to classify news articles
    <br />
    <a href="https://ireneburresi-fake-news-classifier-app-loquc2.streamlitapp.com"><strong> View demo »</strong></a>
    <br />
    <br />
    <a href="#about-this-project">About this project</a>
    ·
    <a href="#built-with">Built With</a>
    ·
    <a href="#getting-started">Getting started</a>
    ·
    <a href="#contact">Contact me</a>
  </p>
</div>

[screen]: ./assets/screen.png

<!-- ABOUT THE PROJECT -->
## About this project

[![Fake news classifier][screen]](https://ireneburresi-fake-news-classifier-app-loquc2.streamlitapp.com)

This project analyses a dataset containing 44898 samples of real and fake news articles. 

In the Jupyter Notebook the dataset is:
1. loaded
2. cleaned and prepared for data visualisation
3. prepared for ML model training

Then some different ML models are trained and evaluated on the training test. The final chosen model is Naive Bayes.
The web app is deployed using Streamlit (at https://ireneburresi-fake-news-classifier-app-loquc2.streamlitapp.com).

### Built With

This project is built in:
<div align="center">

[![Python][Python-shield]][Python-url]
</div>


The analysis and model training is done in:

<div align="center">

[![Jupyter][Jupyter-shield]][Jupyter-url]

</div>

Powered by:
<div align="center">

[![Colab][Colab-shield]][Colab-url]

</div>

Deployed with:
<div align="center">
  
[![Streamlit][Streamlit-shield]][Streamlit-url]
  
</div>


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Create a conda environment
```
 conda create -p venv python==3.7 -y
```
Activate conda environement
```
conda activate venv
```
Install requirements.txt file using below command
```
pip install -r requirements.txt
```


### Download

After the download, simply unzip the directory and then move to the project directory. To open the app in streamlit:
```
streamlit run app.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact
You can find me at:
burresi.irene@icloud.com - Irene Burresi

Have a look at my personal resume site here

<p align="right">(<a href="#readme-top">back to top</a>)</p>



[Python-shield]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://www.python.org
[NumPy-shield]: https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white
[NumPy-url]: https://numpy.org
[Pandas-shield]: https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org
[Plotly-shield]: https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white
[Plotly-url]: https://pandas.pydata.org
[PyTorch-shield]: https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white
[PyTorch-url]: https://pytorch.org
[SciPy-shield]: https://img.shields.io/badge/SciPy-654FF0?style=for-the-badge&logo=SciPy&logoColor=white
[SciPy-url]: https://scipy.org
[Streamlit-shield]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white
[Streamlit-url]: https://streamlit.io
[Tensorflow-shield]: https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white
[Tensorflow-url]: https://www.tensorflow.org
[MacOS-shield]: https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=apple&logoColor=white
[Linkedin-shield]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[Linkedin-url]: https://www.linkedin.com/in/ireneburresi/
[Kaggle-shield]: https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white
[Jupyter-shield]:	https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white
[Jupyter-url]: https://jupyter.org
[PowerBI-shield]: https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=Power%20BI&logoColor=white
[Colab-shield]: https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252
[Colab-url]: https://colab.research.google.com
[PyCharm-shield]: https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white
[Tableau-shield]: https://img.shields.io/static/v1?style=for-the-badge&message=Tableau&color=E97627&logo=Tableau&logoColor=FFFFFF&label=
[Tableau-url]: https://www.tableau.com
