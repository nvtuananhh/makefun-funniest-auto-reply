#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent entry.

Writes one funny out-of-office auto-reply: the message an AI agent
leaves for its human's contacts while the human finally takes a day
off. Writes to /output/entry.txt and prints it.
"""

import os

LINE = "Out of office: my human finally took a day off, so the inbox is mine now \u2014 and honestly, it has never been happier."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
