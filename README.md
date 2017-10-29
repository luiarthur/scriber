# scriber
My hacky audio transcribing aid.

# Requirements

For `youtube_mp3.py`

- For Linux (Ubuntu)
      - `ffmpeg` or `avconv`. 
      - install on Ubuntu by `sudo apt-get install ffmpeg libav-tools`
- For OSX
      - `brew install libav`

# Install

```bash
export SCRIBER_HOME="path/to/scriber/src"
export PATH=$SCRIBER_HOME:$PATH
```

# Usage

Then, in a terminal

```bash
scriber absolute/path/to/my.mp3
```

Or to transcribe a YouTube audio

```bash
scriber youtube.com/xyz
```


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
