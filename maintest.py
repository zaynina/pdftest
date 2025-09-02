import streamlit as st

def main():
    st.set_page_config(page_title="Main Page", page_icon="🏠")

# Custom title with different font and color using HTML and CSS
    st.markdown(
        """
        <h1 style='font-family: "Junge", Courier, monospace; color: #ocean;'>
            Welcome to My Website
        </h1>
        """,
        unsafe_allow_html=True
    )


    st.write("This is the main page of the website.")
    st.write("Feel free to explore and customize it!")


    st.markdown("© 2024 My Website")

if __name__ == "__main__":
    main()
