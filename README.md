# scriber
My hacky audio transcribing aid. (Currently no support for Windows.)

# Required Python Libraries

```bash
pip install youtube_dl
pip install numpy
pip install scipy
pip install pandas
```

# System Requirements

For `youtube_mp3.py`

- For Linux (Ubuntu)
      - `ffmpeg` or `avconv`. 
      - install on Ubuntu by `sudo apt-get install ffmpeg libav-tools`
- For OSX
      - `brew install libav`


# Install

Clone (or download and unzip) this repository somewhere (a permanent location). 
Then add the following to your `~/.bashrc` (on Ubuntu) or `~/.profile` (on OSX).

```bash
export SCRIBER_HOME="path/to/scriber/src"
export PATH=$SCRIBER_HOME:$PATH
```

# Usage

In a terminal

```bash
scriber absolute/path/to/my.mp3
```

Or to transcribe a YouTube audio

```bash
scriber link/to/youtube/audio
```

Then, open a browser and go to

```bash
localhost:2499
```

If you need to change the port-number, just change `PORT` to whatever
number you want in the `src/scriber` file. 


# Install Python Dependencies
???

# Quick Start

# More
My sandbox is [here][1].

# To Do
- [ ] test on OSX. (especially `sed` in the executable `scriber`)
- [ ] allow installation. (export statement in `~/.bashrc.`)
- [ ] do the parsing in python, instead of bash (for portability)

[1]: https://github.com/luiarthur/signal_processing/tree/master/sandbox/python
