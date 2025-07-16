# Project Repository | Natural Language Processing

Welcome! 👋 This repository contains the practical assignments developed for the **Natural Language Processing (NLP)** course. The projects presented here demonstrate the application of various techniques and tools, from text processing with regular expressions to creating *Word Embedding* models and developing web applications for data visualization.

---

## 🚀 Core Projects (Main Assignments)

These are the two central projects of the course, integrating various concepts learned throughout the semester.

### Core Project 1: PDF Information Extractor and Processor
The goal of this project was to develop a tool capable of processing `.pdf` documents to extract relevant information (terms, descriptions, etc.) and structure it in an organized and reusable format.

* **Key Topics:**
    * Conversion of PDF files to text.
    * Text cleaning and normalization using regular expressions.
    * Extraction of term-designation pairs.
    * Storing the extracted data in `JSON` files for future use.
* **Technologies:** `Python`, `Regular Expressions (re)`, `JSON`, `pdftotext`.

### Core Project 2: Term Visualization and Analysis Tool
This project involved creating a web application to visualize and interact with the data extracted in the previous project. The tool allows users not only to consult terms but also to enrich them with external information (translations) and explore the relationships between them.

* **Key Topics:**
    * Development of an API and web interface.
    * Data enrichment from external sources.
    * Implementation of features to query, add, edit, and delete concepts.
    * Intuitive data visualization.
* **Technologies:** `Python`, `Flask`, `Bootstrap`, `HTML`, `JSON`.

---

## 📚 Homework Assignments (TPCs)

This section contains the weekly exercises that served as the foundation for the core projects.

* **TPC1: Review Exercises**
    * Solved review exercises on fundamental **Python** topics, including creating an anagram dictionary from a text file.

* **TPC2: String Analysis with Regular Expressions**
    * Used the Python `re` library to learn and apply functions like `re.match`, `re.findall`, `re.search`, and `re.sub` for string analysis and manipulation.

* **TPC3: HTML Generator from PDF**
    * Developed a Python program that converts a `.pdf` file to `.txt` and then uses regular expressions to extract term-designation pairs and generate an **HTML** page styled with **CSS**.

* **TPC4: Webpage with HTML and CSS**
    * Created a static webpage about a hobby (Formula 1), using only **HTML** and **CSS** to structure and style the content, including custom fonts and column-based layouts.

* **TPC5: Term Tagger and JSON Generation**
    * Enhanced a term-tagging script. The work involved extracting translations from a `.txt` file, creating a dictionary, and saving it as a **JSON** file. The main script was then modified to use this dictionary to add the English translation to the `title` attribute of an HTML tag.

* **TPC6: Medical Concept Visualization Website with Flask**
    * Developed a dynamic website using the **Flask** framework to visualize medical concepts. The application allows users to add, edit, and query concepts and their translations, which are stored in a JSON file. The interface was built with **Bootstrap**.

* **TPC7: Website Enhancement with Permissions and Search**
    * Evolved the TPC6 project by adding features such as a search page and displaying data in a dynamic table using the **jQuery (DataTable)** library. Routines were implemented to ensure data consistency in the JSON file after each change.

* **TPC8: Word Embedding Models**
    * Developed and evaluated *Word Embedding* models using the **Gensim** library and the **Word2Vec** technique. Texts from the Harry Potter series were used to train different models, assessing their performance on similarity and analogy tasks.
