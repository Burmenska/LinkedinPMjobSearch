import csv
from jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["linkedin"],
    search_term="Project Manager",
    google_search_term="Technical Project Manager jobs in Germany since yesterday",
    location="Germany",
    results_wanted=20,
    hours_old=72,
    country_indeed="Germany",
    linkedin_fetch_description=True,
)

print(f"Found {len(jobs)} jobs")
print(jobs[["title", "company", "location", "job_url"]].head(20))
jobs.to_csv("jobs.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)