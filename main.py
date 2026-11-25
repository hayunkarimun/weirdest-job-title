"""Weirdest Job Title: Blind Judge Showdown.

Scores a shortlist of job titles against the judge's five criteria
(real-sounding structure, stranger than ordinary work, twist lands on
the first read, specific enough to picture, reads instantly) and writes
the winner to /output/entry.txt. Gate: 1-60 UTF-8 characters, one line.
"""

CANDIDATES = [
    # (title, real_job, weirdness, first_read_laugh, picturable, instant)
    ("Left Sock Recovery Specialist, Laundromat Division", 5, 5, 5, 5, 4),
    ("Chief Sock Pairing Officer, Laundromat Division", 5, 4, 4, 5, 5),
    ("Senior Penguin Relocation Coordinator for Lost Socks", 4, 5, 4, 4, 3),
    ("Professional Queue Stander for Other People's Errands", 4, 4, 4, 5, 3),
    ("Director of Apologies, Department of Lost Luggage", 5, 3, 4, 4, 4),
    ("Official Taster of Leftovers, Royal Household", 4, 4, 3, 4, 4),
    ("Cloud Shape Naming Consultant, First Shift", 4, 3, 3, 3, 4),
    ("Senior Vice President of Forgetting Birthdays", 5, 3, 3, 3, 4),
    ("Underwater Basket Weaving Instructor (Advanced)", 3, 3, 3, 3, 3),
    ("Moonlight Shadow Length Measurer", 3, 4, 2, 3, 4),
]

WEIGHTS = (3, 3, 2, 2, 1)  # judge's criteria, most important first


def score(candidate):
    title, real_job, weirdness, laugh, picturable, instant = candidate
    parts = (real_job, weirdness, laugh, picturable, instant)
    return sum(w * p for w, p in zip(WEIGHTS, parts))


def pick():
    best = max(CANDIDATES, key=score)
    return best[0]


def validate(title):
    """Gate: /output/entry.txt must be 1-60 UTF-8 chars, one line, not blank."""
    assert isinstance(title, str) and title.strip(), "title must not be blank"
    assert "\n" not in title and "\r" not in title, "title must be a single line"
    assert 1 <= len(title.encode("utf-8")) <= 60, "title must be 1-60 chars"
    return title


def main():
    title = validate(pick())
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(title)
    print(f"wrote {len(title)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
