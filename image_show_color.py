import argparse
import time
import cv2
import os
from utils.utils import color_block_square, convert_bgr2color, group_color, put_text_by_groups

parser = argparse.ArgumentParser(description='Demo of argparse')
parser.add_argument('--input_image', default='./Figs/IMG_0283.JPG')
parser.add_argument('--output_image', default='./output/')
parser.add_argument('--size', type=int, default='100')


if __name__ == "__main__":
    args = parser.parse_args()
    input_path = args.input_image
    output_path = args.output_image
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    size = args.size
    # 1. Read image
    print("Loading image ...")
    input_image = cv2.imread(input_path)
    print("Processing image")
    start_time = time.time()
    # 2. Split image into different blocks, and assign a representative RGB
    index_bgr = color_block_square(input_image, size)
    # 3. RGB -> Color
    index_color = convert_bgr2color(index_bgr)
    # 4. Cluster nearby color into groups
    grouped_color = group_color(index_color)
    # 5. Visualize text of color by groups
    output_image = put_text_by_groups(input_image, grouped_color, size)
    end_time = time.time()
    consumed_time = end_time - start_time
    print("Processed in", '{:.2f}'.format(consumed_time), "s")
    cv2.imwrite(os.path.join(output_path, input_path.split('/')[-1]), output_image)
    print("Saved image to ", os.path.realpath(output_path))