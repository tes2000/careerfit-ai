
import requests
import streamlit as st


API_BASE_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="CareerFit AI",
    page_icon="🎯",
    layout="wide",
)


st.title("🎯 CareerFit AI")
st.subheader("Job market intelligence and skill gap guidance for early-career data professionals")

st.markdown(
    """
CareerFit AI helps international graduates and early-career professionals in Germany understand
job requirements, identify skill gaps, and improve their career readiness.

This Day 1 prototype is intentionally simple. It uses sample job data and a basic backend API.
"""
)


st.info(
    "CareerFit AI is a candidate self-improvement tool. "
    "It is not an employer-side screening or rejection system."
)


with st.sidebar:
    st.header("Navigation")
    page = st.radio(
        "Choose a section",
        [
            "Project Overview",
            "Sample Jobs",
            "Skill Gap Demo",
            "ATS Checklist",
        ],
    )


def check_backend_health() -> dict | None:
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None


backend_status = check_backend_health()

if backend_status:
    st.success(f"Backend connected: {backend_status['project']} v{backend_status['version']}")
else:
    st.warning(
        "Backend is not connected. Start it with: fastapi dev app/backend/main.py"
    )


if page == "Project Overview":
    st.header("Project Overview")

    st.markdown(
        """
### Mission

Help international graduates and early-career professionals in Germany understand job requirements,
identify skill gaps, and receive explainable learning recommendations.

### Target roles

- Data Analyst
- Data Scientist
- Machine Learning Engineer
- Applied AI Engineer
- Data Engineer
- MLOps Engineer
- GenAI Engineer

### Day 1 status

- Project documentation created
- Sample data created
- Skill taxonomy created
- FastAPI backend skeleton created
- Streamlit frontend skeleton created
"""
    )


elif page == "Sample Jobs":
    st.header("Sample Jobs")

    if not backend_status:
        st.stop()

    try:
        response = requests.get(f"{API_BASE_URL}/jobs/sample", timeout=5)
        response.raise_for_status()
        jobs = response.json()

        for job in jobs:
            with st.expander(f"{job['title']} — {job['location']}"):
                st.write(f"**Company type:** {job['company_type']}")
                st.write(f"**Seniority:** {job['seniority']}")
                st.write(job["description"])

    except requests.RequestException as error:
        st.error(f"Could not load sample jobs: {error}")


elif page == "Skill Gap Demo":
    st.header("Skill Gap Demo")

    st.markdown(
        """
This is a basic Day 1 demo. Later, this will use the full skill taxonomy and better matching logic.
"""
    )

    job_description = st.text_area(
        "Paste a job description",
        height=180,
        value=(
            "We are looking for a Junior Data Scientist with Python, Pandas, "
            "Scikit-learn, statistics, regression, classification, and communication skills."
        ),
    )

    candidate_skills_text = st.text_input(
        "Enter your current skills separated by commas",
        value="Python, SQL, Pandas, Excel",
    )

    candidate_skills = [
        skill.strip()
        for skill in candidate_skills_text.split(",")
        if skill.strip()
    ]

    if st.button("Analyze skill fit"):
        if not backend_status:
            st.error("Please start the backend first.")
            st.stop()

        payload = {
            "job_description": job_description,
            "candidate_skills": candidate_skills,
        }

        try:
            response = requests.post(
                f"{API_BASE_URL}/analyze/skills",
                json=payload,
                timeout=10,
            )
            response.raise_for_status()
            result = response.json()

            col1, col2, col3 = st.columns(3)

            with col1:
                st.subheader("Detected job skills")
                st.write(result["detected_job_skills"])

            with col2:
                st.subheader("Matched skills")
                st.write(result["matched_skills"])

            with col3:
                st.subheader("Missing skills")
                st.write(result["missing_skills"])

            st.caption(result["note"])

        except requests.RequestException as error:
            st.error(f"Skill analysis failed: {error}")


elif page == "ATS Checklist":
    st.header("Basic ATS-Friendliness Checklist")

    st.markdown(
        """
Use this checklist to make a CV easier to read by both humans and applicant tracking systems.

This is general guidance, not a guarantee for any specific ATS.
"""
    )

    checklist_items = {
        "Clear section headings": st.checkbox("Uses clear headings like Education, Experience, Projects, Skills"),
        "Simple formatting": st.checkbox("Avoids complex tables, graphics, icons, and text boxes"),
        "Relevant keywords": st.checkbox("Includes relevant skills from the job description naturally"),
        "Consistent dates": st.checkbox("Uses consistent date formats"),
        "Measurable impact": st.checkbox("Includes project outcomes, metrics, or results where possible"),
        "Readable file": st.checkbox("Uses a standard PDF or DOCX format"),
    }

    completed = sum(checklist_items.values())
    total = len(checklist_items)

    st.metric("Checklist progress", f"{completed}/{total}")

    if completed == total:
        st.success("Great start. Your CV appears structurally ATS-friendly based on this checklist.")
    elif completed >= 4:
        st.info("Good progress. Review the remaining items before applying.")
    else:
        st.warning("Your CV may need formatting improvements before applications.")
