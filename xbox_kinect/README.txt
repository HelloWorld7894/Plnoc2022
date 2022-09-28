For Plnoc 2022, I also used my old xbox 360 kinect, 
and basically ran it only on linux machines, so this README will be for linux.

To establish communication with xbox 360 kinect, i used libfreenect -> https://github.com/OpenKinect/libfreenect
(to communicate with newer xbox kinects, use libfreenect2 -> https://github.com/OpenKinect/libfreenect2)

Install documentations:
https://github.com/OpenKinect/libfreenect
https://openkinect.org/wiki/Getting_Started (I prefer manual build, worked on ubuntu, raspian and arch)

Build commands:
git clone https://github.com/OpenKinect/libfreenect.git
cd libfreenect
mkdir build && cd build
cmake .. -DBUILD_PYTHON3=ON
make
sudo make install

Usage:
cd bin
(by ls command, you will see all executable bash scripts)
sudo ./#YOUR_FREENECT_BASH_SCRIPT#

