
# MVP Scope

## 1. MVP Goal

The first MVP of CareerFit AI will provide a simple candidate-facing workflow:

1. User selects or enters a job description
2. System identifies relevant skills from a predefined taxonomy
3. User enters their current skills
4. System compares job skills with user skills
5. System shows matched skills, missing skills, and learning recommendations
6. System provides a basic ATS-friendliness checklist

## 2. In Scope

### Job Skill Understanding

The MVP will support:

- Reading sample job descriptions from CSV
- Matching skills using a predefined skill taxonomy
- Grouping skills into categories such as programming, ML, data engineering, cloud, visualization, and soft skills

### Candidate Skill Input

The MVP will support:

- Manual entry of candidate skills
- Simple comma-separated input
- Comparison against job-required skills

### Skill Gap Output

The MVP will show:

- Skills found in the job description
- Candidate skills that match the job
- Missing skills
- Suggested next learning areas

### ATS-Friendliness Checklist

The MVP will include a simple checklist for CV quality:

- Uses clear section headings
- Avoids complex tables and graphics
- Includes relevant keywords naturally
- Uses standard file format
- Uses consistent dates and titles
- Includes measurable project outcomes
- Avoids spelling and formatting issues

### Explainability

The MVP should explain:

- Which skills were detected
- Why a skill is considered missing
- Why a recommendation appears

## 3. Out of Scope for MVP

The MVP will not include:

- Real-time job scraping
- User accounts
- Database storage
- Automated CV parsing
- Paid APIs
- LLM-generated recommendations
- Employer dashboard
- Candidate ranking
- Hiring decision automation
- Production deployment
- Advanced model training

## 4. MVP User Journey

1. User opens the Streamlit app
2. User reads a short explanation of CareerFit AI
3. User selects a sample job
4. User enters their current skills
5. User clicks a button to analyze fit
6. User sees:
   - Detected job skills
   - Matching skills
   - Missing skills
   - Basic recommendations
   - ATS checklist

## 5. MVP Inputs

Initial inputs:

- Sample job descriptions from `data/sample/sample_jobs.csv`
- Skill taxonomy from `skill_taxonomy/skills_v0.json`
- Manually entered user skills

## 6. MVP Outputs

Initial outputs:

- Skill match summary
- Missing skill list
- Learning priority list
- ATS checklist feedback

## 7. MVP Quality Requirements

The MVP should be:

- Easy to run locally
- Easy to understand
- Well documented
- Ethical by design
- Explainable
- Beginner-friendly
- Suitable for a GitHub portfolio
