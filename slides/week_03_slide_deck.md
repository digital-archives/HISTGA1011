---
marp: true
theme: gaia
size: 16:9
paginate: true
mermaid: true

style: |
 img {
 max-width: 100%;
 max-height: 100%;
 height: auto;
 width: auto;
 display: block;
 margin: 0 auto;
 }

    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 20px;
        font-size: 28px;
        font-weight: bold;
        margin-top: 20px;
    }
    .box {
        padding: 15px 25px;
        border-radius: 8px;
        font-weight: bold;
        text-align: center;
        min-width: 200px;
        position: relative;
        font-size: 30px;
    }
    .file { background-color: #e67e22; color: white; }
    .container-box { background-color: #27ae60; color: white; min-width: 260px; }
    .codec { background-color: #e57373; color: white; min-width: 280px; }

    /* Symbols */
    .equals, .plus { font-size: 36px; }

    /* Descriptions */
    .description {
        font-size: 22px;
        font-weight: normal;
        text-align: center;
        color: black;
        margin-top: 8px;
        background: rgba(255, 255, 255, 0.6);
        padding: 6px;
        border-radius: 5px;
    }

    /* File name under Media File */
    .filename {
        margin-top: 10px;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
    }

    /* Bullet Lists Inside Boxes */
    .container-box ul, .codec ul {
        list-style-type: disc;
        text-align: left;
        font-size: 24px;
        margin-top: 10px;
        padding-left: 20px;
    }

 th {
  font-weight: bold;
  font-size: 1.2em;
  color: black !important;
  background-color: #f4f4f4 !important;
  border-bottom: 2px solid black;
 }

 .mermaid {
 max-width: 100%;
 overflow: hidden;
 }

 .custom-title {
 text-align: center;
 font-size: 2rem;
 color: #0044cc;
 font-weight: bold;
 }
 
 table, td, th, ul {
 background: rgba(0, 0, 0, 0) !important;
 border: none !important;
 }

 .pink-box {
 background-color: #d184c2;
 color: white;
 padding: 20px;
 border-radius: 5px;
 font-weight: bold;
 text-align: center;
 box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
 }

 .green-box {
 background-color: #a2c9a5;
 padding: 20px;
 border-radius: 5px;
 font-weight: bold;
 text-align: center;
 box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
 margin: 10px;
 }

 .row {
 display: flex;
 justify-content: space-around;
 margin-bottom: 20px;
 }

 .quote {
 font-size: 1.5rem;
 font-style: italic;
 text-align: left;
 line-height: 1;
 color: #4a4a4a;
 margin: 0 auto;
 width: 100%;
 }

 .author {
 font-size: 1.0rem;
 text-align: right;
 margin-top: 20px;
 color: #6a6a6a;
 }

 .work {
 font-size: 1rem;
 text-align: right;
 color: #8a8a8a;
 }

 .slide-title {
 text-align: center;
 color: #2e7d32;  font-size: 2rem;
 font-weight: bold;
 margin-bottom: 30px;
 }
 
 .takeaway {
 display: flex;
 align-items: flex-start;
 margin-bottom: 20px;
 gap: 15px;
 }

 .circle {
 background-color: #2e7d32;  color: white;
 font-size: 1.5rem;
 font-weight: bold;
 width: 50px;
 height: 50px;
 display: flex;
 justify-content: center;
 align-items: center;
 border-radius: 50%;
 flex-shrink: 0;
 }
 .content {
 flex-grow: 1;
 }
 .content h2 {
 margin: 0;
 color: #2e7d32;  font-size: 1.2rem;
 }
 .content p {
 margin: 5px 0 0;
 font-size: 1rem;
 color: #4a4a4a; }

 .activity-title {
 text-align: center;
 color:rgb(144, 0, 255);  font-size: 2rem;
 margin-bottom: 20px;
 font-weight: bold;
 }
 .shapes {
 text-align: center;
 margin-bottom: 30px;
 }
 .shapes span {
 display: inline-block;
 margin: 0 10px;
 width: 30px;
 height: 30px;
 border-radius: 50%;
 }
 .triangle {
 width: 0;
 height: 0;
 border-left: 15px solid transparent;
 border-right: 15px solid transparent;
 border-bottom: 30px solid #ffb347;  display: inline-block;
 margin: 0 10px;
 }
 .circle {
 background-color: #00c0ff; }
 .square {
 width: 30px;
 height: 30px;
 background-color: #ff6767; }
 .activity-list {
 font-size: 1.1rem;
 line-height: 1.1;
 color:rgb(81, 0, 168);  margin-left: 20px;
 }
 .activity-list li {
 margin-bottom: 10px;
 }
 .activity-list li strong {
 color:rgb(235, 133, 133); }

---

# Week 3 
## Processing Born-Digital Archives

---

# Today
- **Settle in/Reminders/Announcements** (15 min)
- **Discuss Last Week's Activity: Breaking BagIt** (20 min)
- **Lecture: Processing Born-Digital Archives** (45 min)
- **Break** (10 min)
- **Start Weekly Activity** (70 min)
- **Wrap up** (10 min)

---

# Announcements

Job announcements:
* <a href="https://www.rfcuny.org/careers/postings?pvnID=VA-2501-006680" target="_blank">Newmark CUNY Wikimedia Documentarian (apply by March 28)</a>
* <a href="https://www.archivingtheblackweb.org/warc-school/apply/" target="_blank">Archiving the Black Web Web Archiving (WARC) School Fellow and Teaching Assistant</a> (apply by January 31)
* <a href="https://memoryrising.us21.list-manage.com/subscribe?u=33964c505212f62c031cc170e&id=866da7c133" target="_blank">Memory Rising</a> Newsletter, No Time For Fear (podcast on the New Deal) by Eira Tansey</a>

---

# Activity Discussion: Breaking BagIt

- Top-level folder
  - `bagit.txt`
  - `bag-info.txt`
  - `manifest-md5.txt`
  - `tagmanifest-md5.txt`
  - `data`
    - `file1.txt`
    - etc.

<!--presenter notes

https://datatracker.ietf.org/doc/html/rfc8493

-->

---

## Processing Born-Digital Archives
- Acquisitions
- Accessioning
- Processing (arrangement and description)

---

## Definition
# Born-digital

**Born-digital** refers to items or materials whose contents were captured using binary encoding.

Born-digital items are distinct from contents created using analog recording tools and subsequently digitized.

<!--presenter notes

Definition comes from: https://primarysources.yale.edu/what-does-born-digital-mean

-->

---

## Definition
# Digital storage device or media

A **digital storage device** (sometimes just referred to as "media") is a physical device used to store, read, or write digital-encoded data. 

Examples: hard drive, compact disc, floppy disk, computer, smartphone

---

<img src="img/week_03_media.png" alt="Photograph of various digital media types such as floppy disks and hard drives of various shapes and sizes">

<!--presenter notes

Some examples of digital storage devices include floppy disks, compact discs or CDs, and hard drives. All are used to store, read and write digital data, to varying degrees.

Digital storage devices are commonly associated with legacy born-digital collections, and look similar to the image on the slide. However, digital carriers are not exclusive to things that are “old”. Smartphones, at least at the moment, are a ubiquitous digital carrier that have and will likely continue to make their way into archival processing queues, and should be considered a digital storage device on its own.

-->

---

## Definition
# Acquisition

When an institution gets ownership of item or a body of work, either through purchasing (resulting in an invoice), or donation/gift/bequest (resulting in some sort of legally-binding agreement such as a deed of gift), the legal and physical transfer of materials is referred to as the/an **acquisition**.

---

## Definition
# Accessioning - 1/2

"**Accessioning** is ... the suite of activities through which archivists appraise, transfer, stabilize, and document archival acquisitions. Accessioning provides pathways to access, informs future decisions, and promotes sustained resource commitment for the care of archival materials."

_Archival Accessioning Best Practices (2024)_

---

## Definition
# Accessioning - 2/2

"Accessioning is the process of transferring and documenting the transfer of collections material into the Libraries' care. For **born-digital materials**, that means safely copying them into the Libraries' temporary storage system and documentating the process. Digital files should be accessioned within four months of receipt."

<!--presenter notes

This definition comes from University of Georgia Libraries Github documentation on born-digital accessioning. See: https://github.com/uga-libraries/born-digital-accessioning?tab=readme-ov-file

-->

---

## Definition
# [Archival] Appraisal

**Appraisal** is the process of determining whether records and other materials have permanent (archival) value.

It may be done at the collection, creator, series, file, or item level.

It can take place _prior_ to acquisition, or _after_ accessioning, or both.

<!--presenter notes

Definition source:
https://dictionary.archivists.org/entry/appraisal.html

The basis of appraisal decisions may include a number of factors, including the records’ provenance and content, their authenticity and reliability, their order and completeness, their condition and costs to preserve them, and their intrinsic value. Appraisal often takes place within a larger institutional collecting policy and mission statement.

-->

---

### Workflow: Acquisition -> Processing

- Acquisition proposed
- Deliver raw materials (secure file transfer, or ship temporary and/or original physical media)
- Accession, stabilize (virus scan, create disk images)
- Pre-processing analysis
- Arranagement and description

---

# Some media cannot be properly handled until their contents are _imaged_.

---

## Definition
# Floppy Disk 💾
A **floppy disk** is a thin, flexible magnetic storage medium encased in a rectangular plastic shell.

---

![width:1000px](img/week_04_floppy_inside.png) <!-- fit -->

<!--presenter notes

Screen capture of a person handling the insides of a floppy disk, from this YouTube video:
https://www.youtube.com/watch?v=1-oH2T3W-q4

-->

---

## Floppy disks use magnetism to encode binary data.
- A flexible piece of plastic is coated in a magnetic substrate made up of microscopic particles.
- The computer:
  - **Writes** data by applying an electromagnetic field to particles. Direction "Up" = 1 and Direction "Down" = 0
  - **Reads** data using a sensitive electromagnetic head that detects variance in directions amd translates to binary information.

---

## Definition
# Disk sector

A **disk sector** is a fundamental unit of storage on a disk. It represents the smallest addressable unit of data on the disk.

---

<img src="img/week_04_disk_sectors.png" alt="Diagram of magnetic disk structures, showing a circle divided into slices and sectors, resembling evenly-spaced race tracks.">

<!--presenter notes

Diagram from Wikipedia article on disk sectors: https://en.wikipedia.org/wiki/Disk_sector

This diagram illustrates how data is written to the surface of a magnetic storage disk, which can be thought of as a circular map with data stored in specific, measurable locations. Each disk is divided into sectors that correspond to precise points on the disk's surface and are defined by their size in bytes, making sectors the smallest unit of storage.  

When a file is saved to a hard drive, the file system assigns it to a series of contiguous sectors whenever possible. This grouping of sectors is known as a cluster, and would appear like tracks.

-->

---

## Definition
# Transfer

A **transfer** refers to moving select data from one device to another.


---

## Definition
# Imaging

**Imaging** describes the process of creating a bit-identical copy of some sort of physical source media. The imaging process copies data _sector-by-sector_ from the disk. The result is an image file.

<!--presenter notes

Disk imaging describes the process of creating a bit-identical copy of the source media. The imaging process copies data sector-by-sector from the raw device.

-->

---

<div class="quote">
“[D]isk images can be stored redundantly, backed up, and audited in ways that physical carriers like DVDs or external hard drives cannot…they are a much better suited for preservation of digital information over time, while retaining all characteristics of the original physical media as a storage volume.” 
</div>

<div class="author">
Canadian Center for Architecture (CCA)
</div>

<div class="work"><a href="https://github.com/CCA-Public/digital-archives-manual/blob/master/guides/diskimaging.md" target="_blank">Digital Archives Manual</a>
</div>

---

<div class="quote">
“From a preservation perspective, this makes forensic imaging ideal; an exact copy of the original data can be ingested into a secure and long-term storage environment. Derivative copies can later be used for continued appraisal and processing.”
</div>

<div class="author">Dorothy Waugh, Emory University</div>

<div class="work"><a href="https://ecommons.cornell.edu/server/api/core/bitstreams/f85f26b7-859c-4f5e-9fab-aabed683c3c4/content" target="_blank">A Dogged Pursuit: Capturing Forensic Images of 3.5” Floppy Disks</a></div>

---

# A disk image
- "Liberates" the bitstream from its physical media
- Disk images can be evaluated on modern computing environment
- Resulting analyses can be used for appraisal,and for coming up with a processing plan

<!--presenter notes

Disk imaging liberates bitstreams from digital storage media, which can otherwise be subject to all the inherent risks associated with born-digital items. Disk images can be migrated into modern computing environments where they can be analyzed. The analysis may be for appraisal purposes, or throughout the course of archival processing in arranging and describing the contents.

-->

---

<div class="shapes">
  <div class="triangle"></div>
  <span class="circle"></span>
  <span class="square"></span>
</div>

<div class="activity-title">Mini Activity - Disk Image</div>

_Play an Apple II disk image file._

<ul class="activity-list">
<li><a href="https://archive.org/details/softwarelibrary_apple_games" target="_blank">Open the Apple II Games Library</a> on the Internet Archive.</li>
<li>Browse the archive and select a game of interest.</li>
<li>On your selected game's page, find the <b>Download Options</b> section; select <b>Show All</b>.</li>
<li>Find *.2mg disk image file listed.</li>
</ul>

<!--presenter notes

https://archive.org/details/a2gs_Volcanoes_Deluxe_1988_Earthwave_Services

What does a disk image look like, and how can we look into it or interact with it once it is made?

One way to easily look at and experience a disk image is by perusing the Internet Archive. There are a number of vintage video game collections. Take a moment to look up a game on the Internet Archive by searching for “apple ii games internet archive” in a web browser. Click on any game that comes up that is interesting to you.

When you click on a video game, notice how the main screen will briefly show you a blue screen that says something along the lines of “Apple II” and some copyright information. When you see this, what you are seeing is the Internet Archive booting up a disk image of the Apple II operating system. This is necessary because these video games have a dependency on the Apple II operating system to be played. So right off the bat, you are interacting with a disk image, first of an operating system, and then immediately afterwards, the disk image of the videogame.

You can see the image file listed by clicking “Show all files” on the right/bottom-hand side of the game screen. In the list, locate the *.2mg file. This is the disk image. Really, it looks like any other file, with a name, a period, and a file extension, which you can even download to your computer, if you wish. This enables you and I to play these games without subjecting the original disks to wear and tear. And because it is an exact copy of the original, we can experience it in a similar way to an original game player.

-->

---

<img src="img/week_04_image_capture_workstation.png">

<!--presenter notes

What does a disk imaging workstation look like?

- Dedicated capture workstation: A laptop or desktop computer used for disk imaging.  
- Write blocker: A hardware device that sits between the capture workstation and the disk reader, preventing accidental modification of the source media.  
- Disk reader: A device that reads the physical media (e.g., a floppy disk drive for floppy disks).  
- Various cables connect the workstation, write blocker, and disk reader to each other, ensuring proper data transfer, and to power.


-->

---

## Pre-Imaging Step: Virus Scan  

- **Run a virus scan**: Before creating a disk image, a virus scan should be performed to check for potential malware. A common tool used is known as ClamAV. 
- **Air-gapped workstations**: To reduce risk, capture workstations are sometimes **non-networked**, preventing malware from spreading beyond the imaging environment.  

---

# The capture workstation will have some sort of program that provides the archivist an interface with the drive making the image.

---

## Tool
# Disk Imaging Tools

**Guymager**: Imaging utility; part of the BitCurator suite of born-digital processing tools.
**Forensic Toolkit (FTK)**: Suite of born-digital processing tools; Windows-based
**ISO Buster**: Imaging specific to optical media (CDs, DVDs, etc.)

...and many more

---

<center>
<img src="img/week_03_ftk.png" style="width: 70%; height: auto;" alt="Screen capture of Forensic Toolkit">
</center>

<!--presenter notes

This is a screen capture of the FTK Imager graphical user interface (GUI), which is one of many tools offered in the Forensic Toolkit environment.

On the left-hand side of the screen is a folder directory or "tree" showing one of the disk images (ending in the file format extension AFF, which stands for "advanced file format", a forensic disk image file format.) On the lower right-hand side of the screen is a hex editor, which lists the hexadecimal representations of the binary code stored on the image, as well as their sector location (a sector refers to a specific area of a disk) listed in the left-hand column.

Along with creating a disk image, FTK Imager also “...calculates MD5 and SHA-1 checksums in order to verify that the capture was successful … a text file including some technical metadata and fixity information, and a CSV file listing the file names and paths of data contained on the imaged media.”

-->

---

# Tool
## Write blocker

A piece of hardware or even physical component on a device that prevents a system from overwriting data held in a target born-digital item.

<!--presenter notes

A write blocker is piece of hardware or even physical component on a storage device that prevents a system from overwriting data held in a target born-digital item. It is a physical gate that puts you into read-only mode.

-->

---

<table>
  <tr>
    <td style="vertical-align: top; width: 60%;">
      <h1>Question</h1>
      <h2>Can you guess what might happen if you attempt to read a disk without applying a write blocker when imaging a disk?</h2>
    </td>
    <td style="vertical-align: top; width: 40%;">
      <img src="img/week_04_file_properties.png" style="max-width: 100%; height: auto;" />
    </td>
  </tr>
</table>

<!--presenter notes

What happens when you don’t toggle a write blocker? A good example of this are the created, modified and accessed metadata properties of a file. Each of these three data points holds important details about provenance. File systems, by design, automatically update this data without asking you whether or not you would like to commit the change. As a result, if you were to image a disk without the write blocker turned on, you would see the Created, Modified and Accessed data change to today’s date, rather than the date the original file was accessed by its creator.

-->

---

# Arrangement & Processing of Born-Digital Archives

---

## Considerations
- **Arrangement** is the first step in processing digital and analog archives.
- Factors affecting arrangement include **original order**, **institutional priorities**, and **researcher needs**.
- There is no one strategy that can be applied to any or all collections!

---

## Approaches to Arrangement

- **Separate digital series**: Fonds → Digital Files  
- **Sub-series within existing series**: Fonds → Series → Digital Files  
- **Co-arranged with other formats**: Fonds → Series → Project File (includes digital and physical files)  
- When possible, **co-arrange digital records with similar physical records**.

---

## Factors Affecting Arrangement

- **How records arrive**: Large transfers (e.g., full hard drives) retain **original structure**; Small media (e.g., floppies, CDs) may require **more active arrangement**.  
- **Existing organization**:  
  - Does the order reflect original use?  
  - Does it support researcher accessibility?  
- **Context of creation & archival collection**:  
  - Relationship to physical records?  
  - Full fonds vs. partial collection?
---

## Developing a Processing Plan

- **Survey & Familiarization**: Archivist reviews structure, content, and documentation.
- **Pre-Processing Meeting**: Archivists, digital specialists, and stakeholders draft an arrangement plan.
- **Decisions Made On**:  
  - Descriptive standards  
  - Preservation concerns  
  - Normalization requirements  
  - Handling of original storage media  

---

## Processing & SIP Packaging for Archivematica

- **SIP Creation Tools**:  
  - **Disk Image Processor**: Processes forensic disk images.  
  - **Folder Processor**: Organizes directories into SIPs.  
  - **SIP Creator**: Combines directories and files.  
- **Normalization**: Files may be manually migrated to preservation formats.

---

<img src="img/week_03_kryoflux_01.png">

<!--presenter notes

Emory took one more step. After consulting with archivists on listservs, they decided to purchase a KryoFlux device.

On the slide is what a KryoFlux controller card and all of its various components looks like “out of the box”. These images were taken from a Github repo called “The Archivist’s Guide to KryoFlux”, which was a collaborative document written by several digital archivists from different repositories.

You have several components. Starting from the top left going from left to right, is the KryoFlux board, which looks like an exposed computer chip.

The KryoFlux board is connected to the floppy drive using a data cable. The data cable size will depend on the type of drive you are transferring from. The image on the slide shows a 3.5” floppy drive, but a KryoFlux board can be connected a multitude of floppy drives.

Once your floppy drive is connected to the KryoFlux board, you will next connect the board to your computer using a USB cable. Once your drive and board are connected to your computer, you launch the tool via the command line. Once this is done, you connect your floppy drive to an power source using a power adapter. Again, depending on the drive you are using for imaging, you will use a different power adapter.

This ultimately enabled Emory to capture all of Walkers disks. Why did the KryoFlux work so much better? KryoFlux is known to be able to capture disk images of a variety of formats.

Along with the KryoFlux card, you will need to install the Disk Tool Controller (DTC) software. DTC is used to control the board and interact with floppy disk drives and provides a user-friendly interface for controlling the board and performing various disk-related tasks. This software is available for various operating systems, including Windows, Linux, and macOS.

-->

---

<img src="img/week_03_kryoflux_02.png">

<!--presenter notes

Here is a photo of the KryoFlux board, which comes with a built-in write-blocker, circled in red. To enable write-blocking functionality, you would actually physically remove the jumper for the write gate.

-->

---

**Downstream effects**  
Uninformed appraisal decisions can create unintended negative outcomes later in the stewardship lifecycle.

**Scale**  
The scale we are dealing with (thousands of files on a harddrive, an entire laptop) complicates deciding what/not to keep.

**Format diversity**  
Unexpected media and file formats can challenge a repository's technical capacity.

---

# Born-Digital Appraisal Considerations
__Question 1:__ Do we have the tools to extract the record off the media?
__Question 2:__ Can we preserve/maintain the record over time?
__Question 3:__ Can we provide access to the record?
__Question 4:__ Do these records speak to our collection development policy, or its overall goals?
__Question 5:__ Do we have access to the creator/organization, who can provide us context as far as who and how records are being created?

---

<img src="img/born_digital_gallery.webp" alt="An array of born-digital media formats: CD-RW, Zip disk, hard drives, flash drives, various floppy disks.">

<!--presenter notes

Image credit:
"Assortment of obsolete and current media that the AHC’s Born Digital unit handles on a daily basis." Digital Preservation 101: Demystifying the Digital, American Heritage Center, 20 July 2020, https://ahcwyo.org/2020/07/20/digital-preservation-101-demystifying-the-digital/.

-->

---

## Definition
# File Format

A **file format** "...refers to the internal structure and encoding of a digital object, which allows it to be processed, or to be rendered in human-accessible form. A digital object may be a file, or a bitstream embedded within a file."

From the <a href="https://www.nationalarchives.gov.uk/aboutapps/pronom/pdf/pronom_unique_identifier_scheme.pdf" target="_blank">PRONOM PUID Scheme: A scheme of persistent unique identifiers for representation information</a>

<!--presenter notes

When we are working with media containing files, it is very likely that we will encounter files at scale. For example, we may receive a pile of floppy disks, each containing 20 files. So, maybe it might be easy enough to just manually identify each file manually.

But what if an archivist is handling an entire harddrive, containing hundreds or even thousands of files. Performing a technical appraisal at this scale is simply impossible to do manually.

-->

---

![Screen capture of the ExifTool graphical user interface (GUI).](img/week_03_exiftool.png)

<!--presenter notes

On screen is an image of ExifTool, which can be used to extract so-called "technical metadata" from a file or group of files.

Archivists can (and do) use tools like this to peer into the technical metadata of a file. Here, we can see things about the file, such as what device it was shot on (a Canon EOS 450D), and other details. This can definitely helpful for appraising individual files.

-->

---

## Definition
# Technical Metadata

**Technical metadata** refers to data that describes technical characteristics of a file, such as the file format, file size, provenance (i.e. creation date, last modified date), and other details.

---

## Tool
# File Information Tool Set (FITS)

Developed by Harvard University, the File Information Tool Set (FITS) is a suite of tools (including ExifTool) that, together, may be used to identify and extract technical metadata from files. The data is output into XML format.

<!--presenter notes

Exiftool is one of many tools that can be used to see technical metadata about a file. Another tool, known as FITS, was developed by Harvard to bulk extract tech metadata into XML format. What's nice about this is, once you get it into a structured format like XML, you can do all sorts of things with it, like import it into your database, and you could potentially do this for many many files at once.

-->

---

## Tool
# BitCurator

**BitCurator** is an open-source program providing a suite of tools used to help with born-digital processing tasks.

---

## Tool
# Digital Record Object Identification (DROID)

**DROID (Digital Record Object Identification)** is an open-source file format identification tool developed by The National Archives (TNA) in the UK. It is used for digital preservation, archiving, and forensics to identify file formats based on their PRONOM database signatures.

---

## Tool
# Siegfried

Siegfried (or sf) is an open-source file format identification tool used for digital preservation and file forensics. 

<!--presenter notes

And another tool! Siegfried also does bulk identifying, but is known to be nimble and quick, and can compare against PRONOM database.

-->

---

## Question
### Why might an archivist need to identify the file formats present in a specific accession?

---

## Tool
# PRONOM

**PRONOM** is an on-line information system about data file formats and their supporting software products. Originally developed to support the accession and long-term preservation of electronic records held by the National Archives, PRONOM is now being made available as a resource for anyone requiring access to this type of information.

https://www.nationalarchives.gov.uk/pronom/

---

<div class="shapes">
  <div class="triangle"></div>
  <span class="circle"></span>
  <span class="square"></span>
</div>

<div class="activity-title">Mini Activity - PRONOM</div>

_Use PRONOM to look up a registered file format._

<ul class="activity-list">
<li>Open <a href="https://archive.org/details/softwarelibrary_apple_games" target="_blank">PRONOM</a> in a browser; select "Search PRONOM".</li>
<li>Select the "File format" tab.</li>
<li>Input the file format JPG; select Search.</li>
<li>Notice how there are a lot of results! Click on the first result for PRONOM unique ID fmt/41.</li>
<li>Have a look at the Summary.

</ul>

---

# Pronom Summary: Things to notice

---

## Definition
# Format signature

A **format signature** is a unique pattern of bytes that identifies a specific file format.

_To see the signature of a JPEG, click the Signatures tab_

---

- "Has lower priority than": Refers to format identification precedence when multiple related file formats could apply to a given file. When a file is analyzed (using, for example, DROID or Siegfried), it may match multiple format signatures.


---

# Digital Forensics

---

## Definition
# Digital forensics

__Digital forensics__ describes various techniques, practices and tools that focus on recovering and analyzing information from storage devices.

<!--presenter notes

So how do we address risks inherent to born-digital items, all the while making sure that provenance, original order, chain of custody, and other archival principles are maintained? This is especially important because storage media can contain swaths of data that ideally would be handled in bulk, but all the while enable the archivist to take precise measures to properly appraise, arrange and describe the contents.

One way to do this is through taking digital forensics measures. Know that digital forensics requires a little bit of understanding of how computers work, especially in terms of how they store, read, write, delete, and make sense of what it is that they store. Know that knowing this is what I would consider a necessary skill for any archivist, not just those archivists with “digital” in front of their names.

Archives have a need to create and analyze authentic, trustworthy and complete version of digital storage devices to preserve the digital historical record. One way to do this is to take digital forensics measures. Digital forensics refers to techniques, practices and tools that are used by archivists and other technicians to recover and analyze information from born-digital media and devices such as computer hard drives, floppy disks, flash drives, smartphones and so on.

-->

---

# Weed unnecessary, redundant files
- __Application data__: Files that are tied to specific applications (example: config.ini)
- __Encrypted or password-protected data__: Unless the decryption key is available, these files can be considered inaccessible.
- __Duplicates__: Identical files that waste storage space and complicate processing.
- __Temp files__: These often don’t hold any long-term value and can be safely discarded.
- __Binned files__: Files deleted by the creator.

---

# Reason 2: Determine processing plan
- __Size and complexity of the file system__: How much organization and descriptive file naming is already present.
- __Sensitive or personally-identifying information__: Identifying and addressing areas with potentially sensitive data that may require special handling.
- __Manual sampling needs__: Areas that may need manual review or sampling for appraisal.
- __Complexity of file formats__: Some formats may require special access or reformatting, which needs to be considered early on.

---

# Case Study: Alice Walker Papers (Emory University)
**Inventory:**
- 37 3.5" floppy disks
- 2 optical media
- 1 Mac laptop

**Issue:** At first, archivists could only successfully image a few of the 37 disks. Other disks appeared totally un-imageable.

<!--presenter notes

We have talked about what a disk image is, and with that in mind, I want to pull all of these concepts together into a digital archiving-centered case study, and use this to step through a typical born-digital processing workflow, to introduce you to various tools and devices used.

In 2007, Emory University acquired the papers of Alice Walker. Walker is an acclaimed novelist, essayist, poet and short story writer, who in 1983, became the first African American woman to win the Pulitzer Prize for Fiction for her novel The Color Purple.

Her papers included drafts of her manuscripts, photographs, journals and memorabilia from her life, some which were in received on born-digital media, including 37 3.5” floppy disks, 2 optical media CDs, and 1 Mac laptop.

Finding aid for Alice Walker Papers: https://findingaids.library.emory.edu/documents/walker1061/series13/

Case study is written in depth at: https://practicaltechnologyforarchives.org/issue2_waugh/

-->

---

## Tools Used by Emory

- FTK Imager (failed to capture all)
- Acronis Backup & Recovery
- Kryoflux

<!--presenter notes

“Unfortunately, FTK Imager was only able to capture images of a handful of the floppy diskss. When unsuccessful, the software frequently failed to recognize the external floppy disk drive or became unresponsive. Neither was this problem necessarily remedied by removing the problem disk and replacing it with another; on several occasions, an unreadable disk seemed to corrupt the entire imaging process, requiring that the drive be switched off and disconnected from the computer workstation, and the software restarted. Only then would another otherwise readable disk be recognized. As might be expected, this slowed the imaging process substantially.

Further attempts were made using another imaging tool, Acronis Backup & Recovery. As the name suggests, this is a proprietary product designed to help small businesses backup their data through the capture of forensic images. However, imaging attempts using this tool and the same configuration of hardware as had been used with FTK Imager were no more successful.”

-->

---

# Alice Walker Imaging Takeaways
1. **Appraisal**: Knowing the type of operating/file system used by the creator can help with troubleshooting.

3. **Potential imaging challenges**:
   - Damaged hardware/incompatible or outdated software
   - Unavailability of necessary hardware, software, or peripherals
   - Proprietary disk image formats
   - Insufficient or missing metadata

4. **Be prepared to try (and try) again**

<!--presenter notes

The archivists at Emory knew Walker was a Mac user. This meant her floppy disks were formatted in a specific way (i.e. only a Mac could "read" the floppies). They attempted to image the remaining disks on a modern Mac workstation using the Disk Utility tool.

-->