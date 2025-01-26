---
title: Breaking Bag(It)
layout: default
parent: Weekly Activities
nav_order: 4
has_children: false
---

# Breaking Bag(It)

## Introduction
This activity revolves around the Open Archival Information System (OAIS), information packages, and the [Library of Congress BagIt Specification](https://datatracker.ietf.org/doc/html/rfc8493).

In this activity:
- You will first act as the "producer" (as defined by the OAIS model) and take the first steps to prepare a **Submission Information Package (SIP)**.
- For this exercise, your SIP will be implemented using the BagIt specification. Think of your BagIt bag as a concrete example of a SIP (note, SIP and bag, for this activity, will be used interchangeably)
- Once you've prepped your SIP (bag), you will hand it over to me for processing. I will create:
  1. A valid BagIt-conforming SIP (good bag).
  2. A deliberately altered, broken SIP (bad bag).

Your goal will be to troubleshoot and document what went wrong with the bad bag.

## Steps

### 1. Upload bag contents

- Open the [Breaking Bag Google Drive folder](https://drive.google.com/drive/folders/1U1Va5o9ksyrg5yBtqL8RAOe5Y8OttCwX?usp=sharing) and within it, create a new folder titled your first name, underscore, and last name (e.g., `mary_kidd`).
- Within your personal folder, create a subfolder within it and title it `files`.
- Upload _at least_ five files of your choice to your `files` folder. These can be any files you want (please avoid large files like audio/video files, if possible!)

### 2. Bag Creation

- Once you have created your folders and uploaded files into it, let me know (if we are in class, let me know verbally; otherwise, if this happens outside of class, send me an email).
- I will use the [bagit-python](https://github.com/LibraryOfCongress/bagit-python) script on my computer to transform your folder into a BagIt-compliant Submission Information Package (SIP).
- I will upload **two versions** of your newly-minted SIPs/bags to your Google Drive folder, to allow you to compare a valid SIP/bag with an intentionally corrupted one:
1. **Your good SIP/bag** – named `yourfirstname_yourlastname_good_bag`
2. **Your broken SIP/bag** – named `yourfirstname_yourlastname_bad_bag`

### 3. Review Each Bag
- I will notify you (either verbally in class, or by email) that your SIPs/bags are ready. Once this happens, open both the good and bad SIPs/bags. Your task is to examine the contents of each and try to identify how they are broken.
- Some changes may be obvious, while others may be subtle. You may need to look at certain files within the SIP/bag, like the manifest, to determine what went wrong.

### 4. Submit your activity summary in Brightspace

In the Assignments section of Brightspace, please submit answers to the following questions:
- What do you think I altered?
- What did you examine to figure this out? What clues did you find that told you something went wrong?
- _Optional:_ If you couldn't find exactly what went wrong, were there any differences, in general, between the two SIP/bags, that you noticed? What were they?
- From a broader perspective, what rules or policies might a repository put in place to ensure data submitted to it is in tact?

### 5. Discuss your findings in class

Come prepared for Week 3's class to spend 2-3 minutes discussing your experience investigating what went wrong. I will also reveal to you what I altered, so you can compare your findings with my doings!