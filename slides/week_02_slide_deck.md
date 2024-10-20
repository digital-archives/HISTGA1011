---
marp: true
---

# Week 2: Open Archival Information System (OAIS)

---

# Today
- Reminders/announcements
- Lecture: Open Archival Information System (OAIS)- Break
- Next class

---

# Open Archival Information System (OAIS)

---

# __Question__: What does Owens mean by “craft” of digital preservation? What does that term imply in regards to digital preservation?

---

“If the permanent maintenance of any given state, or set of states, was the definition of digital sustainability, then we could merely select a suitable technical strategy to permanently inscribe those states and entrust the objects to an appropriate storage and preservation strategy. However, the layers of dependencies and interdependencies, standards, agreements, understandings, technologies, strategies, workflows, and business models render that simple preservation model indefensible.”

Kevin Bradley, from “Defining Digital Sustainability” (2007)

<!--presenter notes

Source for quote: Lee, Christopher A., and Tibbo, Helen. “Where’s the Archivist in Digital Curation? Exploring the Possibilities through a Matrix of Knowledge and Skills.” Archivaria: 72 (Fall 2011) pp. 123-168. http://www.ils.unc.edu/callee/p123-lee.pdf

-->

---

https://muse.jhu.edu/article/223247

![](img/week_02_slide_deck0.png)

<!--presenter notes

This diagram provides a timeline for some of the earliest developed digital preservation standards. You’ll see the OAIS Reference Model over near the top-right. You can see how it has been referenced by subsequent frameworks since it became an official ISO standard in 2003. We will not be going through all the frameworks OAIS influenced, but will look at one in particular: ISO 16363, aka the “Audit and certification of trustworthy digital repositories” standard, sometimes known just as “TRAC”, which stands for “Trustworthy Repositories Audit & Certification”.

-->

---

## Definition
# Open Archival Information System (OAIS)

__An Open Archival Information System__ (OAIS) is an Archive consisting of an organization, which may be part of a larger organization, of people and systems that has accepted the responsibility to preserve information and make it available for a Designated Community.

<!--presenter notes

An Open Archival Information System, or OAIS, is defined as an Archive, consisting of an organization, which may be part of a larger organization, of people that has accepted the responsibility to preserve information and make it available for a Designated Community. When we are referring to an OAIS, we are referring, basically, to an archive who has accepted this responsibility.

Now that we have a definition for OAIS under our belts, we will first define what the Reference Model for an OAIS is, and then unpack some of the terms used in the definition on the slide: information, and later, designated community.

-->

---

# Why is the OAIS important?

- __Widely accepted:__  key digital preservation standard
- __Comprehensive:__ covers ingest to end-user access
- __Flexible:__ can be applied to a variety of environments and systems
- __Clear:__ Well-defined attributes for a robust digital archives system

<!--presenter notes

Source: These bullets are derived from a SERI Educational Webinar, viewable on YouTube: https://www.youtube.com/watch?v=MWITvx5yAEs (the slide I’ve transferred can be found at 9:33)

“Over the past several years, the OAIS has become a widely accepted foundation for research and development on digital archives. The OAIS has become ‘the reference model of choice of those involved in the digital preservation world serving as a ‘galvanizing force’ and a ‘major factor in the advancement of digital archiving efforts.’ It has contributed ‘a common language and concepts for different professional groups involved in digital preservation and developing archiving systems’ and represents ‘common ground upon which to consolidate understanding of the needs and requirements of digital preservation.’ Many types of institutions – including archives – were involved in its development and have used it as a basis for their work.”

-->

---

# OAIS Reference Model Limitations
- __Non-specific__: Written at a high level of abstraction
- __Narrow scope__: Does not address core archival functions such as advocacy and outreach, deaccessioning, reference and user support services, or selection, appraisal, and disposition
- __Non-prescriptive__: Does not detail how to collaborate, coordinate or implement the model

<!--presenter notes

Source: Lee, Christopher A., and Tibbo, Helen. “Where’s the Archivist in Digital Curation? Exploring the Possibilities through a Matrix of Knowledge and Skills.” Archivaria: 72 (Fall 2011) pp. 123-168. http://www.ils.unc.edu/callee/p123-lee.pdf

The OAIS Reference Model employs a very general nomenclature made up of "terms that are not already overloaded with meaning so as to reduce conveying unintended meanings" (Consultative Committee for Space Data Systems 2002, pp. 1–7). This is useful because many of us rely on jargon unique to our own archival settings, which can make communication across archives difficult. You might have also noticed that the OAIS does not prescribe any specific system or technical setup and is written at a high level of abstraction.

The result of these generalistic terms, is that the various archival communities need to translate OAIS terminology to the relevant concepts that apply in their specific contexts. For some institutions this may be to their advantage. On the other hand, this may seem very out of reach to an archive just starting out, or lacks the resources required to establish such a multi-faceted system.

Additionally, the OAIS does not address core archival functions such as advocacy and outreach, deaccessioning, reference and user support services, or selection, appraisal and disposition. Implementation of an OAIS or OAIS-like system without integrating these other, and equally important archival functions risks the OAIS failing to garner buy-in and support from stakeholders.

The OAIS also does not address how to collaborate, coordinate or implement the model. Most archives do not exist in a vacuum. To establish this sort of system, they would likely need to coordinate with folks in IT, for example.

-->

![](img/week_02_slide_deck1.png)

# Text: Reference Model for an Open Archival Information System (OAIS)
—

__The__  __Reference Model for an Open Archival Information System__ __ document was developed for use in facilitating a broad, discipline- independent consensus on the requirements for an archive or repository to provide long-term preservation of digital information.__

---

This week, you were assigned to skim parts of the Reference Model for an OAIS document. The Reference Model for an Open Archival Information System (OAIS) document was developed for use in facilitating a broad, discipline-independent consensus on the requirements for an archive or repository to provide long-term preservation of digital information. It is sometimes referred to as the “Magenta Book” because of the color of its cover page.The OAIS Reference Model was approved in January 2002 as ISO International Standard 14721; a revised and updated version was published in 2012 as ISO (International Standards Organization) Standard 14721:2012.

