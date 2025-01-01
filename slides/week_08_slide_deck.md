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

  .circle {
    background-color: #2e7d32; /* Green background */
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

# Recap: Digitization

_Metadata-driven digital preservation workflow_

1. Catalog record or finding aid serves as basis for digitization work.

2. Digitization staff create preservation files and derivatives.

3. Files are packaged and ingested into archival storage.

4. Finding aid, catalog or other access endpoints, like a digital library, are updated.

<!--presenter notes

Digital preservation metadata workflows vary a lot from one institution to another. The bulleted list here represents a very generalized, high-level description of how metadata informs digitization workflows. Just know that the order which these events occur may differ.

Digitization work usually starts with gathering existing descriptive metadata. Although most descriptive metadata, like through a finding aid, will likely be at a collection or series level, it is still is useful because it contains data that can be used to give the project a name, populate digitization work orders or requests, and structure the work performed by digitization staff, such as putting forth the proper order in which to create captures.

With existing metadata in hand, digitization staff will create image captures, which will serve as the basis for derivatives such as a preservation master and access copies. These captures will result in the creation of additional technical metadata describing the systems and environments in which captures were created and manipulated.

Since these additional files are in relationship with one another, we need to capture this metadata through structural metadata. One basic way to do this is through filenaming or foldering files in a uniform and sequential manner. You might also use some sort of system, like a digital asset or metadata management system, to import or point to these files, enter information about their relationships, and maybe even use them to create preservation metadata files, like a METS file.

Lastly, you will need to update your digital library in some way that brings the project full circle, syncing the digitized files back to the finding aid component, a catalog record, or an exhibition site. This can be accomplished through descriptive metadata systems like ASpace, an institutional repository or other access system.

-->

---

## Definition
# Discovery and delivery

“[Discovery and delivery] [d]escribes what people,processes, and systems do to support finding accessing and using material from archives and special collections.”

Maria Matienzo and Dinah Handel, _Lighting the Way_ White Paper 2021

---

## Question

Wiedeman discusses the challenge that current archival access and discovery platforms face in accommodating the hierarchical nature of archival description. He suggests that this difficulty may stem from users' preference for bibliographic-based systems which they find less confusing and more intuitive compared to the complex and specialized nature of archival description.

__Should the design of these systems prioritize “traditional” finding aid structures or should they lean towards the formats that are more widely understood and accepted by users?__

---

![Entry for Safiya Noble's Alogithms of Oppression book in a typical library catalog](img/week_08_slides6.png)

<!--presenter notes

This is an example of bibliographic description. Most library items (books, CDs, DVDs, whatever) use a 1-to-1 relationship between thing (book) and description (record).

-->

---

![Entry for Records of the Forest Service archival collection in NARA's catalog](img/week_08_slides7.png)

<!--presenter notes

https://www.archives.gov/research/guide-fed-records/groups/095.html](https://www.archives.gov/research/guide-fed-records/groups/095.html

Archival collections, on the other hand, do not have the same 1-to-1 relationship between a single item, and its description. Instead, we have different levels of description: collection, series, box, folder. Rarely, do you ever go beyond folder (at least, in terms of a “traditional” finding aid. However, we are seeing more systems emerging that connect digital items to finding aids).

-->

---

![Screenshot of James Baldwin papers collection on NYPL's Archives & Manuscripts Portal](img/week_08_slides8.png)

<!--presenter notes

In this NYPL example, we are looking at the James Baldwin finding aid; specifically, the Correspondence series.

Let’s flip this example over and look at the underlying XML.

-->

---

![Underlying XML data for the James Baldwin papers finding aid](img/week_08_slides9.png)

<!--presenter notes

Here is the XML describing the Correspondence series of the James Baldwin collection. As you can see here (and as you saw within several examples presented during last week’s lecture on preservation metadata), XML is expressed hierarchically. You can see that plainly here: wherever there are indentations. What is powerful about this is that this allows for lower-level components, like folders, to inherit the metadata of higher-level components, like box, or series.

-->

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
  <div class="circle">1</div>
  <div class="content">
    <h2>Need for dynamic navigation</h2>
    <p>Archival description requires sophisticated navigation options.</p>
  </div>
</div>

<div class="takeaway">
  <div class="circle">2</div>
  <div class="content">
    <h2>It’s easy to get lost</h2>
    <p>Users, especially those new to navigating finding aids, report feeling lost, confused, or unsure over where they are within the collection.</p>
  </div>
</div>

<div class="takeaway">
  <div class="circle">3</div>
  <div class="content">
    <h2>Online availability is difficult to determine</h2>
    <p>Users assume all components listed are available online and feel frustrated when they realize some or all parts are not available.</p>
  </div>
</div>

---

<div class="takeaway">
  <div class="circle">4</div>
  <div class="content">
    <h2>Training and guidance needed</h2>
    <p>Users would appreciate more training beyond a “Help” page.</p>
  </div>
</div>

<div class="takeaway">
  <div class="circle">5</div>
  <div class="content">
    <h2>Too much jargon</h2>
    <p>Certain words displayed in finding aids can lead to further confusion if required later on to successfully navigate the site.</p>
  </div>
</div>

<div class="takeaway">
  <div class="circle">6</div>
  <div class="content">
    <h2>Want quick results</h2>
    <p>Rather than navigating a table of contents, users would rather a finding aid be navigable in the same way a modern search engine works.</p>
  </div>
</div>

---

<div class="takeaway">
  <div class="circle">7</div>
  <div class="content">
    <h2>Less texts, more lists</h2>
    <p>Large blocks of text are distracting; users prefer hyperlinked, easy-to-read bulleted lists.</p>
  </div>
</div>

<div class="takeaway">
  <div class="circle">8</div>
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

<div class="shapes">
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

# Accessibility

---

## Definition
# Accessibility

Within digital archives, __accessibility__ commonly refers to the general discoverability and ease of use of online archival collection, enabling equal or equivalent access to archival facilities and services for people with disabilities, and minimizing or eliminating barriers. Accessibility should be integral to institutional cultures, workflows, and services.

---

# Accessibility is essential to building access platforms

Most institutions’ accessibility expectations will be informed by federal law, state law, and/or institutional best practices. Section 508 Standards for Accessible Electronic and Information Technology, the World Wide Web Consortium’s Web Content Accessibility Guidelines (WCAG), and PDF-UA (ISO 14289-1) are the most common tools used to build digital accessibility policies.

---

<div class="slide-title">Accessibility Recommendations</div>

---

<div class="takeaway">
  <div class="circle">1</div>
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
  <div class="circle">2</div>
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
  <div class="circle">3</div>
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
  <div class="circle">4</div>
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