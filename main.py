import json

def main():
  file = read_minecraft_translation_file("ja_jp.json")
  print(file)

def read_minecraft_translation_file(file):
  with open(file, "r", encoding="utf-8") as f:
    return json.load(f)

if __name__ == "__main__":
  main()