#!/bin/bash

# Create necessary directories
mkdir -p ~/netspeed_executable
mkdir -p ~/.local/share/applications

# Download the executable from GitHub
curl -L -o ~/netspeed_executable/netspeed https://github.com/iRaM-sAgOr/python_packages/raw/netspeed/dist/netspeed

# Set the correct permissions
chmod +x ~/netspeed_executable/netspeed

# Create the .desktop entry
cat <<EOF > ~/.local/share/applications/netspeed.desktop
[Desktop Entry]
Version=1.0
Name=Net Speed Test
Comment=Check your internet speed
Exec=$HOME/netspeed_executable/netspeed
Icon=$HOME/netspeed_executable/netspeed_icon.jpeg
Terminal=false
Type=Application
Categories=Utility;
EOF

# Download and install the icon
curl -L -o ~/netspeed_executable/netspeed_icon.jpeg https://github.com/iRaM-sAgOr/python_packages/raw/main/icons/netspeed_icon.jpeg

# Refresh the desktop database
update-desktop-database ~/.local/share/applications

echo "Net Speed Test app installed successfully!"
