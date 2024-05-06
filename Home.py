import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="",
)


def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://static.vecteezy.com/system/resources/thumbnails/005/256/397/small/leaf-icon-logo-template-used-for-environment-and-plants-free-vector.jpg);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
                margin-left: 10px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "Dhanvantari";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


add_logo()

st.write("# Welcome to Dhanvantri!")
st.write("# ")

st.markdown(
    """


    This application is used to identify different Medicinal Plants/Raw materials through
     Image Processing Using Machine Learning Algorithms.

    ### This Application is useful for :
    - Researchers
    - Herbalists
    - Wholesalers, Distributors and General Public
    ### How can you use this application?
    - Upload a file from your device locally.
    - Take an image using your camera.
"""
)