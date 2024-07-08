import cv2
import numpy as np
import os

# Example event log (replace with your actual event log file and format)
event_log = [
    (0.02, 3, "mustard", "Entry"),
    (0.06, 2, "white", "Entry"),
    (0.10, 4, "dark green", "Entry"),
    (0.13, 1, "yellow", "Entry")
]

frames_dir = "frames"  # Directory where frames are saved
start_frame = 77  # Starting frame number
end_frame = 1999  # Ending frame number

# Function to detect ball color in a frame
def detect_ball_color(frame):
    # Convert frame to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define HSV color ranges for each potential ball color
    color_ranges = {
        "yellow": ([(20, 100, 100), (30, 255, 255)]),    # HSV range for yellow
        "blue": ([(90, 50, 50), (120, 255, 255)]),       # HSV range for blue
        "red": ([(0, 50, 50), (10, 255, 255)]),          # HSV range for red (lower)
        "red2": ([(170, 50, 50), (180, 255, 255)]),      # HSV range for red (upper)
        "orange": ([(10, 100, 100), (20, 255, 255)]),    # HSV range for orange
        "mustard": ([(20, 100, 100), (30, 255, 255)]),   # HSV range for mustard
        "white": ([(0, 0, 150), (180, 50, 255)])         # HSV range for white
    }

    detected_color = None

    # Iterate through color ranges and find the matching color
    for color_name, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)

        # Threshold the HSV image to get only the specified color range
        mask = cv2.inRange(hsv_frame, lower, upper)

        # Count non-zero pixels (color regions) in the mask
        if cv2.countNonZero(mask) > 0:
            detected_color = color_name
            break

    return detected_color

# Function to verify events against frames
def verify_events(event_log, frames_dir, start_frame, end_frame):
    for timestamp, quadrant, expected_color, event_type in event_log:
        # Convert timestamp to frame number
        frame_number = int(timestamp * 30) + start_frame

        # Ensure frame number is within the specified range
        if start_frame <= frame_number <= end_frame:
            frame_path = os.path.join(frames_dir, f"frame_{frame_number:04d}.png")

            if not os.path.exists(frame_path):
                print(f"Error: Could not find frame {frame_path}")
                continue

            frame = cv2.imread(frame_path)

            if frame is None:
                print(f"Error: Could not load frame {frame_path}")
                continue

            detected_color = detect_ball_color(frame)

            if detected_color is None:
                print(f"Error: Could not detect color in frame {frame_path}")
            elif detected_color != expected_color:
                print(f"Event {frame_number}: Ball color mismatch! Detected: {detected_color}, Expected: {expected_color}")
            else:
                print(f"Time: {timestamp}, Quadrant Number: {quadrant}, Ball Colour: {detected_color}, Type: {event_type}")

if __name__ == "__main__":
    # Step 1: Verify events against extracted frames
    verify_events(event_log, frames_dir, start_frame, end_frame)
