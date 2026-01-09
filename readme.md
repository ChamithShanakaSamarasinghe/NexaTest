# 📄 SRS Segmentation & Software Feature Extraction System

## 📌 Project Overview

This project implements an **end-to-end automated SRS (Software Requirements Specification) processing pipeline** that converts unstructured SRS PDF documents into structured, queryable data.  
The system extracts SRS sections, identifies functional requirements, maps software features, and persists all information in a relational database.

The solution is designed as a **foundation system for AI/ML-based requirement engineering**, while currently relying on rule-based NLP techniques.

---

## 🎯 Project Objectives

- Process SRS documents in PDF format
- Extract raw text from SRS files
- Segment SRS content into standard IEEE-style sections
- Automatically extract functional requirements
- Identify and map software features from requirements
- Store all processed data in a structured SQLite database
- Enable future AI/ML model integration

---

## 🧠 Concepts & Techniques Used

- Natural Language Processing (NLP)
- Rule-based Requirement Extraction
- Text Segmentation
- Feature Mapping
- Modular Pipeline Design
- Relational Database Modeling

---

## 🏗️ System Architecture

SRS PDF
↓
PDF Text Extraction
↓
SRS Section Segmentation
↓
Functional Requirement Extraction
↓
Feature Identification
↓
SQLite Database


---

## 🛠️ Technology Stack

| Category | Technology |
|--------|------------|
| Language | Python 3 |
| NLP | NLTK |
| Database | SQLite |
| PDF Processing | PyPDF |
| Development OS | Windows |
| DB Tool | DB Browser for SQLite |

---

## 📁 Project Structure

SRS Segmentation/
│
├── data/
│ ├── input/
│ │ └── OSMS_SRS.pdf
│ ├── output/
│ │ ├── extracted_text.txt
│ │ ├── segmented_sections.txt
│ │ ├── functional_requirements.txt
│ │ └── feature_mapping.txt
│ └── srs.db
│
├── src/
│ ├── extract_text.py
│ ├── segment_sections.py
│ ├── segment_requirements.py
│ ├── extract_features.py
│ ├── main.py
│ │
│ └── db/
│ ├── init_db.py
│ ├── db_config.py
│ ├── insert_document.py
│ ├── insert_sections.py
│ ├── insert_requirements.py
│ └── insert_features.py
│
└── README.md


---

## 🗄️ Database Schema

The system uses an SQLite relational database (`srs.db`) with the following tables:

### 📂 documents
Stores metadata related to each SRS document.
- `document_id` (Primary Key)
- `file_name`
- `created_at`

### 📂 sections
Stores segmented SRS sections.
- `section_id` (Primary Key)
- `document_id` (Foreign Key)
- `section_name`
- `section_text`

### 📂 requirements
Stores extracted functional requirements.
- `requirement_id` (Primary Key)
- `section_id` (Foreign Key)
- `requirement_text`

### 📂 features
Stores identified software features.
- `feature_id` (Primary Key)
- `requirement_id` (Foreign Key)
- `feature_name`

---

## ⚙️ How to Run the System

### 1️⃣ Initialize the Database
```bash
python -m src.db.init_db

Running the complete Pipeline
# python src/main.py


🧪 Pipeline Execution Flow

During execution, the pipeline performs the following steps:

Registers the SRS document in the database

Extracts raw text from the PDF

Segments the document into SRS sections

Stores sections in the database

Extracts functional requirements from each section

Stores requirements in the database

Identifies software features from requirements

Stores feature mappings in the database


Sample Console Output
Document registered
Sections stored
Requirements extracted
Features mapped
All data persisted in SQLite


📊 Results

Successfully processed SRS PDF documents

Automatically extracted multiple functional requirements

Generated software feature mappings

Persisted all extracted knowledge in a relational database

Enabled multi-document support


⚠️ Limitations

Feature extraction is rule-based

No machine learning models implemented yet

Semantic understanding is limited

Language-dependent (English SRS documents)


🔮 Future Enhancements

Requirement classification using Machine Learning

Feature prediction using supervised ML models

Semantic similarity search using vector embeddings

Retrieval-Augmented Generation (RAG) integration

Analytics dashboard for requirement insights


👤 Author

Chamith Shanaka Samarasinghe
BSc (Hons) in Software Engineering