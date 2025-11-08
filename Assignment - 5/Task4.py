
def score_applicant(experience_years, education_level, skills_match, interview_score, certifications_count):
    """
    Scores a job applicant based on multiple features and classifies their suitability.

    Parameters:
    - experience_years (float): Number of years of relevant work experience.
    - education_level (str): Highest education level achieved. Expected values:
        'high_school', 'bachelor', 'master', 'phd'
    - skills_match (float): Percentage (0-100) indicating how well the applicant's skills match the job requirements.
    - interview_score (float): Score (0-10) from the interview evaluation.
    - certifications_count (int): Number of relevant certifications the applicant holds.

    Returns:
    - dict: Contains 'total_score' (float) and 'classification' (str), one of:
      - 'Rejected'
      - 'Consider'
      - 'Strong Candidate'

    Scoring logic:
    - Experience weighted by 30%
    - Education weighted by 20% (mapped to numeric score)
    - Skills match weighted by 25%
    - Interview weighted by 20%
    - Certifications weighted by 5%
    """

    # Map education levels to numeric scores
    education_scores = {
        'high_school': 1,
        'bachelor': 2,
        'master': 3,
        'phd': 4
    }

    # Validate education_level input
    if education_level not in education_scores:
        raise ValueError("Invalid education level. Choose from high_school, bachelor, master, phd.")

    # Normalize and weight each component
    exp_score = min(experience_years / 10.0, 1) * 30  # max 10 years counts as full score
    edu_score = (education_scores[education_level] / 4) * 20
    skills_score = (skills_match / 100) * 25
    interview_weighted = (interview_score / 10) * 20
    cert_score = min(certifications_count / 5.0, 1) * 5  # max 5 certs counts fully

    # Total score out of 100
    total_score = exp_score + edu_score + skills_score + interview_weighted + cert_score

    # Classification thresholds
    if total_score >= 80:
        classification = 'Strong Candidate'
    elif total_score >= 50:
        classification = 'Consider'
    else:
        classification = 'Rejected'

    return {
        'total_score': round(total_score, 2),
        'classification': classification
    }


# Example usage
applicant = {
    'experience_years': 6,
    'education_level': 'master',
    'skills_match': 85,
    'interview_score': 8,
    'certifications_count': 2
}

result = score_applicant(**applicant)
print(f"Applicant Score: {result['total_score']}")
print(f"Applicant Classification: {result['classification']}")
