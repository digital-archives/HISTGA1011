---
title: Breaking Bag(It)
layout: default
parent: Weekly Activities
nav_order: 9
has_children: false
---

# Breaking Bag(It)

## Introduction
This activity introduces students to the [Library of Congress BagIt Specification](https://datatracker.ietf.org/doc/html/rfc8493). Specifically, it provides experience in creating a bag, reviewing its contents, and troubleshooting a "broken" bag.

## Steps

### 1. Upload Bag Contents

Typically, bags are created automatically through a script (e.g., [bagit-python](https://github.com/LibraryOfCongress/bagit-python) or a software application (e.g., [Bagger](https://github.com/LibraryOfCongress/bagger). For this activity, you’ll manually submit your bag’s contents.

- Open the [Breaking Bag Google Drive folder](https://drive.google.com/drive/folders/1U1Va5o9ksyrg5yBtqL8RAOe5Y8OttCwX?usp=sharing) and create a folder titled with your name (e.g., `mary_kidd`).
- Within your personal folder, create a subfolder named `files`.
- Upload at least five files into the `files` folder. These can be any small files you choose (please avoid large files such as movies, as I will download these files to create your bag).

### 2. Bag Creation

After I receive your files, I will use the bagit-python script on my computer to create your bag. I’ll upload two versions of this bag to your folder in Google Drive:

1. **Your good bag** – named `yourfirstname_yourlastname_bag`
2. **Your broken bag** – named `yourfirstname_yourlastname_bad`

These will allow you to compare a valid bag with an intentionally corrupted one.

### 3. Review Each Bag

Once I email you that your bags are ready, open both the good and bad versions. Your task is to examine the contents of each bag and identify any differences. Some changes may be obvious (e.g., an altered sentence in a document), while others may be subtle.

### 4. Discuss Your Findings

Come prepared for Week 3's class to discuss your observations. Key questions to consider:
- What made the bad bag invalid?
- What did you examine to find this out?
- What new insights did you gain about bags and the BagIt specification?
