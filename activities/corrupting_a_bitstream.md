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
* Open IMG_3782.jpg in your hex editor. Using what you know about looking up and identifying file signatures, confirm the file type of this file by locating its file signature, and make a note of it somewhere.
* Confirm the file type for PRPR19.docx by locating its file signature, and also make note of it somewhere. Hint: you may need to read up a bit on what a DOCX is and what it is made of to properly confirm this file's signature.

## Task 2
### Corrupt some bitstreams!

***Use the .docx file from Task 1 for the remainder of the activity.***

#### Fundmentally change a file's bitstream using hex and text editors

* Open Terminal (Mac) or PowerShell (Windows)
* Input the cd (“change directory”) command followed by the directory path command to navigate to the location of PRPR19.docx. For example, if I wanted to navigate to my downloads file I would type cd C:\Users\kiddm\Downloads [Enter]
* Rename PRPR19.docx:
  * Mac: mv oldfilename newfilename 
  * Windows: Rename-Item -Path oldfilename -NewName newfilename
* Run a checksum of your file, and then output the checksum to a plain text file.
  * Mac: Run command: md5 filename. To save the checksum to a file, run command:  md5 filename > md5.txt
  * Windows: Run command: Get-FileHash filename -Algorithm md5 | Format-List. To save the checksum to a file, replace | Format-List with > md5.txt
* Open PRPR19.docx in the hex editor
* Confirm the filetype using magic numbers/file signature as you did in Task 1.
* Examine the ASCII text. At first, this may look a bit strange, but look a little closer, as there are some human-readable elements. Can you identify any useful information from the available ASCII text to learn more about this file?
* Anywhere within the ASCII text on the right side, change one letter. Be sure to note exactly where and what you changed, as you will be changing it back later. Tip: Note the byte position (use the "Current Address" feature of the hex editor).
* Save the file.
* Run and output a new checksum text file; name it md5-1.txt.
* Compare your first and second checksums: are they the same? Different?
* Go back to hex editor, change the letter back to the original
* Run and output another checksum text file; name it md5-2.txt. Compare all checksums generated so far: are they the same? Different?
* Open the file in Word or Google Docs (if using Google Docs, you will need to import it first). Make a change to the document by deleting or altering a word.
* Run and output a new checksum text file; name it md5-3.txt. Compare the checksums again.
* Open the file in Word again and undo the change you made. Save the file (if you used Google Docs, make sure to export it as a DOCX file, and overwrite the original file you imported).
* Run and output another checksum text file; name it md5-4.txt. Compare the checksums again.

## Submission instructions
Submit your findings in Brightspace with the following details:
* Magic number/file signature of IMG_3782.jpg. Confirm filetype.
* Magic number/file signature of PRPR19.docx. Confirm filetype.
* List all the checksums you generated:
 * Original
 * Letter change (hex)
 * Letter fixed (hex)
 * Word change (Word or Google Docs)
 * Word fixed (Word or Google Docs)
* Provide a brief summary of any relevant information you are able to pull from ASCII text in hex editor.
* Provide a brief summary of findings from corrupting the bitstream of your file in both the text and hex editors.
