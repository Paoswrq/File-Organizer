import os
import shutil

def organizer(file_path):
    #remember to put in a file_path, its the file that you want to clean 
    files = os.listdir(file_path)

    for file in files:        
        #gets the file extension using the splitext.
        file_name, file_extension = os.path.splitext(file)
        #checks if it has a extension, if not it will moved to the no extension file
        file_type = file_extension if file_extension else 'No Extension'
        #creates a new folder for each extension and for the No extension.
        new_dir = os.path.join(file_path, file_type[1:].upper() + " Files") if file_type != 'No Extension' else os.path.join(file_path, file_type)

        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        #move it to its corresponding folders.
        shutil.move(os.path.join(file_path, file), os.path.join(new_dir, file))

if __name__ == "__main__":
    import sys
    file_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    organizer(file_path)
