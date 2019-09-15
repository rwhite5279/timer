timer.py
========

**timer.py** is a Python3 program that runs a countdown timer in the Terminal, and then plays an alarm bell sound when 00:00:00 is reached. This program has been tested in macOS, Ubuntu 16.04, and Raspbian.

## Getting Started

Download the project and unzip it in a convenient directory.

```
cd ~/Downloads
sudo mv timer-master.zip /usr/bin/local/
cd /usr/bin/local
sudo unzip timer-master.zip
cd timer-master
```

To run the program:

```
python timer.py
```

or 

```
python3 timer.py
```


### Prerequisites

The program is written in Python3. The Python modules `pyaudio` and `wave` are required to play the sound. 

### Installing

To use this program, download the package with `timer.py` and `alarm_bell.wav`. Open a Terminal window, navigate to the download directory, and run the program.

If you don't have `pyaudio` installed you will need to import it using the command line utility `pip` or `pip3` (depending on how you are running Python3).

```
pip install pyaudio
```

or

```
pip3 install pyaudio
```

If you don't have `pip` installed for Python3, install it in Ubuntu using:

```
sudo apt-get install python3-pip
```

#### Ubuntu, Ubuntu for Windows
```
sudo apt-get install python3-pip
sudo apt-get install portaudio19-dev
pip3 install pyaudio
```

## Author

* **Richard White** - *Initial work*, 2018-11-07

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


