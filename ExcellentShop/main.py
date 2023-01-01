import json
import yaml

def main():
  translation = read_minecraft_translation_file("ja_jp.json")
  messages = read_yaml_file("messages_ja.yml")

  # GameMode
  for key in messages["GameMode"].keys():
    for t_key in translation.keys():
      if key.upper() == t_key.split(".")[-1].upper() and t_key.startswith("gameMode."):
        messages["GameMode"][key] = translation[t_key]
        break

  # Enchantment
  for key in messages["Enchantment"].keys():
    for t_key in translation.keys():
      if key.upper() == t_key.split(".")[-1] and t_key.startswith("enchantment.minecraft."):
        messages["Enchantment"][key] = translation[t_key]
        break

  # EntityType
  for key in messages["EntityType"].keys():
    for t_key in translation.keys():
      if key.upper() == t_key.split(".")[-1].upper() and t_key.startswith("entity.minecraft."):
        messages["EntityType"][key] = translation[t_key]
        break

  # Item
  for key in messages["Material"].keys():
    for t_key in translation.keys():
      if key.upper() == t_key.split(".")[-1].upper() and (t_key.startswith("item.minecraft.") or t_key.startswith("block.minecraft.")):
        messages["Material"][key] = translation[t_key]
        break
  
  # PotionEffectType
  for key in messages["PotionEffectType"].keys():
    for t_key in translation.keys():
      if key.upper() == t_key.split(".")[-1].upper() and t_key.startswith("effect.minecraft."):
        messages["PotionEffectType"][key] = translation[t_key]
        break


  write_yaml_file("messages_ja_.yml", messages)

def read_minecraft_translation_file(file):
  with open(file, "r", encoding="utf-8") as f:
    return json.load(f)

def read_yaml_file(file):
  with open(file, "r", encoding="utf-8") as f:
    return yaml.safe_load(f.read())

def write_yaml_file(file, data):
  with open(file, "w", encoding="utf-8") as f:
    f.write(yaml.safe_dump(data, allow_unicode=True))

if __name__ == "__main__":
  main()