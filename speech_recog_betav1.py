#!/usr/bin/env python
# coding: utf-8

# In[1]:


import speech_recognition as sr


# In[ ]:

print("\n\t███████╗     ██╗\n\t██╔════╝     ██║\n\t███████╗     ██║\n\t╚════██║██   ██║\n\t███████║╚█████╔╝\n\t╚══════╝ ╚════╝\n")

obj = sr.Recognizer()
x = '0'

def check():
    return input("\nDo You want to Try Again or Exit?\nPress 1 for Exit\nPress O to Speak Again\n")

try:
    while(x=='0'):
        with sr.Microphone() as source:
            print("Say Something\nam Listening...")
            audio = obj.listen(source)
            print("Processing....................")
        data = obj.recognize_google(audio)
        print(data)
        x = check()
        if (x != '0'):
            break
except:
    print("\nPlease try again\n")
    pass
    

# In[ ]:




