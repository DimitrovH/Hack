def get_people_count(activity):
    people = []
    
    for person in activity:
        if person not in people:
            people += [person]

    return len(people)

print(get_people_count(["Ivan","Martina","Petko","Kremena"]))