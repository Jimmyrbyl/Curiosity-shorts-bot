import random
from datetime import datetime
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip
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
speech_text = (
    episode["hook"] + " " +
    episode["story"] + " " +
    episode["ending"]
)

tts = gTTS(text=speech_text, lang="en")
tts.save("narration.mp3")
print("Audio narration saved successfully!")
# Create a vertical background for YouTube Shorts
width, height = 1080, 1920
background = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(background)

# Dark blue gradient background
for y in range(height):
    shade = int(12 + (y / height) * 25)
    draw.line((0, y, width, y), fill=(shade, shade, shade + 35))

# Add episode title
try:
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    title_font = ImageFont.truetype(font_path, 76)
    small_font = ImageFont.truetype(font_path, 38)
except:
    title_font = ImageFont.load_default()
    small_font = ImageFont.load_default()

draw.text((80, 550), "THE CURIOSITY FILES",
          font=small_font, fill="white")

draw.text((80, 700), episode["title"],
          font=title_font, fill=(255, 210, 90))

draw.text((80, 950), episode["category"],
          font=small_font, fill="white")

draw.text((80, 1450), "A STORY WORTH KNOWING",
          font=small_font, fill=(180, 200, 230))

background.save("background.png")


# Combine background, narration, and synchronized captions
audio = AudioFileClip("narration.mp3")

video = ImageClip("background.png").set_duration(audio.duration)

video = video.resize(
    lambda t: 1 + 0.05 * t / audio.duration
).crop(
    x_center=width / 2,
    y_center=height / 2,
    width=width,
    height=height
)

# Split narration into caption groups
words = speech_text.split()
caption_groups = [
    words[i:i + 4] for i in range(0, len(words), 4)
]

# Estimate caption timing based on spoken text length
weights = [sum(len(word) for word in group) for group in caption_groups]
total_weight = sum(weights)

caption_clips = []
current_time = 0

for group, weight in zip(caption_groups, weights):
    duration = audio.duration * weight / total_weight

    caption_image = Image.new(
        "RGBA", (1080, 220), (0, 0, 0, 0)
    )
    caption_draw = ImageDraw.Draw(caption_image)

    caption_text = " ".join(group)

    caption_draw.rounded_rectangle(
        (50, 20, 1030, 190),
        radius=30,
        fill=(0, 0, 0, 210)
    )

    bbox = caption_draw.textbbox(
        (0, 0), caption_text, font=small_font
    )

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    caption_draw.text(
        ((1080 - text_width) / 2,
         (220 - text_height) / 2 - bbox[1]),
        caption_text,
        font=small_font,
        fill=(255, 220, 90),
        stroke_width=2,
        stroke_fill=(0, 0, 0)
    )

    caption_clip = (
        ImageClip(caption_image)
        .set_start(current_time)
        .set_duration(duration)
        .set_position(("center", 1250))
    )

    caption_clips.append(caption_clip)
    current_time += duration

# Combine everything
video = video.set_audio(audio)

final_video = CompositeVideoClip(
    [video] + caption_clips,
    size=(1080, 1920)
).set_duration(audio.duration)

final_video.write_videofile(
    "curiosity-short.mp4",
    fps=24,
    codec="libx264",
    audio_codec="aac"
)

audio.close()
final_video.close()
video.close()

print("Your captioned video was created successfully!")


print("Your video was created successfully!")

print("Script saved successfully!")
print("Generated:", datetime.now().strftime("%Y-%m-%d %H:%M"))


