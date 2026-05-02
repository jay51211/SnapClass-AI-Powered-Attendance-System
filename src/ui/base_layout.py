import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: #09090E !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#151522 !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    border: 1px solid #00F0FF33 !important;
                    box-shadow: 0px 0px 20px #00F0FF11 !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: #09090E !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
                color: #00F0FF !important;
                text-shadow: 0px 0px 10px #00F0FF44 !important;
            }
                

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
                color: #FF0055 !important;
                text-shadow: 0px 0px 10px #FF005544 !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
                color: #E2E8F0 !important;
            }
                

            button{
                border-radius: 1.5rem !important;
                background-color: #00F0FF !important;
                color: #09090E !important;
                padding: 10px 20px !important;
                border: none !important;
                box-shadow: 0px 0px 15px #00F0FF66 !important;
                transition: transform 0.25s ease-in-out !important;
                font-weight: bold !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #FF0055 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                box-shadow: 0px 0px 15px #FF005566 !important;
                transition: transform 0.25s ease-in-out !important;
                font-weight: bold !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: transparent !important;
                color: #00F0FF !important;
                padding: 10px 20px !important;
                border: 1px solid #00F0FF !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button:hover{
                transform :scale(1.05)}
        </style>  

                """
            ,unsafe_allow_html=True)