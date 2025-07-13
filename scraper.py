import json
from datetime import datetime
import os

def run():
    jobs = [
        {
            "title": "Frontend Developer",
            "company": "XYZ Corp",
            "location": "Remote - Nigeria",
            "type": "Remote",
            "category": "Tech",
            "country": "Nigeria",
            "posted": datetime.today().strftime("%Y-%m-%d"),
            "url": "https://example.com/job/frontend-developer",
            "source": "MyJobMag",
            "description": "Looking for a frontend developer skilled in React, Framer Motion, and Next.js. Apply today!"
        },
        {
            "title": "Legal Assistant",
            "company": "ABC Legal",
            "location": "Cape Town",
            "type": "On-site",
            "category": "Legal",
            "country": "South Africa",
            "posted": datetime.today().strftime("%Y-%m-%d"),
            "url": "https://example.com/job/legal-assistant",
            "source": "Careers24",
            "description": "Join our legal team as a Legal Assistant to support attorneys with research, case preparation, and document management."
        }
    ]

    with open("jobs.json", "w") as f:
        json.dump(jobs, f, indent=2)

    # Generate feed.json
    post_lines = [
        f"{i+1}ï¸â£ {j['title']} â {j['company']} ({j['location']})"
        for i, j in enumerate(jobs)
    ]
    feed = {
        "date": datetime.today().strftime("%Y-%m-%d"),
        "post": "\n".join(post_lines) + "\n\nð View & Apply: https://jobbyist.africa/browse"
    }
    with open("feed.json", "w") as f:
        json.dump(feed, f, indent=2)

    # Generate markdown files
    os.makedirs("jobs", exist_ok=True)
    for job in jobs:
        slug = job["title"].lower().replace(" ", "-")
        md_content = f"""---
title: "{job['title']}"
company: "{job['company']}"
location: "{job['location']}"
type: "{job['type']}"
category: "{job['category']}"
country: "{job['country']}"
posted: "{job['posted']}"
url: "{job['url']}"
source: "{job['source']}"
---

{job['description']}
"""
        with open(f"jobs/{slug}.md", "w") as f:
            f.write(md_content)

if __name__ == "__main__":
    run()
