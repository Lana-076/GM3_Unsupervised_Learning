"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
from PIL import Image

# Data handling dependencies
import pandas as pd
import numpy as np
import base64

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')


# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Exploratory Data Analysis","Solution Overview", "About/Contact Us"]
    

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------

        
        logo = Image.open('resources/imgs/team/logo.png')
        st.sidebar.image(logo, use_column_width=True)

        
    if page_selection == "Solution Overview":
        logo = Image.open('resources/imgs/team/logo.png')
        st.sidebar.image(logo, use_column_width=True)
        # Background of the app
        st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://github.com/Orion316/mypackage/blob/master/SolutionOverview.jpeg?raw=true");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
        st.title("Solution Overview")
        st.markdown("![Alt Text](https://cdn.dribbble.com/users/31818/screenshots/1891002/math.gif)")

        st.write("There were two sections to this predict and both sections had content based and collaborative filtering. The content based filtering showed good signs of predicting a rating but needed way more computing power to make predict ratings on massive dataset. Therefore was hard to evaluate if the predictor was accurate")
        st.subheader("What can be done differently next time")

        st.write("The use of metrics such as hit rate, coverage and diversity would be taken into account, this will help evaluating how well the recommendation systems perform. Adjusting the threshold of the long-tail distribution so that movies that are not popular but fit users criteria could be recommended instead of just popular movies.")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.

    # ------------- EDA Section of the App -------------------
    if page_selection == "Exploratory Data Analysis":
        logo = Image.open('resources/imgs/team/logo.png')
        st.sidebar.image(logo, use_column_width=True)
        # Background of the app
        st.markdown(
                f"""
                <style>
                .stApp {{
                    background: url("https://github.com/Orion316/mypackage/blob/master/eda.png?raw=true");
                    background-size: cover
                }}
                </style>
                """,
                unsafe_allow_html=True
            )

        st.title("Exploratory Data Analysis")
        st.write("Exploratory data analysis is an approach to analyzing data sets to summarize their main characteristics, often with visual methods. EDA is the critical process of performing initial investigations on data to discover patterns, to spot anomalies, to test hypothesis and to check assumptions with the help of summary statistics and graphical representations. A statistical model can be used or not, but primarily EDA is for seeing what the data can tell us beyond the formal modelling or hypothesis testing task. It is a good practice to understand the data first and try to gather as many insights from it. EDA is all about making sense of data in hand, before getting them dirty with it, which will be done below. Pandas dataframe.info() function is used to get a concise summary of the dataframe. It comes really handy when doing exploratory analysis of the data")
        st.title("Count of Ratings")
        st.image('resources/imgs/EDA/1.png',use_column_width=True)
        st.title("Movies Duration Bar Graph")
        st.image('resources/imgs/EDA/2.png',use_column_width=True)
        st.title("Density Plot for the Ratings")
        st.image('resources/imgs/EDA/3.png',use_column_width=True)
        st.title("Yearly Analysis of Movies")
        st.image('resources/imgs/EDA/4.png',use_column_width=True)
        


    # ------------- Model Section of the App -------------------
    if page_selection == "About/Contact Us":
        logo = Image.open('resources/imgs/team/logo.png')
        st.sidebar.image(logo, use_column_width=True)

        st.title("About/Contact Us")
	    #st.markdown("Solid Solutions is an innovation tech company with a key focus on creating up to date technological products designed to make light of any problem thrown our way. We are extremely passionate about giving back to the community. Strengthening Today for a Stronger Tomorrow!")
		# You can read a markdown file from supporting resources folder

        col1, col2, col3, col4 = st.columns(4)
        img1 = Image.open("resources/imgs/team/Katlego.jpeg")
        img2 = Image.open("resources/imgs/team/Aphiwe.jpeg")
        img3 = Image.open("resources/imgs/team/Nomfundo.jpeg")
        img4 = Image.open("resources/imgs/team/me.jpeg")

        with col1: 
            st.caption("CEO")
            st.image(img1)
            st.caption("Tholwana Katleho Lebona")

        with col2: 
            st.caption("Market Technologist")
            st.image(img2)
            st.caption("Aphiwe Rasisemula")

        with col3: 
            st.caption("UI/UX Designer")
            st.image(img3)
            st.caption("Nomfundo Mbambo")

        with col4: 
            st.caption("Full-stack Developer")
            st.image(img4)
            st.caption("Morema Moloisi")


        st.subheader("Message Us")
        with st.form("form", clear_on_submit=True):
            name = st.text_input("Enter Full Name")
            email = st.text_input("Enter Email Address")
            message = st.text_area("Message")

            submit = st.form_submit_button("Submit")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Address")
            img = Image.open("resources/imgs/team/map.png")
            st.image(img)
            st.markdown("137 Saisy")
            st.markdown("Johannesburg, Sandton")
            st.markdown("2196")

        with col2:
            st.subheader("Phone")
            st.markdown("Monday - Friday")
            st.markdown("08h00 - 17h00 GMT+2")
            st.markdown("(+27) 021 554 1091")
            st.markdown("(+27) 081 579 4965")

        with col3:
            st.subheader("Email")
            st.markdown("katleho@datagernalist.com")
            st.markdown("morema@datagernalist.com")


        st.markdown(
                f"""
                <style>
                .stApp {{
                    background: url("https://github.com/Orion316/mypackage/blob/master/work.jpeg?raw=true");
                    background-size: cover
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
        



    


    
# Background of the app
st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://github.com/Orion316/mypackage/blob/master/Background.png?raw=true");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

if __name__ == '__main__':
    main()
