---
marp: true
theme: gaia
size: 16:9
paginate: true
style: |
  img {
    max-width: 100%;
    max-height: 90%;
    height: auto;
    width: auto;
    display: block;
    margin: 0 auto;
  }
  .white-background-slide {
  background-color: white !important; /* Override Gaia theme */
  width: 100%;
  height: 100vh;
  margin: 0;
  padding: 0;
  }


---

# Week 5
## Digital Preservation Storage Systems

---

# Announcements

- **Lecture: Digital Preservation Storage Systems**
- **Break**
- **Share: Tech Stack Slides**
- **In-class activity: Archivematica Sandbox**

---

# Lecture
## Digital Preservation Storage Systems

---

<!--presenter notes

Digital repositories rely on redundant storage to function. By storage, I am referring to the hardware and software components that are used to store digital content and ensure its long-term accessibility, integrity and usability. Because storage is so fundamental to digital repositories, we are going to spend some time specifically focusing on how storage is set up, and go over various storage architectures, technologies, hardware, and solutions.

In addition to this, we will also discuss how storage systems are prone to failure: much like a physical space is prone to leaks, mold, and pests, storage media vulnerable to these same threats, but also to threats that happen on a microscopic scale in terms of the site or sites of failure, that cannot be discerned by the naked eye, as well as threats on an economic scale, tied to the cost of maintaining and powering storage devices.

We will discuss strategies to detect and mitigate failure, that can lead to loss on scales of incredible magnitude.

-->

---

## Definition
# Storage Architecture
—

__Storage architecture__  refers to the overall design and organization of a storage system. This usually includes the types of storage devices used, the way data is stored and organized, and the methods used to access and manage the stored data.

<!--presenter notes

Storage architecture refers to the overall design and organization of a storage system, including the types of storage devices used, the way data is stored and organized, and the methods used to access and manage the stored data.

The storage architecture of a system can have a significant impact on the overall performance and reliability of an organization's digital preservation infrastructure, as well as its ability to meet the demands of growing amounts of data and changing business requirements.

-->

---

# Storage Technology
## Three Types

<!--presenter notes

Source: https://www.nedcc.org/fundamentals-of-av-preservation-textbook/chapter-4-introduction/chapter-4-section-3
There are three common types of storage infrastructures used in digital preservation.

-->

---

# Online Storage
* Networked
* Rapid access
* Always powered on
* Production environment

<!--presenter notes

Online: Storage that is accessible through a network. The result is information sharing that is quick and nearly instantaneous, so it is sometimes referred to as “hot” storage. Online storage is best suited for a production environment. For example, when I worked in New York Public Radio’s archive, reporters, producers and other staff had ready access to online storage containing recently used news clips, audio and video.

-->

---

# Nearline Storage
* Networked
* Slower to access
* Require less immediate access

<!--presenter notes

Nearline: The term “nearline” is a portmanteau of “near” and “online”. Like online storage, it is also accessible via a network. However, you may need to wait several seconds or minutes to request and retrieve data. This storage may be more suitable for less used archival data. Following my radio station example, this may be more appropriate for a reporter working on a long investigative journalism piece requiring weeks or months or research.

-->

---

# Offline Storage
* Not networked
* Requires action to connect and access
* Best for long-term
* Passive

<!--presenter notes

Offline: Offline storage architecture refers to non-networked storage. Depending on your offline storage solution, as well as the size of file you are trying to access, delivering the file to you could take several hours. However, the purpose of offline storage is never for quick access and so is sometimes referred to as “cold storage”.

Hybrid: These days, you will likely see institutions establishing so-called “hybrid” storage systems that are a combination 2 or all of these storage architecture types.

The type of storage architecture established should take into consideration the types of data being stored, the expected growth of the data over time, the access patterns to the data, and the requirements for data protection and data availability. Each type of storage architecture has advantages and disadvantages which we will discuss later on in the lecture.

-->

---

