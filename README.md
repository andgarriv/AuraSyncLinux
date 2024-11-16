# AuraSyncLinux
AuraSyncLinux is a graphical user interface (GUI) built for Linux that uses `asusctl` to control the RGB lighting of keyboards compatible with AuraSync. Designed specifically for Linux users, it provides an intuitive interface for configuring lighting modes and colors.

## Features

- Dynamic rainbow-colored title animation.
- Multiple lighting modes, including Static, Breathe, Pulse, Rainbow Cycle, and Rainbow Wave.
- Custom color picker to define your unique lighting preferences.
- Compatible with `asusctl` for seamless integration with AuraSync hardware.
- Responsive and modern GUI built with `ttkbootstrap`.

## Requirements

- Python installed
- `asusctl` installed and configured on your Linux system
- Libraries:
  - `ttkbootstrap`
  - `tkinter` (usually pre-installed with Python)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/andgarriv/AuraSyncLinux
   cd AuraSyncLinux
   ```

2. **Set Up a Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Required Python Libraries**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure `asusctl` is Installed**
   Follow the instructions for your Linux distribution to install `asusctl`:
   - For Arch Linux:
     ```bash
     sudo pacman -S asusctl
     ```
   - For other distributions, refer to the [asusctl documentation](https://gitlab.com/asus-linux/asusctl).

5. **Run the Application**
   ```bash
   python auraforlinux.py
   ```

## Compilation Instructions

To create a standalone executable of the application, follow these steps:

### Using the Provided Compile Script

A Bash script `compile.sh` is included in the repository to simplify the compilation process.

1. **Ensure the Script is Executable**
   ```bash
   chmod +x compile.sh
   ```

2. **Run the Script**
   ```bash
   ./compile.sh
   ```

3. **Output**
   The executable will be created in the `dist/` folder:
   ```plaintext
   dist/auraforlinux
   ```

4. **Cleaning Temporary Files**
   The script automatically cleans up temporary files such as the `build/` folder and the `.spec` file.

### Using PyInstaller Manually

1. **Install PyInstaller**
   ```bash
   pip install pyinstaller
   ```

2. **Compile the Application**
   Run the following command to generate a standalone executable:
   ```bash
   pyinstaller --onefile --noconsole --icon=icon.ico auraforlinux.py
   ```

   - `--onefile`: Packages everything into a single executable file.
   - `--noconsole`: Prevents the console from opening when running the GUI.
   - `--icon=icon.ico`: Adds a custom icon for the application (optional).

3. **Locate the Executable**
   The compiled executable will be located in the `dist/` folder:
   ```plaintext
   dist/auraforlinux
   ```

4. **Run the Executable**
   Navigate to the `dist/` folder and run the program:
   ```bash
   ./dist/auraforlinux
   ```

## Icon File

- The default icon file is `icon.ico`. Place this file in the same directory as `auraforlinux.py` and `compile.sh` before compiling.
- If you do not have an `.ico` file, you can convert any image to `.ico` format using [ConvertICO](https://convertico.com/) or similar tools.
- Recommended icon size: `256x256` or `128x128`.

## Usage

1. Launch the compiled executable or run the script with Python.
2. Select your preferred lighting mode from the main menu.
3. Customize colors or choose preset colors for Static, Breathe, and Pulse modes.
4. Enjoy full control of your keyboard's RGB lighting on Linux!

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

### Development Setup

1. Fork the repository.
2. Clone your fork locally.
3. Create a new branch for your feature or fix:
   ```bash
   git checkout -b feature-name
   ```
4. Test your changes thoroughly before submitting a pull request.

## License

This project is licensed under GPL-3.0 license. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [asusctl](https://gitlab.com/asus-linux/asusctl) for providing the core functionality to control AuraSync lighting.
- The Linux community for their support and contributions.
