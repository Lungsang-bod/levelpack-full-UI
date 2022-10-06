import streamlit as st
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pandas import Series

st.set_page_config(page_title="Input Data", page_icon="📁")
st.subheader("Method of import 📁")
st.sidebar.header("Uploading")


class InputMethod:
    @staticmethod
    def gdrive():
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)

        path = "/home/ubuntu/levelpack-origina-UI/content/A0/1 docx-raw/"
        folder = "1kCrY4cyIhpH1N04-3VDrpDs4QT2v90B9"

        file_list = drive.ListFile({'q': f"'{folder}' in parents and trashed=false"}).GetList()
        if st.checkbox("Show file list?", True):
            for index, file in enumerate(file_list):
                st.write(index + 1, file['title'])
                file.GetContentFile(path + file['title'])

    @staticmethod
    def local():
        data_file = st.file_uploader("", type=["docx"])

        if data_file is not None:
            with open(os.path.join("/home/lungsang/Desktop/levelpack-UI/content/A0/1 docx-raw", data_file.name),
                      "wb") as f:
                f.write(data_file.getbuffer())

            st.success("File uploaded in content/A0/1 docx-raw")


options = {'upload from computer': InputMethod.local, 'upload from google drive': InputMethod.gdrive}
selection = st.radio('Select page', Series(options.keys()))
options[selection]()

st.button("Re-run")  # this button is not connected to any other logic, it just causes a plain rerun.

hide_streamlit_style = """
<style>
#MainMenu{visibility:hidden}
footer{visibility:hidden}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
