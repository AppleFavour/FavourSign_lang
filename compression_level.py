# Plugins/compression_level.py
compression_level_strings = {
    "en": {
        "compression_prompt": (
            "📁 **Select Compression Level**\n\n"
            "This setting affects the signing speed and the final file size.\n\n"
            "**0**: Fastest signing, largest file size.\n"
            "**9**: Slowest signing, smallest file size.\n\n"
            "Currently selected: **{selected}**"
        ),
        "already_selected": "⚠️ This level is already selected.",
        "save_error": "Could not save the compression level.",
        "db_error": "A database error occurred. Please try again.",
        "compression_selected": "📌 Compression level set to **{selected}**.",
        "selected_notification": "📌 Selected: {selected}",
        "generic_error": "⚠️ An unexpected error occurred.",
        "back_button": "🔙 Go Back",
    },
    "tr": {
        "compression_prompt": (
            "📁 **Sıkıştırma Seviyesini Seçin**\n\n"
            "Bu ayar, imzalama hızını ve son dosya boyutunu etkiler.\n\n"
            "**0**: En hızlı imzalama, en büyük dosya boyutu.\n"
            "**9**: En yavaş imzalama, en küçük dosya boyutu.\n\n"
            "Mevcut seçim: **{selected}**"
        ),
        "already_selected": "⚠️ Bu seviye zaten seçili.",
        "save_error": "Sıkıştırma seviyesi kaydedilemedi.",
        "db_error": "Bir veritabanı hatası oluştu. Lütfen tekrar deneyin.",
        "compression_selected": "📌 Sıkıştırma seviyesi **{selected}** olarak ayarlandı.",
        "selected_notification": "📌 Seçildi: {selected}",
        "generic_error": "⚠️ Beklenmedik bir hata oluştu.",
        "back_button": "🔙 Geri Dön",
    },
    "ru": {
        "compression_prompt": (
            "📁 **Выберите уровень сжатия**\n\n"
            "Этот параметр влияет на скорость подписи и конечный размер файла.\n\n"
            "**0**: Самая быстрая подпись, самый большой размер файла.\n"
            "**9**: Самая медленная подпись, самый маленький размер файла.\n\n"
            "Текущий выбор: **{selected}**"
        ),
        "already_selected": "⚠️ Этот уровень уже выбран.",
        "save_error": "Не удалось сохранить уровень сжатия.",
        "db_error": "Произошла ошибка базы данных. Пожалуйста, попробуйте еще раз.",
        "compression_selected": "📌 Уровень сжатия установлен на **{selected}**.",
        "selected_notification": "📌 Выбрано: {selected}",
        "generic_error": "⚠️ Произошла непредвиденная ошибка.",
        "back_button": "🔙 Назад"
    },
    "de": {
        "compression_prompt": (
            "📁 **Komprimierungsstufe auswählen**\n\n"
            "Diese Einstellung beeinflusst die Signiergeschwindigkeit und die endgültige Dateigröße.\n\n"
            "**0**: Schnellste Signierung, größte Dateigröße.\n"
            "**9**: Langsamste Signierung, kleinste Dateigröße.\n\n"
            "Aktuell ausgewählt: **{selected}**"
        ),
        "already_selected": "⚠️ Diese Stufe ist bereits ausgewählt.",
        "save_error": "Komprimierungsstufe konnte nicht gespeichert werden.",
        "db_error": "Ein Datenbankfehler ist aufgetreten. Bitte versuche es erneut.",
        "compression_selected": "📌 Komprimierungsstufe auf **{selected}** gesetzt.",
        "selected_notification": "📌 Ausgewählt: {selected}",
        "generic_error": "⚠️ Ein unerwarteter Fehler ist aufgetreten.",
        "back_button": "🔙 Zurück",
    },
    "es": {
        "compression_prompt": (
            "📁 **Seleccionar Nivel de Compresión**\n\n"
            "Esta configuración afecta la velocidad de firmado y el tamaño final del archivo.\n\n"
            "**0**: Firmado más rápido, tamaño de archivo más grande.\n"
            "**9**: Firmado más lento, tamaño de archivo más pequeño.\n\n"
            "Seleccionado actualmente: **{selected}**"
        ),
        "already_selected": "⚠️ Este nivel ya está seleccionado.",
        "save_error": "No se pudo guardar el nivel de compresión.",
        "db_error": "Ocurrió un error en la base de datos. Por favor, inténtalo de nuevo.",
        "compression_selected": "📌 Nivel de compresión establecido en **{selected}**.",
        "selected_notification": "📌 Seleccionado: {selected}",
        "generic_error": "⚠️ Ocurrió un error inesperado.",
        "back_button": "🔙 Volver",
    },
    "fr": {
        "compression_prompt": (
            "📁 **Sélectionner le niveau de compression**\n\n"
            "Ce paramètre affecte la vitesse de signature et la taille finale du fichier.\n\n"
            "**0**: Signature la plus rapide, taille de fichier la plus grande.\n"
            "**9**: Signature la plus lente, taille de fichier la plus petite.\n\n"
            "Actuellement sélectionné: **{selected}**"
        ),
        "already_selected": "⚠️ Ce niveau est déjà sélectionné.",
        "save_error": "Impossible d'enregistrer le niveau de compression.",
        "db_error": "Une erreur de base de données est survenue. Veuillez réessayer.",
        "compression_selected": "📌 Niveau de compression défini sur **{selected}**.",
        "selected_notification": "📌 Sélectionné: {selected}",
        "generic_error": "⚠️ Une erreur inattendue est survenue.",
        "back_button": "🔙 Retour",
    },
    "zh-cn": {
        "compression_prompt": (
            "📁 **选择压缩级别**\n\n"
            "此设置会影响签名速度和最终文件大小。\n\n"
            "**0**: 签名最快，文件最大。\n"
            "**9**: 签名最慢，文件最小。\n\n"
            "当前选择: **{selected}**"
        ),
        "already_selected": "⚠️ 此级别已被选中。",
        "save_error": "无法保存压缩级别。",
        "db_error": "发生数据库错误。请重试。",
        "compression_selected": "📌 压缩级别设置为 **{selected}**。",
        "selected_notification": "📌 已选择: {selected}",
        "generic_error": "⚠️ 发生未知错误。",
        "back_button": "🔙 返回",
    },
    "ar": {
        "compression_prompt": (
            "📁 **تحديد مستوى الضغط**\n\n"
            "يؤثر هذا الإعداد على سرعة التوقيع وحجم الملف النهائي.\n\n"
            "**0**: أسرع توقيع، أكبر حجم للملف.\n"
            "**9**: أبطأ توقيع، أصغر حجم للملف.\n\n"
            "المحدد حاليا: **{selected}**"
        ),
        "already_selected": "⚠️ هذا المستوى محدد بالفعل.",
        "save_error": "تعذر حفظ مستوى الضغط.",
        "db_error": "حدث خطأ في قاعدة البيانات. الرجاء المحاولة مرة أخرى.",
        "compression_selected": "📌 تم تعيين مستوى الضغط على **{selected}**.",
        "selected_notification": "📌 المحدد: {selected}",
        "generic_error": "⚠️ حدث خطأ غير متوقع.",
        "back_button": "🔙 رجوع",
    },
    "pt": {
        "compression_prompt": (
            "📁 **Select Compression Level**\n\n"
            "This setting affects the signing speed and the final file size.\n\n"
            "**0**: Fastest signing, largest file size.\n"
            "**9**: Slowest signing, smallest file size.\n\n"
            "Currently selected: **{selected}**"
        ),
        "already_selected": "⚠️ This level is already selected.",
        "save_error": "Could not save the compression level.",
        "db_error": "A database error occurred. Please try again.",
        "compression_selected": "📌 Compression level set to **{selected}**.",
        "selected_notification": "📌 Selected: {selected}",
        "generic_error": "⚠️ An unexpected error occurred.",
        "back_button": "🔙 Go Back",
    },
    "it": {
        "compression_prompt": (
            "📁 **Select Compression Level**\n\n"
            "This setting affects the signing speed and the final file size.\n\n"
            "**0**: Fastest signing, largest file size.\n"
            "**9**: Slowest signing, smallest file size.\n\n"
            "Currently selected: **{selected}**"
        ),
        "already_selected": "⚠️ This level is already selected.",
        "save_error": "Could not save the compression level.",
        "db_error": "A database error occurred. Please try again.",
        "compression_selected": "📌 Compression level set to **{selected}**.",
        "selected_notification": "📌 Selected: {selected}",
        "generic_error": "⚠️ An unexpected error occurred.",
        "back_button": "🔙 Go Back",
    },
    "ja": {
        "compression_prompt": (
            "📁 **Select Compression Level**\n\n"
            "This setting affects the signing speed and the final file size.\n\n"
            "**0**: Fastest signing, largest file size.\n"
            "**9**: Slowest signing, smallest file size.\n\n"
            "Currently selected: **{selected}**"
        ),
        "already_selected": "⚠️ This level is already selected.",
        "save_error": "Could not save the compression level.",
        "db_error": "A database error occurred. Please try again.",
        "compression_selected": "📌 Compression level set to **{selected}**.",
        "selected_notification": "📌 Selected: {selected}",
        "generic_error": "⚠️ An unexpected error occurred.",
        "back_button": "🔙 Go Back",
    },
    "ko": {
        "compression_prompt": (
            "📁 **Select Compression Level**\n\n"
            "This setting affects the signing speed and the final file size.\n\n"
            "**0**: Fastest signing, largest file size.\n"
            "**9**: Slowest signing, smallest file size.\n\n"
            "Currently selected: **{selected}**"
        ),
        "already_selected": "⚠️ This level is already selected.",
        "save_error": "Could not save the compression level.",
        "db_error": "A database error occurred. Please try again.",
        "compression_selected": "📌 Compression level set to **{selected}**.",
        "selected_notification": "📌 Selected: {selected}",
        "generic_error": "⚠️ An unexpected error occurred.",
        "back_button": "🔙 Go Back",
    },
    "hi": {
        "compression_prompt": (
            "📁 **Select Compression Level**\n\n"
            "This setting affects the signing speed and the final file size.\n\n"
            "**0**: Fastest signing, largest file size.\n"
            "**9**: Slowest signing, smallest file size.\n\n"
            "Currently selected: **{selected}**"
        ),
        "already_selected": "⚠️ This level is already selected.",
        "save_error": "Could not save the compression level.",
        "db_error": "A database error occurred. Please try again.",
        "compression_selected": "📌 Compression level set to **{selected}**.",
        "selected_notification": "📌 Selected: {selected}",
        "generic_error": "⚠️ An unexpected error occurred.",
        "back_button": "🔙 Go Back",
    },
    "vi": {
        "compression_prompt": (
            "📁 **Select Compression Level**\n\n"
            "This setting affects the signing speed and the final file size.\n\n"
            "**0**: Fastest signing, largest file size.\n"
            "**9**: Slowest signing, smallest file size.\n\n"
            "Currently selected: **{selected}**"
        ),
        "already_selected": "⚠️ This level is already selected.",
        "save_error": "Could not save the compression level.",
        "db_error": "A database error occurred. Please try again.",
        "compression_selected": "📌 Compression level set to **{selected}**.",
        "selected_notification": "📌 Selected: {selected}",
        "generic_error": "⚠️ An unexpected error occurred.",
        "back_button": "🔙 Go Back",
    },
    "id": {
        "compression_prompt": (
            "📁 **Select Compression Level**\n\n"
            "This setting affects the signing speed and the final file size.\n\n"
            "**0**: Fastest signing, largest file size.\n"
            "**9**: Slowest signing, smallest file size.\n\n"
            "Currently selected: **{selected}**"
        ),
        "already_selected": "⚠️ This level is already selected.",
        "save_error": "Could not save the compression level.",
        "db_error": "A database error occurred. Please try again.",
        "compression_selected": "📌 Compression level set to **{selected}**.",
        "selected_notification": "📌 Selected: {selected}",
        "generic_error": "⚠️ An unexpected error occurred.",
        "back_button": "🔙 Go Back",
    },
    "pl": {
        "compression_prompt": (
            "📁 **Select Compression Level**\n\n"
            "This setting affects the signing speed and the final file size.\n\n"
            "**0**: Fastest signing, largest file size.\n"
            "**9**: Slowest signing, smallest file size.\n\n"
            "Currently selected: **{selected}**"
        ),
        "already_selected": "⚠️ This level is already selected.",
        "save_error": "Could not save the compression level.",
        "db_error": "A database error occurred. Please try again.",
        "compression_selected": "📌 Compression level set to **{selected}**.",
        "selected_notification": "📌 Selected: {selected}",
        "generic_error": "⚠️ An unexpected error occurred.",
        "back_button": "🔙 Go Back",
    },
    "nl": {
        "compression_prompt": (
            "📁 **Select Compression Level**\n\n"
            "This setting affects the signing speed and the final file size.\n\n"
            "**0**: Fastest signing, largest file size.\n"
            "**9**: Slowest signing, smallest file size.\n\n"
            "Currently selected: **{selected}**"
        ),
        "already_selected": "⚠️ This level is already selected.",
        "save_error": "Could not save the compression level.",
        "db_error": "A database error occurred. Please try again.",
        "compression_selected": "📌 Compression level set to **{selected}**.",
        "selected_notification": "📌 Selected: {selected}",
        "generic_error": "⚠️ An unexpected error occurred.",
        "back_button": "🔙 Go Back",
    }
}
