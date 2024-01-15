---
title: Reproduction Requests
layout: default
parent: Weekly Activities
nav_order: 8
has_children: true
---

# File conversion and renaming activity

### Overview

The goal of this activity is to do some batch processing of images and evaluating their effectiveness/workflows. Mac and PCs have different tools available to them, so please make sure that you are stepping through the directions for your particular operating system.

****

For the activity you will be provided with a group of raw images in a zip file (DA-Sample.zip) taken by a photographer using a copy stand. These images have been transferred to your department to be converted into preservation files and renamed to fit your institution’s file naming schema (provided in the steps below).

****

[Overview](https://docs.google.com/document/d/1bvjKzswnECwDImmV12rntOVgS3PQaQ62cQV-yfBaUNA/edit#heading=h.vy0g9rsjo0vh)

[Assignment Submission Guidelines](https://docs.google.com/document/d/1bvjKzswnECwDImmV12rntOVgS3PQaQ62cQV-yfBaUNA/edit#heading=h.8pn7fkbuavat)

[Setup Instructions](https://docs.google.com/document/d/1bvjKzswnECwDImmV12rntOVgS3PQaQ62cQV-yfBaUNA/edit#heading=h.g0rsqv2foc4u)

[Windows - Steps](https://docs.google.com/document/d/1bvjKzswnECwDImmV12rntOVgS3PQaQ62cQV-yfBaUNA/edit#heading=h.d62c30f3nhh0)

[Mac - Steps](https://docs.google.com/document/d/1bvjKzswnECwDImmV12rntOVgS3PQaQ62cQV-yfBaUNA/edit#heading=h.17cpzhltivkh)


### Assignment Submission Guidelines

Submit your final folder through Brightspace containing the following content:

1. A single text file noting:

   - Original format type and dpi

   - Preservation file format type, bit depth, dpi

   - Note any challenges/difficulties/problems you encountered (if any) and if you were able to output your preferred preservation file format and image quality following best practices.

   - Answer this question: Pretend that your next project is to create a new group of access files, and include them in your batch. How would you go about batch renaming these files?

2. 5 preservation files with correct file naming


### Setup Instructions

All files and materials can be found in the shared [Assignments and Activities](https://drive.google.com/drive/folders/1m_74KkdORh17jdqxcDw7HrbuRk0QV58e?usp=sharing) > [File Conversion and Renaming Exercise](https://drive.google.com/drive/folders/12FacixHm5b3fqJAGoXPHkX_rk729M-eJ?usp=sharing) folder.

****

If you are using Windows, download and install Irfanview and Bulk Rename Utility programs. If you are using a Mac, you do not have to download any programs.

- **Install Irfanview:**

  - Open <https://www.irfanview.net/>.

  - Select “Download” from the top menu (select 32- or 64-bit).

    - Select 32-bit (even if you are working with a 64-bit system)

    - Click the link for FossHub - download IrfanView and PlugIns

    - In the download page, click on each of these items to download both the program and the plugin package (make sure to select either 32-bit or 64-bit, depending on your system):

      - Irfanview ##-bit Windows installer 

      - Irfanview All Plugins - ##-bit Windows Installer

    - Double-click on the Irfanview EXE file to launch the installer. Once installed, close the program.

    - Double-click on the Irfanview plugins EXE file to launch the installer.

- **Install Bulk Rename Utility:** 

  - Open <https://www.bulkrenameutility.co.uk/>

  - Click the “Free Download” button

  - Click the “Install Bulk Rename” Utility button

  - Double-click the BRU\_setup\_3.4.4.0.exe to launch the installer.


### Windows - Steps

**Batch convert files using Irfanview**

_You will use the free tool Irfanview to bulk convert 63 image files from their raw file format to a preservation file format._

****

1. Download DA\_Sample.zip from the [File Conversion and Renaming Exercise](https://drive.google.com/drive/folders/12FacixHm5b3fqJAGoXPHkX_rk729M-eJ?usp=sharing) folder.

2. Unzip DA\_Sample.zip. This folder contains the set of raw source files you will work with for this activity.

3. Open the DA\_Sample folder. Within this folder, create a new folder called “DA\_Sample\_output”.

4. Open Irfanview and in the main menu click File > Thumbnails from the main menu. Use the folder navigator on the left-hand side of the window to locate and select the unzipped DA-Sample folder containing the raw images. This will populate a list of thumbnails in the main window (will take a few seconds).

5. Double-click on the first thumbnail listed to view it in full screen. Some things to notice:

   - The first image is a target reference file, which is a capture of a colored piece of tape with the collection, box and folder number name.

   - Use your right arrow key to tab through subsequent images. The captures following this target reference file “belong” to the collection/box/folder noted.

   - After pressing your right arrow key 10 times, notice how you come across another target reference file for a different collection/box/folder combination. Again, the subsequent captures are children of this parent box/folder. The photographer worked in this way, by capturing the reference target first, and following with captures from within that folder, to convey hierarchical relationships between folders and captures.

   - The images need color correction and cropping but that is out of scope for this activity, so don’t worry about taking any steps to fix that.

6. Note the file format of all the files and open the PRONOM File Format Registry (<https://www.nationalarchives.gov.uk/PRONOM/>) and click the “Search Pronom” button. Click the File Format tab. Enter the file format extension into the search box and click the Search > button. Click the link for the file format to learn more about this format.

7. Return to Irfanview - Thumbnails window. Single-click on one thumbnail, and then on your keyboard, hold down Ctrl + A to select/highlight all thumbnails displayed.

8. Click File > Start batch dialog with selected files to open the Batch Conversion window. Set up your batch conversion:

   - **Input Files Section:** Check to make sure all 63 raw image files are listed. If not, use the Look in: browser to find the DA-Sample folder, and click the **Add all** button (or you can close the Batch Conversion window and repeat Step 7.)

   - **Work as:** Select the radio button next to “Batch conversion”

   - **Batch Conversion Settings Section:**

     1. Output format: Select a preservation-quality file format

     2. Check “Use advanced options…” and click the **Advanced** button. Look at all the options, such as Resize, Change Color Depth, Color Balance, Horizontal/Vertical flip, etc. No need to change anything here, just take note of the various technical specifications you can set here (you can also save these settings for future conversions). Click X or OK.

   - **Output folder for result files:** Click the **Browse** button and navigate to the DA\_Sample\_output folder created in Step 3. Click **OK**.

9. When you are ready click the **Start Batch** button. A processing progress window will appear. When the conversion is complete, the window name will change to “Batch conversion done”. Click the **Exit Batch** button.

10. Close the Thumbnails window. In the main Irfanview window in the upper left-hand corner, click the **Open** button (icon is a folder with an arrow coming out of it) and navigate to the DA\_Sample\_output folder containing the converted files. Open one converted image.

11. From the main menu, click Image > Information to view technical metadata. Click **OK**.

12. Close Irfanview.

****

**Batch Rename Files using Windows/Bulk File Utility**

_You will use the free tool Bulk File Utility to batch rename your preservation files._

****

|                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sample file naming schema**\[collection\_short\_name]\_b##\_f##\_#####\[3-digit collection short name]\_\[box number]\_\[folder number]\_\[sequence number with leading zeros, 4 digits total]Collection short names: CENTRO is “cen” and Aspira is “asp”Sequence numbers reset back to 1 for each folder.Example: cen\_b20\_f04\_0002 |

****

1. Open the Bulk Rename Utility program.

2. On the upper right-hand side of the screen, click on the little folder icon to navigate to and select the DA\_Sample\_output folder.

3. Identify a group of captures belonging to one distinct collection/box/folder group. Remember, for each box/folder they were working with, the photographer would first capture a target reference image indicating the box/folder numbers, followed by the associated captures. You may need to use Irfanview or some other preview program to identify these groups.

4. Note the collection name, box number, and folder number, and the filenames for the first and last files in the group.

5. Shift-click to select all files belonging to your selected collection/box/folder.

6. Add these parameters in this order. Note: The left-most “Name” column shows the current filename. The next column to the right, “New Name” provides a preview of how files will be renamed based on the parameters entered, and will dynamically update itself as you take the steps below:

   - **Replace section:** 

     1. Replace: Aspira\_ or CENTRO\_

     2. With: asp\_ or cen\_

****

_Click the_ **_Rename_** _button to apply, and_ **_OK_** _to finalize._

_Click the_ **_Reset_** _button._

_Shift-click to re-select all files belonging to your selected collection/box/folder._

****

- **Add section:**

  1. Insert: \_b10\_f08

  2. At pos.: 4 (“pos.” stands for position in the filename string; notice how if you click on the up/down arrows, the insert string will change positions in the New Name preview.

****

_Click the_ **_Rename_** _button to apply, and_ **_OK_** _to finalize._

_Click the_ **_Reset_** _button._

****

- **Remove section:** 

  1. Last n: 4

****

- **Numbering section:** 

Mode: Insert

Start: 0

Pad: 4

Break: 11

At: 12

Incr: 1

Sep: \_

****

_Click the_ **_Rename_** _button to apply._

_Click the_ **_Reset_** _button._

****

7. Take Steps 3-6 for each of the remaining collection/box/folder groups.


### Mac - Steps

**Batch convert files using Mac Preview**

_For this activity you will be converting raw image files into preservation and access files and rename them to fit the file naming schema for Centro. You will use the Mac’s native Preview application to perform bulk file conversions._

****

1. Download DA\_Sample.zip from the [File Conversion and Renaming Exercise](https://drive.google.com/drive/folders/12FacixHm5b3fqJAGoXPHkX_rk729M-eJ?usp=sharing) folder.

2. Unzip DA\_Sample.zip. This file contains a set of raw source files you will work with for this activity.

3. Note the file format of all the files and open the PRONOM File Format Registry (<https://www.nationalarchives.gov.uk/PRONOM/>) and click the “Search Pronom” button. Click the File Format tab. Enter the file format extension into the search box and click the Search > button. Click the link for the file format to learn more about this format.

4. Using the DA\_Sample folder in Finder. Within this folder, create a new folder called “DA\_Sample\_output”.

5. Select all the images and drag and drop them into the Preview icon in the dock bar OR Ctrl+Click and select “Open With > Preview”. 

6. Click on the very first thumbnail listed in the navigation pane to view the image in full screen mode. Some things to notice:

   - The first image is a target reference file, which is a capture of a colored piece of tape with the collection, box and folder number name.

   - Single-click onto the full-screen image, and then use your right arrow key to tab through subsequent images. The captures following this target reference file “belong” to the collection/box/folder noted.

   - After pressing your right arrow key 10 times, notice how you come across another target reference file for a different collection/box/folder combination. Again, the subsequent captures are children of this parent box/folder. The photographer worked in this way, by capturing the reference target first, and following with captures from within that folder, to convey hierarchical relationships between folders and captures.

   - The images need color correction and cropping but that is out of scope for this activity, so don’t worry about taking any steps to fix that.

7. In the left sidebar of the Preview tool, select all images the images (click on one image and use the keyboard shortcut Command + A)

8. Select File > Export Selected Images

9. Click the **Show Options** button. In the provided drop-downs, select preservation-quality Format, Depth, and Compression of your choice.

10. In the file list, click to select the DA\_Sample\_output folder created in Step 3: this is where your exported images will be output.

11. Click the **Choose** button to initiate the export. The “Exporting documents…” progress bar will appear (this will take a few seconds). Note: Tools > Show Inspector tells you info about the images so you can assess the quality of your preservation images.

****

**Batch Rename Files using Mac Preview**

_You will use the Mac Preview tool to batch rename your preservation files._

****

|                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sample file naming schema**\[collection\_short\_name]\_b##\_f##\_#####\[3-digit collection short name]\_\[box number]\_\[folder number]\_\[sequence number with leading zeros, 4 digits total]Collection short names: CENTRO is “cen” and Aspira is “asp”Sequence numbers reset back to 1 for each folder.Example: cen\_b20\_f04\_0002 |

****

_Before starting, review site does a nice breakdown of how to do batch renames with Preview:_ [_https://www.imore.com/how-rename-multiple-files-once-mac_](https://www.imore.com/how-rename-multiple-files-once-mac)

****

Note that you will not be able to get the exact file-naming format with the sequence numbers with Preview, that’s ok, I’ll accept the available Preview output (the counter outputs 5 digits instead of 4.) For the file renaming the Format section in Preview rename is where you want to work. You can set up the prefix in the custom format and then add a counter for the sequence number.

****

1. Launch Finder and navigate to the DA\_Sample\_output containing your converted files.

2. Identify a group of captures belonging to one distinct collection/box/folder group (remember, for each box/folder they were working with, the photographer would first capture a target reference image indicating the box/folder numbers, followed by the associated captures.)

3. Note the collection name, box number, and folder number, and the filenames for the first and last files in the group.

4. Shift-click to select all files belonging to your selected collection/box/folder.

5. Control + click on the selected files to bring up the Action menu.

6. Select “Format” from the top-most drop-down menu.

7. Fill out the form:

   - **Name Format:** Select “Name and Counter” from the drop-down.

   - **Custom Format:** \[collection\_short\_name]\_b##\_f##\_#####

   - **Where:** after name

   - **Start numbers at:** 0 (remember, the target reference file, which is the first file in a capture, is not going into the preservation repository.)

8. Discard your target reference file.

9. Repeat these steps for every distinct collection/box/folder combination. Note: Preview will save your last rename settings, so once you do one group, it will make subsequent renaming in the same manner move along quicker.