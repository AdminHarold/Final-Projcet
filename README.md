
# Project Title: Climbing Pose and Hold Detection with Mediapipe

## Overview
This project involves detecting climbing holds and human poses from videos using the Mediapipe library. The workflow includes video processing, pose landmark extraction, hold prediction, and visualization of results. 

## Features
- **Video Input**: Processes video files to extract frames and analyze poses.
- **Pose Detection**: Uses Mediapipe's Pose solution to extract human pose landmarks.
- **Hold Prediction**: Identifies climbing holds in the climbing wall images using a predictive model.
- **Visualization**: Generates annotated videos highlighting holds and poses.

## Dependencies
The project requires the following libraries and tools:
- Python 3.10
- OpenCV
- Mediapipe
- NumPy
- Matplotlib
- PIL (Pillow)
- scipy

Install dependencies using the following commands:
```bash
pip install mediapipe==0.8.10 opencv-python-headless numpy matplotlib pillow scipy
pip install -r requirements.txt
```
You might need to download the wheel of mediapipe from this website manually:
[Mediapipe 0.8.10 Dashboard](https://dashboard.stablebuild.com/pypi-deleted-packages/pkg/mediapipe/0.8.10)

## Files and Directories
- `predict_holds.py`: Contains the model and functions for hold prediction.
- `utils/`: Helper functions used in video and pose processing.
- `videos/`: Directory containing input video files.
- `images/`: Directory containing images of climbing walls.
- `requirements.txt`: List of required libraries.

## Workflow
### 1. Input Video
Specify the input video path by assigning the variable `VIDEO_PATH` to the desired file in the code. The corresponding climbing wall image path is assigned to `HOLDS_PATH`.

### 2. Frame Extraction
Frames are extracted from the input video using OpenCV's `cv2.VideoCapture` and stored as NumPy arrays.

### 3. Pose Detection
Pose landmarks are detected for each frame using Mediapipe's Pose solution. Results include key joint positions and their respective confidences.

### 4. Hold Prediction
Climbing holds are identified in the climbing wall images using a predictive model implemented in `predict_holds.py`. The predictions are used to determine which holds are being used by the climber.

### 5. Visualization
Frames are annotated with detected holds and poses, and the resulting frames are compiled into a new video file.

## How to Run on Colab
1. Mount your Google Drive in Colab.
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```
2. Clone or copy the project files into your Google Drive.
3. Create a folder called videos and copy those files into that folder: [videos](https://drive.google.com/drive/folders/1EYcls7qSolRovH0nQZaxIADZVEbPgvPi?usp=sharing)
4. Create a folder called images and copy those files into that folder: [images](https://drive.google.com/drive/folders/1ifc1rHQRMNd8tEw6KH2x8KI9ixlWlKp9?usp=sharing)
5. Install required dependencies as shown above.
6. Set the `VIDEO_PATH` and `HOLDS_PATH` variables in the code to point to the appropriate files.
7. Run the cells sequentially to process the video and generate annotated output.
8. Download the processed video using:
   ```python
   from google.colab import files
   files.download('output_video.avi')
   ```
## How to Run on Local
Follow the same process but run the local file instead the colab one.


## Example Output
The processed video includes annotations of:
- Pose landmarks such as hands, hips, and legs.
- Climbing holds being used by the climber.

## Notes
- Ensure that input videos and climbing wall images have adequate resolution and lighting for better results.
- Adjust the frame size or visualization parameters if needed for your use case.

## Acknowledgments
This project uses the Mediapipe library for pose detection and custom models for hold prediction.
