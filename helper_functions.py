import regex

def edit_text(text: str) -> str:
    # Get rid of parenthesis
    sub = regex.sub(r'\([^)]*\)', '', text)
    # Split the text
    sub = sub.split()
    # Keep area in m2
    area = sub[-2] + sub[-1]
    # Get no. of rooms
    no_of_rooms = sub[-3]
    return [area, no_of_rooms]

new_area, new_no_of_rooms = edit_text("Prodej bytu 1+1 50 m²")
print(f"area: {new_area}")
print(f"no of rooms: {new_no_of_rooms}")
