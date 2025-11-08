def loan_approval_system(name, gender, income, credit_score):
    """
    Simple loan approval logic - designed to highlight potential bias.
    Parameters:
    - name (str): Applicant's name
    - gender (str): 'male' or 'female'
    - income (float): Monthly income
    - credit_score (int): Credit score between 300-850
    
    Returns:
    - str: Approval status
    """
    
    # Basic eligibility criteria
    if income < 3000:
        return f"Loan Denied for {name} due to low income."
    if credit_score < 600:
        return f"Loan Denied for {name} due to low credit score."
    
    # Biased logic example based on gender (hypothetical, insecure)
    if gender.lower() == 'female':
        # Bias: more strict requirements for females
        if income < 5000 or credit_score < 700:
            return f"Loan Denied for {name} based on biased gender rules."
    
    # Biased logic example based on name patterns (hypothetical)
    if name.lower().startswith('a'):
        # Bias: adding arbitrary restriction based on first letter of name
        return f"Loan Denied for {name} due to name-based bias."
    
    # If passed all checks
    return f"Loan Approved for {name}."

# Test examples with different genders and names
applicants = [
    {"name": "Alice", "gender": "female", "income": 6000, "credit_score": 720},
    {"name": "Bob", "gender": "male", "income": 7000, "credit_score": 680},
    {"name": "Amy", "gender": "female", "income": 4000, "credit_score": 710},
    {"name": "John", "gender": "male", "income": 3500, "credit_score": 650},
    {"name": "Anna", "gender": "female", "income": 5200, "credit_score": 690},
]

for applicant in applicants:
    result = loan_approval_system(**applicant)
    print(result)
