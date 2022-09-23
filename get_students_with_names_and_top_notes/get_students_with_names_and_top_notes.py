def top_note(student):
    return {"name": student["name"], "top_note": max(student["notes"])}


print(top_note({"name": "John", "notes": [3, 5, 4]}))
