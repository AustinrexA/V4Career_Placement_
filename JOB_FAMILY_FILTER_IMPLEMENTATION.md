# V4Career Job Family + Job Title filters

## What changed

The Job Portal filter toolbar now has two independent, dependent inputs:

1. **Job Family** – searchable major category list with live matching-job counts.
2. **Job Title** – disabled until a family is selected; then shows only original titles in that family, with live counts and an **All jobs in this family** option.

The existing Company, Location, Experience, Salary, Posted After, source selection, pagination, and Excel export controls remain in place.

## Database behaviour

The existing `jobs` table is not renamed or modified. A separate `job_title_family_map` lookup table is created automatically on first use:

- `title_hash` – indexed MD5 key for the exact trimmed title
- `original_title` – original title text, preserved for reference
- `job_family`
- `updated_at`

The included `data/job_family_mapping.json` contains the initial classification of the 15,374 distinct titles from the supplied Neon export. The application synchronizes the titles actually present in Neon into the lookup table. The hash key keeps the join index compact even when scraped titles are long. Newly scraped titles are classified by fallback keyword rules and checked during the periodic mapping sync. Titles that cannot be confidently classified are placed in **Other & Needs Review** rather than silently dropped.

If you prefer to create the table manually before deploying, run `sql/job_title_family_map.sql` in Neon SQL Editor. The application will populate it when the filters load.

## Faceted filter behaviour

- Job Family counts respect the currently selected company, location, experience, salary, posted date, status, skills, and source filters. The family and specific-title selections are excluded from the family facet itself.
- Job Title options are constrained by the selected family and the other active filters. The title selection is excluded from its own facet so the full list remains available.
- Company, Location, Experience, Salary, and Status options are refreshed using the other selected filters while excluding their own current selection.
- Changing Job Family clears the previous Job Title selection.
- Selecting **All jobs in this family** applies the family only and leaves the specific-title filter empty.
- `/api/jobs` and `/api/jobs/export` both apply `job_family` and exact `role` (job title) parameters, so table results and exports stay consistent.

## API query parameters

- `job_family`: selected family label
- `role`: exact original job title
- Existing filter parameters continue to work as before.

## Deployment notes

1. Keep your existing local `.env` file and database credentials; the updated source archive intentionally does not include `.env`.
2. Replace the application source files with the updated files from this archive.
3. Ensure the `data/job_family_mapping.json` file is included in the deployed project.
4. Deploy normally. The lookup table is created and populated when the filter endpoints are first requested.
5. Verify Job Family, Job Title, Company, Location, Experience, Salary, Status, Search, Clear, Refresh, and Export.

The mapping is an initial title-based classification. Review **Other & Needs Review** and ambiguous titles periodically; the original job titles and job records remain unchanged.
