
import os
import zipfile
import patoolib

def extract_archive(file_path, extract_folder):
    # Extract zip files using zipfile module
    if file_path.lower().endswith('.zip'):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_folder)
        return True

    # Extract rar files using patoolib
    elif file_path.lower().endswith('.rar'):
        patoolib.extract_archive(file_path, outdir=extract_folder)
        return True

    return False

def unzip_downloads(download_folder, max_size_MB=10):
    # Iterate through files in the download folder
    for filename in os.listdir(download_folder):
        file_path = os.path.join(download_folder, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Check if it's an archive file and its size is less than max_size_MB
        if (filename.lower().endswith('.zip') or filename.lower().endswith('.rar')) and os.path.getsize(file_path) < max_size_MB * 1024 * 1024:
            try:
                # Extract the contents to the same folder
                extract_archive(file_path, download_folder)
                print(f"Extracted: {filename}")

                # Optional: Remove the original archive file after extraction
                os.remove(file_path)
                print(f"Removed: {filename}")

            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    download_folder = r"C:\Users\your-username\Downloads"
    unzip_downloads(download_folder)
