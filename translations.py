# Plugins/announcements.py
announcements_strings = {
    "EN": {
        "no_reply": "🔍 Announcement message not found. Please reply to a message and try again.",
        "no_content": "🔍 Announcement content not found. Please reply to a message with text or a file.",
        "permission_denied": "🚫 You do not have permission to perform this action.",
        "announcement_complete": "✅ Announcement completed.\n\nTotal users: {total}\nSent: {sent}\nNot sent: {failed}",
    },
    "TR": {
        "no_reply": "🔍 Duyuru mesajı bulunamadı. Lütfen bir mesaja yanıt verin ve tekrar deneyin.",
        "no_content": "🔍 Duyuru içeriği bulunamadı. Lütfen bir metin veya dosya ile bir mesaja yanıt verin.",
        "permission_denied": "🚫 Bu işlemi gerçekleştirmek için izniniz yok.",
        "announcement_complete": "✅ Duyuru tamamlandı.\n\nToplam kullanıcı: {total}\nGönderilen: {sent}\nGönderilemeyen: {failed}",
    },
    "RU": {
        "no_reply": "🔍 Сообщение для объявления не найдено. Пожалуйста, ответьте на сообщение и попробуйте снова.",
        "no_content": "🔍 Контент объявления не найден. Пожалуйста, ответьте на сообщение с текстом или файлом.",
        "permission_denied": "🚫 У вас нет прав для выполнения этого действия.",
        "announcement_complete": "✅ Объявление завершено.\n\nВсего пользователей: {total}\nОтправлено: {sent}\nНе отправлено: {failed}",
    },
    "DE": {
        "no_reply": "🔍 Ankündigungsnachricht nicht gefunden. Bitte antworte auf eine Nachricht und versuche es erneut.",
        "no_content": "🔍 Ankündigungsinhalt nicht gefunden. Bitte antworte auf eine Nachricht mit Text oder einer Datei.",
        "permission_denied": "🚫 Du hast keine Berechtigung für diese Aktion.",
        "announcement_complete": "✅ Ankündigung abgeschlossen.\n\nGesamtnutzer: {total}\nGesendet: {sent}\nFehlgeschlagen: {failed}",
    }
}
# Plugins/certificate_select.py
certificate_select_strings = {
    "EN": {
        "cert_loading_error": "⚠️ An error occurred while loading certificate information.",
        "select_certificate_prompt": "📃 Please select a certificate.\nSelected: {selected}",
        "cert_saved": "📌 Certificate selected: {cert_name}",
        "already_selected": "⚠️ Already selected",
        "back_button": "Go Back 🔙",
        "saving_error": "A database error occurred. Please try again later.",
        "callback_error": "⚠️ An error occurred.",
    },
    "TR": {
        "cert_loading_error": "⚠️ Sertifika bilgilerini yüklerken bir hata oluştu.",
        "select_certificate_prompt": "📃 Lütfen bir sertifika seçin.\nSeçilen: {selected}",
        "cert_saved": "📌 Seçilen sertifika: {cert_name}",
        "already_selected": "⚠️ Sertifika zaten seçilmiş.",
        "back_button": "Geri Dön 🔙",
        "saving_error": "Bir veritabanı hatası oluştu. Lütfen daha sonra tekrar deneyin.",
        "callback_error": "⚠️ Bir hata oluştu.",
    },
    "RU": {
        "cert_loading_error": "⚠️ Произошла ошибка при загрузке информации о сертификате.",
        "select_certificate_prompt": "📃 Пожалуйста, выберите сертификат.\nВыбран: {selected}",
        "cert_saved": "📌 Сертификат выбран: {cert_name}",
        "already_selected": "⚠️ Уже выбрано",
        "back_button": "Назад 🔙",
        "saving_error": "Произошла ошибка с базой данных. Пожалуйста, попробуйте снова позже.",
        "callback_error": "⚠️ Произошла ошибка.",
    },
    "DE": {
        "cert_loading_error": "⚠️ Beim Laden der Zertifikatsinformationen ist ein Fehler aufgetreten.",
        "select_certificate_prompt": "📃 Bitte wähle ein Zertifikat aus.\nAusgewählt: {selected}",
        "cert_saved": "📌 Zertifikat ausgewählt: {cert_name}",
        "already_selected": "⚠️ Bereits ausgewählt",
        "back_button": "Zurück 🔙",
        "saving_error": "Ein Datenbankfehler ist aufgetreten. Bitte versuche es später erneut.",
        "callback_error": "⚠️ Ein Fehler ist aufgetreten.",
    }
}
# Plugins/compression_level.py
compression_level_strings = {
    "EN": {
        "compression_prompt": (
            "📁 Select the compression level\n"
            "Selected: {selected}\n"
            "This setting determines the bot's speed and the size of the signed file.\n\n"
            "**0** — **Fastest Signing**, **Minimum Compression (Larger File Size)**\n"
            "**9** — **Slowest Signing**, **Maximum Compression (Smaller File Size)**"
        ),
        "already_selected": "⚠️ Already selected.",
        "save_error": "Compression level could not be saved.",
        "compression_selected": (
            "📌 Compression level selected: {selected}\n\n"
            "This setting determines the bot's speed and the size of the signed file.\n\n"
            "**0** — **Fastest Signing**, **Minimum Compression (Larger File Size)**\n"
            "**9** — **Slowest Signing**, **Maximum Compression (Smaller File Size)**"
        ),
        "selected_notification": "📌 Selected: {selected}",
        "generic_error": "⚠️ An error occurred.",
        "back_button": "Go Back 🔙",
    },
    "TR": {
        "compression_prompt": (
            "📁 Sıkıştırma seviyesini seçin\n"
            "Seçilen: {selected}\n"
            "Bu ayar, botun hızını ve imzalanmış dosyanın boyutunu belirler.\n\n"
            "**0** — **En Hızlı İmzalama**, **Minimum Sıkıştırma (Daha Büyük Dosya Boyutu)**\n"
            "**9** — **En Yavaş İmzalama**, **Maksimum Sıkıştırma (Daha Küçük Dosya Boyutu)**"
        ),
        "already_selected": "⚠️ Zaten seçilmiş.",
        "save_error": "Sıkıştırma seviyesi kaydedilemedi.",
        "compression_selected": (
            "📌 Seçilen sıkıştırma seviyesi: {selected}\n\n"
            "Bu ayar, botun hızını ve imzalanmış dosyanın boyutunu belirler.\n\n"
            "**0** — **En Hızlı İmzalama**, **Minimum Sıkıştırma (Daha Büyük Dosya Boyutu)**\n"
            "**9** — **En Yavaş İmzalama**, **Maksimum Sıkıştırma (Daha Küçük Dosya Boyutu)**"
        ),
        "selected_notification": "📌 Seçilen: {selected}",
        "generic_error": "⚠️ Bir hata oluştu.",
        "back_button": "Geri Dön 🔙",
    },
    "RU": {
        "compression_prompt": (
            "📁 Выберите уровень сжатия\n"
            "Выбран: {selected}\n"
            "Эта настройка определяет скорость бота и размер подписанного файла.\n\n"
            "**0** — **Самая Быстрая Подпись**, **Минимальное Сжатие (Больший Размер Файла)**\n"
            "**9** — **Самая Медленная Подпись**, **Максимальное Сжатие (Меньший Размер Файла)**"
        ),
        "already_selected": "⚠️ Уже выбрано.",
        "save_error": "Не удалось сохранить уровень сжатия.",
        "compression_selected": (
            "📌 Выбран уровень сжатия: {selected}\n\n"
            "Эта настройка определяет скорость бота и размер подписанного файла.\n\n"
            "**0** — **Самая Быстрая Подпись**, **Минимальное Сжатие (Больший Размер Файла)**\n"
            "**9** — **Самая Медленная Подпись**, **Максимальное Сжатие (Меньший Размер Файла)**"
        ),
        "selected_notification": "📌 Выбрано: {selected}",
        "generic_error": "⚠️ Произошла ошибка.",
        "back_button": "Назад 🔙"
    },
    "DE": {
        "compression_prompt": (
            "📁 Wähle die Komprimierungsstufe\n"
            "Ausgewählt: {selected}\n"
            "Diese Einstellung bestimmt die Geschwindigkeit des Bots und die Größe der signierten Datei.\n\n"
            "⬢ **0** — **Schnellste Signierung**, **Minimale Komprimierung (Größere Dateigröße)**\n"
            "⬢ **9** — **Langsamste Signierung**, **Maximale Komprimierung (Kleinere Dateigröße)**"
        ),
        "already_selected": "⚠️ Bereits ausgewählt.",
        "save_error": "Komprimierungsstufe konnte nicht gespeichert werden.",
        "compression_selected": (
            "📌 Komprimierungsstufe ausgewählt: {selected}\n\n"
            "Diese Einstellung bestimmt die Geschwindigkeit des Bots und die Größe der signierten Datei.\n\n"
            "**0** — **Schnellste Signierung**, **Minimale Komprimierung (Größere Dateigröße)**\n"
            "**9** — **Langsamste Signierung**, **Maximale Komprimierung (Kleinere Dateigröße)**"
        ),
        "selected_notification": "📌 Ausgewählt: {selected}",
        "generic_error": "⚠️ Ein Fehler ist aufgetreten.",
        "back_button": "Zurück 🔙",
    }
}
# Plugins/countdown.py
countdown_strings = {
    "EN": {
        "signed": "Signed",
        "app_name": "App Name",
        "bundle_id": "Bundle ID",
        "certificate": "Certificate",
        "install_button": "📲 Install",
        "explore_button": "🔎 Discover more iPA",
        "mnm_notify": "Do you see this because message.edit_text is failed"
    },
    "TR": {
        "signed": "İmzalandı",
        "app_name": "Uygulama Adı",
        "bundle_id": "Uygulama ID",
        "certificate": "Sertifika",
        "install_button": "📲 Yükle",
        "explore_button": "🔎 Daha fazla iPA keşfedin",
        "mnm_notify": "Mesaj düzenlenmesi başarısız oldu."
    },
    "RU": {
        "signed": "Подписан",
        "app_name": "Название приложения",
        "bundle_id": "ID приложения",
        "certificate": "Сертификат",
        "install_button": "📲 Установить",
        "explore_button": "🔎 Daha fazla iPA",
        "mnm_notify": "Ошибка при редактировании сообщения"
    },
    "DE": {
        "signed": "Signiert",
        "app_name": "App-Name",
        "bundle_id": "Bundle-ID",
        "certificate": "Zertifikat",
        "install_button": "📲 Installieren",
        "explore_button": "🔎 Mehr entdecken",
        "mnm_notify": "Sie sehen dies, weil message.edit_text fehlgeschlagen ist"
    }
}
# Plugins/download.py
download_strings = {
    "EN": {
        "download_failed_message": "❌ {file_name} can't be downloaded!",
        "download_attempt_failed_message": "An error occurred while downloading {file_name}, retrying... ({current}/{limit})",
        "download_successful_message": "✅ {file_name} downloaded successfully!",
        "download_error_detected": "Detected an error during download",
        "httpnot200": "There is nothing to see here.",
        "httpnotfile": "There is nothing to download.",
        "connection_error": "Unable to establish connection.",
        "unexpected_response_error": "Unexpected response from server.",
        "invalid_url_error": "Invalid URL provided.",
        "too_many_redirects_error": "Too many redirects encountered.",
        "ssl_error": "SSL connection error.",
        "payload_error": "Invalid or incomplete data received.",
        "server_disconnected_error": "Server connection was interrupted.",
        "general_download_error": "An error occurred during file download.",
        "file_not_found_error": "File not found.",
        "file_corrupted_error": "Corrupted file detected.",
        "unknown_exception_error": "An unexpected error occurred.",
        "retrying_message": "Retrying download... ({current}/{limit})"
    },
    "TR": {
        "download_failed_message": "❌ {file_name} indirilemedi",
        "download_attempt_failed_message": "{file_name} indirilirken bir hata oluştu, yeniden deneniyor... ({current}/{limit})",
        "download_successful_message": "✅ {file_name} başarıyla indirildi",
        "download_error_detected": "İndirme sırasında bir hata tespit edildi",
        "httpnot200": "Burada görülecek bir şey yok.",
        "httpnotfile": "İndirilecek bir şey yok.",
        "connection_error": "Bağlantı kurulamadı.",
        "unexpected_response_error": "Sunucudan beklenmeyen yanıt.",
        "invalid_url_error": "Geçersiz URL sağlandı.",
        "too_many_redirects_error": "Çok fazla yönlendirme ile karşılaşıldı.",
        "ssl_error": "SSL bağlantı hatası.",
        "payload_error": "Geçersiz veya eksik veri alındı.",
        "server_disconnected_error": "Sunucu bağlantısı kesildi.",
        "general_download_error": "Dosya indirilirken bir hata oluştu.",
        "file_not_found_error": "Dosya bulunamadı.",
        "file_corrupted_error": "Bozuk dosya tespit edildi.",
        "unknown_exception_error": "Beklenmedik bir hata oluştu.",
        "retrying_message": "İndirme yeniden deneniyor... ({current}/{limit})"
    },
    "RU": {
        "download_failed_message": "❌ {file_name} не может быть скачан!",
        "download_attempt_failed_message": "Ошибка при скачивании {file_name}, повторная попытка... ({current}/{limit})",
        "download_successful_message": "✅ {file_name} скачан успешно!",
        "download_error_detected": "Обнаружена ошибка при скачивании",
        "httpnot200": "Здесь нет ничего интересного.",
        "httpnotfile": "Нет файла для скачивания.",
        "connection_error": "Невозможно установить соединение.",
        "unexpected_response_error": "Получен неожиданный ответ от сервера.",
        "invalid_url_error": "Неверный URL.",
        "too_many_redirects_error": "Слишком много перенаправлений.",
        "ssl_error": "Ошибка SSL-соединения.",
        "payload_error": "Получены неполные или повреждённые данные.",
        "server_disconnected_error": "Соединение с сервером было прервано.",
        "general_download_error": "Произошла ошибка при скачивании файла.",
        "file_not_found_error": "Файл не найден.",
        "file_corrupted_error": "Обнаружен повреждённый файл.",
        "unknown_exception_error": "Произошла неизвестная ошибка.",
        "retrying_message": "Повторная попытка загрузки... ({current}/{limit})"
    },
    "DE": {
        "download_failed_message": "❌ {file_name} kann nicht heruntergeladen werden!",
        "download_attempt_failed_message": "Ein Fehler ist beim Herunterladen von {file_name} aufgetreten, neuer Versuch... ({current}/{limit})",
        "download_successful_message": "✅ {file_name} erfolgreich heruntergeladen!",
        "download_error_detected": "Fehler beim Download erkannt",
        "httpnot200": "Hier gibt es nichts zu sehen.",
        "httpnotfile": "Hier gibt es nichts zum Herunterladen.",
        "connection_error": "Verbindung konnte nicht hergestellt werden.",
        "unexpected_response_error": "Unerwartete Antwort vom Server.",
        "invalid_url_error": "Ungültige URL angegeben.",
        "too_many_redirects_error": "Zu viele Weiterleitungen.",
        "ssl_error": "SSL-Verbindungsfehler.",
        "payload_error": "Ungültige oder unvollständige Daten empfangen.",
        "server_disconnected_error": "Serververbindung wurde unterbrochen.",
        "general_download_error": "Ein Fehler ist beim Herunterladen der Datei aufgetreten.",
        "file_not_found_error": "Datei nicht gefunden.",
        "file_corrupted_error": "Beschädigte Datei erkannt.",
        "unknown_exception_error": "Ein unerwarteter Fehler ist aufgetreten.",
        "retrying_message": "Download wird wiederholt... ({current}/{limit})"
    }
}
# Plugins/help.py
help_strings = {
    "EN": {
        "user_not_registered": "You are not registered.",
        "available_cmds": "Available Commands:",
        "user_cmds": "User Commands:",
        "cmd_prefixes": "Active Command prefixes: {prefixes}",
        "admin_cmds": "Admin Commands:",
        "help_cmd": "Shows this help message.",
        "speedtest_cmd": "Tests connection speed.",
        "info_cmd": "Shows information about bot.",
        "sign_cmd": "Send or reply to ipa.",
        "clear_cmd": "Disables modify options",
        "profile_cmd": "Removes embeddedmmobile provision file from iPA",
        "stripencslices_cmd": "Removes encrypted slices from the iPA file.",
        "stripslices_cmd": "Remove non arm64 slices from iPA file.",
        "filesupport_cmd": "Tries to fix 'Files App' support if app has.",
        "watch_cmd": "Removes watch app from iPA",
        "rmdevicelimit_cmd": "Removes device specific installation restriction.",
        "setlimit_cmd": "Sets Minimum required OS to bypass installation restriction. - Not guaranteed to work",
        "id_cmd": "Change App's package/bundle ID",
        "version_cmd": "Change App's package/bundle version",
        "name_cmd": "Change App's package/bundle name",
        "update_cmd": "Update bot (Pull from repo)",
        "duyur_cmd": "Make a announcement for all registered users.",
        "exec_cmd": "Execute shell commands",
        "restart_cmd": "Restart bot",
        "shutdown_cmd": "Shutdown bot",
        "user_cmd": "Register/Unregister users to db.",
        "premium_cmd": "*obsolute* mark user as premium in feature they can access exclusive stuff.",
        "unknown_exception": "An error occurred while processing help request from @{username} ({userID}): {error}"
    },
    "TR": {
        "user_not_registered": "Kayıtlı değilsiniz.",
        "available_cmds": "Mevcut Komutlar:",
        "user_cmds": "Kullanıcı Komutları:",
        "cmd_prefixes": "**to_do** {prefixes}",
        "admin_cmds": "Yönetici Komutları:",
        "help_cmd": "Bu yardım mesajını gösterir.",
        "speedtest_cmd": "Bağlantı hızını test eder.",
        "info_cmd": "Bot hakkında bilgi gösterir.",
        "sign_cmd": "iPA’ya gönder veya yanıtla.",
        "clear_cmd": "Düzenleme seçeneklerini devre dışı bırakır.",
        "profile_cmd": "iPA’dan mobileprovision dosyasını kaldırır.",
        "stripencslices_cmd": "iPA dosyasından şifrelenmiş kısımları kaldırır.",
        "stripslices_cmd": "iPA dosyasından arm64 olmayan kısımları kaldırır.",
        "filesupport_cmd": "Eğer destekleniyorsa 'Dosyalar Uygulaması' desteğini düzeltmeye çalışır.",
        "watch_cmd": "iPA dosyasından Apple Watch uygulamasını kaldırır.",
        "rmdevicelimit_cmd": "Cihaza özgü yükleme kısıtlamasını kaldırır.",
        "setlimit_cmd": "Yükleme kısıtlamasını aşabilmek için gerekli minimum OS’u ayarlar. (Çalışmayabilir)",
        "id_cmd": "Uygulamanın paket/bundle kimliğini değiştirir.",
        "version_cmd": "Uygulamanın paket/bundle sürümünü değiştirir.",
        "name_cmd": "Uygulamanın paket/bundle adını değiştirir.",
        "update_cmd": "Botu günceller (Repo’dan çeker).",
        "duyur_cmd": "Tüm kayıtlı kullanıcılar için bir duyuru yapar.",
        "exec_cmd": "Shell komutları çalıştırır.",
        "restart_cmd": "Botu yeniden başlatır.",
        "shutdown_cmd": "Botu kapatır.",
        "user_cmd": "Kullanıcıları veritabanına kaydeder/kaldırır.",
        "premium_cmd": "*Eski* Kullanıcıyı premium olarak işaretler, gelecekte özel içeriklere erişebilirler (eğer böyle bir içerik oluşturursam).",
        "unknown_exception": "@{username} ({userID}) kullanıcısından yardım isteği işlenirken bir hata oluştu: {error}"
    },
    "RU": {
        "user_not_registered": "Вы не зарегистрированы.",
        "available_cmds": "Доступные команды:",
        "user_cmds": "Команды пользователей:",
        "cmd_prefixes": "**todo** {prefixes}",
        "admin_cmds": "Команды администраторов:",
        "help_cmd": "Показывает это сообщение помощи.",
        "speedtest_cmd": "Тестирует скорость соединения.",
        "info_cmd": "Показывает информацию о боте.",
        "sign_cmd": "Отправляет или отвечает любым ipa-файлом.",
        "clear_cmd": "Отключает параметры редактирования.",
        "profile_cmd": "Удаляет мобильный профиль из ipa-файла.",
        "stripencslices_cmd": "Удаляет зашифрованные срезы из ipa-файла.",
        "stripslices_cmd": "Удаляет срезы, не относящиеся к arm64, из ipa-файла.",
        "filesupport_cmd": "Пытается исправить поддержку 'Files App' если приложение поддерживает.",
        "watch_cmd": "Удаляет приложение часов из ipa-файла.",
        "rmdevicelimit_cmd": "Удаляет ограничение на устройство.",
        "setlimit_cmd": "Устанавливает минимально необходимую версию ОС для обхода ограничения на устройство. - Не гарантируется.",
        "id_cmd": "Изменяет идентификатор приложения.",
        "version_cmd": "Изменяет версию приложения.",
        "name_cmd": "Изменяет имя приложения.",
        "update_cmd": "Обновляет бота (выполняет pull из репозитория).",
        "duyur_cmd": "Делает объявление для всех зарегистрированных пользователей.",
        "exec_cmd": "Выполняет shell-команды.",
        "restart_cmd": "Перезапускает бота.",
        "shutdown_cmd": "Закрывает бота.",
        "user_cmd": "Регистрирует/удаляет пользователей из базы данных.",
        "premium_cmd": "*Устарело* Отмечает пользователя как премиум, чтобы он мог получить доступ к эксклюзивному контенту (если я когда-нибудь создам его).",
        "unknown_exception": "Произошла неизвестная ошибка при обработке запроса помощи от @{username} ({userID}): {error}"
    },
    "DE": {
        "user_not_registered": "Du bist nicht registriert.",
        "available_cmds": "Verfügbare Befehle:",
        "user_cmds": "Benutzer-Befehle:",
        "cmd_prefixes": "Aktive Befehlspräfixe: {prefixes}",
        "admin_cmds": "Admin-Befehle:",
        "help_cmd": "Zeigt diese Hilfemeldung an.",
        "speedtest_cmd": "Testet die Verbindungsgeschwindigkeit.",
        "info_cmd": "Zeigt Informationen über den Bot.",
        "sign_cmd": "Sende oder antworte auf eine IPA.",
        "clear_cmd": "Deaktiviert Änderungsoptionen",
        "profile_cmd": "Entfernt eingebettete mobile Provision-Datei aus der IPA",
        "stripencslices_cmd": "Entfernt verschlüsselte Slices aus der IPA-Datei.",
        "stripslices_cmd": "Entfernt nicht-arm64 Slices aus der IPA-Datei.",
        "filesupport_cmd": "Versucht, die 'Files App'-Unterstützung zu reparieren, falls die App diese hat.",
        "watch_cmd": "Entfernt Watch-App aus der IPA",
        "rmdevicelimit_cmd": "Entfernt gerätespezifische Installationsbeschränkung.",
        "setlimit_cmd": "Setzt das erforderliche Mindest-OS, um Installationsbeschränkungen zu umgehen. - Keine Garantie",
        "id_cmd": "Ändert die App-Paket/Bundle-ID",
        "version_cmd": "Ändert die App-Paket/Bundle-Version",
        "name_cmd": "Ändert den App-Paket/Bundle-Namen",
        "update_cmd": "Aktualisiert den Bot (Pull vom Repository)",
        "duyur_cmd": "Macht eine Ankündigung für alle registrierten Benutzer.",
        "exec_cmd": "Führt Shell-Befehle aus",
        "restart_cmd": "Startet den Bot neu",
        "shutdown_cmd": "Fährt den Bot herunter",
        "user_cmd": "Registriert/Deregistriert Benutzer in der Datenbank.",
        "premium_cmd": "*veraltet* markiert Benutzer als Premium für zukünftige exklusive Inhalte.",
        "unknown_exception": "Ein Fehler ist bei der Verarbeitung der Hilfeanfrage von @{username} ({userID}) aufgetreten: {error}"
    }
}
# Plugins/info.py
info_strings = {
    "EN": {
        "greeting": "👋 Hello! {name}",
        "system_info": "\nSystem Information:\n",
        "bot_info": "\nBot Information:\n",
        "bot_stats": "{uptime} - {usage}",
        "total_users": "Registered Users: {count}",
        "active_users": "Active users: {count}",
    },
    "TR": {
        "greeting": "👋 Merhaba! {name}",
        "system_info": "\nSistem Bilgileri:\n",
        "bot_info": "\nBot Bilgileri:\n",
        "bot_stats": "{uptime} - {usage}",
        "total_users": "Kayıtlı Kullanıcı Sayısı: {count}",
        "active_users": "Aktif Kullanıcı Sayısı: {count}",
    },
    "RU": {
        "greeting": "👋 Привет! {name}",
        "system_info": "\nСистемная информация:\n",
        "bot_info": "\nИнформация о боте:\n",
        "bot_stats": "{uptime} - {usage}",
        "total_users": "Пользователи: {count}",
        "active_users": "Активные пользователи: {count}",
    },
    "DE": {
        "greeting": "👋 Hallo! {name}",
        "system_info": "\nSysteminformationen:\n",
        "bot_info": "\nBot-Informationen:\n",
        "bot_stats": "{uptime} - {usage}",
        "total_users": "Registrierte Benutzer: {count}",
        "active_users": "Aktive Benutzer: {count}",
    }
}
# Plugins/language_select.py
language_select_strings = {
    "EN": {
        "select_language": "🌐 Select a language",
        "selected": "Selected:",
        "already_selected": "⚠️ You have already selected the current language.",
        "save_failed": "⚠️ Failed to save the language.",
        "new_language_selected": "🌐 New language selected",
        "error_in_language_selection": "⚠️ An error occurred during language selection.",
        "database_error": "A database error occurred. Please try again later.",
        "language_clear_success": "Now following telegram client language choice",
        "language_clear_failed": "Nothing to remove?",
        "back_button": "Go Back 🔙",
        "clear_button": "Clear Language 🧹"
    },
    "TR": {
        "select_language": "🌐 Bir dil seçin",
        "selected": "Seçilen:",
        "already_selected": "Mevcut dili zaten seçtiniz.",
        "save_failed": "Dil kaydedilemedi.",
        "new_language_selected": "🌐 Yeni dil seçildi",
        "error_in_language_selection": "Dil seçimi sırasında bir hata oluştu.",
        "database_error": "Veritabanı hatası oluştu. Lütfen daha sonra tekrar deneyin.",
        "language_clear_success": "Artık Telegram istemcisindeki dil seçimini takip ediyorsunuz.",
        "language_clear_failed": "Silinecek bir şey yok.",
        "back_button": "Geri Dön 🔙",
        "clear_button": "Dili Temizle 🧹"
    },
    "RU": {
        "select_language": "🌐 Выберите язык",
        "selected": "Выбранный:",
        "already_selected": "Вы уже выбрали текущий язык.",
        "save_failed": "Не удалось сохранить язык.",
        "new_language_selected": "🌐 Новый язык выбран",
        "error_in_language_selection": "Произошла ошибка при выборе языка.",
        "database_error": "Произошла ошибка базы данных. Пожалуйста, попробуйте позже.",
        "language_clear_success": "",
        "language_clear_failed": "",
        "back_button": "Назад 🔙",
        "clear_button": "🧹"
    },
    "DE": {
        "select_language": "🌐 Wähle eine Sprache",
        "selected": "Ausgewählt:",
        "already_selected": "Du hast bereits die aktuelle Sprache ausgewählt.",
        "save_failed": "Sprache konnte nicht gespeichert werden.",
        "new_language_selected": "🌐 Neue Sprache ausgewählt",
        "error_in_language_selection": "Bei der Sprachauswahl ist ein Fehler aufgetreten.",
        "language_saved_successfully": "Sprache {lang} erfolgreich für Benutzer {userID} gespeichert",
        "database_error": "Ein Datenbankfehler ist aufgetreten. Bitte versuche es später erneut.",
        "language_clear_success": "",
        "language_clear_failed": "",
        "back_button": "Zurück 🔙",
        "clear_button": "🧹"
    }
}
# Plugins/modifier.py
modifier_strings = {
    "EN": {
        "save_error": "Failed to save {options}. Error: {error}.",
        "json_decode_error": "Failed to read {options}. Error: {error}.",
        "read_runtime_error": "An error occurred while reading: {error}.",
        "update_error": "Failed to update {options}. Error: {error}.",
        "app_name_usage": "Usage: /name <app_name> or /n <app_name>.",
        "set_app_name": "The app name has been set to **{name}**.",
        "unset_app_name": "The app name has not been changed.",
        "app_version_usage": "Usage: /version <app_version> or /v <app_version>.",
        "set_app_version": "The app version has been set to **{version}**.",
        "unset_app_version": "The app version has not been changed.",
        "invalid_app_version": "Invalid format. Only numbers, dots, and hyphens are allowed.",
        "app_id_usage": "Usage: /id <bundle_id> or /b <bundle_id> (e.g., xyz.turannul.appname).",
        "set_app_id": "The app bundle ID has been set to **{id}**.",
        "unset_app_id": "The app bundle ID has not been changed.",
        "min_os_usage": "Usage: /setlimit <min_os_version> or /nl <min_os_version>.",
        "set_min_os": "The minimum OS version has been set to **{os_version}**.",
        "unset_min_os": "The minimum OS version has not been changed.",
        "invalid_min_os": "Invalid OS version format. Please use a valid version string (e.g., 14.0).",
        "set_install_restriction": "Install restrictions have been applied.",
        "unset_install_restriction": "Install restrictions have been removed.",
        "set_remove_watchapp": "Watch app removal has been enabled.",
        "unset_remove_watchapp": "Watch app removal has been disabled.",
        "set_file_support": "File support has been enabled. (This may or may not work.)",
        "unset_file_support": "File support has been disabled.",
        "set_remove_architectures": "Architectures have been marked for removal.",
        "unset_remove_architectures": "Architecture removal settings have been cleared.",
        "set_remove_encrypted_binaries": "Encrypted binaries will be removed.",
        "unset_remove_encrypted_binaries": "Encrypted binaries will not be removed.",
        "set_profile_removal": "Profile removal settings have been applied.",
        "unset_profile_removal": "Profile removal settings have been cleared.",
        "tweak_added_expecting_ipa": "Added: {file_name}. Waiting for ipa...",
        "error_while_resetting": "An error occurred while resetting variables. Try using the /c command. Error: {error}."
    },
    "TR": {
        "save_error": "{options} kaydedilemedi. Hata: {error}.",
        "read_decode_error": "{options} okunamadı. Hata: {error}.",
        "read_runtime_error": "Okuma sırasında bir hata oluştu: {error}.",
        "update_error": "{options} güncellenemedi. Hata: {error}.",
        "app_name_usage": "Örnek Kullanım: /name (veya /n) <uygulama_adi> ",
        "set_app_name": "Uygulama adı **{name}** olarak ayarlandı.",
        "unset_app_name": "Uygulama adı değiştirilemedi.",
        "app_version_usage": "Örnek Kullanım: /version (veya /v) <uygulama_versiyonu> ",
        "set_app_version": "Uygulama sürümü **{version}** olarak ayarlandı.",
        "unset_app_version": "Uygulama sürümü değiştirilemedi.",
        "invalid_app_version": "Geçersiz format. Sadece rakam, nokta ve kısa çizgi kullanılabilir.",
        "app_id_usage": "Örnek Kullanım: /id (veya /b) <bundle_id>. Bundle ID aralığına keyfi bir metin girebilirsiniz.",
        "set_app_id": "Bundle ID **{id}** olaral ayarlandı.",
        "unset_app_id": "Uygulamanın Bundle ID’si değiştirilemedi.",
        "min_os_usage": "Örnek Kullanım: /setlimit (veya /nl) <minimum_os_versiyonu>",
        "set_min_os": "Minimum OS sürümü **{os_version}** olarak ayarlandı.",
        "unset_min_os": "Mininum OS sürümü değiştirilemedi.",
        "invalid_min_os": "Geçersiz OS sürümü formatı. Lütfen geçerli bir sürüm dizesi kullanın. Örnek Kullanım: 14.0",
        "set_install_restriction": "Kurulum kısıtlamaları uygulanmıştır.",
        "unset_install_restriction": "Kurulum kısıtlamaları kaldırılmıştır.",
        "set_remove_watchapp": "Apple Watch uygulaması kaldırma işlemi etkinleştirildi.",
        "unset_remove_watchapp": "Apple Watch uygulaması kaldırma işlemi devre dışı bırakıldı.",
        "set_file_support": "Dosya desteği etkinleştirildi. (Çalışmayabilir)",
        "unset_file_support": "Dosya desteği devre dışı bırakıldı.",
        "set_remove_architectures": "",
        "unset_remove_architectures": "",
        "set_remove_encrypted_binaries": "Şifrelenmiş dosyalar kaldırılacaktır.",
        "unset_remove_encrypted_binaries": "Şifrelenmiş dosyalar kaldırılmayacaktır.",
        "set_profile_removal": "",
        "unset_profile_removal": "",
        "tweak_added_expecting_ipa": "Eklendi: {file_name}. iPA bekleniyor...",
        "error_while_resetting": "Değişkenler sıfırlanırken bir hata oluştu. /c komutunu kullanmayı deneyin: {error}."
    },
    "RU": {
        "save_error": "Failed to save {options}. Error: {error}.",
        "read_decode_error": "Failed to read {options}. Error: {error}.",
        "read_runtime_error": "An error occurred while reading: {error}.",
        "update_error": "Failed to update {options}. Error: {error}.",
        "app_name_usage": "",
        "set_app_name": "The app name has been set to **{name}**.",
        "unset_app_name": "",
        "app_version_usage": "",
        "set_app_version": "The app version has been set to **{version}**.",
        "unset_app_version": "",
        "invalid_app_version": "",
        "app_id_usage": "",
        "set_app_id": "The app bundle ID has been set to **{id}**.",
        "unset_app_id": "",
        "min_os_usage": "",
        "set_min_os": "The minimum OS version has been set to **{os_version}**.",
        "unset_min_os": "",
        "invalid_min_os": "",
        "set_install_restriction": "",
        "unset_install_restriction": "",
        "set_remove_watchapp": "",
        "unset_remove_watchapp": "",
        "set_file_support": "",
        "unset_file_support": "",
        "set_remove_architectures": "",
        "unset_remove_architectures": "",
        "set_remove_encrypted_binaries": "",
        "unset_remove_encrypted_binaries": "",
        "set_profile_removal": "",
        "unset_profile_removal": "",
        "tweak_added_expecting_ipa": "Added: {file_name}. Waiting for ipa...",
        "error_while_resetting": "An error occurred while resetting variables. Try using the /c command. Error: {error}."
    },
    "DE": {
        "save_error": "Failed to save {options}. Error: {error}.",
        "read_decode_error": "Failed to read {options}. Error: {error}.",
        "read_runtime_error": "An error occurred while reading: {error}.",
        "update_error": "Failed to update {options}. Error: {error}.",
        "app_name_usage": "",
        "set_app_name": "The app name has been set to **{name}**.",
        "unset_app_name": "",
        "app_version_usage": "",
        "set_app_version": "The app version has been set to **{version}**.",
        "unset_app_version": "",
        "invalid_app_version": "",
        "app_id_usage": "",
        "set_app_id": "The app bundle ID has been set to **{id}**.",
        "unset_app_id": "",
        "min_os_usage": "",
        "set_min_os": "The minimum OS version has been set to **{os_version}**.",
        "unset_min_os": "",
        "invalid_min_os": "",
        "set_install_restriction": "",
        "unset_install_restriction": "",
        "set_remove_watchapp": "",
        "unset_remove_watchapp": "",
        "set_file_support": "",
        "unset_file_support": "",
        "set_remove_architectures": "",
        "unset_remove_architectures": "",
        "set_remove_encrypted_binaries": "",
        "unset_remove_encrypted_binaries": "",
        "set_profile_removal": "",
        "unset_profile_removal": "",
        "tweak_added_expecting_ipa": "Added: {file_name}. Waiting for ipa...",
        "error_while_resetting": "An error occurred while resetting variables. Try using the /c command. Error: {error}."
    },
}
# Plugins/sign.py
sign_strings = {
    "EN": {
        "no_cert_selected": "Hello, {user_first_name}! 😊\nIt seems like you forgot something. Please make your choice and resend the IPA! 🚀",
        "sign_error_retry": "An error occurred during signing, retrying... ({failed_sign_attempt}/{max_sign_attempt})",
        "signing_failed": "Failed to sign.\nThis issue is often caused by the IPA file or Telegram.",
        "unexpected_error": "An unexpected error occurred.\nIf this issue persists, please reach out to me.",
        "ipa_ready": "Hey! The IPA has been signed and is ready for upload.",
        "forgot_choice": "It seems like you forgot something. Please make your choice and resend the IPA!",
        "file_lost": "The file is lost during the signing operation.",
        "value_error": "A value error occurred during the signing operation.",
        "permission_error": "A permission error occurred during the signing operation.",
        "signing_error": "The signing operation failed.",
        "unknown_error": "An unexpected error occurred during the signing operation.",
        "select_certificate_button": "Select Certificate 📝️️️️️️",
        "signing_in_progress": "📝",
        "executing_command": "Executing: {command}",
        "modify_retry_error": "An error occurred while modifying, retrying... ({failed_modify_attempt}/{max_modify_attempt})",
        "fnfe_err": "The file could not be found during the signing process.",
        "ve_err": "A value error occurred during the signing operation.",
        "pe_err": "A permission error occurred during the signing operation.",
        "sign_err": "The signing operation failed.",
        "unknown_sign_err": "An unknown error occurred during the signing operation."
    },
    "TR": {
        "no_cert_selected": "Merhaba, {user_first_name}! 😊\nGörünüşe göre bir şeyi unuttunuz. Lütfen seçiminizi yapın ve iPA'yı yeniden gönderin! 🚀",
        "sign_error_retry": "İmzalama sırasında bir hata oluştu, yeniden deniyorum... ({failed_sign_attempt}/{max_sign_attempt})",
        "signing_failed": "İmzalama işlemi başarısız oldu.\nBu sorun genellikle iPA dosyasından veya Telegram'dan kaynaklanmaktadır.",
        "unexpected_error": "Beklenmedik bir hata oluştu.\nBu sorun devam ederse, lütfen benimle iletişime geçin.",
        "ipa_ready": "Merhaba! iPA imzalandı ve yükleme için hazır.",
        "forgot_choice": "Görünüşe göre bir şeyi unuttunuz. Lütfen seçiminizi yapın ve iPA’yı yeniden gönderin!",
        "file_lost": "İmzalama işlemi sırasında dosya kayboldu.",
        "value_error": "İmzalama işlemi sırasında bir değer hatası oluştu.",
        "permission_error": "İmzalama işlemi sırasında bir izin hatası oluştu.",
        "signing_error": "İmzalama işlemi başarısız oldu.",
        "unknown_error": "İmzalama işlemi sırasında beklenmedik bir hata oluştu.",
        "select_certificate_button": "Sertifika Seçin 📝️️️️️️",
        "signing_in_progress": "📝",
        "executing_command": "Çalıştırılıyor: {command}",
        "modify_retry_error": "Düzenleme sırasında bir hata oluştu, yeniden deniyorum... ({failed_modify_attempt}/{max_modify_attempt})",
        "fnfe_err": "İmzalama sürecinde dosya bulunamadı.",
        "ve_err": "İmzalama işlemi sırasında bir değer hatası oluştu.",
        "pe_err": "İmzalama işlemi sırasında bir izin hatası oluştu.",
        "sign_err": "İmzalama işlemi başarısız oldu.",
        "unknown_sign_err": "İmzalama işlemi sırasında bilinmeyen bir hata oluştu."
    },
    "RU": {
        "no_cert_selected": "Привет, {user_first_name}! 😊\nПохоже, вы что-то забыли. Пожалуйста, сделайте выбор и отправьте IPA снова! 🚀",
        "sign_error_retry": "Произошла ошибка при подписании, повторная попытка... ({failed_sign_attempt}/{max_sign_attempt})",
        "signing_failed": "Не удалось подписать.\nПроблема, скорее всего, связана с IPA-файлом или Telegram.",
        "unexpected_error": "Произошла неожиданная ошибка.\nЕсли проблема продолжится, пожалуйста, свяжитесь со мной.",
        "ipa_ready": "Готово! IPA подписан и готов к загрузке.",
        "forgot_choice": "Похоже, вы что-то забыли. Пожалуйста, сделайте выбор и отправьте IPA снова!",
        "file_lost": "Файл потерян во время операции подписания.",
        "value_error": "Ошибка значения во время операции подписания.",
        "permission_error": "Ошибка доступа во время операции подписания.",
        "signing_error": "Операция подписания не удалась.",
        "unknown_error": "Произошла неизвестная ошибка во время операции подписания.",
        "select_certificate_button": "Выбрать сертификат 📝️️️️️️",
        "signing_in_progress": "📝",
        "executing_command": "Выполняется: {command}",
        "modify_retry_error": "Произошла ошибка при модификации, повторная попытка... ({failed_modify_attempt}/{max_modify_attempt})",
        "fnfe_err": "Файл не найден во время операции подписания.",
        "ve_err": "Произошла ошибка значения во время операции подписания.",
        "pe_err": "Произошла ошибка доступа во время операции подписания.",
        "sign_err": "Операция подписания не удалась.",
        "unknown_sign_err": "Произошла неизвестная ошибка во время операции подписания."
    },
    "DE": {
        "no_cert_selected": "Hallo, {user_first_name}! 😊\nAnscheinend hast du etwas vergessen. Bitte triff deine Wahl und sende die IPA erneut! 🚀",
        "sign_error_retry": "Beim Signieren ist ein Fehler aufgetreten, neuer Versuch... ({failed_sign_attempt}/{max_sign_attempt})",
        "signing_failed": "Signierung fehlgeschlagen.\nDieses Problem wird oft durch die IPA-Datei oder Telegram verursacht.",
        "unexpected_error": "Ein unerwarteter Fehler ist aufgetreten.\nWenn dieses Problem weiterhin besteht, kontaktiere mich bitte.",
        "ipa_ready": "Hey! Die IPA wurde signiert und ist bereit zum Upload.",
        "forgot_choice": "Anscheinend hast du etwas vergessen. Bitte triff deine Wahl und sende die IPA erneut!",
        "file_lost": "Die Datei ging während des Signierungsvorgangs verloren.",
        "value_error": "Ein Wertfehler ist während des Signierungsvorgangs aufgetreten.",
        "permission_error": "Ein Berechtigungsfehler ist während des Signierungsvorgangs aufgetreten.",
        "signing_error": "Der Signierungsvorgang ist fehlgeschlagen.",
        "unknown_error": "Ein unerwarteter Fehler ist während des Signierungsvorgangs aufgetreten.",
        "select_certificate_button": "Zertifikat auswählen 📝️️️️️️",
        "signing_in_progress": "📝",
        "executing_command": "Ausführung: {command}",
        "modify_retry_error": "Beim Modifizieren ist ein Fehler aufgetreten, neuer Versuch... ({failed_modify_attempt}/{max_modify_attempt})"
    }
}
# Plugins/speedtest.py
speedtest_strings = {
    "EN": {
        "speedtest_start": "🚀 Testing internet speed...",
        "network_error": "Network Error: Please check your internet connection and try again.",
        "timeout_error": "Error: Request timed out.",
        "unknown_error": "Error: An unexpected error occurred.",
    },
    "TR": {
        "speedtest_start": "🚀 Internet hızı test ediliyor.",
        "network_error": "Ağ Hatası: Lütfen internet bağlantınızı kontrol edin ve tekrar deneyin.",
        "timeout_error": "Hata: İstek zaman aşımına uğradı.",
        "unknown_error": "Hata: Beklenmeyen bir hata oluştu.",
    },
    "RU": {
        "speedtest_start": "🚀 Тестирование скорости интернета...",
        "network_error": "Ошибка сети: Пожалуйста, проверьте ваше интернет-соединение и попробуйте снова.",
        "timeout_error": "Ошибка: Время ожидания запроса истекло.",
        "unknown_error": "Ошибка: Произошла непредвиденная ошибка.",
    },
    "DE": {
        "speedtest_start": "🚀 Teste Internetgeschwindigkeit...",
        "network_error": "Netzwerkfehler: Bitte überprüfe deine Internetverbindung und versuche es erneut.",
        "timeout_error": "Fehler: Zeitüberschreitung der Anfrage.",
        "unknown_error": "Fehler: Ein unerwarteter Fehler ist aufgetreten.",
    }
}
# Plugins/start.py
start_strings = {
    "EN": {
        "welcome_registered": "Hello! {name}\nPlease select a certificate to begin.",
        "welcome_unregistered": "Hello, {name}!\n Sorry, you are not authorized to use the bot.\n\n▸ If you have a certificate from AppleFavour, please contact us for authorization using the button below. If you do not have a certificate, you can contact us to purchase one.",
        "select_certificate": "Select certificate 📝️",
        "select_compression": "Select compression ratio 📚",
        "select_language": "Select Language 🌐",
        "approval_purchase": "Get Approval / Purchase"
    },
    "TR": {
        "welcome_registered": "Merhaba! {name}\nBaşlamak için lütfen bir sertifika seçin.",
        "welcome_unregistered": "Merhaba, {name}!\nÜzgünüm, botu kullanabilmek için yetkiniz bulunmamaktadır.\n\n▸ Eğer AppleFavour’dan alınmış bir sertifikanız varsa, yetkilendirme için aşağıdaki butonu kullanarak bizimle iletişime geçin. Sertifikanız yoksa satın almak için iletişime geçebilirsiniz.",
        "select_certificate": "Sertifika Seçin 📝️",
        "select_compression": "Sıkıştırma Oranını Seçin 📁",
        "select_language": "Dil Seçin 🌐",
        "approval_purchase": "Onay / Satın Al"
    },
    "RU": {
        "welcome_registered": "Привет! {name}\nПожалуйста, выберите сертификат, чтобы начать.",
        "welcome_unregistered": "Привет, {name}!\nИзвините, для использования бота требуется одобрение администратора.\n\n▸ Если у вас есть сертификат, свяжитесь с нами через кнопку ниже для получения одобрения, или для покупки, если у вас его нет.",
        "select_certificate": "Выбрать сертификат 📝️",
        "select_compression": "Выбрать степень сжатия 📚",
        "select_language": "Выбрать язык 🌐",
        "approval_purchase": "Получить одобрение / Купить"
    },
    "DE": {
        "welcome_registered": "Hallo! {name}\nBitte wähle ein Zertifikat aus, um zu beginnen.",
        "welcome_unregistered": "Hallo, {name}!\nEntschuldigung, du benötigst die Genehmigung eines Administrators, um den Bot zu nutzen.\n\n▸ Wenn du ein Zertifikat hast, kontaktiere uns über den Button unten für die Genehmigung, oder um eines zu kaufen, falls du keines hast.",
        "select_certificate": "Zertifikat auswählen 📝️",
        "select_compression": "Komprimierungsgrad auswählen 📚",
        "select_language": "Sprache auswählen 🌐",
        "approval_purchase": "Genehmigung / Kauf"
    }
}
# Plugins/user_management.py
user_management_strings = {
    "EN": {
        "admin_only": "Sorry, only administrators can perform database operations. (Permission denied)",
        "invalid_command": "Invalid command usage.\n(/,!)premium and (/,!)pre 1071675334\nOR\n(/,!)user and (/,!)k 1071675334",
        "user_not_found": "User `{user_id}` not found.",
        "user_added": "User `{user_id}` added.",
        "user_removed": "User `{user_id}` removed.",
        "premium_added": "User `{user_id}` upgraded to premium, expires on {expiry_date}.",
        "premium_removed": "User `{user_id}` removed from premium plan.",
        "premium_reg_error": "Error occurred during premium registration. Please try again.",
        "premium_unreg_error": "Error occurred during premium removal. Please try again.",
        "not_enough_arguments": "Not enough arguments, You need to provide a user ID(s). /user user1.ID ..."
    },
    "TR": {
        "admin_only": "Üzgünüm, Botun veri tabanidaki islemleri, sadece yöneticiler gerceklestirilebilir. (Permission denied)",
        "invalid_command": "Hatalı komut kullanımı.\n(/,!)premium and (/,!)pre 1071675334\nOR\n(/,!)user and (/,!)k 1071675334",
        "user_not_found": "Kullanıcı `{user_id}` bulunamadı.",
        "user_added": "Kullanıcı `{user_id}` eklendi.",
        "user_removed": "Kullanıcı `{user_id}` silindi.",
        "premium_added": "Kullanıcı `{user_id}` premium'a yukseltildi, {expiry_date} tarihinde sona erecek.",
        "premium_removed": "Kullanıcı `{user_id}` premium planindan cikartildi.",
        "premium_reg_error": "Premium üyelik kaydında bir hata oluştu. Lütfen tekrar deneyin.",
        "premium_unreg_error": "Premium üyelik iptali sırasında bir hata oluştu. Lütfen tekrar deneyin.",
        "not_enough_arguments": ""
    },
    "RU": {
        "admin_only": "Извините, только администраторы могут выполнять операции с базой данных. (Permission denied)",
        "invalid_command": "Неверное использование команды.\n(/,!)premium и (/,!)pre 1071675334\nИли\n(/,!)user и (/,!)k 1071675334",
        "user_not_found": "Пользователь `{user_id}` не найден.",
        "user_added": "Пользователь `{user_id}` добавлен.",
        "user_removed": "Пользователь `{user_id}` удален.",
        "premium_added": "Пользователь `{user_id}` был переведен в премиум, срок действия истекает {expiry_date}.",
        "premium_removed": "Пользователь `{user_id}` удален из премиум-плана.",
        "premium_reg_error": "Произошла ошибка при регистрации премиум. Пожалуйста, попробуйте снова.",
        "premium_unreg_error": "Произошла ошибка при удалении премиум. Пожалуйста, попробуйте снова.",
        "not_enough_arguments": ""
    },
    "DE": {
        "admin_only": "Entschuldigung, nur Administratoren können Datenbankoperationen durchführen. (Zugriff verweigert)",
        "invalid_command": "Ungültige Befehlsverwendung.\n(/,!)premium und (/,!)pre 1071675334\nODER\n(/,!)user und (/,!)k 1071675334",
        "user_not_found": "Benutzer `{user_id}` nicht gefunden.",
        "user_added": "Benutzer `{user_id}` hinzugefügt.",
        "user_removed": "Benutzer `{user_id}` entfernt.",
        "premium_added": "Benutzer `{user_id}` auf Premium hochgestuft, läuft am {expiry_date} ab.",
        "premium_removed": "Benutzer `{user_id}` aus dem Premium-Plan entfernt.",
        "premium_reg_error": "Fehler bei der Premium-Registrierung. Bitte versuchen Sie es erneut.",
        "premium_unreg_error": "Fehler bei der Premium-Entfernung. Bitte versuchen Sie es erneut.",
        "not_enough_arguments": ""
    }
}
# utils/certificate_handler.py
certificate_handler_strings = {
    "EN": {
        "permission_denied": "You cannot add a new certificate. (Permission denied)",
        "certificate_updated": "Certificate updated: {file_name}",
        "unexpected_git_error": "Unexpected git error: {error}",
        "unexpected_error": "Unexpected error: {error}",
    },
    "TR": {
        "permission_denied": "Yeni sertifika ekleyemezsin. (İzin verilmedi)",
        "certificate_updated": "Sertifika güncellendi: {file_name}",
        "unexpected_git_error": "Beklenmeyen git hatası: {error}",
        "unexpected_error": "Beklenmeyen hata: {error}",
    },
    "RU": {
        "permission_denied": "Вы не можете добавить новый сертификат. (Доступ запрещен)",
        "certificate_updated": "Сертификат обновлен: {file_name}",
        "unexpected_git_error": "Неожиданная ошибка git: {error}",
        "unexpected_error": "Неожиданная ошибка: {error}",
    },
    "DE": {
        "permission_denied": "Sie können kein neues Zertifikat hinzufügen. (Zugriff verweigert)",
        "certificate_updated": "Zertifikat aktualisiert: {file_name}",
        "unexpected_git_error": "Unerwarteter Git-Fehler: {error}",
        "unexpected_error": "Unerwarteter Fehler: {error}"
    }
}
# utils/main_helper.py
main_helper_strings = {
    "EN": {
        "unregistered_user": "Hello, please contact an administrator. (Unregistered user)",
        "unsupported_file_type": "I honestly don't know what to do with this {file_extension} :(",
        "cooldown_wait": "Hey! {user}, please wait {time_to_wait} seconds before uploading another file...",
        "cooldown_update": "Please wait {time_to_wait} seconds before uploading another file...",
        "download_starting": "⏳ **Download pending**",  # !!
        "high_demand": "Request on hold due to high demand.",
        "reply_or_send_ipa_prompt": "Please reply to a message or send an IPA file or a URL containing an IPA."
    },
    "TR": {
        "unregistered_user": "Merhaba, bir yönetici ile iletişime geçin. (Kayıtsız kullanıcı)",
        "unsupported_file_type": "Cidden bu {file_extension} ile ne yapacağımı bilmiyorum :(",
        "cooldown_wait": "Hop! {user}, lütfen başka bir dosya yüklemeden önce {time_to_wait} saniye bekleyiniz...",
        "cooldown_update": "Lütfen başka bir dosya yüklemeden önce {time_to_wait} saniye bekleyiniz...",
        "download_starting": "⏳ **İndirme bekleniyor**",  # !!
        "high_demand": "Yoğun talepten dolayı istek bekletiliyor.",
        "reply_or_send_ipa_prompt": "Bir mesaja yanıt verin veya bir IPA dosyası ya da IPA içeren bir URL gönderin."
    },
    "RU": {
        "unregistered_user": "Здравствуйте, свяжитесь с администратором. (Незарегистрированный пользователь)",
        "unsupported_file_type": "Честно говоря, я не знаю, что делать с этим {file_extension} :(",
        "cooldown_wait": "Эй! {user}, подождите {time_to_wait} секунд перед загрузкой другого файла...",
        "cooldown_update": "Подождите {time_to_wait} секунд перед загрузкой другого файла...",
        "download_starting": "⏳ **Ожидание загрузки**",  # !!
        "high_demand": "Запрос отложен из-за высокой нагрузки.",
        "reply_or_send_ipa_prompt": "Ответьте на сообщение или отправьте файл IPA или URL, содержащий IPA."
    },
    "DE": {
        "unregistered_user": "Hallo, bitte kontaktieren Sie einen Administrator. (Nicht registrierter Benutzer)",
        "unsupported_file_type": "Ich weiß ehrlich gesagt nicht, was ich mit dieser {file_extension} anfangen soll :(",
        "cooldown_wait": "Hey! {user}, bitte warten Sie {time_to_wait} Sekunden, bevor Sie eine weitere Datei hochladen...",
        "cooldown_update": "Bitte warten Sie {time_to_wait} Sekunden, bevor Sie eine weitere Datei hochladen...",
        "download_starting": "⏳ **Download ausstehend**",  # !!
        "high_demand": "Anfrage aufgrund hoher Nachfrage in Warteschleife.",
        "reply_or_send_ipa_prompt": "Bitte antworten Sie auf eine Nachricht oder senden Sie eine IPA-Datei oder eine URL mit einer IPA."

    }
}
# utils/restart.py
restart_strings = {
    "EN": {
        "restart_declined": "Sorry, only admins can restart bot. (Permission denied)",
        "restart_requested": "Restart requested by {user_first_name} - @{username} {process_id}",
        "shutdown_declined": "Sorry, only admins can shutdown bot. (Permission denied)",
        "shutdown_requested": "Shutdown requested by {user_first_name} - @{username} {process_id}",
        "restart_awaiting": "⚠️ Some directories still remain in {web_path}.\nWaiting for cleanup to complete...\n⌛️ Elapsed: {time_elapsed}.",
        "restart_in_progress": "🔁 Bot is restarting...\n⌛️ Total elapsed: {time_elapsed}."
    },
    "TR": {
        "restart_declined": "Uzgunum, sadece adminler botu yeniden baslatabilir. (İzin reddedildi)",
        "restart_requested": "Yeniden baslatma talebi {user_first_name} - @{username} {process_id}",
        "shutdown_declined": "Uzgunum, sadece adminler botu kapatabilir. (İzin reddedildi)",
        "shutdown_requested": "Kapatma talebi {user_first_name} - @{username} {process_id}",
        "restart_awaiting": "⚠️ {web_path} Temizlenme tamamlanana kadar bekleniyor...\n⌛️ Gecen sure: {time_elapsed}.",
        "restart_in_progress": "🔁 Bot Yeniden başlatiliyor...\n⌛️ Toplam süre: {time_elapsed}."
    },
    "RU": {
        "restart_declined": "Извините, только администраторы могут перезапустить бота. (Отказано в доступе)",
        "restart_requested": "Перезапуск запрошен {user_first_name} - @{username} {process_id}",
        "shutdown_declined": "Извините, только администраторы могут отключить бота. (Отказано в доступе)",
        "shutdown_requested": "Отключение запрошено {user_first_name} - @{username} {process_id}",
        "restart_awaiting": "⚠️ {web_path} папка осталась.\nОжидание завершения очистки...\n⌛️ Прошло времени: {time_elapsed}.",
        "restart_in_progress": "🔁 Бот перезапускается...\n⌛️ Прошло времени: {time_elapsed}."
    },
    "DE": {
        "restart_declined": "Entschuldigung, nur Administratoren können den Bot neustarten. (Zugriff verweigert)",
        "restart_requested": "Neustart angefordert von {user_first_name} - @{username} {process_id}",
        "shutdown_declined": "Entschuldigung, nur Administratoren können den Bot herunterfahren. (Zugriff verweigert)",
        "shutdown_requested": "Herunterfahren angefordert von {user_first_name} - @{username} {process_id}",
        "restart_awaiting": "⚠️ Einige Verzeichnisse bleiben noch in {web_path}.\nWarte auf Abschluss der Bereinigung...\n⌛️ Vergangen: {time_elapsed}.",
        "restart_in_progress": "🔁 Bot wird neugestartet...\n⌛️ Gesamtzeit vergangen: {time_elapsed}."
    }
}
# utils/run_cmd.py
run_cmd_strings = {
    "EN": {
        "correct_usage": "Usage: /exec <command>",
        "admin_only_msg": "Sorry, only admins can execute commands. (Permission denied)",
        "exec_cmd_exception": "{userID} {username} - Error while executing command: {user_error_message}",
        "command_out": "Command output:\n{stdout}\n",
        "command_err": "Command error:\n{stderr}\n"
    },
    "TR": {
        "correct_usage": "Kullanim: /exec <komut>",
        "admin_only_msg": "Sorry, only admins can execute commands. (Permission denied)",
        "exec_cmd_exception": "{userID} {username} - Komut calistirirken hata olustu: {user_error_message}",
        "command_out": ":\n{stdout}\n",
        "command_err": ":\n{stderr}\n"
    },
    "RU": {
        "correct_usage": "",
        "admin_only_msg": "",
        "exec_cmd_exception": "{userID} {username} - : {user_error_message}",
        "command_out": ":\n{stdout}\n",
        "command_err": ":\n{stderr}\n"
    },
    "DE": {
        "correct_usage": "Verwendung: /exec <Befehl>",
        "admin_only_msg": "Entschuldigung, nur Administratoren können Befehle ausführen. (Zugriff verweigert)",
        "exec_cmd_exception": "{userID} {username} - Fehler bei der Ausführung des Befehls: {user_error_message}",
        "command_out": "Befehlsausgabe:\n{stdout}\n",
        "command_err": "Befehlsfehler:\n{stderr}\n"
    }
}
# utils/helpers.py
helpers_strings = {
    "EN": {
        "create_folder_error": "Error while creating folder: {error}",
        "hour": "Hour",
        "minute": "Minute",
        "second": "Second",
        "hour_ETA": "{remaining_time} H",
        "minute_ETA": "{remaining_time} M",
        "second_ETA": "{remaining_time} S",
        "ETA": "ETA: {estimated_remaining_download_time}",
        "file_is_lost": "I managed to lose file, i saw it moments ago, where did it go?",
        "file_format_error": "ipa file format is broken.",  # ipa file is not a zip.
        "file_size_unexpected": "Download interrupted unexpectedly. Downloaded: {downloaded}, Expected: {expected}",
        "error": "ERROR: {error}"
    },
    "TR": {
        "create_folder_error": "Hata: {error}",
        "hour": "Saat",
        "minute": "Dakika",
        "second": "Saniye",
        "hour_ETA": "{remaining_time} S",
        "minute_ETA": "{remaining_time} Dk",
        "second_ETA": "{remaining_time} Sn",
        "ETA": "Kalan: {estimated_remaining_download_time}",
        "file_is_lost": "",
        "file_format_error": "",
        "file_size_unexpected": "{downloaded}, {expected}",
        "error": "{error}"
    },
    "RU": {
        "create_folder_error": ": {error}",
        "hour": "",
        "minute": "",
        "second": "",
        "hour_ETA": "{remaining_time}",
        "minute_ETA": "{remaining_time}",
        "second_ETA": "{remaining_time}",
        "ETA": ": {estimated_remaining_download_time}",
        "file_is_lost": "",
        "file_format_error": "",
        "file_size_unexpected": "{downloaded}, {expected}",
        "error": "{error}"
    },
    "DE": {
        "create_folder_error": ": {error}",
        "hour": "",
        "minute": "",
        "second": "",
        "hour_ETA": "{remaining_time}",
        "minute_ETA": "{remaining_time}",
        "second_ETA": "{remaining_time}",
        "ETA": ": {estimated_remaining_download_time}",
        "file_is_lost": "",
        "file_format_error": "",
        "file_size_unexpected": "{downloaded}, {expected}",
        "error": "{error}"
    }
}
