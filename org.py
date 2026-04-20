import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from organizer.categorizer import get_category
from organizer.utils import create_folders

class Handler(FileSystemEventHandler):
    def __init__(self, path):
        self.path = path

    def on_created(self, event):
        if event.is_directory:
            return

        time.sleep(1)

        file_path = event.src_path
        file_name = os.path.basename(file_path)

        category = get_category(file_name)
        dest = os.path.join(self.path, category, file_name)

        try:
            shutil.move(file_path, dest)
            print(f"Moved: {file_name} → {category}")
        except Exception as e:
            print(e)

def start_monitoring(path):
    if not os.path.exists(path):
        print("Invalid path")
        return

    create_folders(path)

    observer = Observer()
    observer.schedule(Handler(path), path, recursive=False)
    observer.start()

    print("Watching folder...")

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
