# scriber
My hacky audio transcribing aid.

# Requirements

For `youtube_mp3.py`

- `ffmpeg` or `avconv`. 
- install on ubuntu by `sudo apt-get install ffmpeg libav-tools`

# Usage

Go to `src`, then

`./scriber <path-to-mp3>`

# Install

```bash
export SCRIBER_HOME="path/to/scriber/src"
export PATH=$SCRIBER_HOME:$PATH
```

# Install Python Dependencies


# Quick Start

# More
My sandbox is [here][1].

# To Do
- [ ] test on OSX. (especially `sed` in the executable `scribe`)
- [ ] allow installation. (export statement in bashrc)
- [ ] do the parsing in python, instead of bash (for portability)

[1]: https://github.com/luiarthur/signal_processing/tree/master/sandbox/python
