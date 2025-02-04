# IMPORTS
import streamlit as st
from components.sidebar import sidebar_component_render
from functions.generate_password import generate_password
from functions.password_security_functions.score_colour_hex_codes import score_colour_links
import pyperclip
import html

st.set_page_config(layout="wide")

# Content for the navigation
sidebar_component_render()

st.title("Generator")

col1, col2 = st.columns(2)

# Initialize placeholders for password and score
password_placeholder = st.empty()
score_placeholder = st.empty()

with col1:
    # Create styled containers for password and score display
    password_container = st.container()
    score_container = st.container()

    # Buttons
    regenerate_password = st.button("Regenerate password", icon=":material/replay:", type="primary", use_container_width=True)

with col2:
    # Inputs for criteria
    length_criteria = st.number_input("Password length", min_value=4, max_value=20, value=8)
    upper_case_criteria = st.checkbox("Include upper case letters (A - Z)", value=True)
    lower_case_criteria = st.checkbox("Include lower case letters (a - z)", value=True)
    numbers_criteria = st.checkbox("Include numbers (0 - 9)", value=True)
    special_characters_criteria = st.checkbox("Include special characters (@ £ ! # %)", value=True)
    st.write("Click the regenerate password button to initially generate your password!")

# Logic for generating password and updating the design


# Inside the regenerate_password button logic:
if regenerate_password:
    result = generate_password(length_criteria, upper_case_criteria, lower_case_criteria, numbers_criteria, special_characters_criteria)
    password = result[0]
    score = result[1][4]
    background_color = score_colour_links[score]

    pyperclip.copy(password)
    st.toast("Copied to clipboard!", icon=":material/check_circle:")

    escaped_password = html.escape(password)

    with password_container:
        st.markdown(
            f"""
            <div style="
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                border-radius: 10px;
                padding: 1rem;
                border: 2px solid #ddd;
                margin-bottom: 1rem;
            ">
                <h2 style="margin: 0; font-size: 2rem; color: white;">{escaped_password}</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )


    # Update score display
    with score_container:
        st.markdown(
            f"""
            <div style="
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                background-color: {background_color};
                border-radius: 10px;
                padding: 1rem;
                margin-bottom: 1rem;
            ">
                <p style="margin: 0; font-size: 2rem; color: white; font-weight: 500;">{score}%</p>
            </div>
            """,
            unsafe_allow_html=True,
        )