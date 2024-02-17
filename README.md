# ColorWeakness
Assist color vision deficient individuals in distinguishing colors. 
## Example of using code

### Process single image(.jpg for default)

`python image_show_color.py --input_image=${input_image_path} --output_image={output_image_path} --size=${pixel_width}`  

--input_image: Path of input jpg files, such as: './figs/example.png'  
--output_image: Path of output jpg files, such as: './output/example.png'  
--size: Size of pixel to distinguish colors of regions, such as: 100  

### Process video(.mp4 for default) 

### Precheck for processing video

Please make sure you have deleted these directories everytime before launching the code:  

`./tmpVideo2Image`  
`./tmpFramesResult`  

Those directories will be generated automatically just for temporary usage, remained files sometimes cause error.

### 1. Split video to images

`python scripts/Video2Image.py --input_video=${input_video_path`  

--input_video: Path of input mp4 files, such as: './Video/1.mp4'

### 2. Process each frame of video

`python video_show_color.py --size=${pixel_width}`

### 3. Covert results to video

`python scripts/Image2Video.py`
