---
marp: true
---

# Week 3 
## Processing Born-Digital Archives

---

# Today
- Reminders/announcements
- Discuss last week's activity
- Lecture: Processing Born-Digital Archives
- Break
- Start Weekly Activity

---

# Announcements

_Feel free to email me with any announcements you would like me to boost (upcoming conferences, webinars, trainings, or other events/topics of interest)._

---

## Processing Born-Digital Archives
# Accessioning & Appraisal

---

# Lots of terms/definitions coming up

---

## Definition
# Born-digital

__Born-digital__ refers to items or materials that were created in a digital format. This includes websites, email, digital photographs, electronic records, and more. Born-digital items are distinct from physical items that were born-physical, and subsequently digitized, such as a photograph that was later scanned.

<!--presenter notes
https://primarysources.yale.edu/what-does-born-digital-mean
-->

---

## Definition
# Digital storage device or media

__Digital storage device__ (sometimes just referred to as "media") is physical device used to store, read, or write digital data. 

Examples: hard drive, compact disc, floppy disks, computer, smartphone

---

<img src="img/week_03_media.png">

<!--presenter notes

Some examples of digital storage devices include floppy disks, compact discs or CDs, and hard drives. All are used to store, read and write digital data, to varying degrees.

Digital storage devices are commonly associated with legacy born-digital collections, and look similar to the image on the slide. However, digital carriers are not exclusive to things that are “old”. Smartphones, at least at the moment, are a ubiquitous digital carrier that have and will likely continue to make their way into archival processing queues, and should be considered a digital storage device on its own.

-->

---

## Workflow
# Acquisition to Processing Workflow

📥 **Decide to acquire something**  
🔍 **Initial Appraisal**  
📦 **Transfer/ship to repository**  
🗂️ **Accession/inventory**  
📤 **Transfer content off of media**  
📋 **Process/input finding aid data**  
🔗 **Reassociate resulting files in finding aid**  
🛡️ **Rights management/review**  
🌐 **Publish**

---

# Why is appraisal and accessioning important in terms of born-digital materials?

**Downstream effects**  
Uninformed appraisal decisions can create unintended negative outcomes later in the stewardship lifecycle.

**Scale**  
The scale we are dealing with (thousands of files on a harddrive, an entire laptop) complicates deciding what/not to keep.

**Format diversity**  
Unexpected media and file formats can challenge a repository's technical capacity.

---

## Definition
# Archival Appraisal

__Appraisal__ is the process of determining whether records and other materials have permanent (archival) value. Appraisal may be done at the collection, creator, series, file, or item level. Appraisal can take place prior to donation and prior to physical transfer, at or after accessioning. The basis of appraisal decisions may include a number of factors, including the records’ provenance and content, their authenticity and reliability, their order and completeness, their condition and costs to preserve them, and their intrinsic value. Appraisal often takes place within a larger institutional collecting policy and mission statement.

<!--presenter notes

Definition source:
https://dictionary.archivists.org/entry/appraisal.html

-->

---

# Appraisal Considerations - Born-Digital Style
__Question 1:__ Do we have the tools to extract the record off the media?
__Question 2:__ Can we preserve/maintain the record over time?
__Question 3:__ Can we provide access to the record?
__Question 4:__ Do these records speak to our collection development policy, or its overall goals?
__Question 5:__ Do we have access to the creator/organization, who can provide us context as far as who and how records are being created?

---

## Definition
# Accessioning - 1/2

"Accessioning is ... the suite of activities through which archivists appraise, transfer, stabilize, and document archival acquisitions. Accessioning provides pathways to access, informs future decisions, and promotes sustained resource commitment for the care of archival materials."

Archival Accessioning Best Practices (2024)

---

## Definition
# Accessioning - 2/2

"Accessioning is the process of transferring and documenting the transfer of collections material into the Libraries' care. For __born-digital materials__, that means safely copying them into the Libraries' temporary storage system and documentating the process. Digital files should be accessioned within four months of receipt."

<!--presenter notes

This definition comes from University of Georgia Libraries Github documentation on born-digital accessioning. See: https://github.com/uga-libraries/born-digital-accessioning?tab=readme-ov-file

-->

---

# How are born-digital materials transferred to a repository?

