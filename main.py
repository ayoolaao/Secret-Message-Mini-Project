import os

def rename_files ():

    file_list = os.listdir("/Users/ayoolaao/Google Drive/Docs_Projects_Portfolios/Portfolios/Full Stack Web Developer Nanodegree/Intro to python/Secret Message Mini-Project/msg")
    print(file_list)

    print(os.getcwd())
    os.chdir("/Users/ayoolaao/Google Drive/Docs_Projects_Portfolios/Portfolios/Full Stack Web Developer Nanodegree/Intro to python/Secret Message Mini-Project/msg")
    print(os.getcwd())

    for i in file_list:
        a = "0123456789"
        b = i.translate(None, a)

        os.rename(i, b)
        print("Done")



rename_files()