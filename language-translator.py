from googletrans import Translator, LANGUAGES

translator = Translator()

def translate(text, dest_language):
    # Translate the text
    translation = translator.translate(text, dest=dest_language)
    return translation.text


text_to_translate = input("Enter the text to translate: ")
dest_language = input("Enter the destination language: ") # en, fr, hi, etc.
translate_text = translate(text_to_translate, dest_language)
print(translate_text) # Output:
