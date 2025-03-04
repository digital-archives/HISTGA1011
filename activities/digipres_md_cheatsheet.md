---
title: Digital Preservation Metadata Cheat Sheet
layout: default
parent: Weekly Activities
nav_order: 7.5
has_children: false
---

# METS & PREMIS Cheat Sheet

---

### **METS (Metadata Encoding and Transmission Standard)**

#### **General Considerations**

- In this example, **METS embeds PREMIS**, meaning some metadata normally in PREMIS standalone files may be handled by METS.
- Some expected elements may be missing from the LOC sample file.

#### **Key Sections in METS**

##### **1. Metadata Wrapping vs. Referencing**

- `<mets:mdWrap>` – Metadata is embedded in the METS document (found in `<mets:mdWrap MDTYPE="MODS">` for descriptive metadata and `<mets:mdWrap MDTYPE="PREMIS">` for preservation metadata).
- `<mets:mdRef>` – Not present in this file.

##### **2. Header**

- `<mets:metsHdr>` which normally indicates the version of **METS** is missing in this file. I'm not sure why!
- The attributes of `<mets:mets>` show us that the:
    - **METS version** used is ambiguous. I derived this example from the [PREMIS XML Usage Examples](https://www.loc.gov/standards/premis/examples.html) page. The specific XML file that you used for this assignment is listed as using version 2.1 (I didn't expect you to figure this out, but in case you were curious!)
    - **PREMIS version** used is **2.0** (`xmlns:premis="info:lc/xmlns/premis-v2"`)
    - **MODS version** is **3.3** (`xmlns:mods="http://www.loc.gov/mods/v3"`).

##### **3. Descriptive Metadata (`<mets:dmdSec>`)**

- Uses **MODS** as the descriptive metadata standard (`<mets:mdWrap MDTYPE="MODS">`).
- Title recorded in MODS: `[Portrait of Louis Armstrong, between 1938 and 1948]`.
- Photographer identified: **William P. Gottlieb**.
- Subjects include **Louis Armstrong, Jazz musicians, Trumpet players (1930-1950)**.

##### **4. Administrative Metadata (`<mets:amdSec>`)**

- **Technical Metadata (`<mets:techMD>`)** – This is repeated twice for two objects, `object1` and `object2`.
- **Digital Provenance (`<mets:digiprovMD>`)** – This is repeated 7 times, describing different preservation events.
- **Source Metadata (`<mets:sourceMD>`)** – Not present in this file.
- **Rights Metadata (`<mets:rightsMD>`)** – **Not explicitly included**. Instead, we see `<mets:mdWrap MDTYPE="PREMIS:AGENT">`, which signals that elements inside `<xmlData>` should be interpreted using PREMIS rather than METS.

##### **5. File Section (`<mets:fileSec>`)**
- Here we see a list of four files. Two are high-resolution TIFF files and another two are lower-resolution JPG files. Each uses `<mets:FLocat>` (File Location) to point to a URL.

##### **6. Structural Map (`<mets:structMap>`)**

- `<div>` sections:
  - **File pointers (`<fptr>`)** – Links to files in `<fileSec>` (e.g., `<mets:fptr FILEID="masterd1e102963"/>`).
  - This section bundles together master with service copies (e.g. a `masterd1e102963` with `serviced1e1029631` and `masterd1e102965` with `serviced1e102965`)
  - **Structural Links (`<mets:smLink>`)** are not present in this file.
  - **Behavior Section (`<mets:behavior>`)** is not present in this file.

---

### **PREMIS (Preservation Metadata: Implementation Strategies)**

_Note_: Most PREMIS within this file does not declare a namespace (e.g. `<premis:` preceeding an element name. Instead, the PREMIS is "wrapped" using `<mets:mdWrap MDTYPE="PREMIS:AGENT">`: tags found within are interpreted as as PREMIS.)

#### **Objects**

1. **Intellectual Entity**: PREMIS does not contain an element specific to Intellectual Entities. Instead, it will rely on the file invoking a descriptive metadata standard. The file uses `<objectIdentifierValue>loc.music/gottlieb.09601</objectIdentifierValue>` which points to a persistent handle. It also uses MODS to further describe the photograph/bibliographic entity.
2. **Representation**: This refers to the full list of files representing the digital object, which covered by <mets:fileSec>.
3. **File**: Again, the <mets:fileSec> lists each file.
4. **Bitstream**: This is not present in the file.

#### **Environment**

- There is an <environment> section, listing:
    - Software required: **Adobe Acrobat (5.0), Windows XP**.
    - Hardware details:
        - **Processor**: Intel x86 (60 MHz minimum).
        - **Memory**: 64 MB RAM (32 MB minimum).

#### **Agents**

- The agent responsible for preservation is **Library of Congress (Prints & Photographs Division)** (`<agentName>LC Repository</agentName>`).

#### **Events**

- **Validation:** File validated using **Jhove 1.1e** (`<eventType>validation</eventType>`).
- **Ingestion:** File ingested into the repository (`<eventType>ingestion</eventType>`).
- **Migration:** File migrated using **Adobe Photoshop** (`<eventType>migration</eventType>`).

#### **Rights Statement**

- The file doesn't explicitly have a Rights Statement. Instead, it links out to one using its `<linkingRightsStatementIdentifierType>` and `<linkingRightsStatementIdentifierValue>`.