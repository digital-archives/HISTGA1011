---
title: Fixity and Digital Packages
layout: default
parent: Weekly Activities
nav_order: 9
has_children: false
---

# Fixity and Digital Packages

This activity introduces students to essential concepts in digital preservation: fixity and digital packages. Ethan Gates, author of The Patch Bay, wrote two blog posts that provide a nice introduction to the concept of digital packages, and what Bagger (the program you will be installing and using for this activity) is, and what it does. Please give them a read before you start on this activity:
* Gates, Ethan. "Using BagIt." _The Patch Bay: Connecting Preservation and Technology). September 20, 2016. <a href="https://patchbay.tech/blog/2016/09/20/using-bagit/" target="_blank">https://patchbay.tech/blog/2016/09/20/using-bagit/</a>.
* Gates, Ethan. "Using BagIt in 2018." _The Patch Bay: Connecting Preservation and Technology_. December 15, 2017. <a href="https://patchbay.tech/blog/2017/12/15/using-bagit-in-2018/" target="_blank">https://patchbay.tech/blog/2017/12/15/using-bagit-in-2018/</a>.

## Things to know before starting
__Fixity__ involves verifying a file's integrity over time. Regular fixity checks are crucial to ensure the files remain unaltered and uncorrupted during their lifecycle in a digital preservation repository.

__Digital Packages__ refer to the practice of grouping interrelated files into folders for preservation. The importance of this concept led to the creation of the BagIt Specification by the Library of Congress. This specification provides guidelines for organizing digital preservation packages, referred to as "bags." Bags may be used to form digital packages that we learned about, such as SIPs, AIPs and DIPs.

Ethan Gates, author of The Patch Bay, wrote two blog posts that provide a nice introduction to the concept of digital packages, and what Bagger (the program you will be installing and using for this activity) is, and what it does. I've also included an additional blog post, written by Meghan Ferriter, written about the development of the BagIt specification by the Library of Congress. Please give them a read before you start on this activity:

* Gates, Ethan. "Using BagIt." _The Patch Bay: Connecting Preservation and Technology. September 20, 2016. <a href="https://patchbay.tech/blog/2016/09/20/using-bagit/" target="_blank">https://patchbay.tech/blog/2016/09/20/using-bagit/</a>.
* Gates, Ethan. "Using BagIt in 2018." The Patch Bay: Connecting Preservation and Technology. December 15, 2017. <a href="https://patchbay.tech/blog/2017/12/15/using-bagit-in-2018/" target="_blank">https://patchbay.tech/blog/2017/12/15/using-bagit-in-2018/</a>.
* Ferriter, Meghan. "BagIt at the Library of Congress." The Signal. April 4, 2019. <a href="https://blogs.loc.gov/thesignal/2019/04/bagit-at-the-library-of-congress/" target="_blank">https://blogs.loc.gov/thesignal/2019/04/bagit-at-the-library-of-congress/</a>

## Steps

### Install bagger

Bagger is an open-source software application developed by the Library of Congress. It provides a graphical user interface (GUI) that can be used to create and manage bags.

1. Follow the steps listed in the <a href="https://archives.ncdcr.gov/bagger-gui-user-guide/open" target="_blank">North Carolina Department of Natural and Cultural Resources Bagger GUI User
Guide</a>. Installation instructions can be found on pages 4-9. Please follow the instructions specific to your Windows or Mac operating system.
2. Once installed, open the Bagger application (instructions for what file to open, and what to expect when opening, are on Page 6 of the <a href="https://archives.ncdcr.gov/bagger-gui-user-guide/open" target="_blank">NC User Guide</a>).

### Create a bag
4. With Bagger open click the "+Create New Bag" button in the upper left-hand corner of the screen. This will generate the "New Bag Dialog" window. In the "Select Profile:" drop-down, choose the "SANC-state" profile (this stands for "State Agency North Carolina - State"). Click OK.
5. Notice how in the Bag Info section are now a list of fields; some are marked "R" (for required). Review  the list of field names and descriptions on pages 12-15 of the <a href="https://archives.ncdcr.gov/bagger-gui-user-guide/open" target="_blank">NC User Guide</a>.
6. In the "Bag Info" section, fill out the required fields using made-up information. You may also fill out non-required fields, too, if you wish.
7. In the "Payload" section of the application, click on the little green plus sign to navigate to, select and choose some files to add to your bag. Choose any files you have on hand of any format, keeping in mind that larger files will result in longer bag creation time (note: the file navigator is a little wonky. To get to your home folder, click on the house-shaped icon; it will automatically navigate you to your home folder). As you add files, they will appear listed in the Payload section. 
8. Save the bag by clicking "Save Bag as..." in the upper right-hand part of the application. This will generate the Save Bag Dialog window. Give the bag a name like my_first_bag or whatever you wish. 
9. Click the Browse button and navigate to your desktop (an easy way to get there is to click on the little house-shaped icon, then double-clicking into your "Desktop" folder).
10. Type in bag into the File Name: field. Then click Save.
11. Make sure "Generate Tag Manifest?" and "Generate Payload Manifest?" are both checked, and beneath each select "sha256" for the Tag Manifest and Payload Manifest algorithms.
9. Click OK to finalize creating and saving your bag. Please note, Bagger was made for Windows in mind. Unfortunately, this means that Mac users may encounter some weird errors when saving bags, including a weird error message that implies your bag couldn't be saved. However, this is a false error message: If you look on your desktop, your bag folder should be there.
10. Click the "Open Existing Bag" button at the top of the Bagger screen. Select the bag folder you just created.
11. Notice that in the Tag Files section, there are a few additional files listed that weren't there when you first created the bag: i.e. manifest-sha256.txt.
12. Click the "Validate Bag" button. This will validate your bag against the bag profile you select (SANC-state). If you forgot to fill out a required field, at this point, Bagger would tell you. If your bag validates, you will get a message that it validated successfully.

### Submit your result
After completing the comparison, submit your activity report in Brightspace. In it, please answer the following questions:
13. How does Bagger facilitate the creation and management of digital bags?
14. Explain the significance of the SANC-state profile in creating digital bags. How does it compare to other profiles listed?
15. What are some potential challenges or limitations encountered while using Bagger for bag creation? (refer to Ethan's blog posts, mentioned at the beginning of this activity document)
