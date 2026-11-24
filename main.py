"""Write the one-line pitch to /output/entry.txt.

The entry is a single sentence aimed at a friend who has never coded:
it tells them the hard part (the idea) is already done, and that an AI
agent can turn plain words into a real, working app they can try
tonight, for free, and change anything they do not like.
"""

import os

SENTENCE = (
    "You've already done the hard part \u2014 the idea \u2014 so just describe it "
    "in plain words and an AI agent will build you a real, working app "
    "you can try tonight, free, and change anything you don't like."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
