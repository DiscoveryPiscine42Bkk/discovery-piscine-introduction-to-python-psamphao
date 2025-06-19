def average(grades):
    return sum(grades.values()) / len(grades)

class_B = {
    "s": 1,
    "i": 5,
    "n": 8,
    "e": 9
}

class_C = {
    "p": 40,
    "a": 35,
    "n": 30,
    "c": 25,
    "a": 20,
    "k": 15,
    "e": 10,
    "g": 5
}

print(f"Average for class B: {average(class_B)}")
print(f"Average for class C: {average(class_C)}")