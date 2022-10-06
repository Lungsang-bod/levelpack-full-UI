import os
import streamlit as st

# file explorer
filelist = []
folder_name01 = os.path.basename("/home/lungsang/Desktop/levelpack-UI/content/A0/1 docx-raw")  # for upload
for root, dirs, files0 in os.walk("/home/lungsang/Desktop/levelpack-UI/content/A0/1 docx-raw"):  # for download
    for file in files0:
        filename = os.path.join(file)
        filelist.append(filename)
    with st.expander("📁 1 docx-raw"):
        st.write(filelist)

filelist = []
folder_name02 = os.path.basename("/home/lungsang/Desktop/levelpack-UI/content/A0/2 docx-text-only")
for root, dirs, files1 in os.walk("/home/lungsang/Desktop/levelpack-UI/content/A0/2 docx-text-only"):
    for file in files1:
        filename = os.path.join(file)
        filelist.append(filename)
    with st.expander('📁 2 docx-text-only'):
        st.write(filelist)

filelist = []
folder_name03 = os.path.basename("/home/lungsang/Desktop/levelpack-UI/content/A0/3 to-segment")
for root, dirs, files2 in os.walk("/home/lungsang/Desktop/levelpack-UI/content/A0/3 to-segment"):
    for file in files2:
        filename = os.path.join(file)
        filelist.append(filename)
    with st.expander('📁 3 to-segment'):
        st.write(filelist)

filelist = []
folder_name04 = os.path.basename("/home/lungsang/Desktop/levelpack-UI/content/A0/4 segmented")
for root, dirs, files3 in os.walk("/home/lungsang/Desktop/levelpack-UI/content/A0/4 segmented"):
    for file in files3:
        filename = os.path.join(file)
        filelist.append(filename)
    with st.expander('📁 4 segmented'):
        st.write(filelist)

filelist = []
folder_name05 = os.path.basename("/home/lungsang/Desktop/levelpack-UI/content/A0/5 to-tag")
for root, dirs, files4 in os.walk("/home/lungsang/Desktop/levelpack-UI/content/A0/5 to-tag"):
    for file in files4:
        filename = os.path.join(file)
        filelist.append(filename)
    with st.expander('📁 5 to-tag'):
        st.write(filelist)


# download function
def download():
    for f in files0:
        if f == st.session_state.names:
            st.download_button('Download file', data=f)

    for f in files1:
        if f == st.session_state.names:
            st.download_button('Download file', data=f)

    for f in files2:
        if f == st.session_state.names:
            st.download_button('Download file', data=f)

    for f in files3:
        if f == st.session_state.names:
            st.download_button('Download file', data=f)

    for f in files4:
        if f == st.session_state.names:
            st.download_button('Download file', data=f)


# upload function
def upload():
    if folder_name01 == st.session_state.name:
        data_file = st.file_uploader("", key='02', type=["docx"])

        if data_file is not None:
            with open(os.path.join("/home/lungsang/Desktop/levelpack-UI/content/A0/1 docx-raw", data_file.name),
                      "wb") as f:
                f.write(data_file.getbuffer())

                st.success("File uploaded in content/A0/1 docx-raw")


    elif folder_name02 == st.session_state.name:
        data_file = st.file_uploader("", key='02', type=["docx"])

        if data_file is not None:
            with open(os.path.join("/home/lungsang/Desktop/levelpack-UI/content/A0/1 docx-raw", data_file.name),
                      "wb") as f:
                f.write(data_file.getbuffer())

                st.success("File uploaded in content/A0/1 docx-raw")

    elif folder_name03 == st.session_state.name:
        data_file = st.file_uploader("", key='02', type=["docx"])

        if data_file is not None:
            with open(os.path.join("/home/lungsang/Desktop/levelpack-UI/content/A0/1 docx-raw", data_file.name),
                      "wb") as f:
                f.write(data_file.getbuffer())

                st.success("File uploaded in content/A0/1 docx-raw")

    elif folder_name04 == st.session_state.name:
        data_file = st.file_uploader("", key='02', type=["docx"])

        if data_file is not None:
            with open(os.path.join("/home/lungsang/Desktop/levelpack-UI/content/A0/1 docx-raw", data_file.name),
                      "wb") as f:
                f.write(data_file.getbuffer())

                st.success("File uploaded in content/A0/1 docx-raw")

    elif folder_name05 == st.session_state.name:
        data_file = st.file_uploader("", key='02', type=["docx"])

        if data_file is not None:
            with open(os.path.join("/home/lungsang/Desktop/levelpack-UI/content/A0/1 docx-raw", data_file.name),
                      "wb") as f:
                f.write(data_file.getbuffer())

                st.success("File uploaded in content/A0/1 docx-raw")


def main():  # upload
    option = st.selectbox(
        'Which folder would you like to upload to?',
        ('-', '1 docx-raw', '2 docx-text-only', '3 to-segment', '4 segmented', '5 to-tag'), key='name')
    st.write('You selected:', option)
    upload_file = st.button('Upload File')
    if upload_file:
        upload()


if __name__ == '__main__':
    st.text_input('Please insert the name of file to be download', on_change=download, key='names')  # for download

    main()  # upload function

# hide streamlit menu
hide_streamlit_style = """
<style>
#MainMenu{visibility:hidden}
footer{visibility:hidden}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
