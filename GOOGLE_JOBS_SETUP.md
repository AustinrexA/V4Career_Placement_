# V4Career – Google Jobs integration (phase 1)

## What changed

- Replaced the old portal catalog with the 15 portals selected for V4Career.
- Registered Google Jobs as the first collector. The other 14 portals are visible in the existing UI but intentionally remain unconfigured until their Actors are tested individually.
- Added Google Jobs dataset mapping. Search-summary rows (`type: search`) are ignored; job rows (`type: job`) are normalized.
- Preserved the Google Jobs job ID, apply URL, alternative apply options, board attribution (`via`), company logo, location, remote flag, employment type, salary, posting date and raw metadata.
- Removed the runner's India-only location validation. Collection can now use worldwide or specific locations.
- Added a PostgreSQL migration for the additional Google Jobs fields.
- Kept the existing job list and job-details modal/apply-link flow unchanged.

## 1. Run the Neon migration first

In Neon SQL Editor, select branch `production` and database `v4career_jobs`. Execute the complete file:

`database/migrations/002_google_jobs_fields.sql`

This is an additive migration. It does not drop tables or delete job data.

## 2. Add Google Jobs settings to your local `.env`

Keep your existing Neon database settings. Add these lines (do not replace your database credentials):

```dotenv
APIFY_ACTOR_GOOGLE_JOBS=vncntlabs~google-jobs-scraper
APIFY_ACCESS_APPROVED_GOOGLE_JOBS=true
APIFY_INPUT_GOOGLE_JOBS={"queries":["Software Engineer","Python Developer","Java Developer"],"locations":["Worldwide"],"maxJobsPerSearch":30,"includeDescription":true}
```

Keep your existing `APIFY_API_TOKEN` in `.env`. Never commit `.env` or share the token.

The `Worldwide` input should be confirmed in a small test run in the Actor's input page before increasing the collection limit. If this Actor's input validation rejects `Worldwide`, use the Actor's supported country/location values in `locations` (for example, a list of countries) rather than changing the application code.

## 3. Run Google Jobs collection

From the project root, with the virtual environment activated:

```powershell
python scripts/run_source_apify.py --source "Google Jobs" --keyword "Software Engineer" --location "Worldwide" --max-results 30
```

The JSON in `APIFY_INPUT_GOOGLE_JOBS` takes precedence over the CLI keyword/location values. The runner saves only actual job records; search metadata records are skipped.

## 4. Verify saved records in Neon

Run this query in Neon SQL Editor:

```sql
SELECT s.name AS portal, j.title, j.company, j.location,
       j.work_mode, j.employment_type, j.posted_via, j.job_url
FROM jobs j
JOIN sources s ON s.id = j.source_id
WHERE s.name = 'Google Jobs'
ORDER BY j.created_at DESC
LIMIT 20;
```

## Notes

- All 15 portal names are now present in the existing sidebar catalog. Only Google Jobs is configured in this phase. The remaining Actors must not be marked enabled until individually tested.
- The existing UI columns remain Job Title, Company, Location, Experience, Salary, Posted After and Job Link. Clicking a job title continues to open the existing full-details modal; the modal's apply link opens the original application page.
- Google Jobs `via` is stored separately as `posted_via`; the portal/source remains `Google Jobs`.
- Jobs without salary remain valid and display as undisclosed. A missing company URL does not block a job.
- The uploaded sample dataset was locally checked: 91 dataset rows contained 3 search-summary rows and 88 valid job rows; all 88 normalized successfully.
