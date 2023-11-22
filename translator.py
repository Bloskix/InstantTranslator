from mtranslate import translate


def translate_message(message, to_language):
    translated_message = translate(message, to_language=to_language)
    return translated_message
