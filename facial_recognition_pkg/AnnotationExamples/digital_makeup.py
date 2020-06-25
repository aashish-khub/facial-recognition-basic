#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:48:56 2020

@author: aashishk29
"""

from PIL import Image, ImageDraw
import face_recognition as frec

# Load the jpg file into a numpy array
image = frec.load_image_file("McConnell.jpg")


# Find all facial features in all the faces in the image
face_landmarks_list = frec.face_landmarks(image)

pil_image = Image.fromarray(image)
for face_landmarks in face_landmarks_list:
    d = ImageDraw.Draw(pil_image, 'RGBA')

    # Make the eyebrows into a nightmare
    d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
    d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
    d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
    d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)

    # Gloss the lips
    d.polygon(face_landmarks['top_lip'], fill=(0, 0, 0, 128))
    d.polygon(face_landmarks['bottom_lip'], fill=(0, 0, 0, 128))
    d.line(face_landmarks['top_lip'], fill=(0, 0, 0, 64), width=8)
    d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)

    # Sparkle the eyes
    d.polygon(face_landmarks['left_eye'], fill=(255, 0, 0, 255))
    d.polygon(face_landmarks['right_eye'], fill=(255, 0, 0, 255))

    # Apply some eyeliner
    d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
    d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=6)

#    d.polygon([(142,349),(409,349),(409,82),(142,89)],fill=(0,0,0,100))
    pil_image.show()