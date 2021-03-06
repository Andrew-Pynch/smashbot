# NOTICE:
I have to pause development on this while waiting for some dependencies to improve their stability. Specifically,
- [Project Slippi](https://github.com/project-slippi/project-slippi)
    - Fork of dolphin emulator with some cool functionality
- [Libmelee](https://github.com/altf4/libmelee)
    - High level API for interfacing with project slippi

Both of these are extremely unstable in their current forms. Experimentation is difficult with regular seg faults etc.
I will return to this project when these codebases have their next major release (probably this summer according to the devs)

# smashbot

SOTA SSBM A.I Trained with Reinforcement Learning &amp; Deep Learning Techniques

This will be my agent in a couple of weeks / months ;-) 

![img](https://github.com/Andrew-Pynch/smashbot/blob/master/visualizations/source.gif?raw=true)

# Getting Started
If you want to try this out for yourself, get started by running
```sh
pip3 install -r requirements.txt
```

# Planned architecture
Previous approaches have enabled hard coded predefined movesets for a learner to
take. This might involve hard coding the exact inputs for a wavedash etc. Additionally, previous approaches all have relied on directly reading from an
emulators memory to represent the game state. Last time I checked, humans aren't 
reading bits and bytes and of emulator memory to play smash

My plan is as follows. Break down the problem of playing smash into one similar to what a human does. Have "hydra" models all operating on the same base architecture 
performing many tasks. One such task might be to try and predict the score of either player from pixel data only. Another might be to predict the either players %damage 
in the next n frames. The point is this, I will rely purely on vision to play this 
game. 

# TODO

* [X] Get libmelee installed - NOTE: This is just to send inputs
* [X] Faster way to get pixel data than pyautogui. Screenshots take 100ms. Might
need to switch to windows and use win32lib-grab_screen function I have...
This one actually turned into a library [repolink](https://github.com/Andrew-Pynch/scalary)
* [ ] Programmatically take actions just to validate I can properly send inputs
to the emulator
* [ ] Implement [curiosity driven exploration by self supervised prediction](https://pathak22.github.io/noreward-rl/resources/icml17.pdf). This paper provides great direction for this project if implemented properly :D`

# The two routes
Once we have a way to detect player health 
(remember, we are determined to do this purely through vision, no reading the emulators memory!), and a way to "see" the game world, there emerges two possible framings for this problem

## 1.) Perception Task
* [ ] Build that model predicts both players health in the next n based off of the pixel
data and the models suggested actions for the next n frame (maybe we give 10 possible
outputs we might take, get a prediction for each then take the action that maximizes 
enemy damage while minimizing our damage??)

## 2.) R.L Task
* [ ] Build model that takes in pixel data and damage prediction models predictions, 
and learns the best outputs through policy gradients or other SOTA techniques in RL?

# Sources

### Dolphin install - [Project Slippi Linux](https://github.com/project-slippi/Slippi-FM-installer)



