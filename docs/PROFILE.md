# Profile maintenance

The README is native Markdown and GitHub-compatible HTML. Its biography, projects, technology links and social links are real selectable text and anchors. Only the original portrait, decorative terminal header and generated contribution chart are images. India has been removed.

`scripts/refresh_profile.py` uses Python's standard library and GitHub's APIs to update the marked README activity section, contribution SVG and machine-readable activity data. It fetches public non-fork repositories and their language byte counts. Contribution levels come from GitHub GraphQL, with the public contribution calendar as a fallback. Failed fetches or incomplete calendars do not replace the last successful output.

`.github/workflows/refresh-profile.yml` runs daily at 00:17 UTC (05:47 India time), when its source files change on main, and through Run workflow in Actions. It uses GitHub's automatic token; no personal access token or paid service is required. Workflow write permissions or branch rules may block commits. Inspect the workflow run if the visible timestamp stops advancing. GitHub may delay scheduled runs and may disable schedules in inactive public repositories after 60 days; re-enable the workflow in Actions if necessary.

To refresh locally:

```sh
python3 scripts/refresh_profile.py
```

An optional `GH_TOKEN` environment variable enables authenticated API limits and GraphQL. Never commit a token. The default anonymous mode uses public APIs and the public contribution calendar.

The heatmap is refreshed data, not a live browser widget. GitHub's contribution rules and processing delays still apply. GitHub sanitizes README HTML and does not execute embedded JavaScript or custom styles; the page adopts the reader's GitHub theme. The earlier full-dashboard PNG assets remain historical files, but README no longer displays them. Updating the old dashboard scripts does not update the native README.
