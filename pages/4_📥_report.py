import streamlit as st
import os
from pandas import Series
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

st.set_page_config(page_title="Report", page_icon="📥")

st.markdown("# Report")
st.sidebar.header("Report")


class InputMethod:
    @staticmethod
    def gdrive():
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)

        path = "/home/lungsang/Desktop/levelpack-UI/content/A0/1 docx-raw/"
        folder = "1tuQxaiDOdbfv1JHXNAln2nbq1IvBOrmP"

        file_list = drive.ListFile({'q': f"'{folder}' in parents and trashed=false"}).GetList()
        if st.checkbox("Show file list?", True):
            for index, file in enumerate(file_list):
                st.write(index + 1, file['title'])
                file.GetContentFile(path + file['title'])

    @staticmethod
    def local():
        st.download_button(
            label="Download report here",
            file_name='large_df.csv',
            mime='text/csv',
            data='csv'
        )


options = {'download to computer': InputMethod.local, 'upload to google drive': InputMethod.gdrive}
selection = st.radio('Select page', Series(options.keys()))
options[selection]()
hide_streamlit_style = """
<style>
#MainMenu{visibility:hidden}
footer{visibility:hidden}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
