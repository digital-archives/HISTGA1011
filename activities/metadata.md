---
title: Digital Preservation Metadata
layout: default
parent: Weekly Activities
nav_order: 7
has_children: false
---

# Digital Preservation Metadata

## Introduction
This activity entails annotating a Metadata Encoding and Transmission Standard (METS) record for one item. The purpose of the assignment is to learn how the elements of a METS record work together, how preservation metadata derived from the PREservation Metadata Implementation Strategies (PREMIS) can be used to document preservation activities and changes to the item over time, and how METS and PREMIS work together.

To do this activity, you will save a Library of Congress sample METS record locally and annotate it to describe its structure. The net result of the activity is a demonstration of the capability to “read” METS and PREMIS records and explain what the digital preservation is and what has happened to it over time.

## Preparation

- You will need to use some sort of text editing program or application to annotate the data. Suggested text editors that you may download are Notepad++ (Windows) or Sublime (Mac or Windows). It doesn't have to be fancy, but should be capable of displaying structured data in a way that isn't too chaotic.
- If you do not have a text editor or are not comfortable downloading one of the previously mentioned text editor programs, you can save the METS as an XML file to your computer, upload it to your Google Drive, and open it within Drive to edit.
- Additionally, it will be good to have the <a href="https://www.loc.gov/standards/mets/" target="_blank">METS</a> and <a href="https://www.loc.gov/standards/premis/" target="_blank">PREMIS</a> standards documents up your browser to reference when performing this activity.

## Steps to Take

1. Save this [METS file](http://www.loc.gov/standards/premis/louis-2-1-mets.xml) locally by opening it in a separate web browser tab, right-clicking anywhere within the text, and selecting “Save As.” When saving, make sure that you are saving it as an XML file by selecting “XML” from the list of file formats available.

2. Open the METS XML file using the text editing program of your choice.

3. Within the text editor, compare the METS record for your item with the [METS Schema 1.12.1](https://www.loc.gov/standards/mets/mets-schemadocs.html) (current version), [METS Primer](https://www.loc.gov/standards/mets/METSPrimer.pdf), and other documentation on the METS website. The goal of this first step is to get comfortable with METS tags, to figure out which elements of the METS schema are included in the record and which might be missing.

4. Annotate the METS record by identifying all the major (and sub-) elements listed below and also commenting on the additional items I listed. Not all the elements are in the record, so make sure to comment on the missing ones. For repeating elements, you do not need to identify each, but add a single comment to explain. The syntax for inline annotations in XML is: `<!-- Your Comment Goes here -->`.

5. A lot of this work is best done by doing an in-document search. For most text editors this can be initiated by the "Find" command and inputting a keyword (shortcuts are typically Command + F on a Mac, Ctrl + F on Windows).

**Find and annotate the following**
- Within the header (very top) of the file, indicate which version of 1.) METS, 2.) PREMIS and 3.) MODS used throughout the file.
- Descriptive metadata section `<dmdSec>` 
  - Indicate what descriptive standard the METS uses.
  - Using the descriptive metadata found within this section, tell me more about the thing being preserved and described. Based on this metadata, try and find a link out to the public-facing LOC record.
- Does the record include any `<mdWrap>` sections? (To answer this question in the XML, add your answer to the first `<mdWrap>` element found. If you cannot find any `<mdWrap>` elements, leave your annotation at the very top of the document).
  - If you find any `<mdWrap>` elements, comment out one and tell me morea bout what you think this element is "wrapping".
- Locate the administrative metadata section `<amdSec>`. Locate and annotate the beginning of this section, and then locate and annotate the end of this section. Within `<amdSec>`, locate and annotate:
  - All `<techMD>` opening tags.
  - Locate at least three `<digiprovMD>` tags and nested within each, their corresponding PREMIS event. For each, tell me what happened.
- Locate `<fileSec>`. Investigate the structure of this section. How many and what type of files does it list here?
  - Within the `<fileSec>` section, find the nested `<mets:file>` tag and within it, the `AMDID` attribute. Choose one of the attributes listed here and describe its connection between other sections of this file. 
- Locate and annotate the beginning of the `<structMap>` section.
  - Describe the relationship here between the `<structMap>` and `<fileSec>` sections (hint: look at the attributes of nested elements).

## Submit Assignment
Attach your annotated METS record as .xml in Brightspace.

## Resources
The following are links to websites with relevant documentation:
- METS: [http://www.loc.gov/standards/mets/](http://www.loc.gov/standards/mets/)
- PREMIS: [http://www.loc.gov/standards/premis/](http://www.loc.gov/standards/premis/)
- PREMIS in METS: [http://www.loc.gov/standards/premis/premis-mets.html](http://www.loc.gov/standards/premis/premis-mets.html)
