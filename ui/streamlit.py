import streamlit as st


def st_maximize_space():
    st.set_page_config(page_title="Complexity viewer", layout="wide", menu_items=None)
    st.markdown("""
        <style>
            .block-container {
                padding-top: 1rem;
                padding-bottom: 0rem;
            }
        </style>
        """, unsafe_allow_html=True)
