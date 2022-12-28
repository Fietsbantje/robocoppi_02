# RoboCoppi_02  

## Joining the Front  

For the front end of RoboCoppi I followed this tutorial on building a chatbot using Python, HTML, CSS and JavaScript:  

https://github.com/python-engineer/pytorch-chatbot   

For learning the basics of front-end development, I followed the course "Introduction to Web Design and Development" by Jen Kramer on [Linkedin Learning](https://www.linkedin.com/learning/). Linkedin Learning isn't free, but some employers provide free access to these courses.  

I used [codepen](https://codepen.io) to play around with the HTML, CSS and JavaScript modules and to customize RoboCoppi's graphical interface.  

## Compare Deep Learning Frameworks and Architecture  

While for RoboCoppi_dir I used [Tensorflow](https://www.tensorflow.org/overview) as the deep learning framework, for RoboCoppi-02 I used [Pytorch](https://pytorch.org/tutorials/index.html).  

I particularly liked the architecture of this second bot (RoboCoppi_02) now that RoboCoppi is starting to grow, because it is built out of separate Python modules that are easier to understand and to modify than the original single Python module in RoboCoppi_dir. I integrated my own modules and intents from RoboCoppi_dir and added new modules. 

## Local Deployment  

For the first deployment of RoboCoppi_02 I took the modules of RoboCoppi_02 and used Flask as a Web Application Framework, to have RoboCoppi work on the local host. Following this tutorial:  

https://github.com/python-engineer/chatbot-deployment  

This tutorial shows two deployment options:

- Deploy within Flask app with jinja2 template  
- Serve only the Flask prediction API. The used html and javascript files can be included in any front end application (with only a slight modification) and can run completely separate from the Flask App.  

## Initial Setup:  

Clone repo
```
$ git clone https://github.com/Fietsbantje/robocoppi_02.git
$ cd robocoppi_02
```

Create and activate an environment using venv
```
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies with pip
```
$ (venv) pip install Flask torch torchvision nltk
```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
```
Modify intents.json with different intents and responses for your Chatbot

Run
```
$ (venv) python train.py
```
This will dump data.pth file. And then run the following command to test it in the console.
```
$ (venv) python chat.py
```

For learning how to implement app.py and app.js watch the original tutorial in the link below.

## Watch the original tutorials  

[![Alt text](https://img.youtube.com/vi/RpWeNzfSUHw/hqdefault.jpg)](https://youtu.be/RpWeNzfSUHw)  
[https://youtu.be/a37BL0stIuM](https://youtu.be/RpWeNzfSUHw)  

[![Alt text](https://img.youtube.com/vi/a37BL0stIuM/hqdefault.jpg)](https://youtu.be/a37BL0stIuM)  
[https://youtu.be/a37BL0stIuM](https://youtu.be/a37BL0stIuM)  

## Credits:  

These repo's were used to build this version: 
 
https://github.com/hitchcliff/front-end-chatjs  
https://github.com/python-engineer/pytorch-chatbot  
https://github.com/python-engineer/chatbot-deployment  
  