The Consultative Committee for Space Data Systems (CCSDS) initiated the creation of this standard, and aimed at developing formal standards for the long-term storage of digital data generated from space missions.

This document was was developed for use in facilitating a broad, discipline-independent consensus on the requirements for an archive or repository to provide long-term preservation of digital information. It was also intended to support the development of additional digital preservation standards.

So now, let’s turn back again to our OAIS definition, and unpack what it means by “preserve information”.

# Definition: Content Information
—

__Content information is composed of the__  __data object__ __ (bitstream) and__  __representation information__ __ (to make sense of the bitstream).__

<span style="color:#595959"> __Data Object__ 

<span style="color:#595959">01001000

<span style="color:#595959"> __Representation Information__ 

<span style="color:#595959">01001000

<span style="color:#595959">= 72 

<span style="color:#595959">= H

<span style="color:#FFFFFF">Content   <span style="color:#FFFFFF">Information

---

Source: https://wiki.dpconline.org/index.php?title=4.2.1.3.1_Representation_Information_Types

At first glance, you might think that an OAIS would only be concerned with preserving bitstreams, the 1s and 0s that underlie things like word processing documents, videos, audio, and even software. But that is far from the case.

Bitstreams are not inherently understandable. Because of this, the OAIS considers both the bitstream and whatever else is needed to decode and make sense of the bitstream equally as important as far as the things it is concerned with preserving go.

The OAIS calls the bitstream the data object. The tools necessary to interpret, decode or render the data object are known in OAIS as representation information, additional information needed to decode the bitstream. The data object and representation information together comprise content information.

Content information is the primary thing that an OAIS is concerned with managing and preserving, and is sometimes also referred to as the preservation target.

Let’s talk more about representation information.

<span style="color:#F3F3F3">01001000

<span style="color:#F3F3F3">01001001

---

Last week, we covered the basics of binaries and bitstreams. A bitstream is defined as sequence of 1s and 0s. We also learned how to interpret one byte of data to a decimal number.

Typically I do not like or endorse trick questions, but I’d like to ask this to prove a point. The trick question is: Can anyone guess what this string of 1s and 0s on the slide means?

The answer is that you can’t really know what any string of 1s and 0s means without some sort of other information that tells you how to interpret it, or can automatically render it. This is especially true when concerning things like a piece of digital art, video, document, that requires some sort of intermediary software or hardware system to interpret. Even if we were to decode this bitstream into decimals, without any sort of context, it still would just be numbers without any meaning.



<span style="color:#274E13">“Representation Information might include a description of the hardware and software environment needed to display the Content Data Object and/or access its contents; it might also summarize the appropriate interpretation of the Content Data Object. For example, if the Content Data Object is an ASCII file of numbers, Representation Information might indicate that the numbers correspond to average daily air temperature readings for London, measured in degrees Celsius, for the period 1972 – 2000.”

The Open Archival Information System (OAIS) Reference Model: Introductory Guide (2nd Edition)

---

So what is an example of representation information? The quote on the slide is from an OCLC Research Publication, The Open Archival Information System (OAIS) Reference Model: Introductory Guide. Here, the author Brian Lavoie describes an example of representation information:

“Representation Information might include a description of the hardware and software environment needed to display the Content Data Object and/or access its contents; it might also summarize the appropriate interpretation of the Content Data Object. For example, if the Content Data Object is an ASCII file of numbers, Representation Information might indicate that the numbers correspond to average daily air temperature readings for London, measured in degrees Celsius, for the period 1972–2000.”

| Sentence | HI |
| :-: | :-: |
| Character |       H          I |
| Number |      72          73 |
| Binary | 01001000     01001001 |
| Hardware |  |

---

Last week, when we discussed binary, we talked about how we can break down letters into its constituent alphanumeric characters H and I, and then further to decimal numbers, which correspond to two bytes of information, each of which are composed of 8 total 0s and 1s. This was my simplistic example of representation information for digital text.

![](img/week_02_slide_deck2.png)

---

We also talked about ASCII. ASCII stands for American Standard Code for Information Interchange. Most digital documents written using word processing software likely use ASCII, or some other sort of internal dictionary, that maps letters, numbers, and other symbols, to a decimal value, and ultimately a binary value.

The slide shows a screenshot of an ASCII chart, that maps out binary representations to decimal numbers to hexadecimals (sometimes known as just “hex”) to the symbol on the screen or keyboard stroke that it ultimately represents.

# Definition: Structure Information
—

__A type of representation information that maps the data object, or bitstream, to understandable data types and structures.__

__Example: file format (i.e. FLAC, PDF, DOC, JPEG, etc.)__

---

There are two types of representation information: structure information and semantic information.

Structure information deals with how to map the bitstream into higher-level data types and meaningful concepts. One example you have likely encountered working on a computer is file format metadata.

When you open up a folder of files, the files themselves have some sort of name, followed by a period, followed by a dot and then the name of a file type like my_image.JPEG or my_song.MP3 or my_writing.DOC. The dot, followed by a typically 3- or 4-character format code is a type of structure information that tells you or the computer how to decode the file. 

[demo changing a file in my Downloads folder from PDF to JPEG and back to PDF, to see what happens]

If you removed the .[whatever] after a file’s name, your computer will throw some sort of error because it’s missing the structure information it expects to interpret and make sense of the file.

https://wiki.dpconline.org/index.php?title=4.2.1.3.1_Representation_Information_Types

# Definition: Semantic Information
—

__A type of representation information that clarifies the meaning or appropriate interpretation of the Content Data Object.__

__Example: A glossary, a data dictionary, and a software application’s user documentation__

---

Semantic information is any other additional information that clarifies, guides or interprets the data object. For example, a glossary, a data dictionary, or a software application’s user documentation. The ASCII dictionary we’ve been looking at is a good example of semantic information.

