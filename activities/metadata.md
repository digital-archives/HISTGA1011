---
title: METS and PREMIS Metadata
layout: default
parent: Weekly Activities
nav_order: 2
has_children: false
---

# Weekly Activity: METS and PREMIS Metadata Exercise

## Introduction
This activity entails annotating a Metadata Encoding and Transmission Standard (METS) record for one item. The purpose of the assignment is to learn how the elements of a simple METS record work together and how preservation metadata derived from the PREservation Metadata Implementation Strategies (PREMIS) can be used to document preservation activities and changes to the item over time. The activity involves saving a record containing rich METS records locally and annotating that METS record to describe the major components of the METS record, including PREMIS components. The net result of the activity is a demonstration of the capability to “read” METS and PREMIS records and explain what happened to the item.

## Preparation

- To do this activity, you will need to use a text editing program or application to annotate the data. Suggested text editors that you may download are Notepad++ (Windows) or Sublime (Mac or Windows).

- If you do not have a text editor, you can save the METS as an XML file to your computer, upload it to your Google Drive, and use Drive’s text editor to annotate.

## Steps to Take

1. Save this [METS file](http://www.loc.gov/standards/premis/louis-2-1-mets.xml) locally by opening it in a separate web browser tab, right-clicking anywhere within the text, and selecting “Save As.” When saving, make sure that you are saving it as an XML file by selecting “XML” from the list of file formats available.

2. Open the METS XML file using the text editing program of your choice.

3. Within the text editor, compare the METS record for your item with the [METS Schema 1.12.1](https://www.loc.gov/standards/mets/mets-schemadocs.html) (current version), [METS Primer](https://www.loc.gov/standards/mets/METSPrimer.pdf), and other documentation on the METS website. The goal of this first step is to get comfortable with METS tags, to figure out which elements of the METS schema are included in the record and which might be missing.

4. Annotate the METS record by identifying all the major (and sub-) elements listed below and also commenting on the additional items I listed. Not all the elements are in the record, so make sure to comment on the missing ones. For repeating elements, you do not need to identify each, but add a single comment to explain. The syntax for inline comments in XML is: `<!-- Your Comment -->`.

- **METS**
  - Does the record include `<mdWrap>` or `<mdRef>`?
  - Header `<metsHdr>` 
    1. Indicate version of METS
    2. Indicate version of PREMIS
    3. Indicate version of MODS
  - Descriptive metadata section `<dmdSec>` 
    1. Indicate what descriptive standard the METS uses
  - Administrative `<amdSec>` 
    1. Technical `<techMD>`
    2. Digital Provenance `<digiprovMD>`
    3. Source `<sourceMD>`
    4. Rights `<rightsMD>`
  - File Section `<fileSec>`
    1. Indicate if the File section uses `<FLocat>` (pointer to resource) or `<FContent>` (content in XML).
  - Structural Map `<structMap>`
    1. Indicate if the `<div>` sections contain multiple METS pointers (`<mptr>`) and/or file pointer (`<fptr>`)
  - Structural links `<smLink>` 
  - Behavior `<behavior>` 

- **PREMIS**
  - Objects: What are the objects?
    1. Intellectual Entity
    2. Representation
    3. File
    4. Bitstream
  - Environment
  - Agents: What is the agent? Person, organization, software
  - Events: Comment to indicate what the events are
  - Rights statement 

## Reporting
- Attach your annotated METS record as .xml in Brightspace.

## Resources
The following are links to websites with relevant documentation:
- METS: [http://www.loc.gov/standards/mets/](http://www.loc.gov/standards/mets/)
- PREMIS: [http://www.loc.gov/standards/premis/](http://www.loc.gov/standards/premis/)
- PREMIS in METS: [http://www.loc.gov/standards/premis/premis-mets.html](http://www.loc.gov/standards/premis/premis-mets.html)
