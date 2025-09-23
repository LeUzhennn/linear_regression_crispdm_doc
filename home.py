import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

st.title("Welcome!")
st.sidebar.success("Select a page above.")

st.markdown(
    """
    This is the home page of your multipage Streamlit app.
    Navigate to other pages using the sidebar.
    """
)
