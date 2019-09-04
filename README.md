#Code used in the application

msc.py is used to control any video playback.

msc-and-sound.py is used to control the playback and the sound of any video. The highest is the state of charge, the higher is the sound output.

gaugelib.py is the code used to generate the gauge graphical interface. It will be called as a library in the file use_gauge.py
The gauge is not used in the project presently, but could be used in a two interface system, or put in a raspberry pi4 which can handle two interfaces (it has two micro HDMI port)

use_gauge.py is used to display the gauge with the value we are getting from the communication with the Arduino Nano 