# Storage Hardware

<!--presenter notes

Next, we will discuss different types of technologies, which may be used in any of these three architecture types. You will see that some storage technologies are more appropriate for the different types.

-->

---
<div style="
    display: flex; 
    justify-content: center; 
    align-items: center; 
    position: relative; 
    height: 100vh;
    max-width: 100%; 
    margin: 0; 
    overflow: hidden; 
    background-color:rgb(255, 255, 255);">
    
  <!-- Image -->
  <img src="img/week_05_hdd.png" 
       alt="Stock image of a hard disk drive (HDD) showing a metal disc, inside of a plastic cartridge, whose right side is nestled up against a metal 'arm'." 
       style="width: 100%; height: auto; max-height: 100vh; object-fit: contain;">
       
  <!-- Header Text -->
  <h1 style="
      position: absolute; 
      top: 5%;
      left: 30%; 
      transform: translateX(-50%); 
      font-weight: bold; 
      color: white; 
      background-color: rgba(154, 1, 151, 0.5); 
      padding: 10px; 
      border-radius: 5px; 
      text-align: center;">
    Hard Disk Drive (HDD)
  </h1>
</div>

<!--presenter notes

Hard disk drive (HDD): Mechanical spinning disk; arm reads/writes bitstreams using magnetism.

-->

---

<div style="
    display: flex; 
    justify-content: center; 
    align-items: center; 
    position: relative; 
    height: 100vh;
    max-width: 100%; 
    margin: 0; 
    overflow: hidden; 
    background-color:rgb(255, 255, 255);">
    
  <!-- Image -->
  <img src="img/week_05_ssd.png" 
       alt="Stock image of a hard disk drive (HDD) showing a metal disc, inside of a plastic cartridge, whose right side is nestled up against a metal 'arm'." 
       style="width: 100%; height: auto; max-height: 100vh; object-fit: contain;">
       
  <!-- Header Text -->
  <h1 style="
      position: absolute; 
      top: 5%;
      left: 30%; 
      transform: translateX(-50%); 
      font-weight: bold; 
      color: white; 
      background-color: rgba(154, 1, 151, 0.5); 
      padding: 20px; 
      border-radius: 5px; 
      text-align: center;">
    Solid State Drive (SSD)
  </h1>
</div>

<!--presenter notes

Great video to watch that clearly explains how SSD technology works: https://www.youtube.com/watch?v=5Mh3o886qpg

You have likely encountered solid state drive technology if you have ever used a laptop, or a smartphone, or flash drive.

Layers of charge trap flash memory cells arrays

Each cell is filled with varying levels of electrons

-->

---

<img src="img/week_05_ssd_explained.png">

<!--presenter notes

How does solid state drive (SSD) technology work?

Reads/writes data onto layers of silicon chips. This stacking method allows for high-storage density over a small space.

These chips, in turn, contain arrays of tiny “charge trap memory cells”. Data is encoded by filling the charge trap memory cells with volumes of electrons. The quantity of electrons contained in a cell corresponds to a single bit, so a lot of electrons corresponds to a 1, and a little bit of electrons corresponds to a 0.
Today’s technology allows for one memory cell to hold up to 3 bits. Advances in SSD storage technology are bound to increase this.

The cells trap or “save” the level of electrons, which is how SSD drives store memory. To read the information, the level is measured. The measurement corresponds to a bitstream. To erase what is stored, you empty the cell of all electrons.

-->

---

<div style="
    display: flex; 
    justify-content: center; 
    align-items: center; 
    position: relative; 
    height: 100vh;
    max-width: 100%; 
    margin: 0; 
    overflow: hidden; 
    background-color:rgb(255, 255, 255);">
    
  <!-- Image -->
  <img src="img/week_05_tape.png" 
       alt="Stock image of a hard disk drive (HDD) showing a metal disc, inside of a plastic cartridge, whose right side is nestled up against a metal 'arm'." 
       style="width: 100%; height: auto; max-height: 100vh; object-fit: contain;">
       
  <!-- Header Text -->
  <h1 style="
      position: absolute; 
      top: 5%;
      left: 30%; 
      transform: translateX(-50%); 
      font-weight: bold; 
      color: white; 
      background-color: rgba(66, 170, 6, 0.5); 
      padding: 20px; 
      border-radius: 5px; 
      text-align: center;">
    Tape
  </h1>
