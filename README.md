
# NASA Hackathon 2023 - Tredisonif - Planetary Motion Music Generator

This project, developed during a NASA Hackathon, transforms planetary and star motion videos into background music by analyzing brightness and motion dynamics. The resulting audio captures the celestial ambiance, creating a unique auditory experience directly from space footage.

## Installation

To run the project, ensure Python 3.7+ is installed. Then, install the required libraries with:

```bash
pip install -r requirements.txt
```

## Usage

1. **Prepare your video**: Place your planetary or star motion video in the `data/` folder and name it `nasa-video-data.mp4`.
2. **Run the main file**: Execute the following command to generate the audio:

    ```bash
    python main.py
    ```

3. **Output**: The generated music will be saved as `generated_audio.mp3` in the `output/` folder.

## How It Works

The program processes each frame of the video, analyzing brightness and motion. This data is mapped to sound frequencies, generating a unique musical composition reflective of the video’s celestial motion.

## Dependencies

The project uses the following libraries:

- `opencv-python`
- `scipy`
- `sounddevice`
- `pydub`

For a complete list, refer to `requirements.txt`.

## License

This project was created during a NASA Hackathon and is open for further development and enhancements. Feel free to contribute and improve the code.

This project is licensed under the MIT License - see the [LICENSE]file for details.
