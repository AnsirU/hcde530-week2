# Week 2 — Competency claim

Short notes on what this submission shows, by domain. (Adjust domain names to match your syllabus if your instructor uses different labels.)

## Working with structured data (CSV)

I can load a small survey export in CSV form using Python’s `csv` module, with UTF-8 encoding and `newline=""` so row boundaries stay correct. Each row is read as a dictionary keyed by column headers (`participant_id`, `role`, `response`), which keeps participant metadata tied to the free-text answer I analyze.

## Text as quantitative data (word counts & summaries)

I treat each open-ended response as a string and compute a simple length metric—word count via splitting on whitespace—so I can compare how much people wrote across roles. I also report descriptive summaries (count of responses, min, max, and mean word count) to characterize the dataset at a glance, alongside a truncated preview of each answer for context.

## Code organization & clarity (for others and future me)

I separated loading data, a small reusable `count_words` function, and printed output so the script reads in the order of the analysis story. Inline comments explain non-obvious choices (CSV options, why we collect `word_counts`, and what the summary lines mean) because my primary audience is human readers, not just the interpreter.
