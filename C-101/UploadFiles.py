#-------------------------------------------------UploadFiles.py-------------------------------------------------#
#Import modules: datetime,shutil,os,dropbox
import datetime
import shutil
import os
import dropbox 

#Declaring variables
name=input("Please enter the name of the folder you want to create:")
path=input("Enter path here:")
access_key="sl.AvTY6pAX77CeTB5bNwkIFWoUYncKgc5ar-Rt708v1sFVMg63yMvd63Ms2dyWALUXFBass62_pujjJQ9yWX0mmISuGB1T5POh0hkNcBtIl6j8uvK_-MdglGYkAve--2BRSs6Hdwc"
choice=input("Create sub-folders in accordance to time(answer as 'Yes' or 'No')")

#Defining function to upload data to Dropbox
def UploadFilesToDropbox(path_arg,access_key_arg,name_arg):
    count=0
    #Case 1
    if(choice=="Yes"):
        if(os.path.exists(path)):
            for roots,dirs,files in os.walk(path):
                for file in files:
                    count+=1
                    time=datetime.datetime.now().strftime("%H:%M")
                    date=datetime.date.today()
                    print(file)
                    new_path=roots+'/'+file
                    updated_path='/'+name+'/'+str(date)+'/'+str(time)+'/'+file
                    dbx=dropbox.Dropbox(access_key)
                    with open(new_path,'rb') as f:
                        dbx.files_upload(f.read(),updated_path,mode=dropbox.files.WriteMode.overwrite)
            if(count>1):            
                print(str(count)+" files found.") 
            else:
                print(str(count)+" file found.")      
            print("Uploading files....")
            print("Files successfully uploaded.")
            print("Thank you for using UploadFiles.py")   
        else:        
            print("Path Not Found")
    #Case2       
    elif(choice=="No"):
        if(os.path.exists(path)):
            for roots,dirs,files in os.walk(path):
                for file in files:
                    count+=1
                   
                    print(file)
                    new_path=roots+'/'+file
                    updated_path='/'+name+'/'+file
                    dbx=dropbox.Dropbox(access_key)
                    with open(new_path,'rb') as f:
                        dbx.files_upload(f.read(),updated_path,mode=dropbox.files.WriteMode.overwrite)
            if(count>1):            
                print(str(count)+" files found.") 
            else:
                print(str(count)+" file found.")   
            print("Uploading files....")
            print("Files successfully uploaded.")
            print("Thank you for using UploadFiles.py")   
        else:        
            print("Path Not Found")        

#Calling the function
UploadFilesToDropbox(path,access_key,name)
#-------------------------------------------------UploadFiles.py-------------------------------------------------#