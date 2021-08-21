import os
import platform

class Organize_Directory():

    def __init__(self,directory_to_organize):
        self.directory_to_organize = directory_to_organize
        self.files_in_directory = os.listdir(directory_to_organize)

    def _get_extension(self):     
        extension_list =[]
        for file in self.files_in_directory:
            temp = file.split('.')[-1]
            #check if any folder present
            check_folder = os.path.isdir(self.directory_to_organize + file)
            #check if any temporary extension present or add your temporary extension name which you do not want to create the folder of
            if temp == "DS_Store" or check_folder:
                continue
            extension_list.append(temp.upper())

        return set(extension_list)

    def organize_files(self):
        self.__create_folders()
        for file in self.files_in_directory:
            check_folder = os.path.isdir(self.directory_to_organize + file)
            if check_folder:
                continue
            self.__add_files_in_created_folder(file)

    def __create_folders(self):
        extensions = self._get_extension()
        #create folder in uppercase
        for ext in extensions:
            check_folder = os.path.exists(self.directory_to_organize + ext)
            if check_folder:
                continue
            os.mkdir(self.directory_to_organize + ext)

    def __add_files_in_created_folder(self, file_name):
        extensions = self._get_extension()
        file_ext = file_name.split('.')[-1].upper()
        for ext in extensions:
            if file_ext == ext:
                folder = self.directory_to_organize + file_name
                #OS based directory path
                if platform.system() != "Windows":
                    dest = self.directory_to_organize + ext + "/" + file_name 
                else:
                    dest = self.directory_to_organize + ext + "\\" + file_name 
                os.rename(folder,dest)                

users_os = platform.system()
directory_to_organize = str(input("Enter your directory path to organise: "))
is_directory = os.path.isdir(directory_to_organize)

if is_directory:
    if users_os != "Windows":
        if not directory_to_organize.endswith("/"):
            directory_to_organize += "/"
    else:
        if not directory_to_organize.endswith("\\"):
            directory_to_organize += "\\"

    organize = Organize_Directory(directory_to_organize)
    organize.organize_files()

else:
    print("Enter a valid directory")
