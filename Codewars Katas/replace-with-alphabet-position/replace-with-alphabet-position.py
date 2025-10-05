def alphabet_position(text):
    text_is_alpha = [x for x in text if x.isalpha()]
    return ' '.join(str(ord(x.lower()) - 96) for x in text_is_alpha)