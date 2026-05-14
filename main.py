from scraper import scrape_jobs
from filters import filter_jobs
from telegram_bot import send_telegram_message
import json

try:
    with open("seen_jobs.json", "r") as f:
        seen_jobs = json.load(f)
except:
    seen_jobs = []

jobs = scrape_jobs()
filtered = filter_jobs(jobs, seen_jobs)

if filtered:

    msg = "🎯 ELIGIBLE ALERTS\n\n"

    for i, job in enumerate(filtered[:10], 1):

        msg += (
            f"{i}. {job['title']}\n"
            f"📂 {job['category']}\n"
            f"🎓 {job['education']}\n"
            f"📅 Start: {job['form_start']}\n"
            f"⛔ End: {job['form_end']}\n"
            f"📝 Exam: {job['exam_date']}\n"
            f"💰 Fees: {job['fees']}\n"
            f"🏢 Posts: {job['posts']}\n"
            f"🌐 {job['source']}\n\n"
        )

    send_telegram_message(msg)

    for job in filtered:
        seen_jobs.append(job["title"])

    with open("seen_jobs.json", "w") as f:
        json.dump(seen_jobs, f, indent=2)

print("DONE")
