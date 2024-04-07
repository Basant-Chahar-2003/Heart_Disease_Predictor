import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os

from streamlit_extras.switch_page_button import switch_page



## Sidebar Settings

# from streamlit_option_menu import option_menu

# with st.sidebar:
#     selected = option_menu(
#                 menu_title='Main Menu',
#                 options = ['Home','Predict'],
#                 icons = ['house','book'],
#                 menu_icon='cast',
#                 default_index = 0,
#         )


## ======================================================================================= ##
## SITE TITLE

## Setting Page Title
st.set_page_config(
                ## Meaning that the sidebar is not opened when visiting the site
                initial_sidebar_state="collapsed",
                ## Page title in the tab
                page_title='Heart Disease Risk Prediction'
                )

## ======================================================================================= ##
## SITE CONFIGURATION

# Note: All the contents that is about the modification of the site settings, must also be copied to every pages.

## Remove the contents in the sidebar itself
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)


## Hide the expander itself. (sidebar)
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

## Hide the github icon on the right side in the deployed app
hide_github_icon = """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob, .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137, .viewerBadge_text__1JaDK{ display: none; } #MainMenu{ visibility: hidden; } footer { visibility: hidden; } header { visibility: hidden; }
    </style>
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)


## To remove the hamburger menu (this is in the right part of the site)
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


## ======================================================================================= ##
## SITE CONTENTS

## Creating a Container for multiple elements
title = st.container()
abstract = st.expander(label='Abstract',expanded=False)
predict = st.container()


## Writing text in the website

with title:
    st.title('Heart Disease Risk Prediction using Machine Learning Algorithms')
    # st.text()



if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

def callback():
    st.session_state.button_clicked = True

def go_back():
    st.session_state.button_clicked = False

with predict:
    if st.button('Begin Risk Assessment',on_click=callback) or st.session_state.button_clicked:
        st.write('**Medical Disclaimer:**')
        st.markdown('<div style="text-align: justify;">The contents of this website are not \
        intended to diagnose or treat any disease, or offer personal medical advice. \
        You should seek the advice of your physician or other qualified health provider\
        with any questions you may have regarding a medical condition. Never disregard \
        professional medical advice or delay in seeking it because of something you have\
        read on this website. </div>', unsafe_allow_html=True)
        st.write('')
        if st.button('Agree'):
            st.session_state.button_clicked = False
            switch_page("page_2")
        st.button('Disgree',on_click=go_back)









