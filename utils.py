import os
def create_folders(path):
    folders = ['Images', 'Documents', 'Code', 'Archives', 'Others']
    for folder in folders:
        os.makedirs(os.path.join(path, folder), exist_ok=True)
