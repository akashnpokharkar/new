import datetime
import shutil
import os

def Folder_backup(source, destination):
    today=datetime.date.today()
    backup_file=os.path.join(destination,f"backup_{today}tar.gz")
    shutil.make_archive(backup_file,'gztar', source)
    
    
source= "C:\\Users\\Akash\\devops"
destination= "C:\\Users\\Akash\\devops\\backup_project_backup"
    
Folder_backup(source,destination)    