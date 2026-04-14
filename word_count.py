import csv  # Built-in module for reading spreadsheet-style CSV files.


filename = "responses.csv"  # Data file in the same folder as this script.
responses = []  # Will hold one dict per survey row after we read the file.

# Read CSV: utf-8 + newline="" for csv; DictReader maps each row to a dict by header.
with open(filename, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)  # First row becomes the keys for each dict in `row`.
    for row in reader:
        responses.append(row)


def count_words(response):
    """Count the number of words in a response string.

    Takes a string, splits it on whitespace, and returns the word count.
    Used to measure response length across all participants.
    """
    return len(response.split())  # Default split() breaks on spaces/tabs/newlines.


# Count words in each response and print a row-by-row summary
# Column widths (<6, <22) keep the printed table aligned for quick scanning.
print(f"{'ID':<6} {'Role':<22} {'Words':<6} {'Response (first 60 chars)'}")
print("-" * 75)

word_counts = []  # Stores each row's count so we can compute min/max/average later.

# Each `row` is a dict from DictReader; keys match the CSV header row.
# participant_id / role: metadata columns; response: full text for counting + preview.
for row in responses:
    participant = row["participant_id"]
    role = row["role"]
    response = row["response"]

    count = count_words(response)  # Reuse one function for every row's text.
    word_counts.append(count)  # Build the list of lengths for the summary stats.

    # Truncate the response preview for display
    if len(response) > 60:
        preview = response[:60] + "..."
    else:
        preview = response

    print(f"{participant:<6} {role:<22} {count:<6} {preview}")

# Print summary statistics
print()
print("── Summary ─────────────────────────────────")
print(f"  Total responses : {len(word_counts)}")  # How many rows we processed.
print(f"  Shortest        : {min(word_counts)} words")  # Smallest word count in the set.
print(f"  Longest         : {max(word_counts)} words")  # Largest word count in the set.
# Mean length: sum of all counts divided by number of responses; :.1f = one decimal place.
print(f"  Average         : {sum(word_counts) / len(word_counts):.1f} words")
