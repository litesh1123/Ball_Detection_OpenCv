# Ball_Detection_OpenCv
 This code is used to take video as input,and would record positions of ball movements in it using OpenCv .

Challenges Faced:
1. Color Detection Accuracy: Due to hand movements and lighting variations in the video, accurately detecting ball colors has been challenging. Specifically, distinguishing between similar colors like mustard and yellow has proven difficult.
   
2. Event Logging Consistency: Ensuring all entry and exit events are logged correctly across frames, especially when multiple balls are in motion simultaneously.

3. Video Frame Extraction: Successfully converting the video into frames and extracting images for analysis.

Achievements:
1. Frame Extraction: Developed a script to convert a 1 minute 45 second video into 2067 frames for detailed analysis.

2. Color Detection Logic: Implemented a color detection algorithm using HSV color space, covering potential ball colors such as yellow, blue, red, orange, mustard, white, and dark green.

3. Event Logging: Created a system to log entry events (ball placements) accurately within specified quadrants along with timestamp details.

Next Steps:
1. Refining Color Detection: nvestigating advanced techniques or machine learning models to improve color recognition accuracy, especially in scenarios with varied lighting and background interference.

2. Ehancing Event Logging: Implementing mechanisms to handle simultaneous events and refine event detection algorithms to ensure consistency.


Conclusion:
Despite challenges in color detection accuracy and event logging consistency, significant progress has been made in video processing tasks, including frame extraction and initial event logging. Moving forward, efforts will focus on refining algorithms and exploring advanced techniques to overcome current limitations.


