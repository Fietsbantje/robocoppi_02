## RoboCoppi 02 - joining the front -
For the front end of RoboCoppi I first created a new Python 'suit' for his intents (the JSON file). After that, I added his looks in a CSS module and implemented his complex features (e.g. his send button) in a JavaScript module. Following this tutorial:  
https://github.com/python-engineer/pytorch-chatbot   

I particularly liked this project as it is built out of separate modules that are easier to understand and to modify than the original single Python module in RoboCoppi 01. Also note that for RoboCoppi 01 I used Tensorflow as the deep learning framework, whereas for RoboCoppi 02 I used Pytorch. In order to have a look at both, in relation to this project.
 
For the deployment of RoboCoppi 02 I used the modules from this Pytorch chatbot. Flask is used as a Web Application Framework. Following this tutorial:  
https://github.com/python-engineer/chatbot-deployment  

This tutorial shows 2 deployment options:
- Deploy within Flask app with jinja2 template
- Serve only the Flask prediction API. The used html and javascript files can be included in any front end application (with only a slight modification) and can run completely separate from the Flask App then.

## Watch the Tutorial
[![Alt text](https://img.youtube.com/vi/a37BL0stIuM/hqdefault.jpg)](https://youtu.be/a37BL0stIuM)  
[https://youtu.be/a37BL0stIuM](https://youtu.be/a37BL0stIuM)

## Credits:
This repo was used for the frontend code:
https://github.com/hitchcliff/front-end-chatjs
