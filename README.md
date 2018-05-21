# Materials for Dash workshop for PyCon CZ 2018

[Workshop info - PyCon CZ page](https://cz.pycon.org/2018/programme/detail/workshop/1/)

## Programme

1. Installation
1. Introduction into data and Dash [Presentation]()
1. Dive into Dash using toy examples [Tutorial]
1. Look closely at migation dash application [App file](https://github.com/anastazie/dash-pycon-2018/blob/master/app.py)

## Installation

*Note:* Python 3.6 or higher can be used for this workshop.

### Windows

#### Python

1. Install Python via [`anaconda`](https://www.anaconda.com/download/).
1. Install GitBash using following command Anaconda prompt: `conda install git`

#### Python libraries
1. Install dependencies located in `requirements.txt` using following command in GitBash: `while read requirement; do conda install --yes $requirement || pip3 install $requirement; done < requirements.txt`

for more details ee [Stack Overflow discussion](https://stackoverflow.com/questions/35802939/install-only-available-packages-using-conda-install-yes-file-requirements-t/)

### Linux, Mac OS

#### Python
1. Ubuntu, Debian
    `sudo apt install python3 python3-pip`
1. MacOS
    `brew install python3`
    
    *Note:* if you do not have `brew`, install it using [this](https://brew.sh/) tutorial.

#### Python libraries

`pip3 install -r requirements.txt`





