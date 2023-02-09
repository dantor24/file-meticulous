import os


class Directory():

    def __init__(self):
        self._user_path = os.path.expanduser("~")
       
        
    
    @property   
    def user_path(self):
        return self._user_path
    
    
    
    
    def os_path(self, *folder_name):
        """return the specified path that the platform supports"""
        path = self.user_path
        for i in folder_name:
            path = os.path.join(path,i)

        return path
        
    
    def create_folder(self,mode = False, *folder_name):
        """create a new folder if it does not exist and return true if the folder was created and false otherwise. but when the mode is false in this case you must add only one path and it must be a full path like /home/user/your/project"""
        if mode:
            if not os.path.exists(self.os_path(*folder_name)):
                try:
                    os.makedirs(self.os_path(*folder_name))
                    return True
                except OSError:
                    print("Error system FM cannot create the repertory")
                    return False
            else:
                print("The repertory already exist")
                return False
        else:
            if not os.path.exists(folder_name):
                try:
                    os.makedirs(folder_name)
                    return True
                except OSError:
                    print("Error system FM cannot create the repertory")
                    return False
            else:
                print("The repertory already exist")
                return False
        
    def filter_files(self, path, extension):
        """return a list of all files matching the specified extension for the specified path"""
        import re
        files = []
        files_and_folder = os.listdir(path)
        files = [file for file in files_and_folder if (os.path.isfile(os.path.join(path,file))) and (re.search(extension,file))]
        
        file_current_path = [os.path.join(path,file) for file in files]
            
        return { 'path_file': file_current_path, 'files': files}
    
    def move_files(self, current_path, destination_path):
        """move the files from the current path to the destination path and return true when files successfully moved"""

        try:
            os.rename(current_path, destination_path)
            return True
        except OSError:
            print("Error system FM cannot move the files")
            return False

    
    
        
    
if __name__ == '__main__':
    direc = Directory()
    print(direc.user_path)
    print(direc.os_path('Documents'))
    print(direc.create_folder(direc.document_fm.value['parent'],direc.document_fm.value['name']))
    print(direc.filter_files(direc.os_path('Documents'),'.xlsx'))

