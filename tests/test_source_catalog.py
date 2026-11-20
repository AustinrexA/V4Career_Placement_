import unittest
from urllib.parse import urlparse
from collectors.source_catalog import JOB_PORTALS, PORTAL_BY_KEY, UI_PORTAL_KEYS, DEFAULT_APIFY_ACTORS


class SourceCatalogTests(unittest.TestCase):
    def test_catalog_contains_the_15_selected_portals_with_unique_keys(self):
        expected = {
            "Google Jobs", "iimjobs", "Jobrapido", "Apna", "Remote OK",
            "We Work Remotely", "Remotive", "Himalayas", "Jobicy",
            "Working Nomads", "Arbeitnow", "Get on Board",
            "Y Combinator – Work at a Startup", "Dice", "Built In",
        }
        self.assertEqual(len(JOB_PORTALS), 15)
        self.assertEqual({portal["name"] for portal in JOB_PORTALS}, expected)
        self.assertEqual(len({portal["key"] for portal in JOB_PORTALS}), 15)
        self.assertEqual(UI_PORTAL_KEYS, {portal["key"] for portal in JOB_PORTALS})

    def test_all_portals_have_valid_https_homepages(self):
        for portal in JOB_PORTALS:
            with self.subTest(portal=portal["name"]):
                parsed = urlparse(portal["base_url"])
                self.assertEqual(parsed.scheme, "https")
                self.assertTrue(parsed.netloc)
                self.assertIn(portal["key"].lower(), PORTAL_BY_KEY)

    def test_only_google_actor_is_enabled_as_a_tested_candidate(self):
        self.assertEqual(DEFAULT_APIFY_ACTORS["GOOGLE_JOBS"], "vncntlabs~google-jobs-scraper")
        self.assertEqual(set(DEFAULT_APIFY_ACTORS), {"GOOGLE_JOBS"})


if __name__ == "__main__":
    unittest.main()