https://wiki.dpconline.org/index.php?title=4.2.1.3.1_Representation_Information_Types

![](img/week_02_slide_deck3.png)

__Case Study__

__Dennis Parichy Lighting Designs__

__Photo credit:__

__Billy Rose Theatre Division, The New York Public Library. "Publicity photo of lighting designer Dennis Parichy (New York)" New York Public Library Digital Collections.__  _[https://digitalcollections.nypl.org/items/858d2d20-1fb7-0136-cbed-478a43ad47de](https://digitalcollections.nypl.org/items/858d2d20-1fb7-0136-cbed-478a43ad47de)_

---

Let’s look at an example from NYPL’s collections to discuss what we’ve learned so far about the OAIS Framework.

In 2013, NYPL acquired the works of Dennis Parichy, a New York City-based lighting designer. Parichy designed lighting for 25 Broadway productions since 1976. He has been nominated three times for a Tony Award for his lighting design work.


![](img/week_02_slide_deck4.png)

---

The Parichy acquisition contained both physical files as well as born-digital materials on floppy disks, because later on in his career, he used two software programs, Lightwright and VectorWorks (which are interoperable with one another), to program stage lighting cues. The slide shows a screenshot of the Lightwright interface. Here, you can see that the user could program a queue of stage lighting directions, and specify things like stage position, sequence, and give each lighting direction a name. We can, if we wanted to, watch a YouTube video of how to use this program. https://www.youtube.com/watch?v=LoBcIxjydKg



![](img/week_02_slide_deck5.png)

---

Photo credit:
Pollard, Collette. "Set Design for DON’T TELL ME I CAN’T FLY." 2011. Digital Image. Accessed January 26, 2024. https://collettepollard.com/production/dont-tell-me-i-cant-fly/

These sorts of lighting cues would translate into something like this (I’m not certain he was using LightWorks or some other program, but, you get what I mean!)


<span style="color:#C27BA0"> __Question__ 

<span style="color:#741B47">Using the Parichy LightWorks example, what might constitute this collection’s Content Information?

<span style="color:#595959"> __Data object__ 

<span style="color:#595959">01001000

<span style="color:#595959"> __Representation Information__ 

<span style="color:#595959">01001000

<span style="color:#595959">= 72  <span style="color:#595959"> 

<span style="color:#595959">= H

<span style="color:#FFFFFF">Content Information

# Definition: Consumers
—

__In the context of an OAIS,__  __consumers__ __ can be simply described as the users of the OAIS.__

# Definition: Designated Community
—

__A__  __designated community__ __ is a special type of consumer that describes the primary users or people accessing the information preserved within the OAIS.__

---

Now that we have a grasp on what the OAIS’ definition of content information is and what that consists of, let’s look at what the OAIS means by a designated community.

Let’s revisit the definition of an OAIS, which is “an Archive consisting of an organization, which may be part of a larger organization, of people and systems that has accepted the responsibility to preserve information and make it available for a Designated Community.”

A Designated Community is a specified class of users expected to consume and understand the archived information in an OAIS. For example:
NARA’s Electronic and Special Media Records Services Division’s Archives’ designated community is the general public.
NASA’s Planetary Data Systems Archive’s designated community is the planetary science community.

Designated communities are determined in large part by the type of knowledge base required to understand the archive’s holdings. Let’s define what we mean by knowledge base next.

Source: https://www.oclc.org/research/publications/2000/lavoie-oais.html

# Definition: Knowledge base
—

__A__  __knowledge base__ __ is a set of information, incorporated by a person or system, that allows that person or system to understand the information preserved in the OAIS.__

__The OAIS must understand the knowledge base of its designated community to understand the minimum representation information that must be maintained.__

---

Designated communities have what’s known as a specific knowledge base. A knowledge base is a set of information, incorporated by a person or system, that allows them to understand the received information. An OAIS should incorporate what it knows about a designated community’s knowledge base in order to understand the minimum representation information that must be maintained for whatever it is preserving to make sense both in the immediate and long-term. 

![](img/week_02_slide_deck6.jpg)

<span style="color:#CE8FFB"> __Mini Activity__ 

<span style="color:#CE8FFB">Page from Forme of Cury, a cookbook from the Late Middle Ages. Part of the Rylands Medieval Collection. It was written in Middle English.   <span style="color:#CE8FFB"> __Determine:__ 

__content information__

__representation__ __ information__

__designated community__

Forme\_of\_Cury-MS\_7-18v.jpg

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

__OAIS Functional Model__

__OAIS Functional Model Diagram__

__Preservation Planning__

__Descriptive information__

__Descriptive information__

__Archival Storage__

---

Diagram credit: By Mathieualexhache (original work); Mess (SVG conversion &amp; English translation) - File:Schema fonctionnel modele oais.jpg, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=98896005


Here we have a diagram showing a visualization of the OAIS functional model, which describes how information enters into, is stored in, and flows out of an OAIS and the various functional entities that interact with the OAIS.

Take a minute to look at the “flow” of information in/outof an OAIS. The various OAIS functions - preservation planning, ingest, data management, archival storage, administration and access - are labeled in brown. Entities that interact with the OAIS - producers, consumers and management - are labeled in plain black text. Various information packages handled by the OAIS - SIPs, AIPs, and DIPs - are labeled in the white circles. The OAIS itself is delineated by the dotted rectangle.

Source: Figure 1 diagram from https://www.oclc.org/research/publications/2000/lavoie-oais.html


__Information Packages__

__Preservation Planning__

__Descriptive information__

__Descriptive information__

__Archival Storage__

---

We are going to focus first on what are known as information packages which are broadly defined as the data submitted, managed and distributed by an OAIS. There are three different types of information packages: Submission Information packages, or “SIPs”, Archival Information Packages, or “AIPs”, and Dissemination Information Packages, or “DIPs”. So SIPs, AIPs and DIPs. These are all highlighted in the slide in yellow.

In defining what each information package is, we will also learn more about the entities who interact with or receive data from an OAIS: Producers, Consumers, and Management. I’ve underlined these entities in yellow.

# Definition: Information Package (1/3)
—

__The OAIS information model is built around the concept of an information package, which consists of the object that is the focus of preservation, along with metadata necessary to support its long-term preservation, access, and understandability, bound into a single logical package (usually, a computer folder)__

---

The OAIS information model is built around the concept of an information package, which consists of the object that is the focus of preservation, along with metadata necessary to support its long-term preservation, access, and understandability, bound into a single logical package (usually, a computer folder)

__Preservation Description__

---

Source: Marks, S. (2015). In M. Shallcross (Ed.), Module 8: Becoming a Trusted Digital Repository (Ser. Trends in Archives Practice, p. 5). essay, Society of American Archivists.

All information packages contain four components containing different types of information, each which serve a purpose in managing the package through various stages, from submission, to storage, and access. They are: Content Information, Preservation Description Information, Packaging Information and Description Information.

# Information Package

<span style="color:#FFFFFF">OAIS

<span style="color:#FFFFFF">1 OAIS Way

<span style="color:#FFFFFF">OAIS, OH 11111

![](img/week_02_slide_deck7.png)

---

Information packages “are necessary for the management of the data, according to the place in the digital life cycle” (Source https://www.iasa-web.org/tc04/open-archival-information-system-oais). Information packages can change in size, shape and form as they move into and out of an OAIS.

You can think of an information package as similar to sending a gift to someone in the mail. Before you send a gift in the mail, you have to wrap it, print out a label, put it into a container. When you go to the post office, it is given various markings and identifiers, like a QR code for tracking, or a post date, to prepare it for its journey to the recipient. The recipient will then unbox and unwrap the package and use it for some intended purpose. I’ll be revisiting this analogy throughout the following slides to help ground us in these concepts.

# Definition: Content Information
—

__Content information is composed of the__  __data object__ __ (bitstream) and__  __representation information__ __ (to make sense of the bitstream).__

<span style="color:#595959"> __Data object__ 

<span style="color:#595959">01001000

<span style="color:#595959"> __Representation Information__ 

<span style="color:#595959">01001000

<span style="color:#595959">= 72 

<span style="color:#595959">= H

<span style="color:#FFFFFF">Content Information

---

The first type is something we already learned about: Content Information.
Content Information is the primary thing being preserved. This includes the data object and its representation information (what we just learned about). 

In our post office analogy, this would be the gift inside of the box being sent: the actual thing being sent.



__Preservation Description__

# Definition: 
Preservation Description Information
—

__Identifiers that__  __allow__ __ outside systems to describe the past and present states of the content information, ensuring it is uniquely identifiable, and ensuring it has not been unknowingly altered.__

---

Preservation description information is information that describes a preserved item’s provenance, references, and fixity.

Post office analogy: post marks that verify that the post office has done something with the package.

Before moving on I want to spend a bit more time unpacking what Preservation Description Information, or PDI is and what it consists of.

__Preservation Description__

<span style="color:#FFFFDB">Provenance

<span style="color:#FFFFDB">(events)

<span style="color:#FFFFDB">Reference

<span style="color:#FFFFDB">(identifiers)

<span style="color:#FFFFDB">Fixity

<span style="color:#FFFFDB">(checksum)

---

Provenance: describes the source of the preserved item as well as events that may have happened to it along the way.
Reference: refers to unique identifiers, like an ID assigned by an external database system.
Fixity: Refers to information that can be used to check the integrity of a preserved object’s bitstream over time. Fixity is an important digital preservation concept to know, so let’s dig a little deeper there.

# Definition: Fixity
—

__Fixity describes the action of checking a file bitstream’s integrity at regular intervals over the time it lives within a digital repository.__

---

Fixity is the process of verifying that a digital object’s bitstream has not been altered. Bitstreams are prone to error degradation or corruption. When bitstreams degrade, this is referred to sometimes as bitrot. Bitrot can happen for a variety of reasons. Remember, all bitstreams are ultimately written onto some sort of physical medium. For example, a hard drive writes bitstreams onto spinning metallic plates using magnetism. If anything were to happen to the plate, or the head that reads and writes data, such as physical damage like dropping the hard drive onto the floor, shifts in humidity or moisture, power surges, accidental exposure to high-powered magnetis or high temperatures, any of these events could result in bitstream corruption. It is important that digital preservation systems are set up to check fixity to ensure bitstream integrity over time.

This can be done by running a checksum algorithm against a bitstream. This process generates a unique string of characters that should match if and when additional checksums are run in the future. If a checksum is run at one point does not match a checksum run against the same preservation object at another point, that indicates that the bitstream has been altered.

# Definition: Checksum
—

__A checksum is a unique string of alphanumeric characters generated by processing the bitstream of a digital object through an algorithm. So long as the bits (1s and 0s) of the bitstream remain the same, the checksum, too, will also remain unchanged.__

---

This can be done by running a checksum algorithm calculation over the bitstream, and generating what is known as a checksum. This process generates a unique string of characters that should match if this same algorithm is run over the same bitstream at another time.

If a checksum is run at one point does not match a checksum run against the same preservation object at another point, that indicates that the bitstream has been altered.

<span style="color:#CE8FFB"> __Mini Activity__ 

<span style="color:#CE8FFB">Go to   <span style="color:#CE8FFB"> _[https://emn178.github.io/online-tools/md5\_checksum.html](https://emn178.github.io/online-tools/md5_checksum.html)_ 

<span style="color:#CE8FFB">Create a text file on your desktop and type some text into it.

<span style="color:#CE8FFB">In the MD5 Checksum Tool, drag and drop the text file into the Drop File Here box. Make sure “Auto Update” is selected.

<span style="color:#CE8FFB">Make a change to your text file and drag and drop again; click on the various hashes to see what happens.

<span style="color:#FFFFDB">Packaging Information

# Definition: Packaging Information
—

__Binds the content and preservation description information__

---

Packaging Information: Binds together all the components of the information package together. Post office analogy: The box, which contains the gift, but also provides a surface on the outside to tie together all the information needed for postal workers to send the gift.

<span style="color:#5B0F00">Descriptive Information

# Definition: Descriptive Information
—

__Subset of data for discovery and access__

---

Descriptive Information: Metadata that allows the object to be located at a later time using search or retrieval functions. Post office analogy: A tracking ID which a user can input into the USPS website to see where the package is geographically.

![](img/week_02_slide_deck8.png)

---

90 sec

So let’s bring it all together. We now know about the four different types of information inside of an OAIS information package: to summarize, that’s Content Information, Preservation Description Information (PDI), Descriptive Information and Packaging Information. This diagram summarizes how each of these information content types are structured in relation to one another.

Here, we see the Content Information – the bitstream, and representation information – and PDI – information about fixity, which we just covered, provenance, and any unique identifiers – bound together into a Packaging Information “basket”. This is analogous to the post office box that holds our gift and information about that gift together into one unit that moves through the post system. Packaging information “wraps around” content and preservation information, creating a sort of preservation intellectual unit.

Descriptive information rests outside of and points to the package: descriptive information is a subset of data used by end-users to discover and access an information packages. This is likely the information that you would see represented in an online catalog or finding aid.

__Information Package Types: SIPs, AIPs and DIPs__

# Definition: Submission Information Package (SIP)
—

__An information package that is formed outside of the context of an OAIS, and delivered by a producer to the OAIS for ingest.__

__Related definition:__

__Producer: The person who prepares and submits the SIP.__

---

A Submission Information Package, or SIP, is the initial information package submitted by a producer to an OAIS.

A producer is a person or system that interacts with the OAIS by submitting the thing to be preserved. An example of a producer might be an archivist whose job is to prepare preservation materials for upload into an OAIS.

SIPs are implicated in two processes commonly called “ingest” and “pre-ingest”.

Source for producer definition: Lee, Christopher A., and Tibbo, Helen. “Where’s the Archivist in Digital Curation? Exploring the Possibilities through a Matrix of Knowledge and Skills.” Archivaria: 72 (Fall 2011) pp. 123-168. http://www.ils.unc.edu/callee/p123-lee.pdf

# Definition: Ingest (1/2)
—

__Ingest describes the steps the OAIS takes to prepare and process SIPs submitted by Producers into archival storage.__

__Prior to ingest, the OAIS will perform some sort of check over the SIP to make sure it contains all the OAIS needs and requires of it.__

---

Sources:
https://www.dpworkshop.org/dpm-eng/terminology/oais.html
https://www.st.nmfs.noaa.gov/Assets/data/edm/documents/OAIS_NODC_Overview_27Aug2013.pdf

Ingest describes the steps an OAIS takes to transform a SIP into an AIP. These actions may include pre-ingest action such as subjecting the SIP to some sort of quality assurance check to make sure what has been submitted by the producer aligns with the OAIS’ submission standards. For example, it will likely always check that there is Content Information, minimal descriptive metadata, or unique identifier. These requirements will vary from one OAIS to another.

If the SIP:
Does not pass QA at this stage, the system will stop the package from going into the OAIS, and perhaps give a reason why (i.e. “Error: ID missing”), prompting the Producer to take the necessary steps to amend the issue and re-submit.
Passes QA, it will move on into the jurisdiction of the OAIS, and the ingest process will officially begin.

![](img/week_02_slide_deck9.png)

<span style="color:#595959"> __Figure 4-2:__   <span style="color:#595959"> __Functions of the Ingest Functional Entity__ 

<span style="color:#595959"> __—__ 

<span style="color:#595959"> __Page 48__ 

<span style="color:#595959"> __Magenta Book__ 

---


Source: https://www.dpconline.org/docs/technology-watch-reports/1359-dpctw14-02/file (text)https://wiki.dpconline.org/index.php?title=4.1.1.2_Ingest (diagram)

Ingest is the set of processes responsible for accepting information submitted by Producers and preparing it for inclusion in the archival store. Specific functions performed by Ingest includes receipt of information transferred to the OAIS by a Producer; validation that the information received is uncorrupted and complete; transformation of the submitted information into a form suitable for storage and management within the archival system; extraction and/or creation of descriptive metadata to support the OAIS’s search and retrieval tools and finding aids; and transfer of the submitted information and its associated metadata to the archival store.

In short, the Ingest function serves as the OAIS’s external interface with Producers, managing the entire process of accepting custody of submitted information and preparing it for archival retention. 


# Definition: Archival Information Package (AIP)
—

__AIP: An information package consisting of the digital object and associated Preservation Description Information (PDI), which is managed and preserved within an OAIS.__

__Management: responsible for policy objectives of the OAIS.__

---

Source: https://www2.archivists.org/groups/standards-committee/open-archival-information-system-oais#:~:text=An%20Archival%20Information%20Package%20(AIP,repository%20to%20perform%20preservation%20services)

So now, we are at the point where the OAIS has created an Archival Information Package or AIP through the submission and ingest processes. An AIP is the set of content and metadata managed by the OAIS, and organized in a way that allows the OAIS to perform preservation activities, like fixity.

Note that a SIP and an AIP do not always have a one-to-one relationship, meaning, you can submit a SIP to an OAIS, which may result in one or multiple AIPs created. For example, let’s say someone submitted a SIP containing video files of performances that occurred through the course of a season or a year, the OAIS may then turn each one of those performances into their own AIP. This behaviour will vary depending on the rules set up by the organization who manages the OAIS.

Management is the entity that sets the policy objectives of the OAIS. This may include determining the rules of how the OAIS operates, such as, this OAIS takes this sort of information but not this other sort of information, this OAIS turns SIPs into multiple AIPs or not, and identifying funding sources to maintain the OAIS as a whole. Note, management does not refer to the traditional organizational sense of management (https://www.oclc.org/research/publications/2000/lavoie-oais.html).

![](img/week_02_slide_deck10.png)

<span style="color:#595959"> __Figure 4-18: Archival Information Package__ 

<span style="color:#595959"> __—__ 

<span style="color:#595959"> __Page 83__ 

<span style="color:#595959"> __Magenta Book__ 

---

1 min 30 sec

Source: https://public.ccsds.org/pubs/650x0m2.pdf

An AIP consists of several components, most which we have covered up through now. This diagram shows how all of these various components fit together.

Notice how there are two main branches that stem off the AIP (top middle).

On the left hand side, we have the Content Information branch, which consists of the Data Object (the bitstream) and Representation Information (things required to interpret the bitstream). This is the thing being preserved.

On the right hand side, we have the Preservation Description Information or PDI branch, which consists of fixity details, unique identifiers, provenance and rights information: any details that describe preservation information and actions taken which further describe the Content Information.

Also notice on either side of the AIP, we have Package Description on the left hand side of the AIP, and Packaging Information on the right. Packaging information can be thought of as a sort of wrapper around the entire AIP, with information about how each of all of the components listed below are packaged together.

On the left-hand side of the AIP in the diagram we have Package Description, which is further described by another diagram.

<span style="color:#595959"> __Figure 4-17: Package Description__ 

<span style="color:#595959"> __—__ 

<span style="color:#595959"> __Page 82__ 

<span style="color:#595959"> __Magenta Book__ 

![](img/week_02_slide_deck11.png)

---

The Package Description “enables the Consumer to locate information of potential interest, analyze that information, and order desired information. The information needed for one Access Aid is called an Associated Description. A single Package Description may contain several Associated Descriptions depending on the number of different Access Aids that can locate, visualize, retrieve or order the associated Content Information and PDI.” Basically, this is the information that is relayed to discovery platforms such as an online finding aid, for example.

This is a good segue into the final of the third information package managed by the OAIS, the DIP.

# Definition: Dissemination Information Package (DIP)
—

__DIP: Derived from one or more AIPs, and are received by the Consumer in response to a request to the OAIS__

__Consumer: The role played by those persons or client systems that interact with OAIS services to find preserved information of interest and to access that information in detail.__

---

Source for DIP definition: Lee, Christopher A., and Tibbo, Helen. “Where’s the Archivist in Digital Curation? Exploring the Possibilities through a Matrix of Knowledge and Skills.” Archivaria: 72 (Fall 2011) pp. 123-168. http://www.ils.unc.edu/callee/p123-lee.pdf

A Dissemination Information Package or DIP is the information package that is delivered from within an OAIS to the consumer making the request.

A Consumer is an entity, taking on the form of a person or client system (or both) that interacts with OAIS service to find preserved information of interest and to access that information in detail.

An example of a Consumer is a researcher using an online finding aid that has been set up to point to one or multiple AIP package descriptions. When they click on a finding aid component to request to read, watch, listen to, or otherwise experience or interact with a preservation object, the finding aid will be set up to query the OAIS. The OAIS, in turn, will retrieve and deliver a DIP. The DIP will contain a derivative of the AIP. By keeping the AIP and the DIP separate, we do not risk disturbing the Content Information in archival storage.

__OAIS Functional Entities__

__Functional Entities__

__Preservation Planning__

__Descriptive information__

__Descriptive information__

__Archival Storage__

---

Now that we know about information packages, let’s go through the six functional entities of an OAIS: Ingest, Archival Storage, Data Management, Administration, Preservation, and Access, labeled in brown boxes. Before we do so, let’s quickly define what functional entity means.

# Definition: Functional Entity
—

__Functional entities describe an entity responsible for a function that is required to ensure the reliable operation of the OAIS system.__

---

Functional entities describe an entity responsible for a function that is required to ensure the reliable operation of a system: in this case, an OAIS. So, all fix functional entities we are going to talk through describe the processes and services that an OAIS undertakes to support preservation operations.

We’ve already covered one functional entity, known as “Ingest”.

<span style="color:#1155CC"> __Administration__ 

<span style="color:#1155CC">Services/functions that control the day-to-day OAIS operations

<span style="color:#1155CC"> __Preservation Planning__   <span style="color:#1155CC">Provide recommendations to ensure long-term viability of OAIS

<span style="color:#1155CC"> __Access__ 

<span style="color:#1155CC">Support Consumer discovery and information requests and queries

<span style="color:#1155CC"> __Ingest__ 

<span style="color:#1155CC">Perform quality assurance over received SIPs; create AIPs

<span style="color:#1155CC"> __Archival Storage__ 

<span style="color:#1155CC">Move AIPs to permanent storage, perform error checking

<span style="color:#1155CC"> __Data Management__ 

<span style="color:#1155CC">Populate and relay data in systems used to manage and access the archive

---

Sources:
https://www.dpworkshop.org/dpm-eng/terminology/oais.html
https://www.st.nmfs.noaa.gov/Assets/data/edm/documents/OAIS_NODC_Overview_27Aug2013.pdf

The 6 functional entities are described as follows:
Ingest: Processes that perform quality assurance over received SIPs and creates AIPs.
Archival storage: Move AIPs from temporary to permanent storage and performs error checking.
Data management: Populate and relay data in systems used to manage and access the archive.
Administration: Services and functions that control the day-to-day OAIS operations.
Preservation planning: Provide recommendations to ensure long-term viability of the OAIS.
Access: Support Consumer discovery and information requests/queries.

Let’s define these functions further. You will notice that a lot of these functions interact with or relay information to one another.

# Definition: Archival Storage
—

__Provide long-term storage__

__Maintain storage hierarchies__

__Maintain/replace storage media__

__Put forth policies to prevent and mitigate disasters__

__Provide data for access functions__

_See Figure 4-3 in the Magenta Book_

---

The story of archival storage is complicated, and goes way beyond just providing a space for AIPs to live over the long-term.

The Ingest function relays AIPs to the archival storage environment. Once placed onto storage media, a number of other routine steps are taken, and generally, those are managed by the Administration entity, who puts forth storage management policies in place, and oversees the performance of the storage environment as a whole through consistent error checking. These policies also pertain to maintaining storage hierarchies, preventive measures to guard against disasters and procedures taken for disaster recovery (such as making copies of damaged or missing AIPs), and replacement of storage hardware intermittently. Storage devices, like bitstreams, can degrade over time.

Storage is used not only to store AIPs, but access copies or DIPs as well. Therefore, archival storage works in tandem with access functions as queries are received from Consumers.

__Provide long-term storage__

__Maintain storage hierarchies__

__Maintain/replace storage media__

__Put forth policies to prevent and mitigate disasters__

__Provide data for access functions__

_See Figure 4-3 in the Magenta Book_

---

The story of archival storage is complicated, and goes way beyond just providing a space for AIPs to live over the long-term.

The Ingest function relays AIPs to the archival storage environment. Once placed onto storage media, a number of other routine steps are taken, and generally, those are managed by the Administration entity, who puts forth storage management policies in place, and oversees the performance of the storage environment as a whole through consistent error checking. These policies also pertain to maintaining storage hierarchies, preventive measures to guard against disasters and procedures taken for disaster recovery (such as making copies of damaged or missing AIPs), and replacement of storage hardware intermittently. Storage devices, like bitstreams, can degrade over time.

Storage is used not only to store AIPs, but access copies or DIPs as well. Therefore, archival storage works in tandem with access functions as queries are received from Consumers.

# Definition: Data management
—

__Maintains databases of descriptive metadata used in finding aids__

__Manages administrative data supporting OAIS internal system operations__

_See Figure 4-4 in the Magenta Book_

---

Source: https://www.dpconline.org/docs/technology-watch-reports/1359-dpctw14-02/file (text) and https://wiki.dpconline.org/index.php?title=4.1.1.4_Data_Management (diagram)

The Data Management function maintains databases of descriptive metadata identifying and describing the archived information in support of the OAIS’s finding aids; it also manages the administrative data supporting the OAIS’s internal system operations, such as system performance data or access statistics. The primary functions of Data Management include maintaining the databases for which it is responsible; performing queries on these databases and generating reports in response to requests from other functional entities within the OAIS; and conducting updates to the databases as new information arrives, or existing information is modified or deleted. In managing these databases, the Data Management function supports search and retrieval of the OAIS’s archived content, and administration of the OAIS’s internal operations. 

# Definition: Administrative
—

__Day-to-day OAIS operations__

__Coordinate activities of the 5 other functional entities__

__Central hub between internal and external interactions__

_See Figure 4-5 in the Magenta Book_

---

Source: https://www.dpconline.org/docs/technology-watch-reports/1359-dpctw14-02/file (text)

The Administration function is responsible for managing the day-to-day operations of the OAIS, as well as coordinating the activities of the other five high-level OAIS functional entities. Other responsibilities include interacting with Producers (e.g., negotiating Submission Agreements), Consumers (e.g., providing customer service support), and Management (e.g., implementing and maintaining archive policies and standards). Administration serves as the central hub for the OAIS’s internal and external interactions: it communicates directly with the five other OAIS high-level services – Ingest, Archival Storage, Data Management, Preservation Planning, and Access, as well as the OAIS’s external stakeholders – Producers, Consumers, and Management.

# Definition: Preservation Planning
—

__Monitor designated communities, consumer and producer groups__

__Identify standards and procedures required for SIP/AIP/DIPs__

__Monitor technology__

__Develop preservation strategies, standards and policies__

_See Figure 4-6 in the Magenta Book_

---

Source:
https://www.dpconline.org/docs/technology-watch-reports/1359-dpctw14-02/file (text) 
https://wiki.dpconline.org/index.php?title=4.1.1.6_Preservation_Planning (diagram)

Preservation Planning is responsible for mapping out the OAIS’s preservation strategy, as well as recommending appropriate revisions to this strategy in response to evolving conditions in the OAIS environment. The Preservation Planning service monitors the external environment for changes and risks that could impact the OAIS’s ability to preserve and maintain access to the information in its custody, such as innovations in storage and access technologies, or shifts in the scope or expectations of the Designated Community. Preservation Planning then develops recommendations for updating the OAIS’s policies and procedures to accommodate these changes. The Preservation Planning function represents the OAIS’s safeguard against a constantly evolving user and technology environment. It detects changes or risks impacting the OAIS’s ability to meet its responsibilities, designs strategies for addressing them, and assists in the implementation of these strategies within the archival system.

# Definition: Access
—

__Coordinate access to data management and archival storage to prepare DIP__

__Ad hoc or event-based triggers__

__Queries to system to generate orders for DIPs__

__Generation of DIPs__

__Can involve subsampling, conversion, image processing, adding information, transforming information__

_See Figure 4-7 in the Magenta Book_

---

Source:
https://www.dpconline.org/docs/technology-watch-reports/1359-dpctw14-02/file (text)
https://wiki.dpconline.org/index.php?title=4.1.1.7_Access (diagram)

As its name suggests, the Access function manages the processes and services by which Consumers – and especially the Designated Community – locate, request, and receive delivery of items residing in the OAIS’s archival store. Typical services provided by Access in support of the Consumer include processing queries of the OAIS’s holdings – specifically, forwarding the request to Data Management and presenting the response (e.g., a result set) to the Consumer; and coordinating the retrieval and delivery of requested content – by forwarding the request to Archival Storage, receiving the requested items, and performing any necessary transformations (such as altering the archived item’s format to one more suitable for dissemination, or stripping away unneeded metadata) that must occur prior to delivery to the Consumer. Access is also responsible for implementing any security or access control mechanisms associated with the archived content. The Access function represents the OAIS’s interface with its Consumers (and Designated Community): as such, it is the primary mechanism by which the OAIS meets its responsibility to make its archived information available to the user community.

__Audit and Certification of Trustworthy Digital Repositories (TRAC)__

# Definition: Audit and Certification of Trustworthy Digital Repositories: Criteria and Checklist - ISO 16363
—

__The Audit and Certification of Trustworthy Repositories: Criteria and Checklist, sometimes referred to as “TRAC” is a document describing the metrics of an OAIS-compliant digital repository__

---

Source: https://en.wikipedia.org/wiki/Trustworthy_Repositories_Audit_%26_Certification

Trustworthy Repositories Audit & Certification (TRAC) is a document describing the metrics of an OAIS-compliant digital repository that developed from work done by the OCLC and National Archives and Records Administration (NARA) task force initiative.
TRAC is basically a framework for auditing a repository. The document itself is basically a checklist that can be used to assess the reliability, commitment and readiness of institutions to assume long-term preservation responsibilities. Though heavily influenced by the OAIS Model, which focuses heavily on the functions and processes required to build and manage a digital repository, TRAC provides more of an “administrative context for building and managing a digital repository” … “[which] creates a more comprehensive model for digital preservation planning and development that sets each digital archive within its full organizational context, and also allows the organization to consider organizational, legal, economic, technical, and implementation issues individually or in relevant combinations.” (https://quod.lib.umich.edu/s/spobooks/bbv9812.0001.001/1:11?rgn=div1;view=fulltext)

# Text: Requirements for Bodies Providing Audit Certification of Candidate Trustworthy Digital Repositories
—

__The Requirements for Bodies Providing Audit Certification of Candidate Trustworthy Digital Repositories document defines “the operations of the organization(s) which assess the trustworthiness of digital repositories using ISO 16363… and provide the appropriate certification.”__

---

Source: https://public.ccsds.org/Pubs/652x1m2.pdf

Another standard, ISO 16919, aka Requirements for Bodies Providing Audit Certification of Candidate Trustworthy Digital Repositories, works in tandem with ISO 16363. This document “provides requirements for the organizations that will carry out audits and certifications of digital repositories”. Meaning, if you are a repository, and you want to get audited, the idea is that the auditor themselves must meet certain requirements.

The standard document itself gives some reasoning behind why this standard was put forth. “Long before [the OAIS Reference Model] became an approved standard in 2002 … [i]nstitutions began to declare themselves ‘OAIS-compliant’ to underscore the trustworthiness of their digital repositories. However, there was no established understanding of ‘OAIS-compliance’ beyond being able to apply OAIS terminology to describe their archive, despite there being a compliance section in OAIS which specifies the need to support the model of information and fulfilling the mandatory responsibilities. Claims of trustworthiness are easy to make but are thus far difficult to justify or objectively prove. Establishing more clear criteria detailing what a trustworthy repository is and is not has become vital.” Source: NARAtions blog (https://narations.blogs.archives.gov/2011/03/15/iso-standards-for-certifying-trustworthy-digital-repositories/)

# TRAC: Pros and Cons

<span style="color:#FFFFFF">3.3.2 “The repository shall have an ingest process which verifies each SIP for completeness and correctness.”

__CON: Cost-prohibitive__

__PRO:__

__Less abstract than OAIS Reference Model.__

![](img/week_02_slide_deck12.png)

__CON: “Trustworthiness” meaningless when very few repositories to date are not TRAC certified.__

__PRO:__

__Written by and for archivists.__

---

Here I have listed some pros and cons of the TRAC standards we just covered.
PRO: The TRAC checklist is written in a more practical way OAIS. It contains clear statements, each starting with “The repository shall…” followed by a short description of an attribute of an OAIS-compliant repository. The example on the slide basically says, the repository ought to have a written policy outlining when it accepts a SIP.
PRO: The TRAC standards was written by and for people working in the archival and digital preservation field.
CON: Certification by ISO 16919 trained auditors is cost-prohibitive in both the short- and long-term: One estimate I have heard thrown around is the cost of getting TRAC certified may be in the $20,000-$30,000 range. This does not include the cost of internal staff time pulling documentation, and speaking/being interviewed by auditors.
CON: Another CON is the fact that very few institutions have actually been audited and certified as “trustworthy” digital repositories, and this likely had to do with the fact that they had the means to not only establish a compliant system, but hire certified auditors to take them through the process of auditing. But what does this mean for the vast majority of repositories that are not certified? Does this mean that they are less trustworthy? Should donors or creators hesitate to give their works to a non TRAC-certified institution?

Thankfully, the discourse surrounding OAIS and TRAC has evolved since their publication in the aughts. In Steve Marks’ Module 8, he suggests that institutions use the TRAC checklist to audit themselves without going through the rigamarole of certification. There are many other accounts of archivists, and other systems maintainers who have used OAIS as a sort of frame of reference for their work. Steve Marks was digital preservation librarian at the Toronto-based Scholars Portal.

Any questions?

![](img/week_02_slide_deck13.gif)

<span style="color:#C27BA0"> __Scenario__ 

<span style="color:#741B47">Pretend you work at a small museum archive that is considering acquiring a collection of indie video games created by members of the   _[Babycastles collective](https://www.babycastles.com/about)_  <span style="color:#741B47">. Some video games depend on obsolete operating systems and machines to play.

<span style="color:#C27BA0"> __Question 1__ 

<span style="color:#741B47">What sorts of questions might you ask the donor/creator of the game? As a digital curator, what details should you take into consideration? How might this impact gift agreements and donor relations?

<span style="color:#C27BA0"> __Question 2__ 

<span style="color:#741B47">What might an AIP look like for this particular video game? Hint: Look at the McDonough article, page 1628 onward.

<span style="color:#C27BA0"> __Question 3__ 

<span style="color:#741B47">What might be some impediments to DIP creation and access for this collection? What are some of the things to consider when thinking about DIP and access?

<span style="color:#FE7600">Post your pre-class reading reactions to Brightspace.

<span style="color:#FE7600">Weekly activity: None this week

<span style="color:#FE7600">Let me know if you have any questions about the File Format Report and the file format you chose

