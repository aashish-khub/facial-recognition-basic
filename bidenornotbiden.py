import numpy as np
import matplotlib.pyplot as plt
import face_recognition as frec
import os

SERIALIZEDDIRECTORY = "encodings/"


class Person():
    name = None
    encoding = None
    trainingSet = None
    
    def __init__(self,personName):
        self.name = personName
        self.encoding = None
        self.trainingSet = []
        
    def addImage(self,fileName):
        img = frec.load_image_file(fileName)
        self.trainingSet.append(img)
    
    def encode(self):
        self.encoding = frec.face_encodings(self.trainingSet[0])[0]
        #Note: the self.trainingSet[0] is because of the current...
        #       ...approach using just a single training image
        #the second [0] is list->np.arr conv.
    
    def serialize(self):
        np.savetxt(SERIALIZEDDIRECTORY+self.name+".csv", self.encoding,delimiter=",")
    
    def deserialize(self):
        loaded = np.loadtxt(SERIALIZEDDIRECTORY+self.name+".csv",dtype=float,delimiter=",")
        self.encoding = loaded

######################################################################

images = {
        "Joe Biden":           ["PresidentBiden.jpg"],
        "Barack Obama":        ["Obama.jpg"], 
        "Bernie Sanders":      ["Sanders.jpg"],
        "Donald Trump":        ["Trump.jpg"],
        "Elizabeth Warren":    ["Warren.jpg"],
        "Mike Pence":          ["Pence.jpg"],
        "Kamala Harris":       ["Harris.jpg"],
        "Nancy Pelosi":        ["Pelosi.jpg"],
        "Mitch McConnell":     ["CocaineMitch.jpg"]
        }
#The dictionary maps people's names to the set of their known images' filenames
######################################################################


people = []


print("\nLoading faces...")
for name in images.keys():
    p = Person(name)
    for imgPath in images[name]:
        p.addImage(imgPath)
    people.append(p)


print("\nEncoding faces...")
for p in people:
    #First we gotta check if there is a serialized version already available...
    try:
        p.deserialize()
        print(p.name+" face loaded from memory!")
    except OSError as e:
    #if not done yet, encode and save! this saves a TON of time!
        p.encode()
        p.serialize()
        print(p.name + " face encoded, saved!")

#Issues that might (or might not) need fixing:
    # 1. every time you change/del. a training image, you MUST delete the encoded .csv
    # 2. no current support for multiple training images!

######################################################################

#ALL YOU HAVE TO CHANGE NOW IS THIS FILE NAME!

UNKNOWNFILENAME = "unknown0.jpg" #currently we have unknown0/1/2/3.jpg

### 

unknownImage = frec.load_image_file(UNKNOWNFILENAME)
unknownEncoding = frec.face_encodings(unknownImage)

print("\nComparing faces...\n")

plt.imshow(unknownImage)


encodings = [p.encoding for p in people]
names = [p.name for p in people] #seems a bit clanky to me but this comparison method is very odd..

for i in range(len(unknownEncoding)):
    results = frec.compare_faces(encodings, frec.face_encodings(unknownImage)[i])
    if True in results:
        print("Found face:  "+names[results.index(True)])
    else:
        print("Face "+str(i+1)+" not identified")

#TODO: draw rectangles around their faces?