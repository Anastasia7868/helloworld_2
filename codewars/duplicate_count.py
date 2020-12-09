def duplicate_count(text):
    text = text.lower()
    count = 0
    text_letter = set()

    for letter in text:
        if text.count(letter) > 1:
            text_letter.add(letter)

    return len(text_letter)
