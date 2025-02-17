---
title: Corrupting a Bitstream
layout: default
parent: Weekly Activities
nav_order: 2
has_children: false
---

# Corrupting a Bitstream

## Introduction
The goal of the "Corrupting a Bitstream" exercise is to introduce you to using a hex editor to analyze file signatures and evaluate changes made on a bit level, get practice generating and comparing checksums, navigate the PRONOM registry, and make controlled modifications to files.

## Setup instructions:
* In your browser, open these three tools in three separate tabs:
  * <a href="https://hexed.it/" target="_blank">HexEd.it</a>
  * <a href="https://emn178.github.io/online-tools/md5_checksum.html" target="_blank">MD5 Checksum Generator</a>
  * <a href="https://www.nationalarchives.gov.uk/pronom/" target="_blank">PRONOM</a>
* Download all <a href="https://drive.google.com/drive/folders/1UzQbxCrIcE0LhKNi7QImC4YryopubrKB?usp=sharing" target="_blank">activity files</a> locally: 1.) IMG_3782.jpg and 2.) PRPR19.docx

## Task 1
#### Identify format types
1. In your HexEd.it tab, click the **Open File** button at the top of the window and select IMG_3782.jpg from wherever you downloaded it.
2. In your PRONOM tab, use the **Search** feature to look up the format registry profile for the JPG file format; look up and note the characteristics of a JPG internal file format signature.
3. Back in HexEd.it, find the file signature in the positions indicated by PRONOM. Please consult the <a href="https://digital-archives.github.io/HISTGA1011/slides/week_03_slide_deck.html#48" target="_blank">format signature key slide</a> for position acronyms.
4. Repeat steps 1-3 for PRPR19.docx: Load it into HexEd.it, look up information DOCX in PRONOM, and use the file signature details to locate its file signature within the hex data. Hint: You will see this will not be as easy as looking up the signature of a JPG. You will need to read up on DOCX files on Wikipedia, or somewhere else, to figure out what a DOCX is really made of, to figure out its proper signature.

## Task 2
### Corrupt some bitstreams!

#### Fundamentally change a file's bitstream using hex and text editors

1. Generate a checksum for PRPR19.docx and note it somewhere (tip: Store this, and subsequent checksums, in a text file, as a sort of "running log" of checksums generated.)
2. With PRPR19.docx open in HexEd.it, examine the ASCII text to the right of the hex values. There will be some human-readable and non-human readable parts.
3. Using HexEd.it, change 2-3 letters within the ASCII text. Note the letters you changed, and their byte positions using the **Current Address** feature (you can find the current address in the left-hand most pane; scroll about half-way down).
4. Using HexEd.it, save the DOCX file using the "Save As" button at the top of HexEd.it. Name it something like PRPR19-changed.docx, or something that distinguishes it from the original.
5. Run and output a new checksum for your altered DOCX file. Note it. Compare your original and newest checksum values. Are they the same or different?
6. Change the letters back to what they were originally in the hex editor. Re-save the file: you can either overwrite the original file, or name it something like PRPR19-changed_back.docx.
7. Run and output another checksum of the file you changed back. Note it. This checksum should match the checksum of unaltered DOCX.

**Work with a file format of your choice**
Lastly, I would like you to choose your own file (could be your own, or something you've downloaded from the web) to examine with HexEd.it. What might be fun is looking back on a file related to the Data Object you explored in Week 1, but you can also work with whatever you you want. Your choice! (just make sure whatever you choose is not a DOCX or JPG file.)

⚠️ _I highly recommend that if you are working with your own files, to **first make a copy of your file, rename it to something that distinguishes it from the original, place it in a separate folder, and load that into HexEd.it. This will help you avoid inadvertently altering your own files by mistake! You may also choose to work with a file you download from the web. I would recommend downloading a file from [https://commons.wikimedia.org/wiki/Main_Page](Wikimedia Commons); scroll down to Content section and unroll "By type"; here, you can browse through and download a variety of different file types)._

Once you've identified a file to work with, take these steps:
1. Search for your chosen file format within PRONOM and look up its file signature characteristics.
2. Use HexEd.it to locate the signature.
3. There is no need to alter your chosen file in any way, unless you are feeling experimental!

## Submission instructions
Submit your findings in Brightspace with the following details:
* How did this activity go for you?
* What file format did you choose for the last part of the activity? For your chosen file, please answer:
  - What are the characteristics of its file signature per PRONOM? Did you consult any other resources?
  - Were you able to locate its internal signature within HexEd.it?
  - Were there other interesting artifacts you found, such as human-readable metadata within the ASCII text that you noticed in HexEd.it? What were they?

## Share your findings
Next week, please come prepared to discuss your chosen file format types in class.