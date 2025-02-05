---
title: Corrupting a Bitstream
layout: default
parent: Weekly Activities
nav_order: 3
has_children: false
---

# Corrupting a Bitstream

## Introduction
The goal of the "Corrupting a Bitstream" exercise is to introduce you to using a hex editor to analyze file signatures, perform checksums, and make controlled modifications to files. By exploring the impact of altering data at the byte level, you will be able to observe changes in checksums and file behavior.

## Setup instructions:
* In your browser, open:
  * [HexEd.it](https://hexed.it/)
  * [MD5 Checksum Generator](https://emn178.github.io/online-tools/md5_checksum.html)
  * Download all <a href="https://drive.google.com/drive/folders/1UzQbxCrIcE0LhKNi7QImC4YryopubrKB?usp=sharing" target="_blank">Activity Files</a> locally: 1.) IMG_3782.jpg and 2.) PRPR19.docx

## Task 1
#### Identify format types
* Open IMG_3782.jpg in HexEd.it (to do this, click the "Open File" button at the top of the window and select the JPG file to load it).
* In a separate tab, open up [PRONOM](https://www.nationalarchives.gov.uk/pronom/). Use the PRONOM Search feature to look up the format registry profile for a JPG file; look up and note the characteristics of a JPG internal file format signature.
* Back in HexEd.it, find the file signature in the positions indicated by PRONOM.
* Take these same steps with PRPR19.docx: Load it into HexEd.it, look up information DOCX in PRONOM, and locate its file signature within the hex data. Hint: You will see this will not be as easy as looking up the signature of a JPG. You will need to read up on DOCX files on Wikipedia, or other resources, to figure out what a DOCX is really made of, to figure out its signature.

## Task 2
### Corrupt some bitstreams!

**Use the .docx file from Task 1 for the remainder of the activity.**

#### Fundamentally change a file's bitstream using hex and text editors

1. Use Finder or File explorer to manually rename your DOCX file to something different ([Windows] Right-click or [Mac] Ctrl+click, select "Rename")
2. Generate a checksum for PRPR19.docx and note it somewhere (tip: Store this, and subsequent checksums, in a text file, as a sort of "running log" of checksums generated. You'll be generating a bunch of checksums for this exercise and comparing them.)
3. With PRPR19.docx open in HexEd.it, examine the ASCII text to the right of the hex values. There will be some human-readable elements. Can you identify any useful information from the available ASCII text to learn more about this file?
4. Change 2-3 letters within the ASCII text. Note the letters you changed, and their byte positions using the "Current Address" feature (you can find the current address in the left-hand most pane; scroll about half-way down).
5. Save the DOCX file using the "Save As" button at the top of HexEd.it.
6. Run and output a new checksum for PRPR19.docx. Compare your original and newest checksum values. Are they the same or different?
7. Change the letters back to what they were originally in the hex editor.
8. Run and output another checksum. It should match your original checksum.
9. Lastly, I would like you to choose your own file to examine with HexEd.it (what might be fun is looking back on the Data Object you explored in Week 1, but you can also just choose whatever you wish). Make sure whatever you choose is not a DOCX or JPG file. Also, you will need a "sample" file to work with here, meaning:
  - You will need to have a file on-hand to load in HexEd.it.
  - ⚠️ _I highly recommend that if you are working with your own files, to **first make a copy of the file**, place it in a separate folder, and load that into HexEd.it. This will help you avoid inadvertently editing your own files by mistake! You may also choose to work with a file you download from the web. I would recommend [https://commons.wikimedia.org/wiki/Main_Page](Wikimedia Commons); scroll down to Content and unroll "By type", where you can browse through and download a variety of different file types)._
10. Search for your chosen file within PRONOM, look up its file signature characteristics, and then use HexEd.it to locate the signature, and make observations of any other data you see displayed.

## Submission instructions
Submit your findings in Brightspace with the following details:
* How did this activity go for you, in general?
* What file format did you choose for steps 9 and 10? For your chosen file, please answer:
  - What are the characteristics of its file signature (sometimes also called "magic number")?
  - Were you able to locate its signature within HexEd.it?
  - Were there other interesting artifacts you found, such as human-readable metadata within the ASCII details that you saw in HexEd.it? What were they?

## Share your findings
Next week, we will discuss your chosen file format types, and how that went for you in HexEd.it.