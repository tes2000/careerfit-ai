
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[3]
SAMPLE_JOBS_PATH = PROJECT_ROOT / "data" / "sample" / "sample_jobs.csv"
SKILL_TAXONOMY_PATH = PROJECT_ROOT / "skill_taxonomy" / "skills_v0.json"


def load_sample_jobs() -> list[dict]:
    """Load sample jobs from the local CSV file."""
    jobs_df = pd.read_csv(SAMPLE_JOBS_PATH)
    return jobs_df.to_dict(orient="records")


def get_sample_job_by_id(job_id: int) -> dict | None:
    """Return one sample job by ID."""
    jobs = load_sample_jobs()

    for job in jobs:
        if int(job["job_id"]) == job_id:
            return job

    return None
