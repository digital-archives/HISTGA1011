---
title: Fixity and Digital Packages
layout: default
parent: Weekly Activities
nav_order: 9
has_children: false
---

# Fixity and Digital Packages

This activity introduces students to essential concepts in digital preservation: fixity and digital packages. Ethan Gates, author of The Patch Bay, wrote two blog posts that provide a nice introduction to the concept of digital packages, and what Bagger (the program you will be installing and using for this activity) is, and what it does.

## Things to know and review before starting this activity
__Fixity__ involves verifying a file's integrity over time. Regular fixity checks are crucial to ensure the files remain unaltered and uncorrupted during their lifecycle in a digital preservation repository.

__Digital Packages__ refer to the practice of grouping interrelated files into folders for preservation. The importance of this concept led to the creation of the BagIt Specification by the Library of Congress. This specification provides guidelines for organizing digital preservation packages, referred to as "bags." Bags may be used to form digital packages that we learned about, such as SIPs, AIPs and DIPs.

Ethan Gates, author of The Patch Bay, wrote two blog posts that provide a nice introduction to the concept of digital packages, and what Bagger (the program you will be installing and using for this activity) is, and what it does. I've also included an additional blog post, written by Meghan Ferriter, written about the development of the BagIt specification by the Library of Congress. Please give them a read before you start on this activity:

* Gates, Ethan. "Using BagIt." _The Patch Bay: Connecting Preservation and Technology. September 20, 2016. <a href="https://patchbay.tech/blog/2016/09/20/using-bagit/" target="_blank">https://patchbay.tech/blog/2016/09/20/using-bagit/</a>.
* Gates, Ethan. "Using BagIt in 2018." The Patch Bay: Connecting Preservation and Technology. December 15, 2017. <a href="https://patchbay.tech/blog/2017/12/15/using-bagit-in-2018/" target="_blank">https://patchbay.tech/blog/2017/12/15/using-bagit-in-2018/</a>.
* Ferriter, Meghan. "BagIt at the Library of Congress." The Signal. April 4, 2019. <a href="https://blogs.loc.gov/thesignal/2019/04/bagit-at-the-library-of-congress/" target="_blank">https://blogs.loc.gov/thesignal/2019/04/bagit-at-the-library-of-congress/</a>

## Steps

### Install bagger
For this activity, you will be installing and using Bagger. Bagger is an open-source software application developed by the Library of Congress to create and manage digital packages via a graphical user interface (GUI).

- Follow the steps listed in the <a href="https://archives.ncdcr.gov/bagger-gui-user-guide/open" target="_blank">North Carolina Department of Natural and Cultural Resources Bagger GUI User
Guide</a>. Installation instructions can be found on pages 4-9. Please follow the instructions specific to your Windows or Mac operating system.
- Once installed, open the Bagger application (instructions for what file to open, and what to expect when opening, are on Page 6 of the <a href="https://archives.ncdcr.gov/bagger-gui-user-guide/open" target="_blank">NC User Guide</a>).

### Create a bag
- With Bagger open click the "+Create New Bag" button in the upper left-hand corner of the screen. This will generate the "New Bag Dialog" window. In the "Select Profile:" drop-down, choose the "SANC-state" profile (this stands for "State Agency North Carolina - State"). Click OK.
- Notice how in the Bag Info section are now a list of fields; some are marked "R" (for required). Review  the list of field names and descriptions on pages 12-15 of the <a href="https://archives.ncdcr.gov/bagger-gui-user-guide/open" target="_blank">NC User Guide</a>.
- In the "Bag Info" section, fill out the required fields using made-up information. You may also fill out non-required fields, too, if you wish.
- In the "Payload" section of the application, click on the little green plus sign to select and choose some files to add to your bag. Choose any files you have on hand on your computer you wish to put into the bag, keeping in mind that larger files will result in longer bag creation time (Note: the file navigator is a little wonky and may start you in the C:\ folder. To get to your home folder where your Downloads and Desktop folders likely are, click on the little house-shaped icon).
- Save the bag by clicking "Save Bag as..." in the upper right-hand part of the application. This will generate the Save Bag Dialog window. Give the bag a name like my_first_bag or whatever you wish. 
- Click the Browse button and navigate to your desktop (an easy way to get there is to click on the little house-shaped icon, then double-clicking into your "Desktop" folder).
- Type in bag into the File Name: field. Then click Save.
- Make sure "Generate Tag Manifest?" and "Generate Payload Manifest?" are both checked, and beneath each select "sha256" for the Tag Manifest and Payload Manifest algorithms.
- Click OK to finalize creating and saving your bag (note: Bagger was made for Windows operating systems. Unfortunately, this means that Mac users may encounter some weird errors when saving bags, including a message that implies your bag couldn't be saved. However, this is a false error message: If you look on your desktop, your bag should be there)

### Open and validate a bag
- Click the "Open Existing Bag" button at the top of the Bagger screen. Select the bag folder you just created.
- Notice that in the Tag Files section, there are a few additional files listed that weren't there when you first created the bag: i.e. manifest-sha256.txt.
- Click the "Validate Bag" button. This will validate your bag against the bag profile you select (SANC-state). If you forgot to fill out a required field, at this point, Bagger would tell you. If your bag validates, you will get a message that it validated successfully.
- Click on the files listed in the Tag Files section, and for each, click the "Click to view the tag files" button (looks like a tiny piece of paper). This will open the Tag Files window; use the tabs at the top to click into the bag-info.txt, tagmanifest-sha256.txt, manifest-sha256.txt, bagit.txt and data files). Close this window when you are done.

### Breaking Bag
- Using your File Explorer (Windows) or Finder (Mac), navigate to the bag. Open the "bag-info.txt" file in a text editor.
- Change the value that appears next to Profile Name: from "SANC-state" to "NYPL". Save the file.
- Go back to the Bagger application and click the "Validate Bag" button. Notice if an error message comes up.
- Again, using your File Explorer (Windows) or Finder (Mac), navigate to the bag. Open the "bag-info.txt" file in a text editor and change the value next to Profile Name back to "SANC-state". Save the file, and try to revalidate the bag again.

### Submit your result
After completing the comparison, submit your activity report in Brightspace. In it, please answer the following questions:
1. How does Bagger facilitate the creation and management of digital bags?
2. Explain the significance of the SANC-state profile in creating digital bags. How does it compare to other profiles listed?
3. When you were "breaking the bag", what sort of error message did you get? What do you think was happened? Hint: Look at the "Console" section of Bagger, which contains an activity log.
4. What are some potential challenges or limitations encountered while using Bagger for bag creation? (refer to Ethan's blog posts, mentioned at the beginning of this activity document)