* Part of physical shipments (i.e. a harddrive arrives in a box that was on a truck)
* Donor instructed to deposit materials through an institutional repository portal (example: <a href="https://library.ccny.cuny.edu/dss/ir" target="_blank">https://library.ccny.cuny.edu/dss/ir</a>) or other networked transfer
* Donor instructed to securely transfer materials to a shared drive/networked folder
* Archivist is called upon to do the transfer themselves (curator gives the archivist a laptop; archivist removes just the hard drive)

---

# Determine What You Have: A Two-Step Identification Process
1. Physical Appraisal: What media am I working with?
2. Technical Appraisal: What file format(s) am I dealing with?

---

<img src="img/born_digital_gallery.webp" alt="An array of born-digital media formats: CD-RW, Zip disk, hard drives, flash drives, various floppy disks.">

<!--presenter notes

Image credit:
"Assortment of obsolete and current media that the AHC’s Born Digital unit handles on a daily basis." Digital Preservation 101: Demystifying the Digital, American Heritage Center, 20 July 2020, https://ahcwyo.org/2020/07/20/digital-preservation-101-demystifying-the-digital/.

-->

---

## Definition
# File Format

A __file format__ defines the way information is encoded and structured within a file. It determines how data is stored, organized, and read by software or systems.

<!--presenter notes

When we are working with media containing files, it is very likely that we will encounter files at scale. For example, we may receive a pile of floppy disks, each containing 20 files. So, maybe it might be easy enough to just manually identify each file manually.

But what if an archivist is handling an entire harddrive, containing hundreds or even thousands of files. Performing a technical appraisal at this scale is simply impossible to do manually.

-->

---

![Screen capture of the ExifTool graphical user interface (GUI).](img/exiftool.png)

<!--presenter notes

On screen is an image of ExifTool, which can be used to extract so-called "technical metadata" from a file or group of files.

-->

---

## Definition
# Technical Metadata

__Technical Metadata__ refers to data that describes technical characteristics of a file, such as the file format, file size, provenance (i.e. creation date, last modified date), and other details.

---

## Tool
# File Information Tool Set (FITS)

Developed by Harvard University, the File Information Tool Set (FITS) is a suite of tools (including ExifTool) that, together, may be used to identify and extract technical metadata from files. The data is output into XML format.

---

# Question: Why might a repository need to identify the file formats present in a specific accession? What practical purposes or benefits could this serve for managing and preserving the collection?

---

![Animated GIF of a garbage bin.](img/c_garbage_bag.gif)

# Reason 1: Weeding Unnecessary or Redundant Files
- __Application data__: Files that are tied to specific applications (example: config.ini)
- __Encrypted or password-protected data__: Unless the decryption key is available, these files can be considered inaccessible.
- __Duplicates__: Identical files that waste storage space and complicate processing.
- __Temp files__: These often don’t hold any long-term value and can be safely discarded.
- __Binned files__: Files deleted by the creator.

---

# Reason 2: Determining the Processing Plan
- __Size and complexity of the file system__: How much organization and descriptive file naming is already present.
- __Sensitive or personally-identifying information__: Identifying and addressing areas with potentially sensitive data that may require special handling.
- __Manual sampling needs__: Areas that may need manual review or sampling for appraisal.
- __Complexity of file formats__: Some formats may require special access or reformatting, which needs to be considered early on.

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

## Definition
# Disk imaging

__Disk imaging__ describes the steps to create a bit-identical copy of the source media, resulting in a disk image. The imaging process copies data sector-by-sector from the raw device.

<!--presenter notes

Disk imaging is one of the more common and critical actions taken when performing digital forensics. Disk imaging describes the process of creating a bit-identical copy of the source media. The imaging process copies data sector-by-sector from the raw device.

What is the purpose of creating disk images? A clear explanation is given in the Canadian Center for Architecture (CCA)’s digital archives workflows Github repo. Here, they say, “[D]isk images can be stored redundantly, backed up, and audited in ways that physical carriers like DVDs or external hard drives cannot…they are a much better suited for preservation of digital information over time, while retaining all characteristics of the original physical media as a storage volume.” (https://github.com/CCA-Public/digital-archives-manual/blob/master/guides/diskimaging.md)

The benefits of disk imaging are further described by an article written by Dorothy Waugh about Emory University’s digital forensics processes. Here, she says, “From a preservation perspective, this makes forensic imaging ideal; an exact copy of the original data can be ingested into a secure and long-term storage environment. Derivative copies can later be used for continued appraisal and processing.”

In short, disk imaging liberates bitstreams from digital storage media, which can otherwise be subject to all the inherent risks associated with born-digital items. Disk images can be migrated into modern computing environments where they can be analyzed and copied, and made available for access.

So what does an image look like?

-->

## Definition
# Disk sector

A __disk sector__ is a fundamental unit of storage on a disk, whether it's a hard disk drive (HDD), solid-state drive (SSD), or other types of storage media like CDs or DVDs. It represents the smallest addressable unit of data on the disk.
