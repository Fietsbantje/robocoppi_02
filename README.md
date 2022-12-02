## RoboCoppi_02  

## Joining the front  
For the front end of RoboCoppi I first created a new Python 'suit' in HTML for his intents (the JSON file). After that, I added his appearance in a CSS module and implemented his complex features (e.g. his send button) in a JavaScript module. Following this tutorial:   
https://github.com/python-engineer/pytorch-chatbot   

I particularly liked this project as it is built out of separate modules that are easier to understand and to modify than the original single Python module in RoboCoppi_01. Also note that for RoboCoppi 01 I used Tensorflow as the deep learning framework, whereas for RoboCoppi 02 I used Pytorch. In order to have a look at both, in relation to this project.  
 
## Deployment  

For the deployment of RoboCoppi 02 I used the modules from this Pytorch chatbot. Flask is used as a Web Application Framework. Following this tutorial:  
https://github.com/python-engineer/chatbot-deployment  

This tutorial shows 2 deployment options:  
- Deploy within Flask app with jinja2 template  
- Serve only the Flask prediction API. The used html and javascript files can be included in any front end application (with only a slight modification) and can run completely separate from the Flask App then.  

## Initial setup:  

Clone repo and create a virtual environment

$ git clone https://github.com/Fietsbantje/robocoppi_02.git
$ cd robocoppi_02
$ python3 -m venv venv
$ . venv/bin/activate

Install dependencies

$ (venv) pip install Flask torch torchvision nltk

Install nltk package

$ (venv) python
>>> import nltk
>>> nltk.download('punkt')

Modify intents.json with different intents and responses for your Chatbot

Run

$ (venv) python train.py

This will dump data.pth file. And then run the following command to test it in the console.

$ (venv) python chat.py

For learning how to implement app.py and app.js watch the original tutorial in the link below.

## Watch the original tutorial  
[![Alt text](https://img.youtube.com/vi/a37BL0stIuM/hqdefault.jpg)](https://youtu.be/a37BL0stIuM)  
[https://youtu.be/a37BL0stIuM](https://youtu.be/a37BL0stIuM)

## Credits:  
This repo was used for the frontend code:  
https://github.com/hitchcliff/front-end-chatjs
