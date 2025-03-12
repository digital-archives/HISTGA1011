---
marp: true
theme: gaia
size: 16:9
paginate: true
style: |
  img {
  max-width: 100%;
  max-height: 100%;
  height: auto;
  width: auto;
  display: block;
  margin: 0 auto;
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

  .description {
    padding: 20px;
    text-align: left;
    font-size: 18px;
    margin-top: 10px;
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
    width: 90%;
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
    color: #2e7d32; /* Green color for the header */
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 30px;
  }
  
  .takeaway {
    display: flex;
    align-items: flex-start;
    margin-bottom: 20px;
    gap: 15px;
  }

  .numcircle {
    background-color: #2e7d32;
    color: white;
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
    color: #2e7d32; /* Green color for subheadings */
    font-size: 1.2rem;
  }
  .content p {
    margin: 5px 0 0;
    font-size: 1rem;
    color: #4a4a4a; /* Gray for body text */
  }

  .activity-title {
    text-align: center;
    color:rgb(144, 0, 255); /* Soft purple */
    font-size: 2rem;
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
    border-bottom: 30px solid #ffb347; /* Orange */
    display: inline-block;
    margin: 0 10px;
  }
  .circle {
    background-color: #00c0ff; /* Blue */
  }
  .square {
    width: 30px;
    height: 30px;
    background-color: #ff6767; /* Red */
  }
  .activity-list {
    font-size: 1.1rem;
    line-height: 1.1;
    color:rgb(81, 0, 168); /* Light lavender */
    margin-left: 20px;
  }
  .activity-list li {
    margin-bottom: 10px;
  }
  .activity-list li strong {
    color:rgb(235, 133, 133); /* Highlighted lavender */
  }

---

## Week 8
# Access and Discovery

---

# Today
- **Settle in/Reminders/Announcements** (15 min)
- **Discuss Last Week's Activity** (20 min)
- **Lecture: Access and Discovery** (45 min)
- **Break** (10 min)
- **Start Weekly Activity** (70 min)
- **Wrap up** (10 min)

---

# Announcements

_Feel free to email me with any announcements you would like me to boost (upcoming conferences, webinars, trainings, or other events/topics of interest)._

---

# Access and Discovery

<!--presenter notes

Today, we'll look at what happens after last week's Imaging and Conservation Activity. At this point, an imaging technician, archivist, or vendor has created a set of digital images. These files might be sitting on a hard drive, a production server, or somewhere else at the institution. They've been named, likely organized into folders, but they’re not accessible to users yet.

So, what happens next? How do we move from having digital files to preparing these for discovery and access?

-->

---

<img src="img/week_07_university_houston_workflow.png">

<!--presenter notes

We will be looking at a particular example, the Bayou City Digital Asset Management System (BCDAMS), used by the University of Houston (UH) Libraries. In late 2015, UH made an institutional commitment to migrate the data for its digitized cultural heritage collections to a group of interoperable open source systems.

Here, we have a workflow diagram created by the University of Houston, representing their digital preservation workflow that we are going to break down into something more digestible and understandable.

A code4lib article provides additional details: https://journal.code4lib.org/articles/12342#unit5

-->

---

# Bayou City Digital Asset Management System (BCDAMS)
<br>

<div class="row">
  <div class="pink-box">ArchivesSpace</div>
  <div class="pink-box">Archivematica</div>
  <div class="pink-box">Hydra-in-a-Box (HyKu)</div>
</div>

<div class="row">
  <div>
    <div class="green-box">Carpenters</div>
    <div class="description">Interface used by digitization staff to manage digitization workflow and preservation ingest.</div>
  </div>
  <div>
    <div class="green-box">Brays</div>
    <div class="description">Interface used by staff working with digital objects to view files and create metadata in preparation for HyKu ingest.</div>
  </div>
  <div>
    <div class="green-box">CEDAR</div>
    <div class="description">Linked data vocabulary manager</div>
  </div>
  <div>
    <div class="green-box">Greens</div>
    <div class="description">Mints persistent identifiers applied to preservation packages like SIPs</div>
  </div>
  <div>
    <div class="green-box">Halls</div>
    <div class="description">Public user interface</div>
  </div>
</div>

<!--presenter notes

The University of Houston uses a preservation systems “ecosystem” of both open-source and homegrown applications and tools, each working in concert with one another to fully or partially automate the entire digital preservation-to-access workflow.

UH uses three open-source tools:
- ArchivesSpace: Used by archivists to describe collections and produce finding aids.
- Archivematica: Used to automate workflows into and from the digital repository.
- Hydra-in-a-Box (aka Hyku): open-source digital repository software platform that allows institutions to manage, preserve, and provide access to digital collections.

UH also uses a number of homegrown tools:
- Carpenters: an internal staff interface used by digitization staff to manage digitization workflow and preservation ingest.
- Brays: a metadata management system used by staff working with digital objects to view files and create metadata in preparation for ingest into HyKu
- CEDAR: A linked data vocabulary manager
- Greens: A persistent identifier minter
- HALLS: HALLS (stands for Houston Area Library Automated Network Delivery System) is a front-end interface for searching and discovering content from various digital repositories and collections maintained by the libraries in the Houston area

-->

---

### **Phase 1: Selection and Capture**

1. **Archivist** creates finding aid in **ArchivesSpace**.
2. **Archivist** opens **Carpenters**, navigates to the “Selection” tab, and imports the finding aid.
3. **Archivist** checks boxes next to the folders/items to be digitized.
4. **Carpenters** populates the shot list in the “Files” tab.
5. **Digitization Unit Tech** opens **Carpenters** and navigates to the “Files” tab, and photographs images in the sequence specified by the shot list.

---

<img src="img/week_07_carpenters_shot_list.png" alt="Image of a planetary scanner" style="width: 100%; height: auto;">

<!--presenter notes

This is a screenshot of the Carpenters interface, with the “Selection” tab open, which is where the archivist works to import the finding aid components and hierarchy.

As you can see, Carpenters allows preservation administrators to organize digitized content into hierarchies that preserve the contextual linkages and provenance of the original archival collection.

-->

---

### **Phase 2: File Management and Association**
1. **Digitization Unit Tech** creates a **preservation file** along with **derivative files** such as **mezzanine and access copies** for each archival object, storing them on the local file system.
2. **Digitization Unit Tech** opens **Carpenters**, navigates to the “Files” tab, and associates each file created with its corresponding archival object **ArchivesSpace URI**.

---

## Definition
# Preservation File

A **preservation file** is a high-quality, minimally processed digital file created to serve as the authoritative source for long-term preservation. It is typically produced during digitization and retains the maximum amount of detail, accuracy, and integrity from the original material.

---

## Definition
# Mezzanine File

A **mezzanine file** is an intermediate-quality digital file derived from a preservation file. It is used for specific workflows, such as editing, while still maintaining a high level of fidelity. Mezzanine files strike a balance between the size and usability of the file and the quality of the original preservation file.

---

## Definition
# Access File

An **access file** (sometimes also "service file") is a derivative digital file used for providing convenient, user-friendly access to the content. Access copies are optimized for distribution, sharing, and everyday use, often with reduced file size and quality compared to the original preservation file.

---

## Definition
# Uniform Resource Identifier (URI)

A **Uniform Resource Identifier (URI)** (in the context of ASpace) is a sequence of characters that represents a specific resource record, an archival object, digital object, or other record.

Example:
<a href="https://archives.yale.edu/repositories/11/resources/13623"
 target="_blank">https://archives.yale.edu/repositories/11/resources/13623</a>
 <b>repositories/11/resources/13623</b> is the URI

---

<img src="img/week_07_carpenters_files_tab.png" alt="Image of a planetary scanner" style="width: 100%; height: auto;">

<!--presenter notes

In this screenshot, we are looking at the Carpenters interface “Files” tab, which is where Digitization Unit staff work. Each row has a box and folder listed, followed by the name of the collection and series title. Here, they can click on the plus sign next to the derivative file type, such as Preservation Master, and add the filename. In this way, they are connecting image captures to archival objects in the finding aid.

-->

---

### **Phase 3: Create SIP**

1. **Carpenters** automatically moves **preservation files** from the local file system to a set of nested directories,organized into an Archivematica-compatible **Submission Information Package (SIP)**.
3. The SIP structure replicates the **intellectual arrangement** of the original collection.

---

<img src="img/week_07_carpenters_folders.png" alt="A screenshot of a SIP containing nested folders, which mimic the hierarchy of a finding aid." style="width: 100%; height: auto;">

---

### **Phase 4: Mint Persistent Identifier; Export DIPs**

1. **Greens** mints an **Archival Resource Key (ARK)** persistent identifier for each SIP.
2. **Carpenters** outputs a **Dissemination Information Package (DIP)** containing access files and a metadata CSV file.

---

### Definition  
## Persistent Identifier (PID) - 1/2

**Persistent identifiers (PIDs)** are a type of Uniform Resource Identifier (URI) designed to provide a stable, long-term reference to a resource, ensuring it remains identifiable even if its location or system infrastructure changes.

PIDs use **resolution systems** that translate the PID to actionable locations or data.

---

## **Archival Resource Key (ARK) Syntax**

`ark:/[Name Assigning Authority Number]/[Qualifier]` 

Example: <a href="https://id.lib.uh.edu/ark:/84475/do2730bw52x" target="_blank">https://id.lib.uh.edu/ark:/84475/do2730bw52x</a><br><br>

#### **Resolution**  
University of Houston's **local resolver** (`id.lib.uh.edu`) redirects to a digital collection resource URL.  
<a href="https://digitalcollections.lib.uh.edu/concern/texts/0v838095w" target="_blank">https://digitalcollections.lib.uh.edu/concern/texts/0v838095w</a>

---

## **Handle Syntax**  

`hdl.handle.net/[Namespace]/[PID-Suffix]`  

Example: <a href="https://hdl.handle.net/10079/fa/beinecke.bookstore" target="_blank">https://hdl.handle.net/10079/fa/beinecke.bookstore</a><br><br>

#### **Resolution**
Handles are resolved through `hdl.handle.net`, directing users to the Yale finding aid resource.  

<a href="https://archives.yale.edu/repositories/11/resources/13623" target="_blank">https://archives.yale.edu/repositories/11/resources/13623</a>  

<!--presenter notes

Yale uses Handle, another kind of persistent identifier. It's pretty similar to ARK, but notice that the URL uses handle.net to resolve, rather than a Yale-hosted domain.

-->

---


### **Phase 5: Metadata Management**

**Metadata Unit Staff**:
- Loads the **Carpenters-generated Dissemination Information Package (DIP)** into the **Brays** descriptive metadata editor.
- Create descriptive metadata for all objects. During editing, **Brays**:
  - Suggests controlled vocabulary terms from **Cedar**.
  - Updates the **metadata CSV file** in the DIP.
  - Color-codes fields as **required**, **recommended**, or **optional**.

---

<img src="img/week_07_brays_01.png" alt="SIP folders" style="width: 100%; height: auto;">

<!--presenter notes

This is the Brays metadata creation staff interface. On the left-hand side, you see a list of all the digital preservation objects, in order. You can click into any one of them, and open up a descriptive metadata record. This record is connected to the CEDAR linked data vocab, which provides controlled lists, metadata validation and type-ahead suggestions.

The access portion of the workflow begins when Metadata Unit personnel loads the Carpenters DIP in the Brays descriptive metadata editor and creates descriptive metadata for all objects. 

Brays suggests controlled vocabulary terms from the Cedar linked data vocabulary manager and validates the record against their descriptive metadata specification.
Brays dynamically reads and writes to a metadata CSV file included in the DIP.

Color coding in the metadata creation interface indicates to staff  which fields are required, recommended, and optional.

Additionally, once the record contains all required fields, the object name in the object viewer turns from red to green.

-->

---

<img src="img/week_07_brays_02.png" alt="SIP folders" style="width: 100%; height: auto;">

<!--presenter notes

You can also use BRAYS to view a copy of the preservation file in full screen mode, so you can toggle back and forth between the image and the description quickly and seamlessly.

-->

---

### **Phase 6: Access through HALLS End-User Interface**

**HALLS** displays search results that convey the **intellectual arrangement** of archival objects, including series, sub-series, and file-level titles and descriptions., and the physical instance information, such as box and folder details.

 **HALLS** presents digital objects in two ways:
   - Integrated within the structure of the finding aid.
   - As a standalone record for direct access.

---

# Try it out - UH Digital Collections

- Visit https://digitalcollections.lib.uh.edu/
- Search for "Galveston 1915 Hurricane Photographs"
- Click on any image that appears in results
- Scroll and find the ARK, rights statement, and descriptive metadata
- Click "View item in finding aid"
- Locate your photograph in the context of the finding aid hierarchy (note: you can widen the "Collection organization" section using your mouse pointer).

---

## Tool
# International Image Interoperability Framework (IIIF) - 1/2

**IIIF** is a set of open standards for delivering high-quality, attributed digital objects online at scale. It’s also an international community developing and implementing the IIIF APIs. IIIF is backed by a consortium of leading cultural institutions.

---

## Tool
# International Image Interoperability Framework (IIIF) - 2/2

IIIF is best known for its ability for institutions hosting digitized content to be interoperable with each other.

---

<img src="img/week_07_iiif_side_by_side.png">

<!--presenter notes

This image is a screencapture of two medieval manuscripts, each held by a different repository: one from the Bodleian Libraries, the other from St. Gallen. Along with side-by-side comparisons or two high-resolution images from their digital collections, IIIF viewers allow deep zoom to see exacting/tiniest details, which supports research, scholarship and interest.

Read more here: https://blog.digitizedmedievalmanuscripts.org/iiif-international-image-interoperability-framework/

-->

---

# Try it out - IIIF - 1/2

- Return to the results page for "Galveston 1915 Hurricane Photographs"; click on a different image.
- Notice the IIIF logo beneath the photo: that indicates that the viewer is IIIF-compliant. <img src="img/week_07_iiif.png" style="width: 10%; height: auto;">
- Click on the IIIF logo to generate a JSON manifest; click on the "Pretty-print" checkbox to make the data more readable.
- Copy the URL for the manifest.

---

# Try it out - IIIF - 2/2

- Visit [https://projectmirador.org/](https://projectmirador.org/); click `DEMO` at the top of the page.
- Click `Add Resource` button (blue circle with +) in the upper left-hand corner.
- Click `+ ADD RESOURCE` (lower right-hand corner)
- In the Resource location field, paste the IIIF manifest URL; Click `ADD
- Your selected image should now appear at the top: click on it to open within the viewer. Notice how the image, title, etc. were auto-imported.

---

## **Question**

Wiedeman discusses the challenge that current archival access and discovery platforms face in accommodating the hierarchical nature of archival description. He suggests that this difficulty may stem from users' preference for bibliographic-based systems which they find less confusing and more intuitive compared to the complex and specialized nature of archival description.

__Should the design of these systems prioritize “traditional” finding aid structures or should they lean towards the formats that are more widely understood and accepted by users?__

---

<div class="quote">
  “...The approaches used by archivists are useful primarily because of the scale of the materials they manage. Got a large but manageable amount of stuff? Use bibliographic description. Got a seemingly never-ending vast mountain of materials? Use archival description.”
</div>

<div class="author">
  Gregory Wiedeman
</div>

<div class="work">
  <em>Designing Digital Discovery and Access Systems for Archival Description</em>, 2023
</div>

---

<div class="slide-title">Online Finding Aid Usability: 8 Takeaways</div>

---

<div class="takeaway">
  <div class="numcircle">1</div>
  <div class="content">
    <h2>Dynamic navigation</h2>
    <p>Archival description requires sophisticated navigation options.</p>
  </div>
</div>

<div class="takeaway">
  <div class="numcircle">2</div>
  <div class="content">
    <h2>Easy to get lost</h2>
    <p>Users new to finding aids report feeling lost within hierarchy.</p>
  </div>
</div>

<div class="takeaway">
  <div class="numcircle">3</div>
  <div class="content">
    <h2>Online availability difficult to determine</h2>
    <p>Users incorrectly assume all components listed are digitized.</p>
  </div>
</div>

---

<div class="takeaway">
  <div class="numcircle">4</div>
  <div class="content">
    <h2>Training / guidance needed</h2>
    <p>Users would appreciate more training beyond a “Help” page.</p>
  </div>
</div>

<div class="takeaway">
  <div class="numcircle">5</div>
  <div class="content">
    <h2>Too much jargon</h2>
    <p>Certain words are too domain-specific.</p>
  </div>
</div>

<div class="takeaway">
  <div class="numcircle">6</div>
  <div class="content">
    <h2>Need quick results</h2>
    <p>Users prefer a UI similar to a modern search engine.</p>
  </div>
</div>

---

<div class="takeaway">
  <div class="numcircle">7</div>
  <div class="content">
    <h2>Less texts, more lists</h2>
    <p>Large blocks of text are distracting; prefer lists.</p>
  </div>
</div>

<div class="takeaway">
  <div class="numcircle">8</div>
  <div class="content">
    <h2>Finding aid savvy can be developed</h2>
    <p>Though not always immediately attainable, studies show users can quickly learn to navigate finding aids through 1+ sessions.</p>
  </div>
</div>

<!--presenter notes

These takeaways were derived from Joyce Celeste Chapman’s article “Observing Users: An Empirical Analysis of User Interaction with Online Finding Aids” in the Journal of Archival Organization (JAO), 8:4–30, 2010 (DOI: 10.1080/15332748.2010.484361)

-->

---

<div class="shapes">
  <div class="triangle"></div>
  <span class="circle"></span>
  <span class="square"></span>
</div>

<div class="activity-title">Mini Activity - Part 1</div>

<ul class="activity-list">
  <li>Go to <strong>archives.nypl.org</strong></li>
  <li>Search for the <strong>James Baldwin Papers finding aid</strong>.</li>
  <li>This collection has been partially digitized. Knowing that, find and open a digitized item. Make a note of its name to use in Part 2 of this activity.</li>
  </li>
  <li><strong>Report back:</strong> How was your experience navigating to the digitized portion of this collection?</li>
</ul>

---

<<div class="shapes">
  <div class="triangle"></div>
  <span class="circle"></span>
  <span class="square"></span>
</div>

<div class="activity-title">Mini Activity - Part 2</div>

<ul class="activity-list">
  <li>Go to <strong>digitalcollections.nypl.org</strong></li>
  <li>Try to find the digital item you noted earlier.</li>
  <li>Look at the record, not just in terms of the digitized item, but other metadata made available.</li>
</ul>

---

<div class="shapes">
  <div class="triangle"></div>
  <span class="circle"></span>
  <span class="square"></span>
</div>

<div class="activity-title">Mini Activity - Part 3</div>

<ul class="activity-list">
  <li><strong>Discuss:</strong> How was your experience navigating the Archives Portal and Digital Collections?</li>
  <li>How easy/hard were the sites to search, browse, filter?</li>
  <li>What metadata is displayed?</li>
  <li>How are media files (audio, video) files displayed?</li>
  <li>What do you not like/does not work as well?</li>
  <li>What sites do you think a scholar would find useful? Student? General public?</li>
</ul>

---

## Definition
# Accessibility

In the context of digital archives, **accessibility** commonly refers to the general discoverability and ease of use of online archival collection, enabling equal or equivalent access to archival facilities and services for people with disabilities, and minimizing or eliminating barriers. Accessibility should be integral to institutional cultures, workflows, and services.

<!--presenter notes 

Accessibility is essential to building access platforms

Most institutions’ accessibility expectations will be informed by federal law, state law, and/or institutional best practices. Section 508 Standards for Accessible Electronic and Information Technology, the World Wide Web Consortium’s Web Content Accessibility Guidelines (WCAG), and PDF-UA (ISO 14289-1) are the most common tools used to build digital accessibility policies.

-->

---

<div class="slide-title">Accessibility Recommendations</div>

---

<div class="takeaway">
  <div class="numcircle">1</div>
  <div class="content">
    <h2>General Recommendations</h2>
    <ul>
<li>Font size can be changed without impacting navigability</li>
<li>Sufficient foreground and background contrast 
<li>Avoid color combos problematic for people who are color-blind</li>
<li>Ensure content is navigable when:</li>
<ul>
<li>Using a screen reader/magnification program
<li>Keyboard without a mouse</li>
<li>Do not rely solely on color, font to convey meaning</li>
<li>Use responsive design, adaptable for mobile/desktop views</li>
<li>Test accessibility of digital content frequently</li>
</li>
  </div>
</div>

---

<div class="takeaway">
  <div class="numcircle">2</div>
  <div class="content">
    <h2>Website Recommendations</h2>
    <ul>
      <li>Include an accessibility information and feedback section.</li>
      <li>Proper HTML markup with correct nesting of elements.</li>
      <li>ARIA landmark roles to indicate navigable regions of the page.</li>
      <li>Use meaningful page titles and document file names.</li>
      <li>Indicate the document language in markup.</li>
      <li>Ensure proper use of heading tags.</li>
      <li>Use descriptive text for hyperlinks (e.g., not "click here").</li>
      <li>Follow Plain Language Guidelines when generating content.</li>
      <li>Provide alternative text for visual content.</li>
    </ul>
  </div>
</div>

---

<div class="takeaway">
  <div class="numcircle">3</div>
  <div class="content">
    <h2>Repository Recommendations</h2>
    <ul>
      <li>Advocate for accessibility provisions in contracts for vendor solutions.</li>
      <li>Scan text documents as text (not as images) or convert scanned documents from image files to text, and use OCR to improve accessibility.</li>
      <li>Include transcripts for materials that cannot be OCRed, such as handwritten manuscripts, media (audio and video).</li>
      <li>Use audio description for video content</li>
      <li>Avoid content with flashing, flickering, or strobing or provide warnings</li>
    </ul>
  </div>
</div>

---

<div class="takeaway">
  <div class="numcircle">4</div>
  <div class="content">
    <h2>Social Media Recommendations</h2>
    <ul>
      <li>Use alt-text where possible.</li>
      <li>Avoid special characters (e.g., 𝕭𝖆𝖉 𝕱𝖔𝖓𝖙).</li>
      <li>Avoid using emojis in succession or in excess.</li>
      <li>Use alternating capitalization for hashtags (e.g., #HashTag).</li>
      <li>Research the culture of the platform before posting.</li>
      <li>Include contact and physical site details.</li>
      <li>Use automated messaging for DMs.</li>
    </ul>
  </div>
</div>

---

<div class="shapes">
  <div class="triangle"></div>
  <span class="circle"></span>
  <span class="square"></span>
</div>

<div class="activity-title">Activity - Accessibility Review</div>

<ul class="activity-list">
  <li>Open the <a href="https://wave.webaim.org/" target="_blank">Web Accessibility Evaluation Tool (WAVE)</a>.</li>
  <li>Input the URL for these two sites:
    <ul>
      <li><a href="https://library.uta.edu/txdisabilityhistory/" target="_blank">https://library.uta.edu/txdisabilityhistory/</a></li>
      <li><a href="https://archives.albany.edu/espy/" target="_blank">https://archives.albany.edu/espy/</a></li>
    </ul>
      </li>
  <li>Use the TopTal Color Blind Filter (to start) to analyze the contrast and visibility of a site.</li>
  <li><strong>Report back</strong>: Identify the most common issues you observed.</li>
    </ul>
</ul>

---

## Weekly Activity
# The User's Experience

Start: <a href="https://digital-archives.github.io/HISTGA1011/activities/user_experience.html" target="_blank">https://digital-archives.github.io/HISTGA1011/activities/user_experience.html</a>

---

![](img/week_00_weekly_activity_sunset.gif)

_Final questions or reflections?_

mary.kidd@nyu.edu