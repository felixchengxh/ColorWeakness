# ColorWeakness
Assist color vision deficient individuals in distinguishing colors. 
![Illustration](https://github.com/felixchengxh/ColorWeakness/blob/main/Figs/illustration.jpg)
## Dependencies
Make sure you have installed following packages in your development environment.  
- os
- time
- glob
- numpy
- argparse
- opencv-python

## Get Started
First, clone this project to your device. Enter the following command at the terminal:  

```shell
git clone https://github.com/felixchengxh/ColorWeakness.git
```  

Then enter the directory of project:  

```shell
cd ColorWeakness
```  

### Process single image(.jpg for default)

```shell
python image_show_color.py --input_image=${input_image_path}
```  
#### Optional
`--input_image`: Path of input .jpg file.  
`--output_dir`: Path of output directory.  
`--size`: Pixel size of color recognition regions. 

### Process video(.mp4 for default) 

#### Precheck

Please make sure you have deleted following directories everytime before launching the code:  

`./tmpVideo2Image`, `./tmpFramesResult`  

Those directories will be generated automatically just for temporary usage, remained files sometimes cause error.

### 1. Split video to images

```shell
python scripts/Video2Image.py --input_video=${input_video_path}
```  

#### Optional

`--input_video`: Path of input .mp4 file.  
`--output_dir`: Path to save splited images.(Recommended not to change)  

### 2. Process each frame of video

```shell
python video_show_color.py --size=${pixel_width}
```

#### Optional
`--input_dir`: Path of splited images.(Recommended not to change)  
`--output_dir`: Path of processed results.(Recommended not to change)  
`--size`: Pixel size of color recognition regions.

### 3. Covert results to video

```shell
python scripts/Image2Video.py  --output_video={output_video_path}
```

#### Optional

`--input_dir`: Path of processed results.(Recommended not to change)  
`--output_video`: Path of output .mp4 file.  
`--FPS`: FPS of output video.

## Contact 

Should you have any question, please feel free to contact me via email:  
`felix1653527@gmail.com`  
`2030660534@qq.com`  
`chengxianhui@senseauto.com`  
`chengxianhui20@fudan.edu.cn`
