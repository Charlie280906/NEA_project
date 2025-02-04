# IMPORTS
import streamlit as st
from functions.user_info_functions.pass_user_data import pass_user_data
from functions.user_info_functions.load_user_stats import load_user_stats

def stats_bar_component_render():
    user_data = pass_user_data()
    user_stats = user_data["user_stats"]

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        with st.container(border=1):
            col1a, col2a = st.columns([1,2])
            with col1a:
                st.write(":material/lock:")
            with col2a:
                st.write(str(user_stats["total"]) + " total")
    with col2:
        with st.container(border=1):
            col1b, col2b = st.columns([1,2])
            with col1b:
                st.write(":material/warning:")
            with col2b:
                st.write(str(user_stats["weak"]) + " weak")
    with col3:
        with st.container(border=1):
            col1c, col2c = st.columns([1,2])
            with col1c:
                st.write(":material/replay:")
            with col2c:
                st.write(str(user_stats["reused"]) + " reused")
    with col4:
        with st.container(border=1):
            col1d, col2d = st.columns([1,2])
            with col1d:
                st.write(":material/bug_report:")
            with col2d:
                st.write(str(user_stats["compromised"]) + " at risk")
    with col5:
        with st.container(border=1):
            col1e, col2e = st.columns([1,2])
            with col1e:
                st.write(":material/speed:")
            with col2e:
                st.write(str(user_stats["average"]) + "% score")