from .en import English
from .tr import Turkish

# For other languages, temporarily map to English to ensure coverage.
file_editor_strings = {
    "en": English.strings,
    "tr": Turkish.strings,
    "ar": English.strings,
    "cn": English.strings,
    "de": English.strings,
    "es": English.strings,
    "fr": English.strings,
    "hi": English.strings,
    "id": English.strings,
    "it": English.strings,
    "ja": English.strings,
    "ko": English.strings,
    "nl": English.strings,
    "pl": English.strings,
    "pt": English.strings,
    "ru": English.strings,
    "vi": English.strings,
}
