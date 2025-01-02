from translate import Translator

def translate_text(text, target_language):
    translator = Translator(to_language=target_language)
    translation = translator.translate(text)
    return translation

while True:
    user_input = input("Enter a word or phrase to translate (or 'q' to quit): ")

    if user_input.lower() == 'q':
        break

    target_language = input("Enter the target language (e.g., fr for French): ")

    translation = translate_text(user_input, target_language)

    print(f'Translation: {translation}')