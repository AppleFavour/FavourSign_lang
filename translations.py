# Plugins/announcements.py
announcements_strings = {
    "EN": {
        "no_reply": "🔍 Announcement message not found. Please reply to a message and try again.",
        "no_content": "🔍 Announcement content not found. Please reply to a message with text or a file.",
        "permission_denied": "🚫 You do not have permission to perform this action.",
        "announcement_complete": "✅ Announcement completed.\n\nTotal users: {total}\nSent: {sent}\nNot sent: {failed}",
    },
    "TR": {
        "no_reply": "🔍 Duyuru mesajı bulunamadı. Lütfen bir mesajı yanıtlayıp tekrar deneyiniz.",
        "no_content": "🔍 Duyuru içeriği bulunamadı. Lütfen metin veya dosya içeren bir mesajı yanıtlayınız.",
        "permission_denied": "🚫 Bunu yapmaya yetkin yok.",
        "announcement_complete": "✅ Duyuru tamamlandı.\n\nToplam kullanıcı: {total}\nİletilen: {sent}\nİletilemeyen: {failed}",
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
        "cert_loading_error": "⚠️ Sertifika bilgileri yüklenirken bir hata oldu.",
        "select_certificate_prompt": "📃 Sertifika seçiminizi yapınız.\nSeçilen: {selected}",
        "cert_saved": "📌 Sertifika seçildi: {cert_name}",
        "already_selected": "⚠️ Zaten seçilmiş",
        "back_button": "Geri Dön 🔙",
        "saving_error": "Bir veritabanı hatası oluştu. Lütfen daha sonra tekrar deneyiniz.",
        "callback_error": "⚠️ Bir hata oldu.",
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
            "📚 Select the compression level\n"
            "Selected: {selected}\n"
            "This setting determines the bot's speed and the size of the signed file.\n\n"
            "⬢ **0** — **Fastest Signing**, **Minimum Compression (Larger File Size)**\n"
            "⬢ **9** — **Slowest Signing**, **Maximum Compression (Smaller File Size)**"
        ),
        "already_selected": "⚠️ Already selected.",
        "save_error": "Compression level could not be saved.",
        "compression_selected": (
            "📌 Compression level selected: {selected}\n\n"
            "This setting determines the bot's speed and the size of the signed file.\n\n"
            "⬢ **0** — **Fastest Signing**, **Minimum Compression (Larger File Size)**\n"
            "⬢ **9** — **Slowest Signing**, **Maximum Compression (Smaller File Size)**"
        ),
        "selected_notification": "📌 Selected: {selected}",
        "generic_error": "⚠️ An error occurred.",
        "back_button": "Go Back 🔙",
    },
    "TR": {
        "compression_prompt": (
            "📚 Sıkıştırma oranı seçiniz\n"
            "Seçilen: {selected}\n"
            "Bu ayar, botun hızı ve imzalanan dosyasının boyutunu belirleyen seçenektir.\n\n"
            "⬢ **0** — **En Hızlı İmzalama**, **Minimum Sıkıştırma (Dosya boyutu daha büyük)**\n"
            "⬢ **9** — **En Yavaş İmzalama**, **Maksimum Sıkıştırma (Dosya boyutu daha küçük)**"
        ),
        "already_selected": "⚠️ Zaten seçtiniz.",
        "save_error": "Sıkıştırma oranı kaydedilemedi.",
        "compression_selected": (
            "📌 Sıkıştırma oranı seçildi: {selected}\n\n"
            "Bu ayar, botun hızı ve imzalanan dosyasının boyutunu belirleyen seçenektir.\n\n"
            "⬢ **0** — **En Hızlı İmzalama**, **Minimum Sıkıştırma (Dosya boyutu daha büyük)**\n"
            "⬢ **9** — **En Yavaş İmzalama**, **Maksimum Sıkıştırma (Dosya boyutu daha küçük)**"
        ),
        "selected_notification": "📌 Seçilen: {selected}",
        "generic_error": "⚠️ Bir hata oldu.",
        "back_button": "Geri Dön 🔙",
    },
    "RU": {
        "compression_prompt": (
            "📚 Выберите уровень сжатия\n"
            "Выбран: {selected}\n"
            "Эта настройка определяет скорость бота и размер подписанного файла.\n\n"
            "⬢ **0** — **Самая Быстрая Подпись**, **Минимальное Сжатие (Больший Размер Файла)**\n"
            "⬢ **9** — **Самая Медленная Подпись**, **Максимальное Сжатие (Меньший Размер Файла)**"
        ),
        "already_selected": "⚠️ Уже выбрано.",
        "save_error": "Не удалось сохранить уровень сжатия.",
        "compression_selected": (
            "📌 Выбран уровень сжатия: {selected}\n\n"
            "Эта настройка определяет скорость бота и размер подписанного файла.\n\n"
            "⬢ **0** — **Самая Быстрая Подпись**, **Минимальное Сжатие (Больший Размер Файла)**\n"
            "⬢ **9** — **Самая Медленная Подпись**, **Максимальное Сжатие (Меньший Размер Файла)**"
        ),
        "selected_notification": "📌 Выбрано: {selected}",
        "generic_error": "⚠️ Произошла ошибка.",
        "back_button": "Назад 🔙"
    },
    "DE": {
        "compression_prompt": (
            "📚 Wähle die Komprimierungsstufe\n"
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
            "⬢ **0** — **Schnellste Signierung**, **Minimale Komprimierung (Größere Dateigröße)**\n"
            "⬢ **9** — **Langsamste Signierung**, **Maximale Komprimierung (Kleinere Dateigröße)**"
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
        "explore_button": "🔎 Discover more",
        "mnm_notify": "Do you see this because message.edit_text is failed"
    },
    "TR": {
        "signed": "İmzalandı",
        "app_name": "Uygulama adı",
        "bundle_id": "Uygulama ID",
        "certificate": "Sertifika",
        "install_button": "📲 Yükle",
        "explore_button": "🔎 Daha fazla iPA",
        "mnm_notify": "Mesaj duzenlenirken bir hata olustu"
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
        "download_pending": "⏳ **Download pending**",
        "nothing_to_download": "Please send a direct link or file",
        "download_failed_message": "❌ {file_name} can't be downloaded!",
        "download_attempt_failed_message": "An error occurred while downloading {file_name}, retrying... ({attempt + 1}/{max_attempts})",
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
        "retrying_message": "Retrying download... ({attempt + 1}/{max_attempts})"
    },
    "TR": {
        "download_pending": "⏳ **İndirme bekleniyor**",
        "nothing_to_download": "Lütfen bir dosya veya doğrudan indirme URL gönderin",
        "download_failed_message": "❌ {file_name} indirilemedi!",
        "download_attempt_failed_message": "{file_name} indirilirken bir hata oluştu, tekrar deneniyor... ({attempt + 1}/{max_attempts})",
        "download_successful_message": "✅ {file_name} başarıyla indirildi!",
        "download_error_detected": "İndirme sırasında bir hata algılandı",
        "httpnot200": "Burada görmeye değer bir şey yok.",
        "httpnotfile": "İndirilecek bir şey yok.",
        "connection_error": "Bağlantı kurulamadı.",
        "unexpected_response_error": "Sunucudan beklenmeyen yanıt alındı.",
        "invalid_url_error": "Geçersiz URL sağlandı.",
        "too_many_redirects_error": "Çok fazla yönlendirme yapıldı.",
        "ssl_error": "SSL bağlantı hatası.",
        "payload_error": "Eksik veya hatalı veri alındı.",
        "server_disconnected_error": "Sunucu bağlantısı kesildi.",
        "general_download_error": "Dosya indirilirken bir hata oluştu.",
        "file_not_found_error": "Dosya bulunamadı.",
        "file_corrupted_error": "Bozuk dosya tespit edildi.",
        "unknown_exception_error": "Beklenmeyen bir hata oluştu.",
        "retrying_message": "İndirme tekrar deneniyor... ({attempt + 1}/{max_attempts})"
    },
    "RU": {
        "download_pending": "⏳ **Ожидание загрузки**",
        "nothing_to_download": "Пожалуйста, отправьте файл или прямую ссылку для скачивания",
        "download_failed_message": "❌ {file_name} не может быть скачан!",
        "download_attempt_failed_message": "Ошибка при скачивании {file_name}, повторная попытка... ({attempt + 1}/{max_attempts})",
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
        "retrying_message": "Повторная попытка загрузки... ({attempt + 1}/{max_attempts})"
    },
    "DE": {
        "download_pending": "⏳ **Download ausstehend**",
        "nothing_to_download": "Bitte sende einen direkten Link oder eine Datei",
        "download_failed_message": "❌ {file_name} kann nicht heruntergeladen werden!",
        "download_attempt_failed_message": "Ein Fehler ist beim Herunterladen von {file_name} aufgetreten, neuer Versuch... ({attempt + 1}/{max_attempts})",
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
        "retrying_message": "Download wird wiederholt... ({attempt + 1}/{max_attempts})"
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
        "info_cmd": "Bot bilgilerini görüntüler.",
        "sign_cmd": "Herhangi bir ipa dosyasını gönderir veya yanıtlar.",
        "clear_cmd": "Düzenleme seçeneklerini devre dışı bırakır.",
        "profile_cmd": "iPA dosyasından gömülü mobil provizyon dosyasını kaldırır.",
        "stripencslices_cmd": "iPA dosyasından şifrelenmiş dilimleri kaldırır.",
        "stripslices_cmd": "iPA dosyasından arm64 olmayan dilimleri kaldırır.",
        "filesupport_cmd": "Eğer uygulama destekliyorsa 'Dosyalar Uygulaması' desteğini düzeltmeye çalışır.",
        "watch_cmd": "iPA dosyasından saat uygulamasını kaldırır.",
        "rmdevicelimit_cmd": "Cihaza özel kurulum kısıtlamasını kaldırır.",
        "setlimit_cmd": "Minimum gerekli işletim sistemini belirler, kurulum kısıtlamasını aşmak için. - Garantisi yoktur.",
        "id_cmd": "Uygulamanın paket/bundle kimliğini değiştirir.",
        "version_cmd": "Uygulamanın paket/bundle sürümünü değiştirir.",
        "name_cmd": "Uygulamanın paket/bundle adını değiştirir.",
        "update_cmd": "Botu günceller (Depodan çekme işlemi yapar).",
        "duyur_cmd": "Tüm kayıtlı kullanıcılara duyuru yapar.",
        "exec_cmd": "Kabuk komutları çalıştırır.",
        "restart_cmd": "Botu yeniden başlatır.",
        "shutdown_cmd": "Botu kapatır.",
        "user_cmd": "Kullanıcıları veritabanına kaydeder/kaldırır.",
        "premium_cmd": "*Eski* Kullanıcıyı premium olarak işaretler, gelecekte özel içeriklere erişebilirler (eğer böyle bir içerik oluşturursam).",
        "unknown_exception": "@{username} ({userID}) kullanıcısından gelen yardım isteği işlenirken bir hata oluştu: {error}"
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
        "greeting": "Hello! {name}",
        "system_info": "\nSystem Information:\n",
        "bot_info": "\nBot Information:\n",
        "bot_stats": "{uptime} - {usage}",
        "total_users": "Registered Users: {count}",
        "active_users": "Active users: {count}",
    },
    "TR": {
        "greeting": "Merhaba! {name}",
        "system_info": "\nSistem özellikleri:\n",
        "bot_info": "\nBot hakkında:\n",
        "bot_stats": "{uptime} - {usage}",
        "total_users": "Kullanıcılar: {count}",
        "active_users": "Aktif kullanıcılar: {count}",
    },
    "RU": {
        "greeting": "Привет! {name}",
        "system_info": "\nСистемная информация:\n",
        "bot_info": "\nИнформация о боте:\n",
        "bot_stats": "{uptime} - {usage}",
        "total_users": "Пользователи: {count}",
        "active_users": "Активные пользователи: {count}",
    },
    "DE": {
        "greeting": "Hallo! {name}",
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
        "select_language": "🌐 Dil seçiniz",
        "selected": "Seçilen:",
        "already_selected": "Zaten seçili dili seçtiniz.",
        "save_failed": "Dil kaydedilemedi.",
        "new_language_selected": "🌐 Yeni dil seçildi",
        "error_in_language_selection": "Dil seçiminde bir hata oluştu.",
        "database_error": "Veritabanı hatası oluştu. Lütfen daha sonra tekrar deneyin.",
        "language_clear_success": "",
        "language_clear_failed": "",
        "back_button": "Geri Dön 🔙",
        "clear_button": "🧹"
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
# Plugins/modifier.py **to-do**
modifier_strings = {
    "EN": {},
    "TR": {},
    "RU": {},
    "DE": {},
}
# Plugins/sign.py
sign_strings = {
    "EN": {
        "greeting": "Hello, {message.from_user.first_name}! 😊\nIt seems like you forgot something. Please make your choice and resend the IPA! 🚀",
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
        "executing_command": "Executing: {command}",
        "modify_retry_error": "An error occurred while modifying, retrying... ({failed_modify_attempt}/{max_modify_attempt})",
        "fnfe_err": "The file could not be found during the signing process.",
        "ve_err": "A value error occurred during the signing operation.",
        "pe_err": "A permission error occurred during the signing operation.",
        "sign_err": "The signing operation failed.",
        "unknown_sign_err": "An unknown error occurred during the signing operation."
    },
    "TR": {
        "greeting": "Merhaba, {message.from_user.first_name}! 😊\nSanırım bir şey unuttunuz. Lütfen seçiminizi yapın ve IPA'yı tekrar göndermeyi unutmayın! 🚀",
        "sign_error_retry": "İmzalama sırasında hata oluştu, tekrar deneniyor... ({failed_sign_attempt}/{max_sign_attempt})",
        "signing_failed": "İmzalanamadı.\nBu sorun genellikle IPA dosyasından veya Telegram'dan kaynaklanabilir.",
        "unexpected_error": "Beklenmedik bir hata oluştu.\nEğer sorun devam ederse lütfen bana yazın.",
        "ipa_ready": "Hey! IPA imzalandı ve yüklenmeye hazır.",
        "forgot_choice": "Sanırım bir şey unuttunuz. Lütfen seçiminizi yapın ve IPA'yı tekrar göndermeyi unutmayın!",
        "file_lost": "Dosya imzalama işlemi sırasında kayboldu.",
        "value_error": "İmzalama işlemi sırasında bir değer hatası oluştu.",
        "permission_error": "İmzalama işlemi sırasında bir izin hatası oluştu.",
        "signing_error": "İmzalama işlemi başarısız oldu.",
        "unknown_error": "İmzalama işlemi sırasında beklenmedik bir hata oluştu.",
        "select_certificate_button": "Sertifika Seç 📝️️️️️️",
        "executing_command": "Çalıştırılıyor: {command}",
        "modify_retry_error": "Düzenleme sırasında hata oluştu, tekrar deneniyor... ({failed_modify_attempt}/{max_modify_attempt})",
        "fnfe_err": "Dosya imzalama işlemi sırasında bulunamadı.",
        "ve_err": "İmzalama işlemi sırasında bir değer hatası oluştu.",
        "pe_err": "İmzalama işlemi sırasında bir izin hatası oluştu.",
        "sign_err": "İmzalama işlemi başarısız oldu.",
        "unknown_sign_err": "İmzalama işlemi sırasında bilinmeyen bir hata oluştu."
    },
    "RU": {
        "greeting": "Привет, {message.from_user.first_name}! 😊\nПохоже, вы что-то забыли. Пожалуйста, сделайте выбор и отправьте IPA снова! 🚀",
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
        "executing_command": "Выполняется: {command}",
        "modify_retry_error": "Произошла ошибка при модификации, повторная попытка... ({failed_modify_attempt}/{max_modify_attempt})",
        "fnfe_err": "Файл не найден во время операции подписания.",
        "ve_err": "Произошла ошибка значения во время операции подписания.",
        "pe_err": "Произошла ошибка доступа во время операции подписания.",
        "sign_err": "Операция подписания не удалась.",
        "unknown_sign_err": "Произошла неизвестная ошибка во время операции подписания."
    },
    "DE": {
        "greeting": "Hallo, {message.from_user.first_name}! 😊\nAnscheinend hast du etwas vergessen. Bitte triff deine Wahl und sende die IPA erneut! 🚀",
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
        "welcome_unregistered": "Hello, {name}!\nSorry, you need admin approval to use the bot.\n\n▸ If you have a certificate, contact us using the button below for approval, or to purchase one if you don't have it.",
        "select_certificate": "Select certificate 📝️",
        "select_compression": "Select compression ratio 📚",
        "select_language": "Select Language 🌐",
        "approval_purchase": "Get Approval / Purchase"
    },
    "TR": {
        "welcome_registered": "Merhaba! {name}\nBaşlamak için sertifika seçimi yapınız.",
        "welcome_unregistered": "Merhaba, {name}!\nÜzgünüm, botu kullanabilmeniz için bir yetkilinin onay vermesi gerekiyor.\n\n▸ Sertifikanız varsa onay için, yoksa da satın almak için aşağıdaki butondan bize ulaşabilirsiniz.",
        "select_certificate": "Sertifika seç 📝️",
        "select_compression": "Sıkıştırma oranını seç 📚",
        "select_language": "Dil Seçimi 🌐",
        "approval_purchase": "Onay / Satın Almak İstiyorum"
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
        "archive_file_response": "I honestly don't know what to do with this {file_ext} :(",
        "specific_file_responses": {
            ".tipa": "You can only install this with TrollStore; {0} is useless here!",
            ".apk": "Seriously?! {0} = 'Android Package Kit (APK)' is useless here!",
        },
        "unsupported_text_file": "What is this, GTA cheat codes?",
        "unsupported_audio_file": "I forgot my headphones, can't listen to this :(",
        "unsupported_video_file": "I forgot my glasses, can't watch this :(",
        "cooldown_wait": "Hey! {user}, please wait {wait_time:.0f} seconds before uploading another file...",
        "cooldown_update": "Please wait {wait_time:.0f} seconds before uploading another file...",
        "high_demand": "Request on hold due to high demand: ({active}/{limit})",
        "reply_or_send_ipa_prompt": "Please reply to a message or send an IPA file or a URL containing an IPA."
    },
    "TR": {
        "unregistered_user": "Merhaba, bir yönetici ile iletişime geçin. (Kayıtsız kullanıcı)",
        "archive_file_response": "Cidden bu {file_ext} ile ne yapacağımı bilmiyorum :(",
        "specific_file_responses": {
            ".tipa": "Bunu yalnızca TrollStore ile kurabilirsiniz; {0} burada işe yaramaz!",
            ".apk": "Cidden mi?! {0} = 'Android Package Kit (APK)' burada işe yaramaz!",
        },
        "unsupported_text_file": "Bu ne böyle GTA hile kodu mu?",
        "unsupported_audio_file": "Kulaklıklarımı unuttum, bunu dinleyemem :(",
        "unsupported_video_file": "Gözlüklerimi unuttum, buna bakamam :(",
        "cooldown_wait": "Hop! {user}, lütfen başka bir dosya yüklemeden önce {wait_time:.0f} saniye bekleyiniz...",
        "cooldown_update": "Lütfen başka bir dosya yüklemeden önce {wait_time:.0f} saniye bekleyiniz...",
        "high_demand": "Yoğun talepten dolayı istek bekletiliyor: ({active}/{limit})",
        "reply_or_send_ipa_prompt": "Bir mesaja yanıt verin veya bir IPA dosyası ya da IPA içeren bir URL gönderin."
    },
    "RU": {
        "unregistered_user": "Здравствуйте, свяжитесь с администратором. (Незарегистрированный пользователь)",
        "archive_file_response": "Честно говоря, я не знаю, что делать с этим {file_ext} :(",
        "specific_file_responses": {
            ".tipa": "Вы можете установить это только через TrollStore; {0} здесь бесполезен!",
            ".apk": "Серьезно?! {0} = 'Android Package Kit (APK)' здесь бесполезен!",
        },
        "unsupported_text_file": "Что это, коды читов для GTA?",
        "unsupported_audio_file": "Я забыл наушники, не могу это послушать :(",
        "unsupported_video_file": "Я забыл очки, не могу это посмотреть :(",
        "cooldown_wait": "Эй! {user}, подождите {wait_time:.0f} секунд перед загрузкой другого файла...",
        "cooldown_update": "Подождите {wait_time:.0f} секунд перед загрузкой другого файла...",
        "high_demand": "Запрос отложен из-за высокой нагрузки: ({active}/{limit})",
        "reply_or_send_ipa_prompt": "Ответьте на сообщение или отправьте файл IPA или URL, содержащий IPA."
    },
    "DE": {
        "unregistered_user": "Hallo, bitte kontaktieren Sie einen Administrator. (Nicht registrierter Benutzer)",
        "archive_file_response": "Ich weiß ehrlich gesagt nicht, was ich mit dieser {file_ext} anfangen soll :(",
        "specific_file_responses": {
            ".tipa": "Sie können dies nur mit TrollStore installieren; {0} ist hier nutzlos!",
            ".apk": "Ernsthaft?! {0} = 'Android Package Kit (APK)' ist hier nutzlos!"
        },
        "unsupported_text_file": "Was ist das, GTA Cheat-Codes?",
        "unsupported_audio_file": "Ich habe meine Kopfhörer vergessen, kann das nicht hören :(",
        "unsupported_video_file": "Ich habe meine Brille vergessen, kann das nicht ansehen :(",
        "cooldown_wait": "Hey! {user}, bitte warten Sie {wait_time:.0f} Sekunden, bevor Sie eine weitere Datei hochladen...",
        "cooldown_update": "Bitte warten Sie {wait_time:.0f} Sekunden, bevor Sie eine weitere Datei hochladen...",
        "high_demand": "Anfrage aufgrund hoher Nachfrage in Warteschleife: ({active}/{limit})",
        "reply_or_send_ipa_prompt": "Bitte antworten Sie auf eine Nachricht oder senden Sie eine IPA-Datei oder eine URL mit einer IPA."

    }
}
# utils/restart.py
restart_strings = {
    "EN": {
        "restart_declined": "Sorry, only admins can restart bot. (Permission denied)",
        "restart_requested": "Restart requested by {userID} - @{username}",
        "shutdown_declined": "Sorry, only admins can shutdown bot. (Permission denied)",
        "shutdown_requested": "Shutdown requested by {userID} - @{username}",
        "restart_awaiting": "⚠️ Some directories still remain in {web_path}.\nWaiting for cleanup to complete...\n⌛️ Elapsed: {calculate_process_time((time.time() - start_time))}.",
        "restart_in_progress": "🔁 Bot is restarting...\n⌛️ Total elapsed: {calculate_process_time((time.time() - start_time))}."
    },
    "TR": {
        "restart_declined": "Uzgunum, sadece adminler botu yeniden baslatabilir. (İzin reddedildi)",
        "restart_requested": "Yeniden baslatma talebi - @{username}",
        "shutdown_declined": "Uzgunum, sadece adminler botu kapatabilir. (İzin reddedildi)",
        "shutdown_requested": "Kapatma talebi - @{username}",
        "restart_awaiting": "⚠️ {web_path} Temizlenme tamamlanana kadar bekleniyor...\n⌛️ Gecen sure: {calculate_process_time((time.time() - start_time))}.",
        "restart_in_progress": "🔁 Bot Yeniden başlatiliyor...\n⌛️ Toplam süre: {calculate_process_time((time.time() - start_time))}."
    },
    "RU": {
        "restart_declined": "Извините, только администраторы могут перезапустить бота. (Отказано в доступе)",
        "restart_requested": "Перезапуск запрошен - @{username}",
        "shutdown_declined": "Извините, только администраторы могут отключить бота. (Отказано в доступе)",
        "shutdown_requested": "Отключение запрошено - @{username}",
        "restart_awaiting": "⚠️ {web_path} папка осталась.\nОжидание завершения очистки...\n⌛️ Прошло времени: {calculate_process_time((time.time() - start_time))}.",
        "restart_in_progress": "🔁 Бот перезапускается...\n⌛️ Прошло времени: {calculate_process_time((time.time() - start_time))}."
    },
    "DE": {
        "restart_declined": "Entschuldigung, nur Administratoren können den Bot neustarten. (Zugriff verweigert)",
        "restart_requested": "Neustart angefordert von {userID} - @{username}",
        "shutdown_declined": "Entschuldigung, nur Administratoren können den Bot herunterfahren. (Zugriff verweigert)",
        "shutdown_requested": "Herunterfahren angefordert von {userID} - @{username}",
        "restart_awaiting": "⚠️ Einige Verzeichnisse bleiben noch in {web_path}.\nWarte auf Abschluss der Bereinigung...\n⌛️ Vergangen: {calculate_process_time((time.time() - start_time))}.",
        "restart_in_progress": "🔁 Bot wird neugestartet...\n⌛️ Gesamtzeit vergangen: {calculate_process_time((time.time() - start_time))}."
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
