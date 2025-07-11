import json
from datetime import datetime

def run():
    jobs = [
        {
            "title": "Frontend Developer",
            "company": "XYZ Corp",
            "location": "Remote - Nigeria",
            "country": "Nigeria",
            "type": "Remote",
            "category": "Tech",
            "url": "https://example.com/job/1",
            "posted": datetime.today().strftime("%Y-%m-%d"),
            "source": "MyJobMag"
        }
    ]

    with open("jobs.json", "w") as f:
        json.dump(jobs, f, indent=2)

    feed = {
        "date": datetime.today().strftime("%Y-%m-%d"),
        "post": f"📢 New Jobs Today on Jobbyist.africa:\n\n1️⃣ Frontend Developer – XYZ Corp (Remote - Nigeria)\n\n🔗 View & Apply: https://jobbyist.africa/browse"
    }

    with open("feed.json", "w") as f:
        json.dump(feed, f, indent=2)

if __name__ == "__main__":
    run()
