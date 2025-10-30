
import cv2
import os
import sys
import glob

def extract_last_frame(video_path):
    """
    Extracts the last frame from a video file and saves it as a JPG image.
    Returns True on success, False on failure.
    """
    # VideoCapture is the only thing that needs to be released.
    cap = None
    try:
        # Check if the video file exists
        if not os.path.exists(video_path):
            print(f"Error: Video file not found at '{video_path}'")
            return False

        # Open the video file
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print(f"Error: Could not open video file '{video_path}'")
            return False

        # Get total frame count
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if frame_count <= 0:
            print(f"Error: Cannot determine frame count for video '{video_path}'")
            return False

        # Set position to the last frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_count - 1)

        # Read the frame
        ret, frame = cap.read()
        if not ret or frame is None:
            print(f"Error: Failed to read the last frame from '{video_path}'.")
            return False

        # Construct output path
        output_filename = os.path.basename(video_path) + ".jpg"
        # The output path should be in the same directory as the video
        output_path = os.path.join(os.path.dirname(video_path), output_filename)

        # Save the frame
        cv2.imwrite(output_path, frame)
        print(f"Successfully extracted last frame to '{output_path}'")
        return True

    except Exception as e:
        print(f"An unexpected error occurred while processing '{video_path}': {e}")
        return False
    finally:
        if cap:
            cap.release()

def main():
    """
    Scans the current directory for .mp4 files and extracts the last frame of each.
    """
    # Determine the directory to scan
    if getattr(sys, 'frozen', False):
        # If running in a PyInstaller bundle
        application_path = os.path.dirname(sys.executable)
    else:
        # If running as a normal script
        application_path = os.path.dirname(os.path.abspath(__file__))

    print(f"Scanning for .mp4 files in: {application_path}")

    # Find all .mp4 files, case-insensitive
    search_pattern = os.path.join(application_path, '*.mp4')
    video_files = glob.glob(search_pattern)

    if not video_files:
        print("No .mp4 files found in the directory.")
        return

    print(f"Found {len(video_files)} video(s). Starting extraction...")
    success_count = 0
    fail_count = 0

    for video_file in video_files:
        # Avoid processing the same video file if it's in the list multiple times for any reason
        if video_file.lower().endswith('.mp4'):
            print(f"--- Processing: {os.path.basename(video_file)} ---")
            if extract_last_frame(video_file):
                success_count += 1
            else:
                fail_count += 1
    
    print("---")
    print(f"Batch processing complete. {success_count} succeeded, {fail_count} failed.")

if __name__ == "__main__":
    main()
