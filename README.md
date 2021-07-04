<p align="center">
  <img src="https://li-shen-amy.github.io/profile/images/projects/behavior.jpg" />
</p>

# Behavior toolbox

## Lick Detection
This python toolbox is for automatically detect rodent licking from video data.
Required packages: numpy, cv2, tkinter, os (python3)
Processing pipeline: 
- Select and Open the movie files
- Select the Region of Interest (ROI) interactively: areas contain tongue image (and trigger LED signal if needed)
- Average gray scale within ROI
- (Optional) Thresholding, Average, Standard-Deviation 
- Save index to Excel file (real-time)
- 
### (1)	Capture video:
Capture mouse licking video using infrared camera (Demo at “demo/ Lick_demo.mp4”). Capture a infrared LED signal in the video as trigger if needed.
No licking and Licking images are shown below:
        <p>
  <img src="https://github.com/li-shen-amy/behavior/raw/main/lick_detect/demo/no_lick.png" Alt="No licking"/>
  <img src="https://github.com/li-shen-amy/behavior/raw/main/lick_detect/demo/licking.png" Alt="licking"/>
</p>     

### (2)	Change configurations:
Change configuration in python script: “ Python_scripts/ Lick_cue_detection.py” Line 41-43:
```.py
cue_detect = 1
lick_detect = 1
use_red_ch = 0
```
if you have trigger signal to detect, please set “cue_detect=1”, otherwise, set “cue_detect=0”.
For lick detection, just leave “lick_detect=1”, otherwise, set “lick_detect=0”.
If video is captured as color mode (mouse tongue shows red), set “use_red_ch = 1” to get better result, otherwise, “use_red_ch = 0”.
### (3)	Run detection code:
Run python code: “ Python_scripts/ Lick_cue_detection.py”
### (4)	Select ROI region. 
If both “cue_detect” and “lick_detect” set to 1, select Cue ROI first, then Lick ROI. Otherwise, just select one ROI according to the parameters.
         <p align="center">
  <img src="https://github.com/li-shen-amy/behavior/raw/main/lick_detect/demo/ROI_selection.png" />
</p>  
### (5)	Export index:
The detected lick_index is saved as “Lick_demo_lick.csv” (or cue_index saved as “Lick_demo_cue.csv” if cue_detect==1)  
### (6)	Thresholding and visualize results:
Open “matlab_scripts\lick_ana.m”, set configurations:
```.m
inv_lick=1; % 0: brighter for lick ; 1: darker for lick
smooth_lick=1; % smooth
smooth_range=51;
thre_percent = 80; % automatic thresholding
diff_lick = 1; % 1: difference signal; 0: absolute signal
```
Run the codes, get the lick timestamp (variable: lick_timestamp) and visualization as following:
        <p align="center">
  <img src="https://github.com/li-shen-amy/behavior/raw/main/lick_detect/demo/vis_lick.png" />
</p>  
 


## Self Stimulation
A behavior box for self-stimulation test: LED stimulation was triggered whenever the animal nose-poked the designated LED-on port, whereas nose-poking the other port did not trigger any photostimulation.

**Details**: Mice were placed in an operant box equipped with two ports for nose poke at symmetrical locations on one of the cage walls. The ports were connected to a photo-beam detection device allowing for measurements of responses. A valid nose poke at the LED-on port lasting for at least 500 ms triggered a 1 sec long 20 Hz (5-ms pulse duration) LED pulse train delivery controlled by an Arduino microcontroller. The LED-on port was randomly assigned and balanced within the group of tested animals. The test lasted for 40 mins. Video and time stamps associated with nose poke and laser events were saved in a computer file for post hoc analysis.

## Real-Time Animal Tracking (Cooperative project)
<p align="center">
  <img src="https://github.com/GuangWei-Zhang/TraCon-Toolbox/raw/master/Images/Architecture.jpg" />
</p>
<p align="center">
  <img src="
https://github.com/GuangWei-Zhang/TraCon-Toolbox/raw/master/Gif_folder/demo_1.gif" />
</p>

Animal tracking from video is used for analyzing behavior data in Real-time place preference, spatial reward seeking, light/dark box test etc.
Software dependency: Python >= 3.0
Operating System: Windows, Linux, MacOS
Typical running time:  5min for 1h video

Procedure:
### (1)	Get the video ready, perform geometric Transform:
Open _“Python_scripts\Batch_GeoTran.py”_, set the geometry dimension (Line 170-171):
```.py
box_length = 480 
box_width = 480
```
Run the script, select batch videos to be processed, select ROI by labeling the four points (top left, top right, bottom left and bottom right), then press “c” button. The output video will be named as _“(original movie filename)_GeometricallyTransformed.mp4”_
### (2)	Automatic tracking:
Run _Mice_Tracking.py_ for general tracking purpose, or _Batch_PlacePreference_Offline.py_ for Real-time Place Preference test, or _Batch_Dark_light_box.py_ for Dark/Light Box test.

Get the coordinate of tracking position (x,y) and speed as three columns stored in _“(original movie filename)_GeometricallyTransformed_trackTrace.csv”_ and trace imposed video as _“(original movie filename)_GeometricallyTransformed_out.mp4”_ as shown in 
_“demo/RTPP_demo.mp4”_, _“Reward_seeking_tracking_demo.mp4”_.
         <p align="center">
  <img src="https://github.com/li-shen-amy/behavior/raw/main/mouse_tracking/demo/RTPP_demo.png" />
</p>  
Real-time place preference Test demo
         <p align="center">
  <img src="https://github.com/li-shen-amy/behavior/raw/main/mouse_tracking/demo/reward_seeking_demo.png" />
</p>  
Reward seeking demo

Paper: Guang-Wei Zhang, Li Shen, Zhong Li,  Huizhong W. Tao, Li I. Zhang (2019). Track-Control, an automatic video-based real-time closed-loop behavioral control toolbox.bioRxiv. doi: https://doi.org/10.1101/2019.12.11.873372

Toolbox: https://github.com/GuangWei-Zhang/TraCon-Toolbox/
