import re

def parse_job(text, source):

    text_clean = " ".join(text.split())

    # default structure
    job = {
        "title": text_clean[:120],
        "category": "Unknown",
        "education": "Not found",
        "form_start": "Not found",
        "form_end": "Not found",
        "exam_date": "Not found",
        "fees": "Not found",
        "posts": "Not found",
        "correction_window": "Not found",
        "source": source
    }

    # CATEGORY detection
    if any(k in text.lower() for k in ["scholarship", "scholar"]):
        job["category"] = "Scholarship"
    elif any(k in text.lower() for k in ["admission", "btech", "engineering"]):
        job["category"] = "Admission"
    elif any(k in text.lower() for k in ["recruitment", "vacancy", "ssc", "railway"]):
        job["category"] = "Gov Exam"

    # DATE patterns (very basic MVP)
    dates = re.findall(r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}', text)

    if len(dates) >= 1:
        job["form_start"] = dates[0]
    if len(dates) >= 2:
        job["form_end"] = dates[1]
    if len(dates) >= 3:
        job["exam_date"] = dates[2]

    # FEES
    fee = re.search(r'₹\s?\d+|\b\d+\s?rupees\b', text.lower())
    if fee:
        job["fees"] = fee.group()

    # POSTS
    posts = re.search(r'\d+\s*(posts|vacancies|vacancy)', text.lower())
    if posts:
        job["posts"] = posts.group()

    # EDUCATION
    if "10th" in text.lower():
        job["education"] = "10th Pass"
    elif "12th" in text.lower():
        job["education"] = "12th Pass"

    return job
