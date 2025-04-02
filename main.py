import cv2
import os

def video_to_frames(video_path, output_folder):
    # Cek apakah folder output ada, kalau belum buat baru
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Buka file video
    cap = cv2.VideoCapture(video_path)

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Stop jika video habis

        # Simpan frame ke file
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)

        print(f"Saved {frame_filename}")
        frame_count += 1

    cap.release()
    print(f"Total frames extracted: {frame_count}")

# Contoh penggunaan
video_path = "D:\\Rakha-Camera-Vision\\1. Dokomentasi\\Trial 5 - Fix Posisi Run.mp4"        # Ganti dengan path video kamu
output_folder = 'output_frames_trial5'        # Folder output untuk menyimpan frame
video_to_frames(video_path, output_folder)
