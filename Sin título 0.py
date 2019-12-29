

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:21:24 2019
@author: daniel
"""

# importing speech recognition package from google api 
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
  
num = 1
def assistant_speaks(file): 
    global num 
  
    # num to rename every audio file  
    # with different name to remove ambiguity 
    #num += 1
    #print("PerSon : ", output) 
  
    #toSpeak = gTTS(text = output, lang ='es', slow = False) 
    # saving the audio file given by google text to speech 
    #file = str(num)+".mp3"  
    #toSpeak.save(file) 
      
    # playsound package is used to play the same file. 
    playsound.playsound(file, True)  
    #os.remove(file) 

# Driver Code 
if __name__ == "__main__": 
    assistant_speaks("PapelCarton.mp3") 