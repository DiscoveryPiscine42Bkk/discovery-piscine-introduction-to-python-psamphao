def array_of_names(name_dict):
    full_name = []
    for first, last in name_dict.items():
        full_name = f"{first.capitalize()} {last.capitalize}"
        full_names.append(full_name)
    return full_names

persons = {
     "jittiput": "Paphawee",
     "singklang": "Samphao",
     "jay": "sine",
     "sine": "jay",
}

print(array_of_names(persons))