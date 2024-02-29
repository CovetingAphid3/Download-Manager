# Download-Manager 

This simple Python script provides functionality to extract archive files (ZIP and RAR) from a specified folder. The script utilizes the `zipfile` module for ZIP files and the `patoolib` library for RAR files.

## Requirements
- Python 3.x
- `patoolib` library (Install using `pip install patool`)

## Usage

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/CovetingAphid3/Download-Manager.git
    cd archive-extractor
    ```

2. **Install Dependencies:**
    ```bash
    pip install patool
    ```

3. **Run the Script:**
    ```bash
    python download_manager.py
    ```
    Make sure to modify the `download_folder` variable in the script to point to your desired download location.

## Functionality

The script, `download_manager.py`, defines the following functions:

### `extract_archive(file_path, extract_folder) -> bool`

This function takes the path of an archive file (`file_path`) and the folder where it should be extracted (`extract_folder`). It supports both ZIP and RAR formats. The function returns `True` if the extraction is successful, otherwise `False`.

### `unzip_downloads(download_folder, max_size_MB=10)`

This function iterates through files in the specified download folder (`download_folder`). It checks if the file is an archive file (ZIP or RAR) and if its size is less than the specified maximum size in megabytes (`max_size_MB`). If these conditions are met, it extracts the contents to the same folder and optionally removes the original archive file.

## Example

```python
if __name__ == "__main__":
    download_folder = r"C:\Users\your-username\Downloads"
    unzip_downloads(download_folder)
```

This example script runs the `unzip_downloads` function on the specified download folder, extracting archive files and removing them after extraction.

## Disclaimer

This script assumes that the archives are not password-protected. It may not handle password-protected archives as-is. Additionally, use this script responsibly and ensure that you have the necessary permissions to extract files in the specified locations.
