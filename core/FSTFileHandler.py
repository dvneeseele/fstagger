import os
import sys
import PIL
import hashlib

class FSTFileHandler():
    def __init__(self):
        pass


    def getFiles(self):
        pass

    def linkFiles(self):
        pass

    def hashFiles(self, file_path, algorithm='sha256'):
        s256 = hashlib.new(algorithm)

        with open(file_path, 'rb') as file:
            while chunk := file.read(8192):  # Read the file in chunks of 8192 bytes
                s256.update(chunk)
        
        return s256.hexdigest()

    def importFiles(self):
        print("Importing Files...")
        # Only adding paths to db right now.
        # using folder of random test images for now.
        image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
        folder_path = './test_images'
        image_list = []
        # List of tags just for testing
        tags = []

        for filename in os.listdir(folder_path):
            if filename.lower().endswith(image_extensions):
                image_path = os.path.join(folder_path, filename)
                
                mydict = {
                    'directory': os.path.dirname(image_path),
                    'filename' : os.path.basename(image_path)
                }
                print(mydict)
                image_list.append(mydict)
        # print(f"Dict List : {image_list}")
        return image_list
    
