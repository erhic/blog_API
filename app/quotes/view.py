from quotes import quotes

@quotes.route('/')
def main_index():
    return 'blueprint for qoutes'
