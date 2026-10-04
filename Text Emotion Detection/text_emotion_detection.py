# Text Emotion Detection

print("=" * 50)
print("        TEXT EMOTION DETECTION")
print("=" * 50)

# Emotion keywords
emotions = {
    "Happy": [
        "happy", "joy", "excited", "great", "wonderful",
        "amazing", "good", "smile", "fun", "love"
    ],

    "Sad": [
        "sad", "unhappy", "cry", "crying", "lonely",
        "hurt", "depressed", "bad", "miss", "pain"
    ],

    "Angry": [
        "angry", "anger", "hate", "mad", "annoyed",
        "irritated", "furious", "rage"
    ],

    "Fear": [
        "afraid", "fear", "scared", "terrified",
        "worried", "nervous", "danger"
    ],

    "Surprise": [
        "surprised", "surprise", "shocked", "wow",
        "unexpected", "astonished"
    ],

    "Love": [
        "love", "lovely", "care", "heart", "romantic",
        "dear", "beautiful", "affection"
    ]
}

# Get input
text = input("\nEnter a sentence or paragraph:\n")

# Convert to lowercase
text = text.lower()

# Count emotion words
emotion_scores = {}

for emotion, keywords in emotions.items():
    score = 0

    for word in keywords:
        if word in text:
            score += 1

    emotion_scores[emotion] = score

# Find highest emotion
detected_emotion = max(emotion_scores, key=emotion_scores.get)
highest_score = emotion_scores[detected_emotion]

print("\n" + "=" * 50)
print("           RESULT")
print("=" * 50)

if highest_score == 0:
    print("\n😐 Emotion could not be detected.")
else:
    print("\nDetected Emotion:", detected_emotion)
    print("Emotion Score:", highest_score)

print("\nEmotion Scores:")
for emotion, score in emotion_scores.items():
    print(f"{emotion}: {score}")

print("\n" + "=" * 50)