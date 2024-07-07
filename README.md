
# ScrcpyGUI

ScrcpyGUI is a graphical user interface (GUI) implementation for `scrcpy`, a free and open-source screen mirroring application that allows control of an Android device from a desktop computer. This GUI simplifies the usage of `scrcpy` by providing an easy-to-use interface for starting and stopping the application, as well as configuring advanced options.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Advanced Options](#advanced-options)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Start and Stop `scrcpy`**: Easily start and stop `scrcpy` with a single click.
- **Advanced Options**: Configure advanced options like bitrate, max FPS, camera settings, recording, and no audio.
- **User-Friendly Interface**: Intuitive and simple interface designed with Tkinter.

## Installation

1. **Clone the repository:**

   ```bash
   [git clone https://github.com/yourusername/scrcpygui.git](https://github.com/CrimsonREwind/scrcpygui-linux.git)
   cd scrcpygui
   ```
   you can download scrcpygui executable file from [Releases](https://github.com/CrimsonREwind/scrcpygui-linux/releases) or build it yourself.

2. **Install the required dependencies:**

   Ensure you have Python installed, then install Tkinter if it's not already available:

   For Debian-based systems:
   ```bash
   sudo apt-get install python3-tk
   ```

   For Red Hat-based systems:
   ```bash
   sudo yum install python3-tkinter
   ```

   For Windows, you can download and install Python from the official [Python website](https://www.python.org/downloads/).

3. **Install `scrcpy`:**

   Follow the installation instructions from the [official `scrcpy` repository](https://github.com/Genymobile/scrcpy).

## Usage

1. **Run the application:**

   ```bash
   python3 scrcpygui.py
   ```

2. **Use the GUI to control `scrcpy`:**

   - Click "START SCRCPY" to start the screen mirroring.
   - Click "STOP SCRCPY" to stop the screen mirroring.
   - Click "Advanced Options" to configure additional settings.

## Advanced Options

The advanced options allow you to customize the behavior of `scrcpy`. You can enable these options by selecting the corresponding checkbox and providing the required values.

- **BitRate**: Set the video bit rate (e.g., `8M` for 8 Mbps).
- **MAX FPS**: Set the maximum frame rate (e.g., `60` for 60 frames per second).
- **CAMERA ONLY**: Use the device's camera as the video source.
- **CAMERA SIZE**: Set the camera resolution (e.g., `1920x1080`).
- **RECORD**: Record the screen to a specified file (e.g., `filename` will save as `filename.mp4`).
- **NO AUDIO**: Disable audio forwarding.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the GNUv3.0 License. See the [LICENENSE](LICENSE) file for more details.
