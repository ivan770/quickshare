# QuickShare
QuickShare is a Flask-based web application, that allow users to make anonymous notes, without leaving any personal info.

It's interface is simple and responsible (based on [Materialize](http://materializecss.com/)), and can be used on any device.

## Installation
(this tutorial uses Flask internal server, which can be insecure for production use)
1. Install Python 3 for your OS.
2. Run `pip3 install flask` to install all Flask default packages.
3. Run `pip3 install flask-wtf` to install Flask-WTForms package.
4. Clone this repository into some directory, and enter this directory.
5. Run `export FLASK_APP=main.py`.
6. Finally, run `flask run`.

**P.S If you have any errors, that are related to missing packages, send logs to issues, so I can fix guide**

**P.P.S If `flask run` does not work, try `python3 -m flask run`**

## Screenshots

![Index page](https://github.com/ivan770/quickshare/raw/master/screenshots/index.png)
![Message preview page](https://github.com/ivan770/quickshare/raw/master/screenshots/message.png)
