import streamlit as st
def style_base_home():
    st.markdown("""
      <style>
            .stApp {
             background : #5865f2; important;
             }
            .stApp div[data-testid="stColumn"] {
                background-color: #f5f5f5 !important;
                padding: 2.5rem !important;
                border-radius: 5rem !important;
                }

      </style>
""",unsafe_allow_html=True)
def style_base_dashboard():
    st.markdown("""
      <style>
             .stApp {
             background : #E0E3FF; important;
             }


      </style>
""",unsafe_allow_html=True)
def style_base_layout():
    st.markdown("""
        <style>
                    
        /* Imports MUST be at the top of the CSS string */
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');
         /* Hide Top Bar of streamlit*/
            
            #MainMenu,header,footer
                {
                visibility: hidden !important;
                }
                .stApp {
                            background : #E6E6FA; important;
                 }
                .block-container {
                    padding-top: 1.5rem !important;
                }
                h1{
                    font-family: 'Climate Crisis', sans-serif ! important;
                    font-size: 3.5rem !important;
                    
                    line-height: 1.1 !important;
                    margin-bottom: 0rem ! important;
                }
                h2{
                    font-family: 'Climate Crisis', sans-serif ! important;
                    font-size: 2rem !important;
                    line-height: 0.9 !important;
                    margin-bottom: 0rem ! important;
                    color: #323232 !important;
                }
                h3, h4, p{
                    font-family: 'Outfit', sans-serif ;
                    
                }
                /* Primary Button */
                button[kind="primary"], 
                button[kind="primary"]:hover, 
                button[kind="primary"]:focus {
                    border-radius: 1.5rem !important;
                    background-color: #5865F2 !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;    
                }
                /* Secondary Button (Fixed case-sensitivity and state overrides) */
                button[kind="secondary"], 
                button[kind="secondary"]:hover, 
                button[kind="secondary"]:focus {
                    border-radius: 1.5rem !important;
                    background-color: #EB459E !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }
                /* Tertiary Button */
                button[kind="tertiary"], 
                button[kind="tertiary"]:hover, 
                button[kind="tertiary"]:focus {
                    border-radius: 1.5rem !important;
                    background-color: black !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }
                button:hover {
                    transform: scale(1.05) !important;
                }

        </style>
                  """
                ,unsafe_allow_html=True)    
def style_base_layout2():
    st.markdown("""
        <style>
                    
        /* Imports MUST be at the top of the CSS string */
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');
         /* Hide Top Bar of streamlit*/
            
            #MainMenu,header,footer
                {
                visibility: hidden !important;
                }
                .stApp {
                            background : #E6E6FA; important;
                 }
                .block-container {
                    padding-top: 1.5rem !important;
                }
                h1{
                    font-family: 'Climate Crisis', sans-serif ! important;
                    font-size: 3.5rem !important;
                    
                    line-height: 1.1 !important;
                    margin-bottom: 0rem ! important;
                }
                h2{
                    font-family: 'Climate Crisis', sans-serif ! important;
                    font-size: 2rem !important;
                    line-height: 0.9 !important;
                    margin-bottom: 0rem ! important;
                    color: #5865F2 !important;
                }
                h3{
                    font-family: 'Climate Crisis', sans-serif ! important;
                    font-size: 2rem !important;
                    line-height: 0.9 !important;
                    margin-bottom: 0rem ! important;
                    color: #323232 !important;
                    
                }
                h4, p{
                     font-family: 'Outfit', sans-serif ;
                     color: #323232 !important;
                }
                /* Primary Button */
                button[kind="primary"], 
                button[kind="primary"]:hover, 
                button[kind="primary"]:focus {
                    border-radius: 1.5rem !important;
                    background-color: #5865F2 !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;    
                }
                /* Secondary Button (Fixed case-sensitivity and state overrides) */
                button[kind="secondary"], 
                button[kind="secondary"]:hover, 
                button[kind="secondary"]:focus {
                    border-radius: 1.5rem !important;
                    background-color: #EB459E !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }
                /* Tertiary Button */
                button[kind="tertiary"], 
                button[kind="tertiary"]:hover, 
                button[kind="tertiary"]:focus {
                    border-radius: 1.5rem !important;
                    background-color: black !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }
                button:hover {
                    transform: scale(1.05) !important;
                }

        </style>
                  """
                ,unsafe_allow_html=True)   
def style_base_layout3():
    st.markdown("""
        <style>
                    
        /* Imports MUST be at the top of the CSS string */
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');
         /* Hide Top Bar of streamlit*/
            
            #MainMenu,header,footer
                {
                visibility: hidden !important;
                }
                .stApp {
                            background : #E6E6FA; important;
                 }
                .block-container {
                    padding-top: 1.5rem !important;
                }
                h1{
                    font-family: 'Climate Crisis', sans-serif ! important;
                    font-size: 3.5rem !important;
                    
                    line-height: 1.1 !important;
                    margin-bottom: 0rem ! important;
                }
                h2{
                    font-family: 'Climate Crisis', sans-serif ! important;
                    font-size: 2rem !important;
                    line-height: 0.9 !important;
                    margin-bottom: 0rem ! important;
                    color: blue !important;
                }
                h3{
                    font-family: 'Climate Crisis', sans-serif ! important;
                    font-size: 2rem !important;
                    line-height: 0.9 !important;
                    margin-bottom: 0rem ! important;
                    color: blue !important;
                    
                }
                h4, p{
                     font-family: 'Outfit', sans-serif ;
                     color: white !important;
                }
                /* Primary Button */
                button[kind="primary"], 
                button[kind="primary"]:hover, 
                button[kind="primary"]:focus {
                    border-radius: 1.5rem !important;
                    background-color: #5865F2 !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;    
                }
                /* Secondary Button (Fixed case-sensitivity and state overrides) */
                button[kind="secondary"], 
                button[kind="secondary"]:hover, 
                button[kind="secondary"]:focus {
                    border-radius: 1.5rem !important;
                    background-color: #EB459E !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }
                /* Tertiary Button */
                button[kind="tertiary"], 
                button[kind="tertiary"]:hover, 
                button[kind="tertiary"]:focus {
                    border-radius: 1.5rem !important;
                    background-color: black !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }
                button:hover {
                    transform: scale(1.05) !important;
                }

        </style>
                  """
                ,unsafe_allow_html=True)   