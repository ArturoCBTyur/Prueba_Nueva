DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

# Prepare to merge

def main():
    print("-----------------------------------")
    print("List comprehesed.")

    all_python_dev = [worker["name"] for worker in DATA if worker["language"] == "python"]
    for worker in all_python_dev:
        print(worker)

    print("-----------------------------------")
    print("High order functions.")

    all_python_dev_2 = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_dev_2 = list(map(lambda worker: worker["name"], all_python_dev_2))
    for worker in all_python_dev_2:
        print(worker)

    print("-----------------------------------")
    print("List comprehesed.")

    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    for worker in all_platzi_workers:
        print(worker)

    print("-----------------------------------")
    print("High order functions.")

    all_platzi_workers_2 = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_workers_2 = list(map(lambda worker: worker["name"], all_platzi_workers_2))
    for worker in all_platzi_workers_2:
        print(worker)

    print("-----------------------------------")
    print("-----------------------------------")
    print("High order functions.")
    
    adults = list(filter(lambda worker: worker["age"] >= 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    for worker in adults:
        print(worker)

    print("-----------------------------------")
    print("List comprehesed.")

    adults_2 = [worker["name"] for worker in DATA if worker["age"] >= 18]
    for worker in adults_2:
        print(worker)

    print("-----------------------------------")
    print("High order functions.")

    # Lists -> list1 + list2 to lists and In Dicts -> dict1 | dict2 to add 2 dictionaries
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    for worker in old_people:
        print(worker)

    print("-----------------------------------")
    print("List comprehesed.")

    old_people_2 = [{**worker, **{"old": worker["age"] > 70}} for worker in DATA ]
    for worker in old_people_2:
        print(worker)

    print("-----------------------------------")

if __name__ == "__main__":
    main()