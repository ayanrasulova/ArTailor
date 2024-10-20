# ArTailor
Using AI to help artists, not replace them

![logo](https://github.com/user-attachments/assets/84dc2c9a-6e33-46e0-854c-2948aed51888)

## Inspiration
ArTailor was inspired by controversies over the use of AI for art and GenAI threatening human artists. We wanted to be able to show that AI can and should be used as a tool to help artists, instead of entirely replacing them. 

Our intention is to use ControlNet software to help artists compare their drawings' anatomy to their references. Besides ControlNet image processing, we also plan on this website consolidating other tools to help artists, such as color palette generators and color matchers.

ControlNet auxiliary models taken from [ControlNet Annotators](https://github.com/lllyasviel/ControlNet/tree/main/annotator). All credit & copyright for ControlNet goes to https://github.com/lllyasviel.

## Feautures
### ControlNet Image Processing
ControlNet image processing software is used to help artists compare their drawings' anatomy to their references. Specifically, we use ControlNet's auxiliary models OpenPose for pose, hand, and face estimation/"pose tailoring," LineArt for generating sketchy-line-art, and MLSD line segment detection for estimating lines of perspective. We demonstrate the usage of ControlNet in the ArTailor.ipynb file, which can also be viewed using [this](https://colab.research.google.com/drive/1N6jfXOUB3qF3oNuN7Bnr9x9Q0kaIGc99?usp=sharing) Google Colab.

#### Google Colab Disclaimers
Sometimes the image may fail to load if selecting an image from your files- this may be due to file size or file type. Please try again with a smaller iamge, or ensure that files are of standard image types

### Image Compare
`imagecompare.py` takes two images and allows the user to compare them using a back-and-forth slider. This tool is useful for artists to compare their own work to reference images to see how closely they match.

#### Image Compare Disclaimer
Please make sure to run the following commands in terminal before: 
- pip install opencv-python
- pip install numpy
- pip install Pillow
  
If that doesnt work still, then run these commands in terminal:
- python3 -m pip install opencv-python
- python3 -m pip install numpy 
- python3 -m pip install Pillow

### User Interface
While we weren't able to build a prototype of the working website, we did create a design plan for the user interface:
![interfaceidea](https://github.com/user-attachments/assets/045fd320-c933-49fd-8293-7eabb881726e)

## Reflection/Next Steps
It was difficult at first to figure out how to allow users to upload files, but we were able to overcome that and provide options for URLs/direct uploads. 

From this project, we learned more about the capabilities of AI and how they should be taken into consideration when creating AI tools. All four of us are relatively new to Hackathons and creating independent projects, so this was a good learning experience overall. 

We are thinking of fully developing this project in the future with more time, as we are genuinely passionate about using AI as a tool for artists rather than something to replace them entirely. 








