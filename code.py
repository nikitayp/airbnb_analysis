# Importing Libraries
import pandas as pd
import pymongo
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image

# Setting up page configuration
icon = Image.open("ICN.png")
st.set_page_config(page_title= "Airbnb Data Visualization | By Nikita Y P",
                   page_icon= icon,
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# This dashboard app is created by *Nikita Y P*!
                                        Data has been gathered from mongodb atlas"""}
                  )

# Creating option menu in the side bar
with st.sidebar:
    selected = option_menu("Menu", ["Home","Overview","Explore"], 
                           icons=["house","graph-up-arrow","bar-chart-line"],
                           menu_icon= "menu-button-wide",
                           default_index=0,
                           styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "#FF5A5F"},
                                   "nav-link-selected": {"background-color": "#FF5A5F"}}
                          )

# CREATING CONNECTION WITH MONGODB ATLAS AND RETRIEVING THE DATA
client = pymongo.MongoClient("Enter your connection string")
db = client.sample_airbnb
col = db.listingsAndReviews



