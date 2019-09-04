# Datacoco - Core

Equinox Common Code Utility for Python 3 with minimal dependencies and easy installation!

Includes utilities for logging and config files

## Installing the latest version
To install the latest version, use pip:
```
pip install cocore
```

## Logger

The logging module is a lightwight wrapper around the default logging module. Basic usage:
```
from cocore.Logger import Logger
l = Logger()
l.l("Your important log message here')
```

By default the log message will be saved in a logs dir of the project root, in a file named by python module and date. For example:
```
cat logs/test.py-20190827-135736.log
2019-08-27 13:57:36,471 Your important message here
```

Optionally, paramters `logname` and `project_name` can be passed on class instantiation to
customize the logfile name, and logfile path respectively.

## Config

The config module is a lightweight wrapper around the configparser module. It converts INI files to a dictionary object.
By default, the Config class will look for a file named in `etl.cfg` in the project root.

Example INI config file:
```
[secret1]
answer_to_the_universe=42
```
This credential can be accessed by the following example code:
```
from cocore.config import Config
c = Config()
c['secret1']['answer_to_the_universe']
42
```
Note: The config class assumes base64 hashing for any key named pwd or password.

## Development

#### Getting Started

It is recommended to use the steps below to set up a virtual environment for development:

```
python3 -m venv <virtual env name>
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
#### Testing

Tests are a WIP.
