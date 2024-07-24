# Hand Gesture Recognition using MediaPipe and OpenCV

This project implements a hand gesture recognition system using MediaPipe and OpenCV. The system captures video from a webcam, detects hand landmarks in real-time, and visualizes them.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/hand-gesture-recognition.git
    cd hand-gesture-recognition
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the main script to start the hand gesture recognition system:
```sh
python main.py
```
Press `q` to quit the application.

## Project Structure

- `main.py`: Main script to run the hand gesture recognition system.
- `data.py`: Contains data-related functionality.
- `comment_dataset.py`: Script for dataset comments processing.