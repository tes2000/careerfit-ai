
from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    project: str
    version: str


class ProjectInfo(BaseModel):
    name: str
    mission: str
    target_users: list[str]
    target_roles: list[str]


class JobSummary(BaseModel):
    job_id: int
    title: str
    company_type: str
    location: str
    seniority: str
    description: str


class SkillAnalysisRequest(BaseModel):
    job_description: str
    candidate_skills: list[str]


class SkillAnalysisResponse(BaseModel):
    detected_job_skills: list[str]
    matched_skills: list[str]
    missing_skills: list[str]
    note: str
