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
    * Windows: Use the keyboard shortcut Windows + R. In the window that appears, type "cmd" (without quotes) and then press Enter.
  * Download <a href="https://drive.google.com/drive/folders/1UzQbxCrIcE0LhKNi7QImC4YryopubrKB?usp=sharing" target="_blank">Activity Files</a> locally: 1.) IMG_3782.jpg and 2.) PRPR19.docx

## Task 1
#### Identify format types
* Open IMG_3782.jpg in your hex editor. Use your knowledge to look up and identify file signatures. Confirm the file type of this file by locating its file signature and make a note of it.
* Confirm the file type for PRPR19.docx by locating its file signature. Make a note of this file's type. Hint: you may need to read up on DOCX files and their components to confirm the signature properly.

## Task 2
### Corrupt some bitstreams!

**Use the .docx file from Task 1 for the remainder of the activity.**

#### Fundamentally change a file's bitstream using hex and text editors

1. Open Terminal (Mac) or PowerShell (Windows).
2. Navigate to the location of PRPR19.docx using the `cd` (change directory) command followed by the directory path. For example: `cd C:\Users\kiddm\Downloads` [Enter].
3. Rename PRPR19.docx:
   * Mac: `mv oldfilename newfilename`
   * Windows: `Rename-Item -Path oldfilename -NewName newfilename`
4. Run a checksum of your file and output the checksum to a plain text file.
   * Mac: Run command: `md5 filename`. To save the checksum to a file: `md5 filename > md5.txt`
   * Windows: Run command: `Get-FileHash filename -Algorithm md5 | Format-List`. To save the checksum to a file, replace `| Format-List` with `> md5.txt`
5. Open PRPR19.docx in the hex editor.
6. Confirm the file type using magic numbers/file signature as in Task 1.
7. Examine the ASCII text. Look closer for human-readable elements. Can you identify any useful information from the available ASCII text to learn more about this file?
8. Change one letter within the ASCII text on the right side. Note the byte position using the "Current Address" feature of the hex editor.
9. Save the file.
10. Run and output a new checksum text file; name it md5-1.txt.
11. Compare your first and second checksums. Are they the same or different?
12. Change the letter back to the original in the hex editor.
13. Run and output another checksum text file; name it md5-2.txt. Compare all checksums generated so far.
14. Open the file in Word or Google Docs (if using Google Docs, import it first). Make a change to the document by deleting or altering a word.
15. Run and output a new checksum text file; name it md5-3.txt. Compare the checksums again.
16. Open the file in Word again and undo the change you made. Save the file.
17. Run and output another checksum text file; name it md5-4.txt. Compare the checksums again.

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
* Provide a brief summary of any relevant information you are able to pull from ASCII text in the hex editor.
* Provide a brief summary of findings from corrupting the bitstream of your file in both the text and hex editors.
