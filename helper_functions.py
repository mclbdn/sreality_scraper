import regex


def edit_text(text: str) -> str:
    # Get rid of parenthesis
    sub = regex.sub(r"\([^)]*\)", "", text)
    # Split the text
    sub = sub.split()
    # Keep area in m2
    area = sub[-2] + sub[-1]
    # Get no. of rooms
    no_of_rooms = sub[-3]
    return [area, no_of_rooms]


def get_prague_area(text: str):
    prague_areas = [
        "Praha 1",
        "Praha 2",
        "Praha 3",
        "Praha 4",
        "Praha 5",
        "Praha 6",
        "Praha 7",
        "Praha 8",
        "Praha 9",
        "Praha 10",
    ]

    for area in prague_areas:
        if area in text:
            return area
