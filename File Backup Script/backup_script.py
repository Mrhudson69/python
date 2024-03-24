import shutil
import os

def backup_directory(source_dir, destination_dir):
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    # Check if destination directory exists, create if not
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        print(f"Destination directory '{destination_dir}' created.")

    try:
        # Copy files from source to destination
        print("Copying files...")
        shutil.copytree(source_dir, destination_dir)
        print("Backup completed successfully.")
    except Exception as e:
        print(f"Error occurred during backup: {e}")

if __name__ == "__main__":
    # Define source and destination directories
    source_directory = "/path/to/source/directory"
    destination_directory = "/path/to/backup/directory"

    # Call backup function
    backup_directory(source_directory, destination_directory)
