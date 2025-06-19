def sinepancake(family):
    return list(filter(lambda name: family[name] == "pancake", family.keys()))

dupont_family = {
    "pancake": "pancake",
    "่sine": "sine",
    "mairu": "tem",
    "warisara": "pancake",
    "khamchata": "pancake"
}

print(sinepancake(dupont_family))