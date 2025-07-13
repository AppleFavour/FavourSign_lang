from .en import English
from .tr import Turkish
from .ru import Russian
from .de import German
from .es import Spanish
from .fr import French
from .zh_cn import Chinese
from .ar import Arabic
from .pt import Portuguese
from .it import Italian
from .ja import Japanese
from .ko import Korean
from .hi import Hindi
from .vi import Vietnamese
from .id import Indonesian
from .pl import Polish


help_strings = {
    "en": English.strings,
    "tr": Turkish.strings,
    "ru": Russian.strings,
    "de": German.strings,
    "es": Spanish.strings,
    "fr": French.strings,
    "zh-cn": Chinese.strings,
    "ar": Arabic.strings,
    "pt": Portuguese.strings,
    "it": Italian.strings,
    "ja": Japanese.strings,
    "ko": Korean.strings,
    "hi": Hindi.strings,
    "vi": Vietnamese.strings,
    "id": Indonesian.strings,
    "pl": Polish.strings,
}


class Help:
    def __init__(self, lang_code):
        self.strings = help_strings.get(lang_code, English.strings)

    def get_string(self, key):
        return self.strings.get(key)
