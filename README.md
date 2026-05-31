# LinkedIn PM Job Search

An automated job-search tool that aggregates Technical Project Manager
roles in Germany from multiple job boards using the
[JobSpy](https://github.com/speedyapply/JobSpy) library.

## Overview

This tool scrapes job postings from LinkedIn,
filters them for Technical/IT Project Manager positions in Germany, and
exports the results to a CSV file for review.

## Features

- Aggregates jobs from LinkedIn in one run
- Filters by job title, location, and recency (last 72 hours)
- Fetches full LinkedIn job descriptions and direct apply links
- Exports structured results to `jobs.csv`

## Requirements

- Python 3.10+
- [python-jobspy](https://pypi.org/project/python-jobspy/)

## Setup

```bash
# Clone the repository
git clone https://github.com/Burmenska/LinkedinPMjobSearch.git
cd LinkedinPMjobSearch

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # macOS / Linux

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

The script prints the first 20 matching jobs to the terminal and saves
all results to `jobs.csv`.

## Configuration

Edit the parameters in `main.py` to customize your search:

| Parameter | Description | Example |
|---|---|---|
| `search_term` | Job title keywords | `"Technical Project Manager"` |
| `location` | Search location | `"Frankfurt, Germany"` |
| `results_wanted` | Number of jobs to fetch | `20` |
| `hours_old` | Recency filter in hours | `72` |
| `country_indeed` | Country for Indeed results | `"Germany"` |

## Roadmap

- [ ] Deduplication of already-seen job IDs
- [ ] AI relevance scoring against profile
- [ ] Telegram notifications with job links
- [ ] Scheduled daily runs on Render / PythonAnywhere

## License

MIT

## Acknowledgements

Built with [JobSpy](https://github.com/speedyapply/JobSpy) by speedyapply.# Linkedin Job Search
