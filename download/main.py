from .ar import Arabic
from .de import German
from .en import English
from .es import Spanish
from .fr import French
from .hi import Hindi
from .id import Indonesian
from .it import Italian
from .ja import Japanese
from .ko import Korean
from .pl import Polish
from .pt import Portuguese
from .ru import Russian
from .tr import Turkish
from .vi import Vietnamese
from .zh_cn import Chinese

download_strings = {
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
