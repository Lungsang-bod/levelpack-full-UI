import streamlit as st
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class lungsang:
    def gdrivee():
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)

        path = "/home/lungsang/Desktop/levelpack-UI/content/A0/1 docx-raw/"
        folder = "1tuQxaiDOdbfv1JHXNAln2nbq1IvBOrmP"

        file_list = drive.ListFile({'q': f"'{folder}' in parents and trashed=false"}).GetList()
        for index, file in enumerate(file_list):
            print(index + 1, 'file Downloaded : ', file['title'])
            file.GetContentFile(path + file['title'])

    gdrivee()

