---
marp: true
---

# Week 3 
## Appraisal and Accessioning
### First Encounters with Born-Digital Materials

---

# Today

- **Discussion**
- **Lecture**
- **Break**
- **Activity**

---

# Announcements

_Feel free to email me with any announcements you would like me to boost (upcoming conferences, webinars, trainings, or other events/topics of interest)._

---

# Appraisal and Accessioning

---

# Why Think Critically About Born-Digital Appraisal?

**Downstream Effects**  
Poor appraisal decisions can create unintended negative outcomes later in the stewardship lifecycle.

**Redundancy at Scale**  
Reviewing files at scale complicates the task of identifying unique records.

**Format Diversity**  
Repositories must be prepared to encounter unexpected media and/or file formats.

**Complexity**  
Born-digital records are not only numerous but often interdependent on other data objects.

---

## Definition
# Archival Appraisal - Paper-Based Definition

__Appraisal__ is the process of determining whether records and other materials have permanent (archival) value. Appraisal may be done at the collection, creator, series, file, or item level. Appraisal can take place prior to donation and prior to physical transfer, at or after accessioning. The basis of appraisal decisions may include a number of factors, including the records’ provenance and content, their authenticity and reliability, their order and completeness, their condition and costs to preserve them, and their intrinsic value. Appraisal often takes place within a larger institutional collecting policy and mission statement.

<!--presenter notes

https://dictionary.archivists.org/entry/appraisal.html

-->

---

# Appraisal Considerations
- Do we have the tools to extract the record off the media?
- Can we preserve/maintain the record over time?
- Can we provide access to the record?
- Do these records speak to our collection development policy, or its overall goals?
- Do we have access to the creator/organization, who can provide to us context as far as who and how records are being created?

---

# Step 1: Donor Agreement / Transfer to the Repository

Example: <a href="https://library.ccny.cuny.edu/dss/ir" target="_blank">https://library.ccny.cuny.edu/dss/ir</a>

Another example: Physical media is shipped/delivered to the repository

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

## Definition
# Born-digital item

__Born-digital__ items are materials that are created in a digital format. This includes websites, email, digital photographs, electronic records, and more. Born-digital items are distinct from analog items that are subsequently digitized, such as paper manuscripts or photographs.

<!--presenter notes
https://primarysources.yale.edu/what-does-born-digital-mean
-->

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
- __Binned Files__: Files deleted by the creator.

---

# Reason 2: Determining the Processing Plan
- __Size and complexity of the file system__: How much organization and descriptive file naming is already present.
- __Sensitive or personally-identifying information__: Identifying and addressing areas with potentially sensitive data that may require special handling.
- __Manual sampling needs__: Areas that may need manual review or sampling for appraisal.
- __Complexity of file formats__: Some formats may require special access or reformatting, which needs to be considered early on.

---