import streamlit as st
import numpy as np
from PIL import Image
from PIL import ImageOps
from keras.models import load_model
import os
os.environ['TF_ENABLE_ONEDNN_OPTS']='0'


model=load_model('kidney_project.h5')
classes=['Normal', 'Stone', 'Tumor', 'Cyst']


def predict(image):
    img=Image.open(image)
    img=img.resize((150,150))
    img=ImageOps.grayscale(img)
    img_array = np.array(img)
    img_array = img_array.reshape((1,150, 150, 1))
    prediction=model.predict(img_array)
    predicted_class=np.argmax(prediction)
    return classes[predicted_class]

#st.title("KIDNEY CONDITION DIAGNOSIS")
st.write("<h1 style='text-align: center; color: violet;'>KIDNEY CONDITION DIAGNOSIS</h1>", unsafe_allow_html=True)
img=Image.open('kidney imag.jpg')
st.image(img,width=600)

on=st.toggle(":blue[About Kidney]")
if on:

    st.markdown("_A healthy kidney performs vital functions such as filtering waste products from the blood, "
                "regulating electrolyte balance, and maintaining fluid balance."
                "It is roughly the size of a fist and has a smooth, bean-shaped appearance._")

    st.write(':green[1.Cyst]: Renal cysts are fluid-filled sacs that can develop in the kidneys.')
    st.write(':green[2.Tumor]: Kidney tumors can be either benign (non-cancerous) or malignant (cancerous).')
    st.write(':green[3.Stone]: Kidney stones are hard deposits of minerals and salts that form in the kidneys. ')
    st.write(':green[4.Normal]: kidney should function without causing any significant symptoms or complications.')
    st.markdown("Visit [Google Colab](https://colab.research.google.com/drive/19J0YJWmgk3xbqFBPUoeT9YL6Fhh02fMb#scrollTo=jDtRbWxnT02P)")


uploaded_file=st.file_uploader("Choose an image.......",type=['png','jpg','jpeg'])
if uploaded_file is not None:
    st.write("Classifying.......:point_down:")
    class_name = predict(uploaded_file)
    st.markdown(f'<span style="color:blue; font-size:30px;"><b>{class_name}</b></span>', unsafe_allow_html=True)
    if class_name == "Normal":
        st.write("A Healthy kidney")
    elif class_name == "Stone":
        st.write(' A solid crystals form your kidneys from substances in the urine.')
    elif class_name == "Tumor":
        st.write('An abnormal growth of cells seen in your kidney')
    else:
        st.write('A fluid-filled sac that develops in your kidney')