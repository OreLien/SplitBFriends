import os
import json


# Translator class
class Translator(object):
    """Translator service"""

    __translation = {}

    def __init__(self, lang="en"):
        self.__id = id
        self.__lang = lang
        self.__translation = load_translation(lang.lower())

    def set_lang(self, lang):
        self.__lang = lang
        self.__translation = load_translation(lang.lower())

    def trans(self, key):
        return self.__translation[key]


# Load translation file by language
def load_translation(lang):
    return json.load(open("resources/translation_" + lang.lower() + ".json"))
