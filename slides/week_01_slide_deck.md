# Week 1 
Introduction to Digital Archives

---

# Today
- **Welcome and introductions**
- **Review the syllabus**
- **Break**
- **Lecture: Digital information basics**
- **Discussion**
- **Next week**

---

# Announcements

_Feel free to email me with any announcements you would like me to boost (upcoming conferences, webinars, trainings, or other events/topics of interest)._

---

# Ground Rules

This class is intended to be a welcoming and productive space.

All questions, including repeat questions, or questions with “obvious” answers, are welcome and encouraged. Anti-oppressive or harmful language will not be tolerated.

---

# About Me

My name is Mary Kidd. My pronouns are she/her. You can call me Mary in class, over email, or anywhere else.

I work at the New York Public Library as the Systems and Operations Manager in the Preservation and Collections Processing Department. I also consult on and have led various digital preservation projects.

My email: [mary.kidd@nyu.edu](mailto:mary.kidd@nyu.edu)

---

# Introduce yourself

* What program are you in and how far along are you?
* What do you hope to learn in this course?

---

# Syllabus Review

[https://digital-archives.github.io/HISTGA1011/](https://digital-archives.github.io/HISTGA1011/)


<!-- presenter notes

This semester’s syllabus is hosted on Github. Has anyone here used or are you familiar with Github?

Briefly: Github is an online platform that is used to store and version information. It is also a platform used widely in the digital archives and preservation fields. We will cover what Github is, more, later on in the semester, and see some "real life" examples of digital archiving and preservation repositories. But for now, you will be using it primarily to access the class syllabus, as well assignments and other documents we will be using for in-class activities.

Syllabus link: https://github.com/kiddmary/HIST-GA-1011

-->

---

# Digital Information Basics

<!-- presenter notes

I want to step you through basic concepts to do with what digital information is, and in particular, how it is encoded.

-->

---

# Why Should We Know About Digital Information?

“As archivists, if we are going to be able to take care of digital collections into the future, we must understand that the basic building blocks of… digital files are… bits and bytes. To know files, we must know how they are constructed… And from this knowledge, we will be better equipped to design preservation strategies for our digital collections.”

Bertram Lyons, _The Digital Archives Handbook_ (2019)

<!-- presenter notes

Lyons, Bertram. "Digital Preservation." In The Digital Archives Handbook: A Guide to Creation, Management, and Preservation, edited by Aaron D. Purcell, 3-18. Rowman & Littlefield Publishers, 2019. Accessed September 11, 2023. http://ebookcentral.proquest.com/lib/nyulibrary-ebook/detail.action?docID=5646172, 3.

-->

---

# Definition: Digital Object

A __digital object__ is a complex entity composed of __bitstreams__, necessitating the use of one or a combination of machines and digital components to access and understand.

<!-- presenter notes

Let's unpack this definition by thinking a bit about digital objects we encounter through our life and work.

-->

---

# Question for Class

What are some examples of digital objects that you know of, or have worked with, in your job, or life?

Answer in the [Airtable Form](https://airtable.com/appX8QYrNyTDJDGmg/pag5PKEZC1XAvye3O/form)

---
# The Complex Relationship of Digital Objects

**Digital Object**  
(e.g., document, media, software)  
↓  
**Requires**  
Software, Hardware, Emulation, Specialized Knowledge  
↓  
**Maintains**  
Accessibility, Preservation  
↓  
**Failure to Maintain**  
→ Obsolescence, Inaccessibility, Data Loss

<!-- 

Digital objects encapsulate various forms of digital content, such as documents, media, or software.

All digital objects, whether it's a single file, or an entire application, will require specialized software, hardware, emulation, specialized knowledge, or one or all of these things, to faithfully render and understand, ensuring their long-term accessibility and preservation.

-->

---

# Digital Object Encoding

<!-- presenter notes

But what makes this even more complicated is the nature of digital information itself. At its core, all digital objects—whether they’re a document, an image, a video, or a piece of software—are nothing more than binary code. If you looked at their core code, you would see an endless stream of numeric ones and zeros.

To understand or interact with a digital object, we need some kind of intermediary, like software to process it, or hardware to run it. In contrast, think about a physical book or a printed photograph. You can hold them in your hands, see the information, and directly interpret it. The content is immediately accessible without requiring any additional technology.

With digital objects, however, every step—from the file type to the program that opens it—requires something to act as a bridge, translating that binary data into something recognizable, something we can make sense of.

And this dependency on intermediaries presents a risk. What happens when the software that interprets that file becomes obsolete? Or when the hardware is no longer available, because the manufacturing plant that produced it is no longer? Without maintaining these layers, digital objects could easily become lost or unreadable, leaving us with nothing more than a stream of binary code that’s effectively inaccessible.

-->

---

# Question

Can you think of an example from your life or work where you use a sequence of numbers to encode something?

I'll start: A zip code

<!-- presenter notes

Question for the class: Can you think of an example from your life or work where meaning is encoded by numbers in a specific order?

Other examples:
- Area code of a telephone number
- DD/MM/YYYY format date

These encodings are akin to how computers encode information into binary. Basically, binary is made up of numbers, in a specific sequence, that represent things in the world.

-->

---

# Definition: Binary

__Binary__ encodes information using:
- A "base-2" system and place values
- The digits 0 and 1, referred to as __bits__

Binary works in a similar way to the familiar __base-10__ decimal system, which also uses digits and place values to represent numbers.

<!-- presenter notes

Binary describes an encoding scheme in which there are only two possible values or states for each value, such as 1 or 0. Because there are only two possible values, binary is considered a base-2 system.

Each individual value is referred to as a “bit”. In the case of a binary computing that uses 1s and 0s, the “1” and the “0” are two individual bits.

Along with bit values, binary also uses place values to represent real-world values.

Computers, true to their name, are machines primarily designed to carry out computations. They excel in understanding the language of numbers.

-->

---

# 0 1 2 3 4 5 6 7 8 9

<!-- presenter notes

If you did not know this already, the numbers that you and I are most familiar with are written in a "base-10" decimal system. The first thing to know about a base-10 system is that it uses 10 digits (0-9) to represent the "base" values.

The second thing to know about a base-10 decimal system is that it uses number placement to represents values that exceed 9.

-->

---

# 10

<!-- presenter notes

Therefore, when we write out a ten, we don't have a "base value" that represents ten. Instead, we move the 1 over left to what is known as the "tenths" place, and combine that with the "0" right next to it, in the "ones" place. Combined, we know these two numbers to represent 10.

-->

---

# 100

<!-- presenter notes
When we go up one hundred values, we again, bump our 1 over one more place to the left, and so on. Each new "place" represents an increment of 10 "to the power of" the placement designation.
-->

---

# 1,200

<!-- presenter notes 

In a base-10 decimal system, we use position to determine a value. So here, we have four individual decimal values, 1, 2, 0 and 0. We know that this represents “1 thousand, two hundred” because the 1 is in the “thousandths” place, which we know to be four positions left from the very right. And to sometimes make base-10 numbers more readable, we'll place a convenient comma to group together three places.

Binary works similarly in that we use bits value and their positions to determine their overall value, but it works in a slightly different manner, which we’ll explore in a bit (joke intended!)

-->

---

# Definition: Byte

A __byte__ is a discrete-length grouping of bits.

__Example: 00000111__

This byte has a discrete length of 8.

A byte's length can determine how many distinct byte values can be represented.

<!-- presenter notes

A byte is a discrete-length grouping of bits. In the slide, we have an example of a byte that consists of 8 bits.

There are other systems that have 16-bit or 24-bit length bytes. But for this example, and for the rest of the lesson, let’s work within a system that uses 8-bit bytes, for simplicity’s sake.

Source: https://www.youtube.com/watch?v=N5SU4RW9opc&ab_channel=CodeHS
https://www.techtarget.com/whatis/definition/binary#:~:text=In%20mathematics%20and%20in%20computing,unit%20(CPU)%20and%20RAM.

-->

---

__00000111__

An 8-bit system can store up to 256 values.

Why 256?
- Each bit represents 1 of 2 values (A base-2 system can only have two possible values: 1 or 0)
- This byte has a length of 8 values. So, the total number of values can be determined by "raising" 2 possible bit values to the power of 8 possible bit values (2^8). This looks like:

```
2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 
= 
256 possible values
```

<!--presenter notes
I mentioned before than in a base-10 counting system, the length and position encodes value. Binary, similarly, can be interpreted by both length and position.

The position of each digit determines its decimal value. Thus, by understanding the position of each bit, a binary number can be converted into a decimal number.

An 8-bit byte system means each byte contains 8 bits.

Each bit represents 1 of 2 values: a 1 or 0.

To calculate how many different combinations of 8 1s and 0s, we raise the number 2 (standing for 2 possible values) to the power of 8 (8 total bits). From this, we get 256 possible values.
-->

---

# Question: How many possible byte values are there in a __16-bit__ system?

Hint:
* Number of possible values: 2
* Length of byte: 16
* Raise 2 to the power of 16 (2^16)

---

# Answer: 65,536

A 16-bit system can be calculated by raising the number of possible values (2) to the power of the length of the byte (16), or "two to the power of 16" (2^16). That is:  

```
2 * 2 * 2 * 2 *  
2 * 2 * 2 * 2 *  
2 * 2 * 2 * 2 *  
2 * 2 * 2 * 2

=

65,536
```
---

![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives0.png)

Example of an 8-bit system: Nintendo Entertainment System (NES) gaming console from the 1980s

---

![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives1.gif)

<!-- presenter notes

Comparing an 8-bit Nintendo Entertainment System to a 16-bit one side-by-side, you can see some differences. There are more colors, shades, textures, and tones in the right-hand screen. The more information you can encode, the more stuff you can represent on-screen.

it's important to understand that when we are referring to an 8-bit versus a 16-bit system, and how many byte values each can handle, does not mean that an 8-bit system can only handle 256 values max across all aspects of the game, such as sound, colors, etc, or 65,000 max values for a 16-bit system. This actually refers more to how large of a byte the Central Processing Unit, or CPU, can handle. The CPU is considered the “brain” of the computer or gaming console: it executes instructions from the game software, which include operations like processing inputs, updating game logic, rendering graphics, and managing sound. This allows a 16-bit system to handle more complex instructions at any given moment in gameplay.

-->
---

# Binary -> Decimal

| Binary value | Decimal value |
| :-: | :-: |
| 0000 0000 | 0 |
| 0000 0001 | 1 |
| 0000 0010 | 2 |
| 0000 0011 | 3 |
| 0000 0100 | 4 |
| 0000 0101 | 5 |
| 0000 0110 | 6 |
| 0000 0111 | 7 |
| 0000 1000 | 8 |
| 0000 1001 | 9 |

<!--presenter notes

Here is a sample list of binary values, corresponding to decimal values, in an 8-bit system. In the right-most column, we have 10 decimals, 0 through 9, and their corresponding binary values. In an 8-bit system, the complete list would show 256 possible values.

You may have noticed that, there seems to be a pattern in the placement of 1s and 0s for each decimal going up in succession. Bytes are not arbitrarily assigned to decimals: there is a mathematical system behind that make it so, if you take a binary value, you can reverse-engineer it to determine, in a few steps, the decimal value it represents.

-->

---

| Bit | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |


__This byte represents the decimal number 7__
How do we get from 0000 0111 to 7?

---

| Bit | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |

__First question to ask__: How many ones (1) are there?__

<!--presenter notes 

Each bit has its own place or position, which is mapped out on the slide. In an 8-bit system, we have 8 possible place values, starting from place 0, up to place 7. Places are read from right to left.

-->

---

| Bit | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |

__Answer__: 3

---

| Bit | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Place | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |

__Second question to ask__: For each 1 we've found, what are their place values?

---

| Bit | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Place | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |

__Answer:__ 0, 1 and 2

---

| Bit | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Place | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| Weight | 2^7 | 2^6 | 2^5 | 2^4 | 2^3 | 2^2 | 2^1 | 2^0 |

__Third question to ask__: For each 1 we've found, what is their __weight__?

---

| Bit | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Place | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| Weight | 2^7 | 2^6 | 2^5 | 2^4 | 2^3 | 2^2 | 2^1 | 2^0 |

__Answer__: 4, 2 and 1, which add up to 7

<!-- presenter notes

What do we mean by weight?

A good example comes from the base-10 decimal system we are most familiar with.

-->

---

Decimal value: 787

| Digit | 7 | 8 | 7 |
| :-: | :-: | :-: | :-: |
| Place | 2 | 1 | 0 |
| Weight | 10^2 | 10^1 | 10^0 |
| Value | 100 | 10 | 1 |

7 + 80 + 800 = 787

<!-- presenter notes

Translating binary to decimals may seem unfamiliar, which is fine, because we rarely ever have to do this (that’s the job of computers, afterall).

However, the steps we take to interpret a binary number are similar to how we interpret a decimal number. Let’s take the number 787.

For decimals we also read placements from right to left, as we did with the binary example. In this case, the rightmost digit, which is in place 0, represents the “ones” place. It carries a weight of 10^0, which equals 1. So, the digit 7 in the ones place contributes 7 * 1 = 7 to the overall value of the number.

Moving to the left, the next digit in Place 1 represents the tens place. It carries a weight of 10^1, which equals 10. Therefore, the digit 8 in the tens place contributes 8 * 10 = 80 to the overall value of the number.

Finally, the last digit in place 2 represents the hundreds place. It carries a weight of 10^2, which equals 100. Therefore, the digit 7 in the hundreds place contributes 7 * 100 = 700 to the overall value of the number.

By multiplying each digit by their weight value, we get three numbers: 700, 80 and 7. If we add these three numbers together, we get 787.

Place value allows us to understand the significance and contribution of each digit within a number based on its position, with each position representing a different power of the base of the number system.

Now that we better understand the concept of weight, let's return to our binary example.

-->

---

Decimal value: 7

| Bit | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Place | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| Weight | 2^7 | 2^6 | 2^5 | 2^4 | 2^3 | 2^2 | 2^1 | 2^0 |
| Value | 0 | 0 | 0 | 0 | 0 | 4 | 2 | 1 |

- The 1 in Place 2 carries a weight of 2^2 or 4. We multiply 4 by 1 to get a total value of 4.
- The 1 in Place 1 carries a weight of 2^1 or 2. We multiply by 1 to get a total value of 2.
- The 1 in position 0 carries a weight of 2^0 or 1. We multiply by 1 to get a total value of 1
- __Add together all values: 4 + 2 + 1 = 7__

---

| Word | OK | |
| :-: | :-: | :-: |

<!--presenter notes

Let’s shift from the raw binary representation to something more familiar—an actual word. In this case, let's use the word "OK" as an example.

When you see the word "OK" on a computer screen, you’re looking at an abstraction built on several layers of encoded data. The process that brings that simple word to your screen involves multiple transformations, from human-readable characters to machine-interpretable code.

In the table on the slide, the left-hand column names each of these layers, while the right-hand column shows how the computer encodes and interprets the information. We are going to "drill down" through these layers, one-by-one.

-->

---

| Word | OK | |
| :-: | :-: | :-: |
| Characters | O | K |

<!--presenter notes

The first layer is what you see—the letters "O" and "K." We are going to separate these letters into two individual letters, and treat them as such moving forward.

-->

---

| Word | OK | |
| :-: | :-: | :-: |
| Characters | O | K |
| Decimals | 79 | 75 |


<!--presenter notes

Each letter is assigned a decimal number through a computer’s internal dictionary, also known as the ASCII table.

The letter "O" corresponds to the decimal number 79, and "K" corresponds to 75.

-->

---

| Word | OK | |
| :-: | :-: | :-: |
| Characters | O | K |
| Decimals | 79 | 75 |
| Hexadecimals | 4F | 4B |

<!--presenter notes

Then, these decimal values are often converted into a hexadecimal system for efficiency, where "O" becomes 4F and "K" becomes 4B. You can think of hexadecimals, referred sometimes in short as "hex", as a kind of shorthand for bytes.

-->

---

| Word | OK | |
| :-: | :-: | :-: |
| Characters | O | K |
| Decimals | 79 | 75 |
| Hexadecimals | 4F | 4B |
| Byte (Binary) | 01001111 | 01001011 |

<!--presenter notes

These values are converted into their binary representations: 01001111 for "O" and 01001011 for "K."

At its core, computers understand and process everything in bits and bytes. In this case, each character in "OK" is made up of 8 bits, with a specific combination of 1s and 0s. These bits are then stored physically in hardware.

-->

---

| Word | OK | |
| :-: | :-: | :-: |
| Characters | O | K |
| Decimals | 79 | 75 |
| Hexadecimals | 4F | 4B |
| Byte (Binary) | 01001111 | 01001011 |
| Hardware (On/Off Signals) | ■ □ □ □ ■ ■ ■ ■ | ■ □ □ □ ■ □ ■ ■ |

<!--presenter notes

If we could microscopically zoom into the physical storage—like a hard drive or memory chip—we would see that these bits are stored using electrical signals or magnetic charges. Think of each 1 and 0 as a tiny "on" or "off" switch, or a north/south magnetic direction.

For example, a 1 might be represented by a magnetic field pointing in one direction, while a 0 is stored as the magnetic field pointing in the opposite direction. On a hard drive or chip, this encoding process happens for every single bit, ensuring that what you see on the screen is faithfully represented by physical signals underneath.

So, whether you're reading a word, watching a video, or listening to music, it's all fundamentally encoded in binary and stored physically as on/off signals or magnetic impressions. This entire process—from the word "OK" you see on the screen down to the magnetic signals on a storage device—is how modern computing translates information into a format both humans and machines can understand.

-->

---

# Break

![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives2.gif)

---

# A Brief History of Digital Preservation and Archiving

<!--presenter notes
Much of this timeline is influenced by Digital Preservation Management’s Timeline of Digital Technology and Preservation (https://www.dpworkshop.org/dpm-eng/timeline/timeline.html).
-->

---

![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives3.jpg)

<span style="color:#FFFFFF">Physical holes punched into a piece of paper told machines what to do\.</span>

---

https://www.dpworkshop.org/dpm-eng/timeline/timeline.html

Here, we are looking at a piece of physical paper containing an array of numbers. The paper is punched through with holes that correspond to what are essentially bits and bytes of information. Punch cards like this were used throughout numerous industries. Some of the earliest examples were punch cards that were used throughout the textile industry. Punch cards were encoded with information that corresponded to various warping and wefting. At its core, each hole in the card corresponds to a number, which the machine interprets into a pattern.

https://meridian.allenpress.com/american-archivist/article/58/2/182/23633/Punch-Card-Records-Precursors-of-Electronic

![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives4.png)

<span style="color:#FFFFFF">US National Archives mentions punch cards as part of the historic record\.</span>

---

Source: https://meridian.allenpress.com/american-archivist/article/58/2/182/23633/Punch-Card-Records-Precursors-of-Electronic

Punch cards were used in the late 19th century for census tabulation. Punch cards would, in fact, be used well into the mid-20th century, and incorporated into how some of the earliest computers read and interpreted information.

Punch cards were recognized as carriers of information, and in the 1939 Records Disposition Act, punch cards were listed as a type of record eligible for preservation. The slide shows an excerpt from this Act, that lists punch cards alongside other record types such as sound recordings, papers, correspondence and others.

![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives5.jpg)

<span style="color:#FFFFFF">Construction of the 30\-ton ENIAC\, one of the first electronic computers\. </span>

---

In 1940, we start to see the development of programmable computers. In the slide above we are looking at the Electronic Numerical Integrator and Computer, aka ENIAC, developed by the United States Army, and housed in Philadelphia, Pennsylvania. In the foreground of the photo is Betty Holberton, an American computer scientist who was one of the six original programmers of the ENIAC. The 1940s heralded the development of computing machines.

Take note of the plug boards you see in the photo on the left. These plug boards are how computations were programmed into the computer. They work in an essentially similar manner to punch cards; instead of holes in paper, you had cables going into boards that corresponded to numbers that the ENIAC could interpret into computations.

![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives6.jpg)

<span style="color:#FFFFFF">Magnetic core memory technology developed to encode binary data using magnetization\.</span>

---

Image source: Konstantin Lanzet - received per EMail Camera: Canon EOS 400D
Core Memory Module – A 32 x 32 core memory plane storing 1024 bits (or 128 bytes) of data. The small black rings at the intersections of the grid wires, organized in four squares, are the ferrite cores.

CC BY-SA 3.0
File: KL CoreMemory.jpg
Created: 14 June 2009


In 1949, Dr. An Wang from the Harvard University Laboratory in the United States invented magnetic core memory.

Magnetic core memory works by subjecting a magnetic field to a magnetic-sensitive “core”. The core, in turn, could be magnetized in a certain direction. One direction would correspond to a 1, and in another direction correspond to a 0. So, instead of holes in paper cards or cables into punch boards, we are seeing magnetic field sensitive cores used to encode bits.

The image you see in the slide shows a 32 x 32 core memory plane storing 1024 bits (or 128 bytes) of data. The small black rings at the intersections of the grid wires, organised in four squares, are the ferrite cores. This so-called “core memory” is one of the first instances of using magnetism to store data. We will see magnetism crop up again with the advent of hard disk drive and recording media later on. 

<span style="color:#FFFFFF">1950 Federal Records Act passed\, which includes a definition of the record as including “machine\-readable materials\.”</span>

---

Computer technology became more compact and faster over the decades. In 1950, the Federal Records Act was passed, providing a legal framework for federal records management. The Act specifically cites “machine-readable materials” as part of the definition of the record, which is the first time we see machine-stored information cited at this level.

The act has since been amended to meet modern circumstances. Most notably and recently the Presidential and Federal Records Act Amendments of 2014 was signed into law by President Obama, modernizing the Federal Records Act by expressly expanding the definition of federal records to include electronic records, which was the first change to the definition of "Federal record" since its initial enactment.

More background on the motivation for this Act being passed can be found in a 1953 American Archivist article: https://www.jstor.org/stable/40289125



![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives7.jpg)

<span style="color:#FFFFFF">IBM introduces first commercial secondary storage computer\, RAMAC\, that weighed a ton and required forklifts to move\. IBM touted its ability to “store the equivalent of 64\,000 </span>  <span style="color:#FFFFFF">[punched cards”\)\, the modern equivalent of 1 MB\.](https://en.wikipedia.org/wiki/Punched_card)</span>

---

The 1950s saw an explosion of computing and storage device technologies. The RAMAC machine you see pictured above -- RAMAC stands for “Random Access Method of Accounting and Control” -- was used in the accounting industry. The RAMAC was the first commercial computer to store memory using a moving-head hard disk drive, or HDD.

Source: https://cs.stanford.edu/people/nick/how-hard-drive-works/
A hard disk drive works in a similar manner to the magnetic core memory example we just covered. Basically, a spinning plate is coated in a thin magnetic-field sensitive substrate. A magnetized head runs over the plate, magnetizing or “writing” into the substrate one of two directions: Magnetic North or South. Each direction corresponds to (you probably guessed it) a 1 or 0. To access this stored information, the head runs over the spinning plate again and instead or writing, “reads” the pattern of magnetized norths and souths.

Magnetic writing and reading of memory was a huge step in revolutionizing computers. Because this information could be written in a near-microscopic manner, computers started to get smaller and more compact.


![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives8.png)

__MARC__  \(MAchine Readable Catalog\) records  <span style="color:#FFFFFF">become</span>  the US standard for library cataloging\.

---

The 1960s saw the development of smaller and smaller computers. In the library field, Machine Readable Catalog records, or MARC, becomes the US standard for library cataloging.

https://www.dlib.org/dlib/may15/papadakis/05papadakis.print.html

The first ARPANET node is installed at UCLA Network Measurement Center\.

![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives9.png)

---

1 min

Image source: 
CC BY-SA 4.0
File:Arpanet in the 1970s.png
Created: 4 January 2022

The late 1960s heralded the first networked computers. Advanced Research Projects Agency Network or ARPANET - a precursor to the modern internet - was the first wide-area packet-switched network. Packet-switched networks transmitted data from one node to another in a more efficient manner, and this model is essentially the backbone for how for data communications in computer networks worldwide today work.

In the chart above, you can see a map of ARPANET node map from the early 1970s.

<span style="color:#5E5E5E"> __USENET emerges as a collection of user\-submitted messages on various subjects posted to servers on a worldwide network\.__ </span>

<span style="color:#5E5E5E"> __Altair 8800\, one of the first personal “microcomputers” are sold through mail order catalogs\.__ </span>

<span style="color:#FFFFFF">The Kurzweil Reading Machine combines omni\-font OCR\, flat\-bed scanners\, and text\-to\-speech synthesis to create the first print\-to\-speech reading machine for the blind\.</span>

<span style="color:#FFFFFF"> __Ohio College Library Center \(OCLC\) established __ </span>  <span style="color:#FFFFFF">to provide a public cataloging network\.</span>

---

3 minutes

The 1970s saw an explosion of computing and networking technology, so I’ve cherry-picked some highlights from this decade. The first being in 1971, the establishing of the Ohio College Library Center or OCLC, which was a shared cataloging system for libraries.

In 1974 we see the development of the Kurzweil Reading Machine, which used scanners to turn text into speech. This is considered the first practical application of optical character recognition or OCR technology. To me, it represents an important shift in how society uses technology. Leading up to this, computers are primarily used to support industries or war efforts. Here, we are seeing assistive technologies break down accessibility barriers to information and knowledge.

In 1975, we see the release of what is considered the first commercially successful personal computers, the Altair 8800. Later in the 1970s, we will see the release of other personal computers such as the Apple II. These developments represents computers entering into the domestic sphere. 

We end the 1970s with the emergence of USENET in 1979. USENET is a precursor to online discussion forums, a precursor to Reddit and others. The domestication of computer technology, and the introduction of these technologies into libraries, herald the socializing potential of networked computing, for better or for worse.







<span style="color:#5E5E5E">The</span>  <span style="color:#FFFFFF"> </span>  <span style="color:#5E5E5E">National Endowment for the Humanities \(NEH\) funds the </span>  <span style="color:#5E5E5E"> __Brittle Books Program__ </span>  <span style="color:#5E5E5E"> to microfilm \(and eventually digitize\) ~3 million of 19th\-century books\.</span>

<span style="color:#5E5E5E">Scott Armstrong \(Executive Director of the National Security Archive\) filed a Freedom of Information Act \(FOIA\) request to ensure that the contents of the White House electronic mail and records system\, contained on magnetic backup tapes\, would not be destroyed and subject to archival review before disposition\.</span>

<span style="color:#FFFFFF">Sony and Philips introduce the first CD player\.</span>

<span style="color:#FFFFFF">The National Information Systems Task Force \(NISTF\) develops the first two formally recognized archival description standards in the US: NISTF Data Elements Dictionary and USMARC AMC\.</span>

<span style="color:#FFFFFF">Sony introduces the first 3½" floppy drives and diskettes\.</span>

---

3 minutes

In 1981 Sony introduced the first 3½” floppy drives and diskettes. Although other floppy disks were released earlier than this, the 3½ disk format was used widely and was very popular carrier.

In 1982 the National Information Systems Task Force (NISTF) developed the first two formally recognized archival description standards in the United States: NISTF Data Elements Dictionary and USMARC AMC. These efforts were used to both standardize the description of archives in order to better exchange or share information across networked catalogs.

In 1988, at the behest of the US Congress, the National Endowment for the Humanities (NEH) funds the Brittle Books Program to microfilm (and eventually digitize) ~3 million 19th-century books. When this program first began, books were digitized through preservation microfilming and even photocopying. Later, this would be replaced with digital scanning and photography methods, into high-resolution file formats such as Tag Image or “TIF” file format.

A year later, Scott Armstrong, Executive Director of the National Security Archive, filed a Freedom of Information Act (FOIA) request to ensure that the contents of the White House electronic mail and records system, contained on magnetic backup tapes stored on the IBM PROFS system, would not be destroyed and subject to archival review before disposition. This FOIA led to a lawsuit known as Armstrong versus the Executive Office of the President implicating both the Reagan and Bush White Houses. This lawsuit resulted in the court ordering the transfer of 5,839 backup tapes to the National Archives.  

See: https://www.jstor.org/stable/40293774 and https://law.justia.com/cases/federal/district-courts/FSupp/821/761/1510466/

__In December 1994\, the Research Libraries Group \(RLG\) and Commission on Preservation and Access \(CPA\) formed a Task Force on __  __Archiving of Digital Information__  __ with the main purpose of investigating what needed to be done to ensure long\-term preservation and continued access to the digital records\.__

---

1 minute

In 1994, the Research Libraries Group and Commission on Preservation and Access (CPA) formed a Task Force on Archiving of Digital Information with the main purpose of investigating what needed to be done to ensure long-term preservation and continued access to digital records.

This report specifically calls out the fact the threat of digital technologies in light of the fact that digital technologies were becoming the standard for recording the cultural memory. In the Task Force report, they call out a specific instance in 1976 where the National Archives realized data from the 1960 Census files resided on tapes that the Bureau could read only with a specific and long-obsolete drive. This required the Census Bureau to migrate this data onto industry-standard tapes.

Source: https://www.clir.org/wp-content/uploads/sites/6/pub63watersgarrett.pdf


<span style="color:#FFFFFF"> __Digital Library Federation \(DLF\) is formed\.__ </span>

<span style="color:#FFFFFF"> __National Digital Library Program \(NDLP\) established at Library of Congress\.__ </span>

<span style="color:#5E5E5E">The Mellon Foundation funds</span>  <span style="color:#5E5E5E"> __ Making of America \(MOA\) __ </span>  <span style="color:#5E5E5E">project\.</span>

<span style="color:#5E5E5E"> __Dublin Core __ </span>  <span style="color:#5E5E5E">metadata schema is established by a working group\.</span>

<span style="color:#5E5E5E"> __Jeffery Rothenberg __ </span>  <span style="color:#5E5E5E">publishes </span>  <span style="color:#5E5E5E"> __“Ensuring the Longevity of Digital Information” __ </span>  <span style="color:#5E5E5E">in </span>  <span style="color:#5E5E5E"> _Scientific American_ </span>  <span style="color:#5E5E5E">\.</span>

<span style="color:#FFFFFF">12 founding member institutions including NARA\, NYPL and LoC\.</span>

<span style="color:#5E5E5E">This schema attempts to universalize how electronic resources are described on the web\.</span>

<span style="color:#5E5E5E">Millions of late 19th\-century journals/monographs digitized\, resulting in ~15\,000 digital objects made available online\.</span>

---

3 minutes

Several key events occurred in 1995 laying down the foundation for digital preservation efforts going forward.

Here, we see several digital preservation and archives efforts underway: the National Digital Library Program (NDLP) was established at the Library of Congress with the goal of “assembling a digital library of reproductions of primary source materials to support the study of history and culture in the United States.” Source: https://memory.loc.gov/ammem/dli2/html/lcndlp.html

The Digital Library Federation (DLF) was established with 12 founding member institutions including the National Archives, the New York Public Library and the Library of Congress. Early efforts focus on building digital infrastructures. The Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH) and Metadata Encoding and Transmission Standard or METS will come out of these efforts. Source: https://www.diglib.org/

Jeffery Rothenberg, a computer scientist for the RAND corporation, published an article “Ensuring the Longevity of Digital Information” in Scientific American, which identified just how fragile digital data is to failure, unreadability, and how much information that only exists digitally will be lost if action isn’t taken. Rothenburg would later go on to develop emulation environments that allow for obsolete software to run on modern-day operating systems.

1995 was was also the year when the National Center for Supercomputing Application (NCSA) and OCLC came together for a joint workshop in Dublin, OH to develop a core set of semantics for Web-based resources would be extremely useful for categorizing the Web for easier search and retrieval called Dublin Core. Source: https://www.dublincore.org/about/history/

Lastly, we have the Andrew W. Mellon Foundation funding the Making of America (MOA) Project, which digitized millions of pages of late 19th-century journals and monographs, and published approximately 15,000 digital objects online. Sources: http://collections.library.cornell.edu/moa_new/ and https://quod.lib.umich.edu/m/moagrp/

<span style="color:#FFFFFF">The non\-profit </span>  <span style="color:#FFFFFF"> _Internet Archive_ </span>  <span style="color:#FFFFFF"> \(archive\.org\) was established “as a response to a rapidly growing problem—the disappearance of content from the World Wide Web\.”</span>

[Rackley\, Marilyn \(2010\) 'Internet Archive'\, Encyclopedia of Library and Information Sciences\, Third Edition\, 1: 1\, 2966 — 2976](https://ia800503.us.archive.org/34/items/internetarchive-encyclis/EncycLisInternetArchive.pdf)

---

1 min

Moving on to 1996, we see the establishment of the non-profit Internet Archive, which was “a response to a rapidly growing problem--the disappearance of content from the World Wide Web.”

Source: Rackley, Marilyn (2010) 'Internet Archive', Encyclopedia of Library and Information Sciences, Third Edition, 1: 1, 2966 — 2976




The first version of  __E__  _X_  __tensible __  _M_  __arkup __  _L_  __anguage__  \(XML\) is released by the World Wide Web Consortium\.

__\<item>__

__\<title>__  __Episode 3: Back it up__  __\</title>__

__\<link>__  __https://ia801001\.us\.archive\.org/18/items/PreserveThisPodcastEpisode3/PreserveThisPodcast\_Episode3\.mp3__  __\</link>__

__	__  __\<pubDate>__

__Thu\, 18 Apr 2019 09:00:00 \+0000__

__\</pubDate>__

__\</item>__

---

2 min

In 1998, the first version of EXtensible Markup Language (XML) is released by the World Wide Web Consortium. XML enables internet-networked machines to “talk” to one another. Similar to the development of Dublin Core, XML allows better sharing of archival electronic resources on the web.

Source: http://www.dlib.org/dlib/february05/vannispen/02vannispen.html


![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives10.jpg)

# Encoded Archival Description (EAD) version 1.0 is released and is XML-compliant.

---

1 min

Encoded Archival Description (EAD) originated at the 1993 Society of American Archivists annual meeting in New Orleans and was headed by Daniel Pitti at the University of California, Berkeley. The project's goal was to create a data standard for describing archives, similar to the MARC standards for describing bibliographic materials. The initial EAD Version 1.0 was released in the fall of 1998. Such a standard enables archives, museums, libraries, and manuscript repositories to list and describe their holdings in a manner that would be machine-readable and therefore easy to search, maintain and exchange. EAD was released as XML-compliant, meaning, you could write a machine-readable EAD using XML and express hierarchical relationships between various finding aid components. This is an important digital archives development. Before this, finding aids were generally either made available to patrons as paper or Word documents, and MARC records were too flat to be able to encode these complex hierarchies.

__Making of America II \(MOA2\) Project__

__Developed standards for creating and encoding digital representations of archival objects\.__

---

2 min

Source: https://www.clir.org/wp-content/uploads/sites/6/pub87.pdf

Funded by the DLF, the Making of America II (MOA2) Project served as a testbed for establishing archival standards around digital object description, access, and tools. The project’s final report states that these efforts were important “...to develop standards for creating and encoding digital representations of archival objects (for example, a digitized photograph or a digital representation of a book or diary)”. Further, the report states, that “If tools are to be developed that work with digitized archival objects across distributed repositories, these objects will require some form of standardization”.

The report put forth a recommendation for what it referred to as Standard Generalized Markup Language (SGML) that served as the basis for the Metadata Encoding and Transmission Standard (METS) standard widely used across digital repositories today. Additionally, the project put forth object modeling frameworks, which result in being able to produce complex digital objects (e.g. a book = one object made up of many image files)

<span style="color:#FFFFFF"> __National Digital Information Infrastructure and Preservation Program \(NDIIPP\)__ </span>  <span style="color:#FFFFFF"> established by the Library of Congress\. This leads to the development of programs such as </span>  <span style="color:#FFFFFF"> __Lots of Copies Keep Stuff Safe__ </span>  <span style="color:#FFFFFF"> \(LOCKSS\)\.</span>

---

1 min

We’ve made it to the 2000s!

In 2000, the National Digital Information Infrastructure and Preservation Program (NDIIPP) was given 100 million dollars by Congress. Led by the Library of Congress, its objective was to archive and provide access to digital resources, convene working groups, administer grant projects, and promote information about digital preservation issues.

The NDIIPP funded several important preservation initiatives including the famous Lots of Copies Keep Stuff Safe (LOCKSS) approach to preservation. LOCKSS basically preserves things by copying and storing copies across nodes, checking copies against other copies to ensure file integrity, and using these copies to maintain continuous access across archives.

![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives11.png)

<span style="color:#FFFFFF"> __Northeast__ </span>  __ __  <span style="color:#FFFFFF"> __Document Conservation Center \(NEDCC\) __ </span>  <span style="color:#FFFFFF">publishes its </span>  <span style="color:#FFFFFF"> __Handbook for Digital Projects__ </span>

---

1 min

The first edition of the Northeast Document Conservation Center (NEDCC)’s Handbook for Digital Projects is published, outlining how to build out digitization projects including prioritization, workflows, tools, planning, rights, preservation and access. Keep this document in mind: it may be useful to you for your final digital preservation plan project. The handbook is specific to flat/2-d scanning to create digital image-based derivatives.

https://www.erecordsusa.com/book-archival-services.html


![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives12.png)

<span style="color:#FFFFFF">Internet Archive’s </span>  <span style="color:#FFFFFF"> _Wayback Machine_ </span>  <span style="color:#FFFFFF"> provides public access to archived versions of the websites it has been crawling since 1996\.</span>

---

1 min

The Internet Archive releases the The Wayback Machine, which had been “crawling” websites since 1996, releases a portal through which users can search for, view and click through captures of websites over their lifetimes. The screen capture you see above is Lycos, one of the earliest search engines, from December 12, 1998.

![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives13.png)

__International Standards Organization \(ISO\) formally adopts the __  __Open Archives Information System \(OAIS\) __  __as the standard model for creating and maintaining a digital repository over time\. __

---

1 min

In 2002, the International Standards Organization (ISO) formally adopts the Open Archives Information System (OAIS) as the standard model for creating and maintaining a digital repository over time. We will be reading and discussing the OAIS in next week’s class, so we won’t really say much here about it, other than the OAIS is now seen as the “gold standard” of digital repository frameworks.

Source: https://www.researchgate.net/figure/OAIS-Functional-Entities-from-Reference-Model-for-an-Open-Archival-Information-System_fig2_272494377


![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives14.png)

<span style="color:#FFFFFF"> __PRONOM__ </span>  <span style="color:#FFFFFF">\, an online registry of file formats and software products\, is developed by the Digital Preservation Department of the UK National Archives\.</span>

---

1 min

In 2002, PRONOM, an online registry of file formats and software products, is developed by the Digital Preservation Department of the UK National Archives. The tool supports both identifying the technical metadata associated with various file formats, and if you happen to come across a new file format that is not in its registry, you can register one yourself. The screen capture you see in the slide was derived from a 2019 blog post (https://openpreservation.org/blogs/using-siegfried-tooling-for-signature-development-for-pronom2019/), whose author gives an example of filling out a fake file format which he has dubbed the “Cafe” file format into the registry by filling out a form.

Source: https://www.nationalarchives.gov.uk/PRONOM/Default.aspx


![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives15.png)

<span style="color:#FFFFFF"> _Google Books_ </span>  <span style="color:#FFFFFF"> project launches to digitize and make available the holdings of large research institutions online\. The project is essentially shuttered in 2017 after decades\-long legal battles\.</span>

---

1 min

In 2002, Google Books project launches to digitize and make available the holdings of large research institutions online. A pilot, spearheaded by Google and Harvard was launched in 2004. Starting in 2005 through to 2013, the Authors’ Guild and others sued Google over copyright infringement. By 2013, the service surpassed 25 million books digitized. Then in 2017, the project basically was shut down by Google after fighting decades-long long legal battles. Seemingly well-meaning mass digitization projects will become a theme through the 2000s.


![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives16.png)

<span style="color:#FFFFFF">RLG\, OCLC and NARA joint task force establishes the </span>  _Trustworthy Repositories Audit & Certification_  \(TRAC\) metric\.

<span style="color:#FFFFFF">Image credit: Illustration by Jørgen Stamp digitalbevaring\.dk CC BY 2\.5 Denmark</span>

---

30 seconds

In 2003, a RLG, OCLC and NARA joint task force established the Trustworthy Repositories Audit & Certification (TRAC) metric. This metric provides a framework through which an institution may be deemed a so-called “trustworthy” digital repository. You should know that there are only a handful of collecting institutions that can actually say they are TRAC certified. Getting certified is a lengthy and expensive process.


<span style="color:#FFFFFF"> __PREMIS__ </span>   <span style="color:#FFFFFF">\(PREservation Metadata Implementation Strategies\) version 1\.0 data dictionary is released as the framework for metadata on preservation activities\.</span>

![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives17.png)

---

1 min

In 2005, the first version of the PREservation Metadata Implementation Strategies (PREMIS) metadata schema is released. This framework is a type of metadata that describes the sorts of preservation activities or actions have occurred through the course of a digital object’s life in a repository. We will discuss PREMIS and also have a hands-on workshop, where we will take a peek into what PREMIS metadata looks like, in a few week’s time. You should know that PREMIS is most usually encoded into XML.

Source (for information and screen capture): https://www.loc.gov/standards/premis/understanding-premis.pdf

<span style="color:#FFFFFF">The term </span>  <span style="color:#FFFFFF"> _linked data_ </span>  <span style="color:#FFFFFF"> is coined by Tim Berners\-Lee\, inventor of the World Wide Web\.</span>

<span style="color:#00FFFF"> __bell hooks__ </span>

<span style="color:#00FFFF">https://en\.wikipedia\.org/wiki/Bell\_hooks</span>

<span style="color:#00FFFF"> __Hopkinsville__ </span>

<span style="color:#00FFFF">https://en\.wikipedia\.org/wiki/</span>

<span style="color:#00FFFF">Hopkinsville\,\_Kentucky</span>

<span style="color:#00FFFF">https://schema\.org/birthPlace</span>

---

1 min

In 2006, the term linked data is coined by Tim Berners-Lee, inventor of the World Wide Web.

Linked data is a way to structure and share information, using links or URLS.

Linked data enables us to make information we share online richer. For example, a website may contain a sentence that states, “bell hooks was born in Hopkinsville” (a city in Kentucky). The sentence in of itself, to a computer, is just an arrangement of alphanumeric digits, A-Z. However, you can parse and attribute meaning to this sentence so that a computer knows more, using linked data. So her name “bell hooks” can be linked to the bell hooks Wiki. Her birthplace can be encoded as a data schema element, birthplace, and the name of her birthplace itself, Hopkinsville, can be connected to the Wiki on Hopkinsville. By structuring text in this way, we can attribute more meaning but also, connect information to broadly-adopted standards or schemas.

Diagram inspired by https://ontola.io/blog/what-is-linked-data/

![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives18.png)

<span style="color:#FFFFFF"> __ePADD__ </span>   <span style="color:#FFFFFF">begins initial work to establish a software for archiving email\.</span>

---

30 seconds

In 2010, Stanford University begins work to establish ePADD, a software tool that allows archivists to better automate processing and making accessible email archives.

https://library.stanford.edu/projects/epadd

![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives19.png)

<span style="color:#FFFFFF">The joint\-led </span>  <span style="color:#FFFFFF"> __BitCurator Project __ </span>  <span style="color:#FFFFFF">begins\, to develop a software application that can perform various digital forensics activities\.</span>

---

1 min

In 2011, the School of Information and Library Science at the University of North Carolina, Chapel Hill (SILS) and the Maryland Institute for Technology in the Humanities (MITH) began joint work developing a software application to support archival digital forensics activities known as Bitcurator.

Bitcurator it addressed two fundamental needs for collecting institutions absent from software designed for the digital forensics industry: incorporation into the workflow of archives/library ingest and collection management environments, and provision of public access to the data. We will use BitCurator as part of an in-class activity in a few weeks time, so you will get some hands-on experience performing digital forensics.

![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives20.png)

<span style="color:#FFFFFF"> _The Digital Preservation Network \(DPN\)_ </span>  <span style="color:#FFFFFF"> is founded as a collaborative use of technology\, expertise\, and financial resources to create a robust and enduring digital preservation service\. It sunsets in 2018\.</span>

---

1 min

https://commons.wikimedia.org/wiki/File:What_is_Digital_Preservation.png

The Digital Preservation Network (DPN) is founded as a collaborative use of technology, expertise, and financial resources to create a robust and enduring digital preservation service. It sunsets in 2018. This is a really interesting case in failing at establishing a networked, national digital preservation network. The way it worked is that institutions would pay a yearly subscription to opt into the DPN technology network and submit their holdings to be stored and shared. There is more written about the ins and outs of why this program failed, but I think even in its failure it has given people in the field a better understanding of institutional limitations in regards to implementing digital preservation in general.

![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives21.png)

<span style="color:#FFFFFF"> _Digital Public Library of America_ </span>  <span style="color:#FFFFFF"> \(DPLA\)\, the US’s aggregator\, is founded as a project aimed at providing public access to digital holdings in order to create a large\-scale public digital library</span> \.

---

1 min

The Digital Public Library of America, or DPLA, was established in 2012. The DPLA sought to aggregate and curate special collections through a centralized website. Similar to DPN, the DPLA faced its own struggle in terms of strategic direction for the program and funding. It, too, also had a membership pay-to-play model. Again, there’s more to be said here about failures in national-level digital preservation efforts like this. Your takeaway should be that sometimes digital preservation programs fail, but through failure there are lessons to be learned in terms of funding and business models, and working on digital preservation at such a large scale. Digital preservation is complicated and takes incredible amount of time and resources.

https://www.flickr.com/photos/dpla/6987082108
https://dp.la/

<span style="color:#FFFFFF">Building on nearly three decades of projects\, workflows and standards\, there is movement to better align standards\, an ever increasing need to develop accessible workflows and tools for digital accession\, ingest\, preservation and access\, and nearly 20 years worth of digital projects and collections that require custodianship\.</span>

---

1 min

__Next week:__

_[https://digital\-archives\.github\.io/HISTGA1011/](https://digital-archives.github.io/HISTGA1011/)_

__Sign up using this Google Form for a file format for the by the start of class\.__

__Post your pre\-class reading reactions to Brightspace by 3:30pm today\.__

__Weekly activity: None this week__

![](img/Week%2001%20-%20Introduction%20to%20Digital%20Archives22.gif)

_Final questions or reflections?_

Email me at mary\.kidd@nyu\.edu\.

