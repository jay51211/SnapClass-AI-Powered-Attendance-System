import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: #F8F9FA !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#FFFFFF !important;
                    padding:2.5rem !important;
                    border-radius: 1rem !important;
                    border: 1px solid #DEE2E6 !important;
                    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.05) !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: #F8F9FA !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Playfair Display', serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
                color: #2C3E50 !important;
                text-shadow: none !important;
            }
                

            h2 {
                font-family: 'Playfair Display', serif !important;
                font-size: 2rem !important;
                line-height:1.2 !important;
                margin-bottom:0rem !important;
                color: #34495E !important;
                text-shadow: none !important;
            }
                
            h3, h4, p {
                font-family: 'Lato', sans-serif;    
                color: #495057 !important;
            }
                

            button{
                border-radius: 0.5rem !important;
                background-color: #FFF3CD !important;
                color: #212529 !important;
                padding: 10px 20px !important;
                border: none !important;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.05) !important;
                transition: transform 0.25s ease-in-out !important;
                font-weight: bold !important;
                }

            button p {
                color: #212529 !important;
            }

            button[kind="secondary"]{
                border-radius: 0.5rem !important;
                background-color: #D1E7DD !important;
                color: #212529 !important;
                padding: 10px 20px !important;
                border: none !important;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.05) !important;
                transition: transform 0.25s ease-in-out !important;
                font-weight: bold !important;
                }

            button[kind="secondary"] p {
                color: #212529 !important;
            }

            button[kind="tertiary"]{
                border-radius: 0.5rem !important;
                background-color: transparent !important;
                color: #212529 !important;
                padding: 10px 20px !important;
                border: 1px solid #212529 !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"] p {
                color: #212529 !important;
            }

            button:hover{
                transform :scale(1.05)}
        </style>  

                """
            ,unsafe_allow_html=True)
