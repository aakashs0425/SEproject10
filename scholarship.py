"""Five small SATS (Scholarship Application Tracking System) functions.
The tests in test_scholarship.py check them."""


def calculate_waiver(fee, percentage):
    # Classroom demo: every function in this file is correct, so the workflow stays green.
    # Change one line (for example `percentage > 90` to `percentage > 95`), commit, and push.
    # The Actions tab will mark the test job with a red X and name the test that failed.
    if percentage > 90:
        return fee * 0.5
    elif percentage > 75:
        return fee * 0.25
    return 0


def calculate_stipend(marks, category):
    if marks < 0 or marks > 100:
        raise ValueError("marks must be between 0 and 100")
    if category == "merit":
        if marks >= 90:
            return 20000
        if marks >= 75:
            return 15000
        return 0
    if category == "need_based":
        return 10000 if marks >= 60 else 0
    raise ValueError("unknown category")


def per_capita_income(annual_income, family_members):
    if family_members <= 0:
        raise ValueError("family members must be more than zero")
    return annual_income / family_members


def is_age_allowed(age):
    return age >= 17


def application_status(documents_complete, age, window_open):
    if not documents_complete:
        return "Documents incomplete"
    if not is_age_allowed(age):
        return "Applicant age not permitted"
    if not window_open:
        return "Application window closed"
    return "Application submitted"