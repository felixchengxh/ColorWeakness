# ColorWeakness
Assist color vision deficient individuals in distinguishing colors. 

## Dependencies
Make sure you have downloaded following packages in your development environment.  
- os
- time
- glob
- numpy
- argparse
- opencv-python

## Example of using code
First, clone this project to your device. Enter the following command at the terminal:  

`git clone https://github.com/felixchengxh/ColorWeakness.git`  

Then enter directory of this project:  

`cd ColorWeakness`  

### Process single image(.jpg for default)

`python image_show_color.py --input_image=${input_image_path}`  
#### Optional
`--input_image`: Path of input .jpg files.  
`--output_dir`: Path of output directory.  
`--size`: Pixel size of color recognition regions. 

### Process video(.mp4 for default) 

#### Precheck

Please make sure you have deleted these directories everytime before launching the code:  

`./tmpVideo2Image`  
`./tmpFramesResult`  

Those directories will be generated automatically just for temporary usage, remained files sometimes cause error.

### 1. Split video to images

`python scripts/Video2Image.py --input_video=${input_video_path`  

#### Optional

`--input_video`: Path of input .mp4 files.  
`--output_dir`: Path to save splited images.(Recommended not to change)  

### 2. Process each frame of video

`python video_show_color.py --size=${pixel_width}`

#### Optional
`--input_dir`: Path of splited images.(Recommended not to change)  
`--output_dir`: Path of processed results.(Recommended not to change)  
`--size`: Pixel size of color recognition regions.

### 3. Covert results to video

`python scripts/Image2Video.py  --output_video={output_video_path}`

#### Optional

`--input_dir`: Path of processed results.(Recommended not to change)  
`--output_video`: Path of output .mp4 file.

