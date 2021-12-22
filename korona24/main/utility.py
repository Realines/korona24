import pytils.translit

def translify(text):
    text = pytils.translit.translify(text)
    text =text.replace(' ', '_')
    text =text.replace("'", "")
    text =text.replace(",", "")
    text =text.replace('!', '')
    text =text.replace('?', '')
    text =text.replace('.', '')
    text =text.replace(':', '-')
    return text.lower()