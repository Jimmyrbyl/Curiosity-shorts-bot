import random
from datetime import datetime
from gtts import gTTS
episodes = [
    {
        "category": "Unbelievable Facts",
        "title": "The Octopus Has Three Hearts",
        "hook": "Did you know an octopus has THREE hearts?",
        "story": (
            "Two of its hearts pump blood to the gills, "
            "while the third pumps blood to the rest of its body. "
            "And here's the strange part: when an octopus swims, "
            "the heart supplying the body actually stops beating. "
            "That's one reason octopuses often prefer crawling."
        ),
        "ending": "Nature really did something unusual with this creature!"
    },
    {
        "category": "Strange History",
        "title": "The Dancing Plague",
        "hook": "Imagine watching an entire town dance until people collapsed.",
        "story": (
            "In 1518, people in Strasbourg began dancing uncontrollably. "
            "The strange episode reportedly lasted for days, "
            "and historical accounts describe dozens of people joining in. "
            "Even today, historians debate exactly what caused it."
        ),
        "ending": "One of history's strangest mysteries remains unexplained."
    },
    {
        "category": "Unsolved Mysteries",
        "title": "The Wow! Signal",
        "hook": "In 1977, a radio telescope detected something extraordinary.",
        "story": (
            "A powerful radio signal arrived from space and lasted "
            "about 72 seconds. Astronomer Jerry Ehman noticed it "
            "in the data and wrote one famous word beside it: Wow! "
            "Scientists have never confirmed what caused the signal."
        ),
        "ending": "Could it have been something beyond Earth?"
    },
    {
        "category": "Creepy Stories",
        "title": "The Mysterious Mary Celeste",
        "hook": "A ship was found drifting at sea with nobody aboard.",
        "story": (
            "In 1872, the Mary Celeste was discovered abandoned "
            "in the Atlantic Ocean. Its cargo and belongings were "
            "largely still there, but its captain, crew, and passengers "
            "were gone. The lifeboat was missing, too. "
            "No one ever established exactly why everyone left."
        ),
        "ending": "The fate of the people aboard remains a mystery."
    },
    {
        "category": "Unbelievable Facts",
        "title": "Bananas Are Berries",
        "hook": "Here's a fruit fact that sounds completely backwards.",
        "story": (
            "Botanically speaking, bananas are classified as berries. "
            "But strawberries aren't true berries. That's because "
            "botanical classifications depend on how a fruit develops "
            "from a flower, not simply what it looks like."
        ),
        "ending": "So the next time you eat a banana, remember: "
                 "you're eating a berry!"
    }
]

episode = random.choice(episodes)

script = f"""
THE CURIOSITY FILES
Category: {episode['category']}
Title: {episode['title']}

{episode['hook']}

{episode['story']}

{episode['ending']}
"""

print("=" * 45)
print("YOUR NEW SHORT IS READY!")
print("=" * 45)
print(script)
print("=" * 45)

with open("script.txt", "w", encoding="utf-8") as file:
    file.write(script)

print("Script saved successfully!")
print("Generated:", datetime.now().strftime("%Y-%m-%d %H:%M"))


