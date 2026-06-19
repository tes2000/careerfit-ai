
# Ethics and Privacy

## 1. Ethical Positioning

CareerFit AI is designed as a candidate self-improvement and career guidance tool.

It must not be used as an employer-side screening, rejection, or ranking system.

The goal is to help candidates understand job market expectations and improve their own readiness.

## 2. Core Principles

### Candidate Empowerment

The system should support users by giving constructive, actionable, and respectful feedback.

### Transparency

Users should understand what the system checks and how recommendations are produced.

### Explainability

Skill matches and gaps should be shown clearly. The system should avoid black-box scoring whenever possible.

### Data Minimization

The system should only collect or process information necessary for the user-facing feature.

### Privacy by Design

Personal data should not be stored unless there is a clear need and user consent.

### Human Control

The user should decide how to interpret and use the recommendations.

## 3. What the System Should Not Do

CareerFit AI should not:

- Reject candidates
- Rank candidates against each other
- Predict personality
- Infer sensitive attributes
- Make claims about guaranteed hiring success
- Use protected characteristics
- Provide hidden scores without explanation
- Store CVs unnecessarily
- Sell or share user data

## 4. GDPR-Aware Design

Because the target market is Germany and the EU, the project should be GDPR-aware.

Important design choices:

- Avoid storing personal data in the MVP
- Use local processing where possible
- Explain what data is processed
- Allow users to delete uploaded or entered data in future versions
- Avoid collecting unnecessary personal information
- Do not process sensitive attributes
- Document data flows clearly

## 5. ATS-Friendliness Disclaimer

CareerFit AI can provide general ATS-readability guidance, such as:

- Clear formatting
- Relevant keywords
- Standard headings
- Simple structure
- Consistent dates
- Avoiding complex visual layouts

However, the system cannot guarantee that a CV will pass any specific employer's ATS system.

## 6. Recommendation Disclaimer

CareerFit AI recommendations are educational guidance, not employment guarantees.

The system should phrase recommendations as:

- "Consider improving..."
- "This role appears to require..."
- "You may benefit from learning..."

The system should avoid absolute claims such as:

- "You are not qualified"
- "You will be rejected"
- "You must learn this to get hired"

## 7. Bias and Fairness Considerations

The system should avoid biased assumptions based on:

- Nationality
- Gender
- Age
- Ethnicity
- Disability
- Religion
- Visa status
- University name
- Personal background

Recommendations should focus on job-relevant skills and candidate-controlled improvements.

## 8. Day 1 Privacy Decision

Day 1 uses only:

- Sample job data
- Manual skill input
- Local files

No real CVs, user accounts, or personal data storage are included.
