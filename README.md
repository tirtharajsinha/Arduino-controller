# Arduino-controller
A web based controller interface for arduino.

<img src="static\controller.png" width="400px" height="auto" style="display:block;margin:auto;">

## Requirements
- Arduino AVR board
- Arduino IDE
- python3


## How to run
> Clone this repository
```
git clone git@github.com:tirtharajsinha/Arduino-controller.git
```

> Clone the arduino repository
```
git clone git@github.com:tirtharajsinha/arduino.git
```

1. Connect the arduino board
2. open the arduino IDE
3. select the board and port number(something like ```COM5```)
4. Now open ```Arduino\control_arduino_from_thirdparty\control_arduino_from_thirdparty.ino``` in arduino ide.
5. install the required libraries listed below.
6. open the Arduino-controller repo in terminal and run following command.
    ```
    virtualenv venv
    ./venv/Scripts/activate
    pip install -r requirements.txt
    ```
7. Now open the util.py in current location repo in notepad and change the ```PORT``` variable as per your case.
8. Connect the circuit available the .ino code location.
9. Open the arduino ide and validate and upload the script.
10. Open serial monitor. You should see the ```0#XX``` printing in the monitor.
11. type ```led1``` and press CTRL+ENTER. if you see one led lights up then you are good to go. othewise contact maintainer.
if maintainer refuses then you are fucked up. 
12. If everything is good, now go the app repo and run following command.
    ```
    ./venv/Scripts/activate
    python app.py
    ```



## Arduino libraries you need
1. Adafruit Circuit Playground by Adafruit
2. Servo by Michael Margolis, Arduino
3. DHT sersor library by Adafruit
4. Adafruit Unified sensor by Adafruit

<hr>
- By Tirtharaj Sinha