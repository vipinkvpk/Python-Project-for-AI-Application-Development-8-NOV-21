"""
Author: VIPIN K
Description: Controller module that handles translations using calls to
IBM Watson Language Translator service.
"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    """
    Takes input text in English and returns output text in French
    :param english_text: Input text in English
    :returns: Output text in French
    """
    french_text = __translate(english_text, 'en', 'fr')
    return french_text


def __translate(text, lang1code, lang2code):
    """
    Wrapper function that handles service call and output handling
    :param text: Input text
    :param lang1code: Two-character code source language (e.g. en=English, fr=French)
    :param lang1code: Two-character code for target language (e.g. en=English, fr=French)
    :returns: Output text in English
    """
    result = language_translator.translate(
        text=text,
        model_id=lang1code+'-'+lang2code
    ).get_result()
    return result['translations'][0]['translation'] if (len(result['translations'])>0) \
        else 'Error: No translations available...'


def french_to_english(french_text):
    """
    Takes input text in French and returns output text in English
    :param french_text: Input text in French
    :returns: Output text in English
    """
    english_text = __translate(french_text, 'fr', 'en')
    return english_text
