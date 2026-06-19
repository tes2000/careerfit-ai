
# Architecture

## 1. Architecture Overview

CareerFit AI starts with a simple local architecture.

The Day 1 version uses:

- Streamlit for the user interface
- FastAPI for backend endpoints
- CSV files for sample job descriptions
- JSON files for skill taxonomy
- Simple Python logic for matching skills

No database, authentication, scraping, deployment, or advanced ML is included on Day 1.

## 2. High-Level Flow

```text
User
  |
  v
Streamlit Frontend
  |
  v
FastAPI Backend
  |
  +--> Sample Jobs CSV
  |
  +--> Skill Taxonomy JSON
  |
  v
Skill Matching Logic
  |
  v
Recommendations and ATS Checklist