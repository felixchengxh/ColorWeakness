import argparse
import time
import cv2
import os
import glob
from utils.utils import color_block_square, convert_bgr2color, group_color, put_text_by_groups

parser = argparse.ArgumentParser(description='Demo of argparse')
parser.add_argument('--input_dir', default='./tmpVideo2Image/')
parser.add_argument('--output_dir', default='./tmpFramesResult/')
parser.add_argument('--size', type=int, default='100')


if __name__ == "__main__":
    args = parser.parse_args()
    input_path = args.input_dir
    output_path = args.output_dir
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    size = args.size
    Image_glob = os.path.join(input_path,"*.jpg")
    Image_name_list = []
    Image_name_list.extend(glob.glob(Image_glob))
    print("Processing", len(Image_name_list), "images ...")
    start_time = time.time()
    for image_path in Image_name_list:
        # 1. Read image
        input_image = cv2.imread(image_path)
        # 2. Split image into different blocks, and assign a representative RGB
        index_bgr = color_block_square(input_image, size)
        # 3. RGB -> Color
        index_color = convert_bgr2color(index_bgr)
        # 4. Cluster nearby color into groups
        grouped_color = group_color(index_color)
        # 5. Visualize text of color by groups
        output_image = put_text_by_groups(input_image, grouped_color, size)
        imsave_path = os.path.join(output_path, image_path.split('/')[-1].split('.')[0] + '_with_color.jpg')
        cv2.imwrite(imsave_path, output_image)
    end_time = time.time()
    consumed_time = end_time - start_time
    print("Processed in", '{:.2f}'.format(consumed_time), "s")
    Result_glob = os.path.join(input_path,"*.jpg")
    Result_name_list = []
    Result_name_list.extend(glob.glob(Image_glob))
    print("Saved", len(Result_name_list), " image to ", os.path.realpath(output_path))

        