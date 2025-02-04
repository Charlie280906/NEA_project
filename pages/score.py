# IMPORTS
import streamlit as st
from components.password_container import password_container_component_render
from functions.user_info_functions.pass_user_data import pass_user_data
from functions.user_info_functions.load_user_stats import load_user_stats
from components.sidebar import sidebar_component_render
from streamlit_extras.stylable_container import stylable_container
from functions.password_security_functions.score_colour_hex_codes import score_colour_links

def score_page():

    user_data = pass_user_data()
    user_stats = user_data["user_stats"]

    st.set_page_config(layout="wide")

    #content for the navigation
    sidebar_component_render()


    st.title("Score")

    score_container = st.container()
    background_color = score_colour_links[user_stats["average"]]
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
            ">
                <p style="margin: 0; font-size: 3rem; color: white; font-weight: 600;">{str(user_stats["average"])}%</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container():
            with stylable_container(
            key="centre_text",
            css_styles="""
            div {
                display: flex;
                align-items: center;
                justify-content: center;
            }
            """,
            ):
                st.subheader(str(user_stats["weak"]) + " weak passwords")

            for password_dict in user_data["user_passwords"]:
                if "weak" in password_dict["security_fields"]:
                    password_container_component_render(password_dict, "score_page_weak")

    with col2:
        with st.container():
            with stylable_container(
            key="centre_text",
            css_styles="""
            div {
                display: flex;
                align-items: center;
                justify-content: center;
            }
            """,
            ):
                st.subheader(str(user_stats["reused"]) + " reused passwords")

            for password_dict in user_data["user_passwords"]:
                    if "reused" in password_dict["security_fields"]:
                        password_container_component_render(password_dict, "score_page_reused")

    with col3:
        with st.container():
            with stylable_container(
            key="centre_text",
            css_styles="""
            div {
                display: flex;
                align-items: center;
                justify-content: center;
            }
            """,
            ):
                st.subheader(str(user_stats["compromised"]) + " at risk passwords")

            for password_dict in user_data["user_passwords"]:
                if "compromised" in password_dict["security_fields"]:
                    password_container_component_render(password_dict, "score_page_compromised")

    # when clicking on password, can redirect to home page, enter search for just that password, then open the expanded view

score_page()