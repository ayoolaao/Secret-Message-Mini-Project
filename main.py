import os

def rename_files ():

    file_list = os.listdir("/Users/ayoolaao/Google Drive/Docs_Projects_Portfolios/Portfolios/Full Stack Web Developer Nanodegree/Intro to python/Secret Message Mini-Project/msg")
    os.chdir("/Users/ayoolaao/Google Drive/Docs_Projects_Portfolios/Portfolios/Full Stack Web Developer Nanodegree/Intro to python/Secret Message Mini-Project/msg")

    for files in file_list:
        x = "0123456789"
        b = files.translate(None, x)

        os.rename(files, b)
        print("Done")



rename_files()