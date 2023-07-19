import random
import time

def get_mood():
  moods = ["happy", "sad", "anxious", "stressed", "neutral"]
  return random.choice(moods)

def get_mental_health_score():
  mood = get_mood()
  if mood == "happy":
    return 100
  elif mood == "sad":
    return 50
  elif mood == "anxious":
    return 25
  elif mood == "stressed":
    return 0
  else:
    return 75

def main():
  score = 0
  for i in range(10):
    mood = get_mood()
    print(f"Your mood is {mood}.")
    score += get_mental_health_score()
  print(f"Your average mental health score is {score / 10}")

if __name__ == "__main__":
  main()
