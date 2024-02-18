import argparse
import cv2
import os

parser = argparse.ArgumentParser(description='Demo of argparse')
parser.add_argument('--input_dir', default='./tmpFramesResult')
parser.add_argument('--output_video', default='./VideoOutput/')
parser.add_argument('--FPS', type=int, default=30)
if __name__ == "__main__":
    args = parser.parse_args()
    source_path = args.input_dir
    output_path = args.output_video
    FPS = args.FPS
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    file_list = os.listdir(source_path)
    file_list.sort()
    num_files = len(file_list)
    # 获取所有图片文件名并排序
    frame = cv2.imread(os.path.join(source_path, file_list[0]))
    height, width, layers = frame.shape
    # 使用cv2.VideoWriter()创建视频编写器
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # 或者使用其他视频编解码器例如'XVID'
    video = cv2.VideoWriter(os.path.join(output_path, '1.mp4'), fourcc, FPS, (int(width), int(height)))

    # 循环读取图片并写入视频
    for i in range(num_files):
        image = cv2.imread(os.path.join(source_path, file_list[i]))
        video.write(image)

    # 释放资源
    cv2.destroyAllWindows()
    video.release()
    print("Changed", num_files, "images into video! Saved in", os.path.realpath(output_path))