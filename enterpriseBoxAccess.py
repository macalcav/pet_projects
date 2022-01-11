##############################################################################################
# Box API for Enterprise BOX
# enterpriseBoxAccess.py
##############################################################################################
from boxsdk import JWTAuth, Client

BOX_CONFIG_FILE_JSON=''#YOUR_BOX_CONFIG_JSON

def set_box_config_params(box_config_json):
    BOX_CONFIG_FILE_JSON=box_config_json

config = JWTAuth.from_settings_file(BOX_CONFIG_FILE_JSON)
client = Client(config)
service_account = client.user().get()
# print('Service Account user ID is {0}'.format(service_account.id))
# print('Service Account login ID is {0}'.format(service_account.login))
root_folder = client.folder(folder_id='0').get() 

def get_box_folder_id(foldername):
    #locate box folder
    FOLDER_ID=''
    folder_items = root_folder.get_items(limit=100,offset=0, sort='date',direction='DESC')
    for folder_item in folder_items:
        if folder_item.name.startswith(foldername):#iterate until find folder name
            #print('Folder Name: ', folder_item.name)
            FOLDER_ID = folder_item.id
            #print('Folder Id:   ', FOLDER_ID)
            break
    return FOLDER_ID

def get_box_file_id(foldername,filename):
    FOLDER_ID=get_box_folder_id(foldername)
    #locate box file in folder
    FILE_ID=''   
    FILES_FOLDER = client.folder(folder_id=FOLDER_ID).get()   
    file_items = FILES_FOLDER.get_items(limit=100,offset=0, sort='date', direction='DESC')
    for file_item in file_items:
        if file_item.name.startswith(filename):
            #print('File Name: %s/%s' %(root_folder.name, file_item.name))
            FILE_ID = file_item.id
            #print('File Id:  ', FILE_ID)
            break
    return FILE_ID

def get_box_file_name(file_id):
    return client.file(FILE_ID).get().name

def get_box_file_date(foldername,filename):
    FILE_ID=get_box_file_id(foldername,filename)
    return client.file(FILE_ID).get().created_at  

def download_excel_file_from_box(foldername,filename):
    FILE_ID=get_box_file_id(foldername,filename)
    EXCEL_FILE_NAME=get_box_file_name(FILE_ID)
    excel_file=open(EXCEL_FILE_NAME, 'w')#clear file
    excel_file.close()
    excel_file=open(EXCEL_FILE_NAME, 'wb')
    client.file(FILE_ID).download_to(excel_file)
    excel_file.close()
    return EXCEL_FILE_NAME
    
def download_file_from_box(foldername,filename):
    FILE_ID=get_box_file_id(foldername,filename)
    FILE_NAME=get_box_file_name(FILE_ID)
    FILE_CONTENT = client.file(FILE_ID).content()  
#     print(FILE_CONTENT)
    file_contents = FILE_CONTENT.decode("utf-8")
    f = open( filename, 'w' )
    f.write(file_contents)
    f.close()
    return FILE_NAME
