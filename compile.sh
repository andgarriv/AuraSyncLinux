#!/bin/bash

# Main application file name (without .py extension)
APP_NAME="auraforlinux"
OUTPUT_NAME="AuraSyncLinux"  # Name of the compiled application
ICON_FILE="icon.ico"         # Path to the .ico icon file

# Check if PyInstaller is installed
if ! command -v pyinstaller &> /dev/null; then
    echo "PyInstaller is not installed. Installing it now..."
    pip install pyinstaller
fi

# Compile the program
echo "Compiling $APP_NAME.py with PyInstaller..."

if [ -f "$ICON_FILE" ]; then
    pyinstaller --onefile --noconsole --name="$OUTPUT_NAME" --icon="$ICON_FILE" "$APP_NAME.py"
else
    echo "Icon file not found. Compiling without an icon..."
    pyinstaller --onefile --noconsole --name="$OUTPUT_NAME" "$APP_NAME.py"
fi

# Check if the compilation was successful
if [ -f "dist/$OUTPUT_NAME" ]; then
    echo "Compilation successful. Executable created at: dist/$OUTPUT_NAME"
else
    echo "Compilation failed. Please check the logs for details."
    exit 1
fi

# Clean up temporary files
echo "Cleaning up temporary files..."
rm -rf build/ "$APP_NAME.spec"

echo "Compilation completed."
