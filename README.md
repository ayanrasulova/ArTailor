# ArTailor
Using AI to help artists, not replace them

## Google Colab Link
https://colab.research.google.com/drive/1N6jfXOUB3qF3oNuN7Bnr9x9Q0kaIGc99?usp=sharing

## Inspiration
We were inspired by controversies over the use of AI for art and GenAI threatening human artists. We wanted to be able to show that AI can and should be used as a tool to help artists, instead of entirely replacing them. 

Our intention is to use ControlNet (OpenPose, LineArt, MLSD) software to help artists compare their drawings' anatomy to their references. We were also planning on this website including more tools to help artists, which we included in our attached slides. 

We were able to get ControlNet working with Python using a Google Colab fork collaboration from an open source library. 

It was difficult at first to figure out a way to iterate through a drive folder rather than using just zip files, but we were able to overcome that and get the drive link to work. 

We're proud of the overall design of the "website" and its intended user interface. We unfortunately weren't able to get the actual website working as we spent most of our time figuring out the pose estimation, but we were able to plan out how we would like the user interface to appear. 

We learned a lot about writing code in general. All four of us are relatively new to Hackathons and creating independent projects, so this was a nice learning experience overall. 

We are thinking of fully developing this project in the future with more time, as we are genuinely passionate about using AI as a tool for artists rather than something to replace them entirely. 

# Google Colab Disclaimers
Sometimes the image may fail to load if selecting an image from your files- this is likely due to the uploaded file size or browser issues. Please try again with a smaller, or use a URL instead


# Image Compare Disclaimer
please make sure to run the following commands in terminal before: 
- pip install opencv-python
- pip install numpy
- pip install Pillow
if that doesnt work still, then run these commands in terminal ...
- python3 -m pip install opencv-python
- python3 -m pip install numpy 
- python3 -m pip install Pillow




