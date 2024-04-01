---
title: Corrupting a Bitstream
layout: default
parent: Weekly Activities
nav_order: 3
has_children: false
---

# Corrupting a Bitstream

## Introduction
The goal of the "Corrupting a Bitstream" exercise is to introduce students to using a hex editor to analyze file signatures, perform checksums, and make controlled modifications to files. By exploring the impact of altering data at the byte level, participants can observe changes in checksums and file behavior. They are also encouraged to extract useful information from the ASCII text and summarize their findings from the exercise.

## Setup instructions:
* Open and use:
  * [HexEd.it](https://hexed.it/) in your browser
  * Terminal
    * Mac: Open Finder > Applications. Find and double-click on Terminal icon.
    * Windows: Use the keyboard shortcut Windows + R. In the window that appears, type in “cmd” (without quotes) and then Enter.
  * Download <a href="https://drive.google.com/drive/folders/1UzQbxCrIcE0LhKNi7QImC4YryopubrKB?usp=sharing" target="_blank">Activity Files</a> locally: 1.) IMG_3782.jpg and 2.) PRPR19.docx

## Task 1
#### Identify format types
* Open IMG_3782.jpg in your hex editor. Using what you know about looking up and identifying file signatures, confirm the file type of this file by locating its file signature.
* Confirm the file type for PRPR19.docx by locating its file signature. Hint: you may need to read up a bit on what a DOCX is and what it is made of to properly confirm this file's signature.

## Task 2
### Corrupt some bitstreams!

#### Use command line to navigate to and change the file
Using the .docx file from Task 1 for the remainder of the activity.
* Open Terminal (Mac) or PowerShell (Windows)
* Use the cd (“change directory”) command followed by the directory path command to navigate to the location of PRPR19.docx. For example, if I wanted to navigate to my downloads file I would type cd C:\Users\kiddm\Downloads [Enter]
* Rename PRPR19.docx:
  * Mac: mv oldfilename newfilename 
  * Windows: Rename-Item -Path oldfilename -NewName newfilename
* Run a checksum of your file, and then output the checksum to a plain text file. Make sure you are in the Desktop directory when you take these steps.
  * Mac: Run command: md5 filename. To save the checksum to a file, run command:  md5 filename > md5.txt
  * Windows: Run command: Get-FileHash filename -Algorithm md5 | Format-List. To save the checksum to a file, replace | Format-List with > md5.txt
* Open PRPR19.docx in the hex editor
* Confirm the filetype using magic numbers/file signature as you did in Task 1.
* Examine the ASCII text. Can you identify any useful information from the available ASCII text to learn more about the file?
* In the ASCII text on the right side, change one letter. Be sure to write down exactly what you did, as you will be changing it back later. Tip: Note the byte position. I.e. “at byte 15548 I changed the C to X”.
* Save file.
* Run and output a new checksum text file. Name it to something distinct like md5-1.txt. Compare your first and second checksums: are they the same? Different?
* Go back to hex editor, change the letter back to the original
* Run checksum on file again. Name it md5-2.txt Compare the checksums: what do you note? Same? Different?
* Open the file in Word. Make a one letter change.
* Run checksum on file. Name it md5-3.txt. Compare the checksums again.
* Open the file in Word again and fix the change you made. Save.
* Run checksum on the file. Name it md5-4.txt
* Compare the checksums: what do you note? Same? Different?

## Submission instructions
Submit your findings in Brightspace with the following details:
* Magic number/file signature of IMG_3782.jpg. Confirm filetype.
* Magic number/file signature of PRPR19.docx. Confirm filetype.
* List all the checksums you generated:
 * Original
 * Letter change (hex)
 * Letter fixed (hex)
 * Letter change (word)
 * Letter fixed (word)
* Brief summary of any relevant information you are able to pull from ASCII text in hex editor.
* Brief summary of findings from corrupting the bitstream of your file.