</div>

<!--presenter notes

Illustrations and text from http://hyperphysics.phy-astr.gsu.edu/hbase/Audio/tape2.html

Magnetic tape, such as what you would find in a cassette tape cartridge or reel-to-reel, is made up of long thin strips of polyester plastic. The tape is coated in an emulsion, which is bound to the tape using a plastic-based “binder”, or a kind of glue that makes the emulsion stick to the tape. The emulsion is embedded with tiny magnetic-sensitive oxide particles.

-->

---
| Technology | Pros                                                                 | Cons                                                                      |
|------------|----------------------------------------------------------------------|---------------------------------------------------------------------------|
| **HDD** | Inexpensive ($40/TB) ([source](https://edwardbetts.com/price_per_tb/)), widely available | Fragile, shorter life span, slower than SSDs, higher failure rate |
| **SSD** | No moving parts, so fast and durable ([source](https://www.backblaze.com/blog/how-reliable-are-ssds/)), compact | Expensive, Limited write cycles affect longevity |
| **Tape**   | Inexpensive ($4–$8/TB), energy-efficient, longer lifespan | Slower, requires proprietary hardware/software |


<!--presenter notes

Comparison chart (updated February 2023) showing cost per terabyte of various HDD/SSD devices:
https://edwardbetts.com/price_per_tb/

We’ve covered three common storage technologies, using HDDs, SSDs and magnetic tape, and various solutions using these technologies.

HDD
Pros: The cost comparison between an HDD and SSD shows that HDDs are less costly than SSDs, coming in at $40 a TB.
Cons
An HDD is made up of moving parts, meaning, mechanical action must occur for it to read and write data. As a result, HDDs, especially when compared to SSDs, tend to run slower. You’ll notice this especially on computers booting up; typically, a computer with an SSD drive tend to start up quicker than those using an HDD.
Because HDDs are mechanical, they are less durable and more prone to physical damage.

SSD

Good overview written by Backblaze on SSD reliability: https://www.backblaze.com/blog/how-reliable-are-ssds/

Pros
- Faster: unlike a hard drive, a solid state drive has no moving parts (i.e. arm/spinning disk). Therefore, it takes less time for it to “seek”. If you boot up an operating system running on an SSD, it will take a shorter amount of time than running off an HDD.
- Durable: because it does not require moving parts, it is more resistant to damage due to physical shock
- Smaller

Cons
- More expensive
- Set life expectancy with a finite number of write cycles before performance becomes erratic.
- Tiered storage uses SSD with backup to cloud or HD

Tape

Pros
- Tape is the least expensive storage solution, especially in terms of cost per terabyte, averaging between $4-$8 per terabyte.
- The latest generations of LTO tape (LTO-8 is the latest, as of 2023) can now hold up to 30 TB per tape.

Cons
- Tape is slower, but in some ways this is less a “con” and more just telling us what it is good for, which is, offline or “cold” storage, and only accessed when you are either performing a routine backup to it, or you are needing whatever it contains to restore part of your repository.

As a result of tape libraries being a type of cold storage, they end up using less energy. Data centers that use HDD or SSD technologies, conversely, require more intensive climate control. This makes tape libraries the most sustainable of the three technologies.

Because tape libraries tend to be used more for cold storage, it also means less wear and tear on the tape library itself. Less wear and tear translates to a longer life expectancy overall for a tape library.
One big con of a tape library is its reliance on proprietary hardware and software. Tapes are made by companies that require specific machines and software to read, write and access them.

-->

---

# Storage Solutions

<!--presenter notes

Next, we are going to talk about storage solutions. Each of the storage solutions presented can utilize any of the three storage technologies and architectures we just stepped through, but you’ll see that some solutions are more specific to one or another technology.

-->

---

## Definition
# Storage Solution
—

A __storage solution__ refers to specific devices or services that can be used for storage.

<!--presenter notes

A storage solution refers to specific devices or services that can be used for storage. They can consist of one or a combination of storage technologies that we covered just now: hard disk drives, solid state drives, or magnetic tape.

-->

---

__Network-__

__attached storage (NAS)__

1 or more networked HDDs or SSDs

Online; quick

Examples: Isilon

![](img/Week%2005%20-%20Digital%20Preservation%20Storage%20Systems3.png)

---

Network-attached storage (NAS) is a type of data storage device that is connected to a network, allowing users to access and share data over that network.

NAS devices typically consist of multiple hard drives. NASs are often served out through a local data center. At NYPL, we keep preservation copies on a type of NAS called “Isilon” that uses what is known as cluster based storage, which is a type of storage that stores data across multiple servers or nodes. To users who have access privileges to the Isilon, it will show up on their File Explorer and appear like any other folder on their local workstation. Because of their networked nature, NAS’ are often used as part of online storage architectures.

Some of the benefits of NAS include:
Centralized storage: NAS devices provide centralized storage for a network, making it easy for users to store, access, and share data from a single location.
Easy access: NAS devices can be accessed from any device on the network, making it easy for users to access their data from multiple locations.
Enhanced security: NAS devices often have built-in security features such as user authentication and data encryption, making it easy to secure sensitive data.
Scalability: NAS devices can be expanded with additional hard drives as needed, making it easy to increase storage capacity as data needs grow.

__Linear-Tape Open (LTO)__

Near or offline storage

Example: CUNY TV uses an LTO tape library for offline storage

![](img/Week%2005%20-%20Digital%20Preservation%20Storage%20Systems4.png)

---

Read more about CUNY TV’s migration from LTO-5 to LTO-7 here: https://blogs.loc.gov/thesignal/2016/03/data-migration-digital-asset-management-and-microservices-at-cuny-tv/

Photo credit: Dinah Handel, who was an NDSR resident at CUNY TV in 2015/2016

A Linear Tape-Open (LTO) tape library is a type of tape storage system that uses magnetic tape technology to store and retrieve data, and is best suited for long-term data retention. Therefore, it is often used in offline storage architectures. LTO tape libraries consist of one or more tape drives and one or more tape cartridges that are housed in a removable magazine or a rack-mounted cabinet.
The LTO format is an open-format standard developed by Hewlett-Packard, IBM, and Quantum, and has been widely adopted by various tape storage vendors.
LTO tapes can store large amounts of data, with capacities in the tens of terabytes, making them well-suited for large-scale data storage.
LTO tapes are highly durable and can last for several decades, making them an ideal choice for long-term data preservation.
Tape storage is often more cost-effective than other types of storage, especially for large-scale data storage, making it a good choice for preserving large amounts of data.
The tapes themselves are small and lightweight, making them easy to store and transport, especially when it comes to off-site storage and disaster recovery.
Tape storage is known for its reliability and longevity, and is less likely to experience data loss due to disk failures, which can be a concern with other types of storage.

![](img/Week%2005%20-%20Digital%20Preservation%20Storage%20Systems5.png)

Remotely located

Maintained by third-party vendor

Arrays of SSDs or HDDs

Near- or offline storage

Example: Amazon S3

---

Image source: https://en.wikipedia.org/wiki/Google_data_centers#/media/File:Google_datacenter_(2007)_-_panoramio_-_erwinboogert_(2).jpg

Cloud storage involves storing data on remote servers that are accessed over the internet, rather than being stored on a local device or server and accessible through a local network. Cloud storage solutions use a network of servers in data centers to store and manage data. Cloud storage is often used for near- or offline storage architectures.

Cloud storage solutions can use either Hard Disk Drives (HDD) or Solid State Drives (SSD) to store data. Some cloud storage providers offer the option to choose between HDD and SSD storage, while others only offer one or the other. The choice between the two technologies depends on the specific needs of the user, such as the amount of data being stored, the performance requirements, and the budget.

If considering cloud storage services, one thing to keep in mind is that the costs are not just specific to the amount of data you intend to store in the cloud; you will likely also be charged by the amount of data being transferred from the cloud to you, or to your access platform, or somewhere else. Something to keep in mind when thinking about storage budgets. The Rosenthal article assigned to you this week talks specifically about the cloud and associated costs.

__Redundant Array of Independent Disks (RAID)__

Array of HDDs or SSDs

Usually onsite for quick access

Uses parity technology to repair corruption

![](img/Week%2005%20-%20Digital%20Preservation%20Storage%20Systems6.png)

---

RAID stands for “redundant array of independent disks”. A RAID is an array of hard disk or solid state drives, that work in concert with one another to ensure that if one drive fails, another can pick up where it left off.

One thing to note about RAIDS is that they are not without their own faults. For one, RAIDS tend to use the same type of hardware across the array, which means that there is a risk of concurrent failures after a certain point.

RAIDS use what is known as parity to restore and repair damaged bitstreams.

# Definition: Parity
—

__Parity__ __describes the process that some storage systems use to identify and recover corrupted bits.__

__It can do this by storing additional information (parity bits) about two twin bits stored on different drives.__

---

Along with storing bitstreams, RAIDs store what are known “parity bits” or “parity data”, which it uses to both identify when a bit has become corrupted, and restore the corrupted bits to their original form. Parity information is stored in its own spot in the RAID adjacent to the data it is storing.

| Date | Bit A Value | Bit B Value | Bit A + Bit B | Parity bit value |
| :-: | :-: | :-: | :-: | :-: |
| 1/1/2024 | 1 | 1 | 1 + 1 = 2 | 1 (Even) |
| 1/2/2024 | 1 | 1 | 1 + 1 + 2 | 1 (Even) |
| … | … | … | … | … |
| 12/31/2024 | 0 | 1 | 0 + 1 = 1 | 0 (Odd) |

---

Parity data stores information about whether or not the sum of the two identical bits over two or more hard drives adds up to an even number, or an odd number. For example, let’s pretend that we have a very simple RAID system with two hard drives. Each hard drive contains exactly 1 bit each, and are a copy of one another.

The first day we hook up our RAID to our computer, we decide to store a bit of information on the RAID: the number 1. The RAID will copy this bit to each of the two drives, as well as record whether or not the sum of these two bits (1 + 1) is even or odd. The sum of 1+1 is 2, so it is even, so the RAID stores the fact that the sum of these two twin bits are even in the place where it stores parity information as a bit itself. In this system, a 1 means “parity bit is even” and a 0 means “parity bit is odd”.

A day later, the RAID, through the course of its usual responsibilities, adds the two bits up together again, 1 and 1, and checks that the sum is even. It is. Great! This means the bit in both drives are the same.

A week later, the RAID notices that one of hard drives has failed. It makes note of which hard drive has failed, and checks the parity, which now calculates to an odd number, because 1 plus nothing or 0 equals 1, which is an odd number. However, because it knows it expects an even number, it can surmise that the bit “flipped”, and additionally, know that the flipped bit is supposed to be a 1, because it knows the sum result must be even.

This is a somewhat oversimplification of how parity works. However, it’s good to know that there are things like parity that devices and software can use to not just check for data corruption, but also restore data. I think this is an important thing to know because when it comes to digital technologies, we are often told that we never really know what’s going on inside of whatever device we are using, and as a result we are always just waiting for catastrophic failure. But just know that there are systems in place that are self-checking, and self-correcting.

<span style="color:#FF8BFF">Case Study

<span style="color:#FF8BFF">__UC San Diego\, Chronopolis__

<span style="color:#FF8BFF"> _Updating storage systems_

---

In your assigned reading for this week, we read about how the Bentley Historical Library developed an integrated system using three of the four digital repository system types we just covered [Digital Preservation System: Archivematica; Institutional Repository: DSpace; and Content Management System: ArchivesSpace]. The purpose here was to play to each of the systems’ strengths to fully support an “end-to-end digital archives workflow”. These sorts of integrative setups are quite common in digital archives in general. These integrations are achieved using what are known as application programming interfaces or APIs. An API is basically just a set of instructions or protocols that allows one system to talk or update data in the other.

Let’s explore each of these systems further.

__Storage example: UC San Diego\,__ __Chronopolis__

_In the past:_

2-TB drives running on RAID 10

Hard disk failure happened

_Current:_

Primary Storage: Isilon NAS (1.6 Petabytes) on 5 nodes

Purchased another cluster 5 years later

Location: On-campus

Fixity audit run every 45 days

_Future:_

Amazon cloud storage

Use a “snowball” SSD to transfer data

Not considering tape backup; would prefer cold cloud storage

---

So how might all of what we covered, architectures, technologies, and solutions fit together? What is an example of their use in a digital preservation environment?

One good example given to us is from the Module 13: Digital Preservation Case Studies SAA publication assigned to you this week. Here, they provide transcribed interviews with various digital preservation archivists and administrators, who describe what systems they have used, their experiences with them, and their plans for the future.

In the UC San Diego example, we are looking at a fairly large institutional repository system that at first used a RAID 10 system. Here, they reflect on how the their RAID often failed, which spurred them to purchase a refurbished Isilon NAS. They remark how the Isilon system allowed them to better scale up their storage capacity, in light of the fact that they are seeing a storage growth rate of about 5TB year-over-year, and expect that rate to increase with the launch of their new DAMS and migrations of their born-digital holdings. Here, they talk about how appraisal may decrease how much of these holdings they actually end up ingesting into their repository.

In the future, it sounds like they are considering cloud storage services. In particular, they talk about how Amazon, for large data transfers, prefer that they use something called a “Snow ball”. A snowball is basically a beefed up hard drive that Amazon sends to the transferring institution. The institution then moves a copy of their archive to the snowball, and then physically ships it back to the data center for processing. Snow balls are useful because transferring over networks means there are bandwidth limitations. Also, networks can be unstable, which could compromise the data.

<span style="color:#CE8FFB">__Mini Activity__

<span style="color:#CE8FFB">Your institution is taking on a mass digitization project to scan and digitize 100 analog films. Each film will result in ~ 2 gigabytes worth of data. With a partner\, do a couple of web browser searches to come up with an estimate for each of the storage solutions below. Present your findings to the class.

__Amazon S3 Glacier__

__LTO tape library__

---

Source: https://en.wikipedia.org/wiki/JPEG_File_Interchange_Format

Let’s put all of what we just learned together about content information, content data objects, representation information, knowledge bases and designated communities.

On the slide we have a screen capture of a scanned page of the Forme of Cury, a cookbook from the Late Middle Ages, dating to the late 14th century, written in Middle English.

Based on the definitions we just reviewed in the previous slides for Data Object and Representation Information, take a guess what might constitute, in an OAIS, its content information, the data object, the designated community and its knowledge base, and the representation information? Take a minute to think about it and write down your thoughts somewhere if you need to.

Would anyone like to share their findings with the class?

An answer (this is not the right answer, just a suggestion):

Data object: the bitstream of the scanned page of text.
The system may require semantic information to convey that this book is written in an obsolete language.
Structural information may include detail to render the bitstream into pixels, or even optical character recognition (OCR) technologies that can transcribe old English handwriting into raw text. 
Other representation information may include some sort of text transcription that translates the cookbook into modern English. This may depend on the repository’s designated community’s knowledge base. If the knowledge base is narrow (say, researchers who are skilled in reading/translating old english texts) then this may not be necessary. However, if the designated community is broad (say, the general public), then this sort of information may be necessary.

---

Next, we are going to talk about storage solutions. Each of the storage solutions presented can utilize any of the three storage technologies and architectures we just stepped through, but you’ll see that some solutions are more specific to one or another technology.

<span style="color:#FF8BFF">__Challenges in data storage management__

<span style="color:#FF8BFF">__Hardware failure__

<span style="color:#FF8BFF">Component malfunction

<span style="color:#FF8BFF">__Software failure__

<span style="color:#FF8BFF">System malfunctions

<span style="color:#FF8BFF">__Economic volatility__

<span style="color:#FF8BFF">Financial instability

<span style="color:#FF8BFF">__Budget cuts__

<span style="color:#FF8BFF">Reduced financial resources

<span style="color:#FF8BFF">__Natural disasters / climate change__

<span style="color:#FF8BFF">Environmental disruptions

<span style="color:#FF8BFF">__Power supply issues__

<span style="color:#FF8BFF">Electrical grid failures

<span style="color:#FF8BFF">__Human error__

<span style="color:#FF8BFF">Operational mistakes

<span style="color:#FF8BFF">__Third-party attack__

<span style="color:#FF8BFF">External security breach

---

There are a considerable number of risks posed to digital storage, a few which I have listed in the slide, many which I have alluded to in covering various storage technologies and solutions. Over the next few slides, we will talk about these risks in terms of how we can mitigate them over the short- and long-term.

![](img/Week%2005%20-%20Digital%20Preservation%20Storage%20Systems7.png)

# Monitor the storage environment

---

Regular monitoring should be done over the digital repository to ensure all parts are functioning as they should. Ideally this should be automated.

This is a screenshot of a Synology NAS system monitoring dashboard. Here, there is a Storage panel that lists all hard disk storage devices, lists their temperatures, and status. On the right-hand side, notice that there are some other facets showing you things like total volume versus used capacity, and a security panel showing you logged in users. Systems like Synology provide these sorts of out-of-the-box dashboards that enable you and your colleagues to better monitor the overall performance of your storage. You can also set it up to receive email or other notifications if, for example, your available capacity reaches a certain threshold.

![](img/Week%2005%20-%20Digital%20Preservation%20Storage%20Systems8.png)

# Perform data audits

---

Image source: https://qanda.digipres.org/332/what-tools-do-you-use-for-the-ongoing-monitoring-of-checksums (note, the screenshot is a “fake” audit log that does not display real data, per the author’s explanation!)

Rehash: Fixity is a term used to describe the integrity of digital files over time. Checking the fixity of digital files at regular intervals involves verifying that the content of the file has not changed or been altered. There are a number of tools and techniques that can be used to check the fixity of files in a digital preservation storage system:

Checksum or hash values: A checksum or hash value is a unique digital signature that can be calculated for a file. By comparing the calculated hash value of a file with the original hash value, it is possible to determine if the file has been altered. Popular hashing algorithms include MD5, SHA-1, and SHA-256. Many digital repository systems include fixity checks as part of the standard software package features. You can set up fixity to run as often as you wish, but keep in mind that fixity monitoring can be very time and energy consuming. You could, for example, only run fixity when files are transferred, for example, from temporary storage to long-term storage.

Logging and auditing: Keeping a log of all changes made to the files in the digital preservation storage system can help identify if any files have been altered or corrupted. Regular auditing of the logs can help ensure that the system is working as intended and that the content of the files remains intact.




<span style="color:#C27BA0">__Question__

<span style="color:#741B47">Frequently backing data up across multiple storage devices is considered a de facto strategy to prevent loss. However\, we now know that bits can “flip”. How might an institution prevent accidentally backing up  <span style="color:#741B47"> _corrupted_  <span style="color:#741B47"> data?

<span style="color:#1155CC">__Redundancy and Replication Strategies__

<span style="color:#1155CC">__3-2-1 or LOCKSS (Lots of Copies Keep Stuff Safe)__

<span style="color:#1155CC">Safety through redundancy

<span style="color:#1155CC">__Offline/non-networked storage for file recovery__

<span style="color:#1155CC">Keep backups in offline or non-networked storage\, to protect data from cyber threats and ensure a reliable recovery option in case of a network breach.

<span style="color:#1155CC">__Delta differencing__

<span style="color:#1155CC">Minimizes storage needs by only saving changes made since the last backup\, rather than duplicating the entire data set.

<span style="color:#1155CC">__Cloud Storage Mirroring__

<span style="color:#1155CC">Mirror (copy) across multiple cloud storage locations

---

3-2-1 strategy (at least): Keep 3 copies, where 2 copies are on separate storage devices, and one copy is stored in a geographically distinct location from the other two.

Offline storage: Consider using some sort of offline storage solution. Not only is it cheap compared to on- or nearline solutions, but by nature of being non-networked, provides added protection against network-specific threats. This includes obvious things like viruses and malware infecting networked devices.

Offline storage also provides protection against accidentally backing up a mistake. For example, let’s say you get a fixity report that shows that some files have been compromised on your NAS. Your NAS is set up to be auto-synced to a cloud backup system, which means that whatever files have been compromised have now been backed up to your backup, which means 2 of your 3 backup devices contain incorrect data. However, your offline backup has not been altered, therefore, you can pull the unaltered copies from your tape library and restore these compromised files back to their original form.

Delta differencing: a backup strategy only backs up blocks that have changed after the first full backup. The differences are recorded in files called deltas. The process involves examining a backup file set and locating the blocks that have changed since the last backup period. Changed data, rather than the entire file set, can then be sent to the backup target. Because only those blocks that contain differences are extracted and backed up, it is possible to perform much faster and more frequent backup cycles without monopolizing bandwidth.

Cloud Storage Mirroring: Data is mirrored across multiple cloud storage locations to enhance accessibility and disaster recovery, ensuring data availability even if one cloud service experiences an outage.

__Data Exit Strategy__

__Scenarios:__

__Your institution goes with a new service__

__Digital preservation software service provider shutters its doors__

__Make sure you document and discuss with your service provider:__

__Steps for how to get data out__

__Are there any software or hardware dependencies?__

__Will they provide training?__

__The steps your service provider will take__

---

https://sr.ithaka.org/publications/the-effectiveness-and-durability-of-digital-preservation-and-curation-systems/

You will also need to plan for the possibility of organizational failure. For example, your digital preservation software service provider goes out of business unexpectedly. A more common scenario is your institution switching providers (there was at least one example of this given in the assigned readings of this happening.) Whatever the case may be, there will probably be a time where your organization will need to get the data out of the system and into another, and you should be prepared for it.

To meet this risk, you should also have a firm understanding of what steps both you and the vendor need to take, to ensure smooth migration of data from one system to another. If the vendor does not have clear documentation of what steps they or you should take, you should consider that as a red flag.

You can and should expect that the vendor has a documented contingency plan. For example, in the event of insolvency, they will place your data into escrow. Understand what hardware or software dependencies there might be in place that may hinder or help data migration.

Another good question to ask is if we do not uphold our end of the contract – let’s say we can’t pay for our license – is there a grace period? Will they just delete our stuff immediately or do we get some sort of grace period? What in general is their retention policy?

![](img/Week%2005%20-%20Digital%20Preservation%20Storage%20Systems9.gif)

<span style="color:#20124D">__In-class activity__

_[Archivematica Sandbox](https://digital-archives.github.io/HISTGA1011/activities/archivematica.html)_

