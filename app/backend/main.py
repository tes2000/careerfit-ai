from fastapi import FastAPI, HTTPException

from app.backend.schemas import (
    HealthResponse,
    JobSummary,
    ProjectInfo,
    SkillAnalysisRequest,
    SkillAnalysisResponse,
)
from app.backend.services.job_service import get_sample_job_by_id, load_sample_jobs


app = FastAPI(
    title="CareerFit AI API",
    description="Candidate-side job market intelligence and skill gap recommendation API.",
    version="0.1.0",
)


@app.get("/", response_model=ProjectInfo)
def get_project_info() -> ProjectInfo:
    """Return basic project information."""
    return ProjectInfo(
        name="CareerFit AI",
        mission=(
            "Help international graduates and early-career professionals in Germany "
            "understand job requirements, identify skill gaps, and improve their career readiness."
        ),
        target_users=[
            "International graduates in Germany",
            "Early-career data professionals",
            "Career switchers entering data and AI roles",
        ],
        target_roles=[
            "Data Analyst",
            "Data Scientist",
            "Machine Learning Engineer",
            "Applied AI Engineer",
            "Data Engineer",
            "MLOps Engineer",
            "GenAI Engineer",
        ],
    )


@app.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Return API health status."""
    return HealthResponse(
        status="ok",
        project="CareerFit AI",
        version="0.1.0",
    )


@app.get("/jobs/sample", response_model=list[JobSummary])
def get_sample_jobs() -> list[JobSummary]:
    """Return all sample jobs."""
    jobs = load_sample_jobs()
    return [JobSummary(**job) for job in jobs]


@app.get("/jobs/sample/{job_id}", response_model=JobSummary)
def get_sample_job(job_id: int) -> JobSummary:
    """Return one sample job by ID."""
    job = get_sample_job_by_id(job_id)

    if job is None:
        raise HTTPException(status_code=404, detail="Sample job not found")

    return JobSummary(**job)


@app.post("/analyze/skills", response_model=SkillAnalysisResponse)
def analyze_skills(request: SkillAnalysisRequest) -> SkillAnalysisResponse:
    """
    Placeholder skill analysis endpoint.

    Day 1 intentionally keeps this simple.
    Real skill extraction logic will be implemented in a later phase.
    """
    candidate_skills_normalized = {
        skill.strip().lower() for skill in request.candidate_skills
    }

    simple_keywords = [
        "python",
        "sql",
        "excel",
        "pandas",
        "scikit-learn",
        "statistics",
        "docker",
        "mlflow",
        "airflow",
        "spark",
        "power bi",
        "tableau",
        "large language models",
        "prompt engineering",
    ]

    job_description_lower = request.job_description.lower()

    detected_job_skills = [
        skill for skill in simple_keywords if skill in job_description_lower
    ]

    matched_skills = [
        skill for skill in detected_job_skills if skill in candidate_skills_normalized
    ]

    missing_skills = [
        skill for skill in detected_job_skills if skill not in candidate_skills_normalized
    ]

    return SkillAnalysisResponse(
        detected_job_skills=detected_job_skills,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        note=(
            "This is a simple Day 1 placeholder analysis. "
            "A taxonomy-based explainable matcher will be added later."
        ),
    )
