from rapidfuzz import fuzz

def filter_jobs(jobs, seen_jobs):

    filtered = []

    for job in jobs:

        # eligibility filter
        if not any(x in job["education"] for x in ["10th", "12th", "Not found"]):
            continue

        # duplicates inside current batch
        duplicate = False

        for existing in filtered:

            if fuzz.ratio(job["title"], existing["title"]) > 85:
                duplicate = True
                break

        if duplicate:
            continue

        # already sent check
        if job["title"] in seen_jobs:
            continue

        filtered.append(job)

    return filtered
