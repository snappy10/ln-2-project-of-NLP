# Import the required module for text 
# to speech conversion

from PIL import Image
from pytesseract import pytesseract
from gtts import gTTS


# play the converted audio
import os

# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract"
image_path = r"C:\Users\Admin\Downloads\L2-project-template-main (7)\L2-project-template-main\imagetext.jpg"

# Opening the image & storing it in an image object
img = Image.open(image_path)

# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract
text=pytesseract.image_to_string(img)
language="en"

# Passing the image object to image_to_string() function
# This function will extract the text from the image


  
# Language in which you want to convert
  

myobj=gTTS(text=text,lang=language,slow=False) 
  
# Saving the converted audio in a mp3 file named
# welcome 


  
myobj.save("welcome.mp3")
os.system("welcome.mp3")