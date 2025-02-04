# IMPORTS
from functions.user_info_functions.pass_user_data import pass_user_data
import streamlit as st
import pyperclip
import time
from functions.password_security_functions.score_colour_hex_codes import score_colour_links
from functions.database_functions.database_push_function import database_push_request
from functions.user_info_functions.load_user_passwords import load_user_passwords
from streamlit_js_eval import streamlit_js_eval
from functions.password_security_functions.changed_password import changed_password

def password_container_component_render(password_dict, reason, width="large"):

    user_data = pass_user_data()

    
    @st.dialog(password_dict["website_name"] + " password information", width="large")
    def password_popover():
        with st.container(border=1):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader("Username:")
                st.write(password_dict["password_username"])
                st.subheader("Password:")
                current_password_flag = "hidden"
                current_password = st.empty()
                current_password.subheader("*"*len(password_dict["password_password"]))
            with col2:
                st.subheader("")
                st.write("")
                st.subheader("")
                st.write("")
                st.subheader("")
                st.write("")
                view_password = st.button(label="View password", icon=":material/visibility:", key=str(password_dict["password_id"]) + "_view_button_1_" + reason)
            with col3:
                st.subheader("")
                st.write("")
                st.subheader("")
                st.write("")
                st.subheader("")
                st.write("")
                if st.button("Copy to clipboard", icon=":material/content_copy:", type="primary", key=str(password_dict["password_id"]) + "_copy_button_1_" + reason):
                    pyperclip.copy(password_dict["password_password"])
                    st.toast("Copied to clipboard!", icon=":material/check_circle:")

            if view_password:
                current_password.write(password_dict["password_password"])
                time.sleep(3)
                current_password.subheader("*"*len(password_dict["password_password"]))
                

        background_color = score_colour_links[password_dict["overall_score"]]
        with st.container(border=1):
            st.subheader("Password security:")
            with st.container():
                st.markdown(
                    f"""
                    <div style="
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        justify-content: center;
                        background-color: {background_color};
                        border-radius: 10px;
                        margin-bottom: 1rem;
                        width: 100%;
                    ">
                        <p style="margin: 0; font-size: 16px; color: white;">Score: {password_dict["overall_score"]}%</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            security_fields = password_dict["security_fields"].split(",")
            for i in range(0, len(security_fields)):
                security_fields[i] = security_fields[i].replace("'", "")
                security_fields[i] = security_fields[i].replace("[", "")
                security_fields[i] = security_fields[i].replace("]", "")

            print(security_fields)
            if security_fields == [""]:
                pass
            else:
                for i in security_fields:
                    with st.container():
                        st.markdown(
                            f"""
                            <div style="
                                display: flex;
                                flex-direction: column;
                                align-items: center;
                                justify-content: center;
                                background-color: #F7655F;
                                border-radius: 10px;
                                margin-bottom: 1rem;
                                width: 100%;
                            ">
                                <p style="margin: 0; font-size: 16px; color: white;">Security tag: {i}</p>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )




            if password_dict["overall_score"] < 75:

                improved_passwords = password_dict["improved_password"].split(",")
                for i in range(0, len(improved_passwords)):
                    improved_passwords[i] = improved_passwords[i].replace("'", "")
                    improved_passwords[i] = improved_passwords[i].replace("[", "")
                    improved_passwords[i] = improved_passwords[i].replace("]", "")

                col1, col2, col3 = st.columns(3)
                with col1:
                    improved_password = st.selectbox("New password suggestions:", improved_passwords, key=str(password_dict["password_id"]) + "_new_passwords_" + reason)
                with col2:
                    st.subheader("")
                    if st.button("Copy to clipboard", icon=":material/content_copy:", type="secondary", key=str(password_dict["password_id"]) + "_copy_button_2_" + reason):
                        pyperclip.copy(improved_password)
                        st.toast("Copied to clipboard!", icon=":material/check_circle:")
                with col3:
                    st.subheader("")
                    change_password = st.button("Change to password", icon=":material/thumb_up:", type="primary", key=str(password_dict["password_id"]) + "_change_button_1_" + reason)

                if change_password:
                    changed_password(improved_password, password_dict["password_id"])

            col1, col2 = st.columns(2)
            with col1:
                own_improved_password = st.text_input("Change password to something else:", type="password", key=str(password_dict["password_id"]) + "_own_new_passwords_" + reason)
            with col2:
                st.subheader("")
                own_change_password = st.button("Change to password", icon=":material/thumb_up:", type="primary", key=str(password_dict["password_id"]) + "_own_change_button_1_" + reason)

            
            if own_change_password:
                changed_password(own_improved_password, password_dict["password_id"])

                
            


    if "password_popover" not in st.session_state:
        if st.button(password_dict["website_name"], use_container_width=True, icon=":material/key:", key=str(password_dict["password_id"]) + "_title_button_1_" + reason):
            password_popover()