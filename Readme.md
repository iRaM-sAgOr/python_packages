# Install dependencies
$ pip install -r requirements.txt

# Create the binary executables
$ pyinstaller --onefile --windowed netspeed.py

# Configure the dependencies:
1. Update the .desktop files
$ nano ~/.local/share/applications/netspeed.desktop
-- then make a folder name "netspeed_executable" in the home(or anyother location)
-- past netspeed file in the directory
-- same for the icon image in the same directory

2. Update the file with

[Desktop Entry]
Version=1.0
Name=Net Speed Test
Comment=Check your internet speed
Exec=/home/<your-username>/netspeed_executable/netspeed
Icon=/home/<your-username>/netspeed_executable/netspeed_icon.png
Terminal=true
Type=Application
Categories=Utility;


# Refresh the Desktop Database
$ update-desktop-database ~/.local/share/applications

# Set the files executables
$ chmod +x ~/.local/share/applications/netspeed.desktop
$ chmod 644 /home/<your-username>/netspeed_executable/netspeed_icon.png

This way your code can become an executable application in linux


*** If you want to clone the repo and Install the app from the code ********
$ curl -L https://github.com/iRaM-sAgOr/python_packages/raw/netspeed/installer.sh | bash
