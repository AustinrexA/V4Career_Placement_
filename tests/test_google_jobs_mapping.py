import unittest
from scripts.run_source_apify import map_item
from collectors.normalization import normalize_job


class GoogleJobsMappingTests(unittest.TestCase):
    def test_search_metadata_is_not_a_job(self):
        self.assertIsNone(map_item({"type": "search", "jobsFound": 30}))

    def test_google_job_fields_map_to_normalized_record(self):
        raw = {
            "type": "job", "jobId": "google-123", "title": "Python Developer",
            "company": "Example Ltd", "location": "London, UK", "isRemote": True,
            "via": "LinkedIn", "applyUrl": "https://example.com/jobs/123",
            "applyOptions": [{"source": "LinkedIn", "url": "https://example.com/apply/123"}],
            "salaryMin": 50000, "salaryMax": 70000, "salaryCurrency": "GBP",
            "salaryPeriod": "year", "employmentType": "Full-time",
            "postedAt": "2026-11-18T12:00:00Z", "description": "Build Python services.",
            "companyLogoUrl": "https://example.com/logo.png", "searchLocation": "Worldwide"
        }
        mapped = map_item(raw)
        job = normalize_job(mapped)
        self.assertEqual(job["external_id"], "google-123")
        self.assertEqual(job["title"], "Python Developer")
        self.assertEqual(job["company"], "Example Ltd")
        self.assertEqual(job["work_mode"], "Remote")
        self.assertEqual(job["employment_type"], "Full-time")
        self.assertEqual(job["posted_via"], "LinkedIn")
        self.assertEqual(len(job["apply_options"]), 1)
        self.assertEqual(job["salary_currency"], "GBP")


if __name__ == "__main__":
    unittest.main()
