import os
#import time
import zipfile
import sys

os.chdir('D:\\WordFind\\rec\\RAW Files\\Failed')

def rename_files_ziprar():

    path = ('D:\\WordFind\\rec\\RAW Files\\Failed')
    fileList = os.listdir(path)
    print(fileList)
    for file in fileList:
        try:
            os.rename(file, file.replace("zipx", "zip" ,1))
        except FileExistsError as ex:
            os.rename(file, file.replace(".doc", ".zip", 1))



def unzip_Displace():
    sys.stdout = open('LOG.dat', 'w')
    extractionPoint = ('D:\\WordFind\\rec\\RAW Files\\ExtractionPoint\\')
    fileList = os.listdir('D:\\WordFind\\rec\\RAW Files\\All Files\\')
    base_Directory = ('D:\\WordFind\\rec\\RAW Files\\All Files\\')

    for file in fileList:
        new_folder = str(extractionPoint + str(fileList.index(file)))
        if not os.path.exists(new_folder):
            os.makedirs(str(extractionPoint+str(fileList.index(file))))
            print("EXTRACTION DIRECTORY: "+ str(new_folder)+"   THE ZIP: "+base_Directory+str(file))
            zip_location = base_Directory+str(file)

            try:
                zip_refrence = zipfile.ZipFile(zip_location, 'r')
            except Exception as ex:
                print("---------------------------------------ERROR ON ZIP REFRENCE-------------------------ERROR  : "+ str(ex) + "||||ERROR ON:  "+zip_location)
                continue
            try:
                zip_refrence.extractall(new_folder)
            except Exception as ex:
                print("---------------------------------------ERROR ON EXTRACTION(OS ERROR/ZIP)-------------------------ERROR  : " + str(ex) + "ERROR ON:  " + zip_location)
                continue
            zip_refrence.close()

            print("Extraded file:" + str(file) +'\nDirectory: '+new_folder)
    sys.stdout.close()





def investigation():

    base_folder = ('D:\\WordFind\\rec\\RAW Files\\ExtractionPoint\\')
    fileList = os.listdir(base_folder)
    print(fileList)
    for file in fileList:

        print("------------------------------------------------------------------------------file: "+str(file))
        temp_folder = base_folder+str(file)
        temp_list = os.listdir(temp_folder)

        #if temp_list.__len__() is 0:
         #   print("THIS FORLDER IS EMPTY:   "+ temp_folder)
        #else:
        for file in temp_list:
            if file.startswith("word"):
                print("GOOD FOLDER, NOW CHECKS THE XML.")
                read_xml(temp_folder+"\\"+str(file))


def read_xml(Directory):
    print("THIS IS THE DIRECTORY WE READ FROM NOW:   "+ Directory)
    list_dir = os.listdir(Directory)

    for file in list_dir:
        if file.startswith("docume"):
            print('FOLDER CONTAINS DOC, NOW CHECKING THE DOC                     :::')
            Checked_file = Directory+"\\"+str(file)
            XML = open(Checked_file, 'r', encoding="UTF-8")
            stringToMatch = 'JAVA'

            for line in XML:
                try:
                    if stringToMatch in line:
                        print("JACKPOT!!!!!!!!!!!!!!~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!!!~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        #break
                except Exception as e:
                    print(" ERRORERROR- " + str(e))
                    continue
            XML.close()



#unzip_Displace()
#rename_files_ziprar()
#investigation()