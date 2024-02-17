import argparse
import cv2
import os

parser = argparse.ArgumentParser(description='Demo of argparse')
parser.add_argument('--input_video', default='./Video/1.mp4')
parser.add_argument('--output_dir', default='./tmpVideo2Image/')

if __name__ == "__main__":
    args = parser.parse_args()
    input_path = args.input_video
    output_path = args.output_dir
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    cap = cv2.VideoCapture(input_path)
    success, frame = cap.read()
    frame_conut = 0
    while success:
        frame_conut += 1
        frame_path = os.path.join(output_path, "frame_{:06d}.jpg".format(frame_conut))
        cv2.imwrite(frame_path, frame)
        success, frame = cap.read()
    cap.release()
    print("Convert video", os.path.realpath(input_path), "to", frame_conut, "images,\n saved at", os.path.realpath(output_path))