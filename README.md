
# Last Frame Extractor (影片最後一幀擷取工具)

A simple, command-line tool to quickly extract the last frame from all `.mp4` video files in a directory.

一個簡單的命令列工具，可以快速擷取資料夾中所有 `.mp4` 影片的最後一幀畫面。

## Demo (執行範例)

Simply place the executable in a folder with your videos and run it.

只需將執行檔與您的影片放在同一個資料夾中，然後執行它。

```bash
$ ./extract_frame

Scanning for .mp4 files in: /Users/user/Desktop/MyVideos
Found 4 video(s). Starting extraction...
--- Processing: video_1.mp4 ---
Successfully extracted last frame to '/Users/user/Desktop/MyVideos/video_1.mp4.jpg'
--- Processing: video_2.mp4 ---
Successfully extracted last frame to '/Users/user/Desktop/MyVideos/video_2.mp4.jpg'
--- Processing: another.mp4 ---
Successfully extracted last frame to '/Users/user/Desktop/MyVideos/another.mp4.jpg'
--- Processing: final_clip.mp4 ---
Successfully extracted last frame to '/Users/user/Desktop/MyVideos/final_clip.mp4.jpg'
---
Batch processing complete. 4 succeeded, 0 failed.
```

## Features (功能)

- **Batch Processing**: Automatically finds and processes all `.mp4` files in its folder.
- **Zero-Config**: No command-line arguments needed. Just run and go.
- **Cross-Platform**: Provides ready-to-use executables for both macOS and Windows.
- **Dependency-Free**: End-users don't need to install Python or any other libraries.

- **批次處理**：自動尋找並處理資料夾中的所有 `.mp4` 檔案。
- **零設定**：無需任何命令列參數，直接執行即可。
- **跨平台**：提供適用於 macOS 和 Windows 的獨立執行檔。
- **無需依賴**：終端用戶無需安裝 Python 或任何其他函式庫。

## How to Use (如何使用)

1.  Go to the [**Releases**](https://github.com/daubas/extract_last_frame_from_mp4/releases) page of this repository.
2.  Download the latest release asset for your operating system (`extract_frame-macos.zip` or `extract_frame-windows.zip`).
3.  Unzip the file.
4.  Place the `extract_frame` (for Mac) or `extract_frame.exe` (for Windows) executable into the folder containing your `.mp4` files.
5.  Run the executable by double-clicking it or by executing it in your terminal.
6.  A `.jpg` image for each video will be saved in the same folder.

1.  前往本專案的 [**Releases**](https://github.com/daubas/extract_last_frame_from_mp4/releases) 頁面。
2.  根據您的作業系統，下載最新的發行版本 (`extract_frame-macos.zip` 或 `extract_frame-windows.zip`)。
3.  解壓縮檔案。
4.  將 `extract_frame` (Mac) 或 `extract_frame.exe` (Windows) 執行檔放入存有您 `.mp4` 檔案的資料夾中。
5.  雙擊執行，或在終端機中執行它。
6.  每個影片的最後一幀畫面將會以 `.jpg` 格式儲存在同一個資料夾中。

## Building From Source (從原始碼建置)

If you want to build the executable yourself, follow these steps:

如果您想自己建置執行檔，請遵循以下步驟：

1.  **Clone the repository (複製專案):**
    ```bash
    git clone https://github.com/daubas/extract_last_frame_from_mp4.git
    cd extract_last_frame_from_mp4
    ```

2.  **Create a virtual environment (建立虛擬環境):**
    ```bash
    python3 -m venv venv
    ```

3.  **Activate and install dependencies (啟用環境並安裝依賴):**
    *   macOS / Linux:
        ```bash
        source venv/bin/activate
        pip install -r requirements.txt
        pip install pyinstaller
        ```
    *   Windows:
        ```bash
        .\venv\Scripts\activate
        pip install -r requirements.txt
        pip install pyinstaller
        ```

4.  **Run PyInstaller (執行打包):**
    ```bash
    pyinstaller --onefile --name extract_frame extract_frame.py
    ```

5.  The executable will be located in the `dist/` directory.
    (執行檔將會產生在 `dist/` 資料夾中。)

## License (授權條款)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

本專案採用 MIT 授權。詳情請見 [LICENSE](LICENSE) 檔案。
