# Plugins/announcements.py
announcements_strings = {
    "en": {
        "no_reply": "🔍 Please reply to a message to announce it.",
        "no_content": "🔍 The message you replied to has no content to announce.",
        "permission_denied": "🚫 You are not authorized to use this command.",
        "announcement_complete": "✅ Announcement sent successfully.\n\nTotal Recipients: {total}\nDelivered: {sent}\nFailed: {failed}",
    },
    "tr": {
        "no_reply": "🔍 Lütfen duyurmak için bir mesaja yanıt verin.",
        "no_content": "🔍 Yanıtladığınız mesajda duyurulacak bir içerik bulunmuyor.",
        "permission_denied": "🚫 Bu komutu kullanma yetkiniz yok.",
        "announcement_complete": "✅ Duyuru başarıyla gönderildi.\n\nToplam Alıcı: {total}\nUlaştırıldı: {sent}\nUlaştırılamadı: {failed}",
    },
    "ru": {
        "no_reply": "🔍 Пожалуйста, ответьте на сообщение, чтобы сделать объявление.",
        "no_content": "🔍 В сообщении, на которое вы ответили, нет содержимого для объявления.",
        "permission_denied": "🚫 У вас нет прав на использование этой команды.",
        "announcement_complete": "✅ Объявление успешно отправлено.\n\nВсего получателей: {total}\nДоставлено: {sent}\nНе доставлено: {failed}",
    },
    "de": {
        "no_reply": "🔍 Bitte antworte auf eine Nachricht, um sie anzukündigen.",
        "no_content": "🔍 Die Nachricht, auf die du geantwortet hast, hat keinen Inhalt zum Ankündigen.",
        "permission_denied": "🚫 Du bist nicht berechtigt, diesen Befehl zu verwenden.",
        "announcement_complete": "✅ Ankündigung erfolgreich gesendet.\n\nGesamtempfänger: {total}\nZugestellt: {sent}\nNicht zugestellt: {failed}",
    }
}

# Plugins/certificate_select.py
certificate_select_strings = {
    "en": {
        "cert_loading_error": "⚠️ Could not load certificate information.",
        "certificate_prompt": "📃 Please select a certificate.\nCurrently selected: {selected}",
        "certificate_selected": "📌 Certificate selected: {selected}",
        "cert_saved": "📌 Certificate saved: {cert_name}",
        "already_selected": "⚠️ This certificate is already selected.",
        "no_selection": "None",
        "back_button": "🔙 Go Back",
        "saving_error": "A database error occurred. Please try again.",
        "callback_error": "⚠️ An unexpected error occurred.",
    },
    "tr": {
        "cert_loading_error": "⚠️ Sertifika bilgileri yüklenemedi.",
        "certificate_prompt": "📃 Lütfen bir sertifika seçin.\nMevcut seçim: {selected}",
        "certificate_selected": "📌 Sertifika seçildi: {selected}",
        "cert_saved": "📌 Sertifika kaydedildi: {cert_name}",
        "already_selected": "⚠️ Bu sertifika zaten seçili.",
        "no_selection": "Hiçbiri",
        "back_button": "🔙 Geri Dön",
        "saving_error": "Bir veritabanı hatası oluştu. Lütfen tekrar deneyin.",
        "callback_error": "⚠️ Beklenmedik bir hata oluştu.",
    },
    "ru": {
        "cert_loading_error": "⚠️ Не удалось загрузить информацию о сертификате.",
        "certificate_prompt": "📃 Пожалуйста, выберите сертификат.\nТекущий выбор: {selected}",
        "certificate_selected": "📌 Сертификат выбран: {selected}",
        "cert_saved": "📌 Сертификат сохранен: {cert_name}",
        "already_selected": "⚠️ Этот сертификат уже выбран.",
        "no_selection": "Не выбрано",
        "back_button": "🔙 Назад",
        "saving_error": "Произошла ошибка базы данных. Пожалуйста, попробуйте еще раз.",
        "callback_error": "⚠️ Произошла непредвиденная ошибка.",
    },
    "de": {
        "cert_loading_error": "⚠️ Zertifikatinformationen konnten nicht geladen werden.",
        "certificate_prompt": "📃 Bitte wähle ein Zertifikat aus.\nAktuell ausgewählt: {selected}",
        "certificate_selected": "📌 Zertifikat ausgewählt: {selected}",
        "cert_saved": "📌 Zertifikat gespeichert: {cert_name}",
        "already_selected": "⚠️ Dieses Zertifikat ist bereits ausgewählt.",
        "no_selection": "Keines",
        "back_button": "🔙 Zurück",
        "saving_error": "Ein Datenbankfehler ist aufgetreten. Bitte versuche es erneut.",
        "callback_error": "⚠️ Ein unerwarteter Fehler ist aufgetreten.",
    }
}

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
    }
}

# Plugins/countdown.py
countdown_strings = {
    "en": {
        "signed": "Signed",
        "app_name": "App Name",
        "bundle_id": "Bundle ID",
        "certificate": "Certificate",
        "install_button": "📲 Install",
        "explore_button": "🔎 Discover More",
        "mnm_notify": "Message could not be edited."
    },
    "tr": {
        "signed": "İmzalandı",
        "app_name": "Uygulama Adı",
        "bundle_id": "Paket Kimliği",
        "certificate": "Sertifika",
        "install_button": "📲 Yükle",
        "explore_button": "🔎 Daha Fazlasını Keşfet",
        "mnm_notify": "Mesaj düzenlenemedi."
    },
    "ru": {
        "signed": "Подписано",
        "app_name": "Название приложения",
        "bundle_id": "Идентификатор пакета",
        "certificate": "Сертификат",
        "install_button": "📲 Установить",
        "explore_button": "🔎 Узнать больше",
        "mnm_notify": "Не удалось отредактировать сообщение."
    },
    "de": {
        "signed": "Signiert",
        "app_name": "App-Name",
        "bundle_id": "Bundle-ID",
        "certificate": "Zertifikat",
        "install_button": "📲 Installieren",
        "explore_button": "🔎 Mehr entdecken",
        "mnm_notify": "Nachricht konnte nicht bearbeitet werden."
    }
}

# Plugins/download.py
download_strings = {
    "en": {
        "download_failed_message": "❌ Download failed for {file_name}.",
        "download_attempt_failed_message": "⚠️ Error downloading {file_name}, retrying... ({current}/{limit})",
        "download_successful_message": "✅ {file_name} downloaded successfully!",
        "download_error_detected": "An error was detected during download.",
        "httpnot200": "The requested URL is not available.",
        "httpnotfile": "The URL does not point to a downloadable file.",
        "connection_error": "Could not establish a connection.",
        "unexpected_response_error": "Received an unexpected response from the server.",
        "invalid_url_error": "The provided URL is invalid.",
        "too_many_redirects_error": "Exceeded maximum number of redirects.",
        "ssl_error": "An SSL connection error occurred.",
        "payload_error": "Received invalid or incomplete data.",
        "server_disconnected_error": "The server connection was unexpectedly closed.",
        "general_download_error": "An error occurred while downloading the file.",
        "file_not_found_error": "The requested file could not be found.",
        "file_corrupted_error": "The downloaded file is corrupted.",
        "unknown_exception_error": "An unexpected error occurred.",
        "retrying_message": "Retrying download... ({current}/{limit})"
    },
    "tr": {
        "download_failed_message": "❌ {file_name} indirilemedi.",
        "download_attempt_failed_message": "⚠️ {file_name} indirilirken hata oluştu, yeniden deneniyor... ({current}/{limit})",
        "download_successful_message": "✅ {file_name} başarıyla indirildi!",
        "download_error_detected": "İndirme sırasında bir hata algılandı.",
        "httpnot200": "İstenen URL mevcut değil.",
        "httpnotfile": "URL indirilebilir bir dosyayı göstermiyor.",
        "connection_error": "Bağlantı kurulamadı.",
        "unexpected_response_error": "Sunucudan beklenmedik bir yanıt alındı.",
        "invalid_url_error": "Geçersiz bir URL sağlandı.",
        "too_many_redirects_error": "Maksimum yönlendirme sayısını aştı.",
        "ssl_error": "Bir SSL bağlantı hatası oluştu.",
        "payload_error": "Geçersiz veya eksik veri alındı.",
        "server_disconnected_error": "Sunucu bağlantısı beklenmedik bir şekilde kesildi.",
        "general_download_error": "Dosya indirilirken bir hata oluştu.",
        "file_not_found_error": "İstenen dosya bulunamadı.",
        "file_corrupted_error": "İndirilen dosya bozuk.",
        "unknown_exception_error": "Beklenmedik bir hata oluştu.",
        "retrying_message": "İndirme yeniden deneniyor... ({current}/{limit})"
    },
    "ru": {
        "download_failed_message": "❌ Не удалось скачать {file_name}.",
        "download_attempt_failed_message": "⚠️ Ошибка при скачивании {file_name}, повторная попытка... ({current}/{limit})",
        "download_successful_message": "✅ {file_name} успешно скачан!",
        "download_error_detected": "Во время загрузки была обнаружена ошибка.",
        "httpnot200": "Запрошенный URL недоступен.",
        "httpnotfile": "URL не указывает на скачиваемый файл.",
        "connection_error": "Не удалось установить соединение.",
        "unexpected_response_error": "Получен непредвиденный ответ от сервера.",
        "invalid_url_error": "Предоставлен неверный URL.",
        "too_many_redirects_error": "Превышено максимальное количество перенаправлений.",
        "ssl_error": "Произошла ошибка SSL-соединения.",
        "payload_error": "Получены неверные или неполные данные.",
        "server_disconnected_error": "Соединение с сервером было неожиданно прервано.",
        "general_download_error": "Произошла ошибка при скачивании файла.",
        "file_not_found_error": "Запрошенный файл не найден.",
        "file_corrupted_error": "Скачанный файл поврежден.",
        "unknown_exception_error": "Произошла непредвиденная ошибка.",
        "retrying_message": "Повторная попытка загрузки... ({current}/{limit})"
    },
    "de": {
        "download_failed_message": "❌ Download für {file_name} fehlgeschlagen.",
        "download_attempt_failed_message": "⚠️ Fehler beim Herunterladen von {file_name}, versuche erneut... ({current}/{limit})",
        "download_successful_message": "✅ {file_name} erfolgreich heruntergeladen!",
        "download_error_detected": "Während des Downloads wurde ein Fehler festgestellt.",
        "httpnot200": "Die angeforderte URL ist nicht verfügbar.",
        "httpnotfile": "Die URL verweist nicht auf eine herunterladbare Datei.",
        "connection_error": "Es konnte keine Verbindung hergestellt werden.",
        "unexpected_response_error": "Unerwartete Antwort vom Server erhalten.",
        "invalid_url_error": "Die angegebene URL ist ungültig.",
        "too_many_redirects_error": "Maximale Anzahl von Weiterleitungen überschritten.",
        "ssl_error": "Ein SSL-Verbindungsfehler ist aufgetreten.",
        "payload_error": "Ungültige oder unvollständige Daten empfangen.",
        "server_disconnected_error": "Die Serververbindung wurde unerwartet geschlossen.",
        "general_download_error": "Beim Herunterladen der Datei ist ein Fehler aufgetreten.",
        "file_not_found_error": "Die angeforderte Datei konnte nicht gefunden werden.",
        "file_corrupted_error": "Die heruntergeladene Datei ist beschädigt.",
        "unknown_exception_error": "Ein unerwarteter Fehler ist aufgetreten.",
        "retrying_message": "Download wird erneut versucht... ({current}/{limit})"
    }
}

# Plugins/help.py
help_strings = {
    "en": {
        "user_not_registered": "You are not registered to use this bot.",
        "available_cmds": "**Available Commands**",
        "user_cmds": "**User Commands**",
        "cmd_prefixes": "Active command prefixes: {prefixes}",
        "admin_cmds": "**Admin Commands**",
        "help_cmd": "Shows this help message.",
        "speedtest_cmd": "Measures the connection speed.",
        "info_cmd": "Displays information about the bot.",
        "sign_cmd": "Signs the replied IPA file.",
        "clear_cmd": "Resets all modification options.",
        "profile_cmd": "Removes the embedded mobile provision file.",
        "minos_cmd": "Sets the minimum OS version required.",
        "id_cmd": "Changes the application's bundle ID.",
        "version_cmd": "Changes the application's version.",
        "name_cmd": "Changes the application's name.",
        "update_cmd": "Updates the bot from the repository.",
        "duyur_cmd": "Sends an announcement to all users.",
        "exec_cmd": "Executes a shell command.",
        "restart_cmd": "Restarts the bot.",
        "shutdown_cmd": "Shuts down the bot.",
        "user_cmd": "Manages user registrations.",
        "premium_cmd": "Manages premium user status.",
        "unknown_exception": "An error occurred while processing the help request from @{username} ({userID}): {error}"
    },
    "tr": {
        "user_not_registered": "Bu botu kullanmak için kayıtlı değilsiniz.",
        "available_cmds": "**Mevcut Komutlar**",
        "user_cmds": "**Kullanıcı Komutları**",
        "cmd_prefixes": "Aktif komut önekleri: {prefixes}",
        "admin_cmds": "**Yönetici Komutları**",
        "help_cmd": "Bu yardım mesajını gösterir.",
        "speedtest_cmd": "Bağlantı hızını ölçer.",
        "info_cmd": "Bot hakkında bilgi görüntüler.",
        "sign_cmd": "Yanıtlanan IPA dosyasını imzalar.",
        "clear_cmd": "Tüm düzenleme seçeneklerini sıfırlar.",
        "profile_cmd": "Gömülü mobil provizyon dosyasını kaldırır.",
        "minos_cmd": "Gerekli minimum işletim sistemi sürümünü ayarlar.",
        "id_cmd": "Uygulamanın paket kimliğini değiştirir.",
        "version_cmd": "Uygulamanın sürümünü değiştirir.",
        "name_cmd": "Uygulamanın adını değiştirir.",
        "update_cmd": "Botu depodan günceller.",
        "duyur_cmd": "Tüm kullanıcılara bir duyuru gönderir.",
        "exec_cmd": "Bir kabuk komutu çalıştırır.",
        "restart_cmd": "Botu yeniden başlatır.",
        "shutdown_cmd": "Botu kapatır.",
        "user_cmd": "Kullanıcı kayıtlarını yönetir.",
        "premium_cmd": "Premium kullanıcı durumunu yönetir.",
        "unknown_exception": "@{username} ({userID}) kullanıcısından yardım isteği işlenirken bir hata oluştu: {error}"
    },
    "ru": {
        "user_not_registered": "Вы не зарегистрированы для использования этого бота.",
        "available_cmds": "**Доступные команды**",
        "user_cmds": "**Пользовательские команды**",
        "cmd_prefixes": "Активные префиксы команд: {prefixes}",
        "admin_cmds": "**Команды администратора**",
        "help_cmd": "Показывает это справочное сообщение.",
        "speedtest_cmd": "Измеряет скорость соединения.",
        "info_cmd": "Отображает информацию о боте.",
        "sign_cmd": "Подписывает отвеченный IPA-файл.",
        "clear_cmd": "Сбрасывает все параметры модификации.",
        "profile_cmd": "Удаляет встроенный мобильный профиль.",
        "minos_cmd": "Устанавливает минимальную требуемую версию ОС.",
        "id_cmd": "Изменяет идентификатор пакета приложения.",
        "version_cmd": "Изменяет версию приложения.",
        "name_cmd": "Изменяет название приложения.",
        "update_cmd": "Обновляет бота из репозитория.",
        "duyur_cmd": "Отправляет объявление всем пользователям.",
        "exec_cmd": "Выполняет команду оболочки.",
        "restart_cmd": "Перезапускает бота.",
        "shutdown_cmd": "Выключает бота.",
        "user_cmd": "Управляет регистрацией пользователей.",
        "premium_cmd": "Управляет статусом премиум-пользователей.",
        "unknown_exception": "Произошла ошибка при обработке запроса помощи от @{username} ({userID}): {error}"
    },
    "de": {
        "user_not_registered": "Du bist nicht registriert, um diesen Bot zu verwenden.",
        "available_cmds": "**Verfügbare Befehle**",
        "user_cmds": "**Benutzerbefehle**",
        "cmd_prefixes": "Aktive Befehlspräfixe: {prefixes}",
        "admin_cmds": "**Admin-Befehle**",
        "help_cmd": "Zeigt diese Hilfenachricht an.",
        "speedtest_cmd": "Misst die Verbindungsgeschwindigkeit.",
        "info_cmd": "Zeigt Informationen über den Bot an.",
        "sign_cmd": "Signiert die beantwortete IPA-Datei.",
        "clear_cmd": "Setzt alle Änderungsoptionen zurück.",
        "profile_cmd": "Entfernt die eingebettete mobile Bereitstellungsdatei.",
        "minos_cmd": "Legt die erforderliche Mindest-Betriebssystemversion fest.",
        "id_cmd": "Ändert die Bundle-ID der Anwendung.",
        "version_cmd": "Ändert die Version der Anwendung.",
        "name_cmd": "Ändert den Namen der Anwendung.",
        "update_cmd": "Aktualisiert den Bot aus dem Repository.",
        "duyur_cmd": "Sendet eine Ankündigung an alle Benutzer.",
        "exec_cmd": "Führt einen Shell-Befehl aus.",
        "restart_cmd": "Startet den Bot neu.",
        "shutdown_cmd": "Fährt den Bot herunter.",
        "user_cmd": "Verwaltet Benutzerregistrierungen.",
        "premium_cmd": "Verwaltet den Premium-Benutzerstatus.",
        "unknown_exception": "Bei der Verarbeitung der Hilfeanfrage von @{username} ({userID}) ist ein Fehler aufgetreten: {error}"
    }
}

# Plugins/info.py
info_strings = {
    "en": {
        "greeting": "👋 Hello, {name}!",
        "system_info": "\n**System Information**\n",
        "bot_info": "\n**Bot Information**\n",
        "bot_stats": "Uptime: {uptime}\nUsage: {usage}",
        "total_users": "Total Users: {count}",
        "active_users": "Active Users: {count}",
    },
    "tr": {
        "greeting": "👋 Merhaba, {name}!",
        "system_info": "\n**Sistem Bilgileri**\n",
        "bot_info": "\n**Bot Bilgileri**\n",
        "bot_stats": "Çalışma Süresi: {uptime}\nKullanım: {usage}",
        "total_users": "Toplam Kullanıcı: {count}",
        "active_users": "Aktif Kullanıcı: {count}",
    },
    "ru": {
        "greeting": "👋 Здравствуйте, {name}!",
        "system_info": "\n**Информация о системе**\n",
        "bot_info": "\n**Информация о боте**\n",
        "bot_stats": "Время работы: {uptime}\nИспользование: {usage}",
        "total_users": "Всего пользователей: {count}",
        "active_users": "Активные пользователи: {count}",
    },
    "de": {
        "greeting": "👋 Hallo, {name}!",
        "system_info": "\n**Systeminformationen**\n",
        "bot_info": "\n**Bot-Informationen**\n",
        "bot_stats": "Betriebszeit: {uptime}\nNutzung: {usage}",
        "total_users": "Gesamte Benutzer: {count}",
        "active_users": "Aktive Benutzer: {count}",
    }
}

# Plugins/language_select.py
language_select_strings = {
    "en": {
        "select_language": "🌐 **Select a Language**",
        "selected": "Selected:",
        "already_selected": "⚠️ This language is already selected.",
        "save_failed": "⚠️ Could not save the language setting.",
        "new_language_selected": "🌐 Language changed successfully.",
        "error_in_language_selection": "⚠️ An error occurred during language selection.",
        "database_error": "A database error occurred. Please try again.",
        "language_clear_success": "Language preference cleared. The bot will now use your client's language.",
        "language_clear_failed": "No language preference was set.",
        "back_button": "🔙 Go Back",
        "clear_button": "🧹 Clear Selection"
    },
    "tr": {
        "select_language": "🌐 **Bir Dil Seçin**",
        "selected": "Seçili:",
        "already_selected": "⚠️ Bu dil zaten seçili.",
        "save_failed": "⚠️ Dil ayarı kaydedilemedi.",
        "new_language_selected": "🌐 Dil başarıyla değiştirildi.",
        "error_in_language_selection": "Dil seçimi sırasında bir hata oluştu.",
        "database_error": "Bir veritabanı hatası oluştu. Lütfen tekrar deneyin.",
        "language_clear_success": "Dil tercihi temizlendi. Bot artık istemci dilinizi kullanacak.",
        "language_clear_failed": "Ayarlanmış bir dil tercihi yoktu.",
        "back_button": "🔙 Geri Dön",
        "clear_button": "🧹 Seçimi Temizle"
    },
    "ru": {
        "select_language": "🌐 **Выберите язык**",
        "selected": "Выбрано:",
        "already_selected": "⚠️ Этот язык уже выбран.",
        "save_failed": "⚠️ Не удалось сохранить настройку языка.",
        "new_language_selected": "🌐 Язык успешно изменен.",
        "error_in_language_selection": "⚠️ Произошла ошибка при выборе языка.",
        "database_error": "Произошла ошибка базы данных. Пожалуйста, попробуйте еще раз.",
        "language_clear_success": "Языковые предпочтения сброшены. Бот теперь будет использовать язык вашего клиента.",
        "language_clear_failed": "Языковые предпочтения не были установлены.",
        "back_button": "🔙 Назад",
        "clear_button": "🧹 Очистить выбор",
    },
    "de": {
        "select_language": "🌐 **Sprache auswählen**",
        "selected": "Ausgewählt:",
        "already_selected": "⚠️ Diese Sprache ist bereits ausgewählt.",
        "save_failed": "⚠️ Spracheinstellung konnte nicht gespeichert werden.",
        "new_language_selected": "🌐 Sprache erfolgreich geändert.",
        "error_in_language_selection": "Bei der Sprachauswahl ist ein Fehler aufgetreten.",
        "database_error": "Ein Datenbankfehler ist aufgetreten. Bitte versuche es erneut.",
        "language_clear_success": "Spracheinstellung gelöscht. Der Bot verwendet nun die Sprache deines Clients.",
        "language_clear_failed": "Es war keine Spracheinstellung festgelegt.",
        "back_button": "🔙 Zurück",
        "clear_button": "🧹 Auswahl löschen",
    }
}

# Plugins/modifier.py
modifier_strings = {
    "en": {
        "save_error": "Could not save {options}. Error: {error}.",
        "update_error": "Could not update {options}. Error: {error}.",
        "app_name_usage": "Usage: /name [new app name]",
        "unset_app_name": "App name modification has been reset.",
        "set_app_name": "App name will be changed to **{name}**.",
        "app_version_usage": "Usage: /version [new version]",
        "invalid_app_version": "Invalid version format. Please use numbers and dots only (e.g., 1.2.3).",
        "unset_app_version": "App version modification has been reset.",
        "set_app_version": "App version will be changed to **{version}**.",
        "app_id_usage": "Usage: /id [new bundle ID]",
        "unset_app_id": "Bundle ID modification has been reset.",
        "set_app_id": "Bundle ID will be changed to **{id}**.",
        "min_os_usage": "Usage: /minos [version]",
        "invalid_min_os": "Invalid OS version format. Please use numbers and dots only (e.g., 15.0).",
        "unset_min_os": "Minimum OS version modification has been reset.",
        "set_min_os": "Minimum OS version will be set to **{os_version}**.",
        "unset_profile_removal": "Embedded profile will no longer be removed.",
        "set_profile_removal": "Embedded profile will be removed.",
        "tweak_added_expecting_ipa": "Tweak added: {file_name}. Now send the IPA file to apply it.",
        "error_while_resetting": "An error occurred while resetting options: {error}."
    },
    "tr": {
        "save_error": "{options} kaydedilemedi. Hata: {error}.",
        "update_error": "{options} güncellenemedi. Hata: {error}.",
        "app_name_usage": "Kullanım: /name [yeni uygulama adı]",
        "unset_app_name": "Uygulama adı değişikliği sıfırlandı.",
        "set_app_name": "Uygulama adı **{name}** olarak değiştirilecek.",
        "app_version_usage": "Kullanım: /version [yeni sürüm]",
        "invalid_app_version": "Geçersiz sürüm formatı. Lütfen sadece rakam ve nokta kullanın (örn. 1.2.3).",
        "unset_app_version": "Uygulama sürümü değişikliği sıfırlandı.",
        "set_app_version": "Uygulama sürümü **{version}** olarak değiştirilecek.",
        "app_id_usage": "Kullanım: /id [yeni paket kimliği]",
        "unset_app_id": "Paket kimliği değişikliği sıfırlandı.",
        "set_app_id": "Paket kimliği **{id}** olarak değiştirilecek.",
        "min_os_usage": "Kullanım: /minos [sürüm]",
        "invalid_min_os": "Geçersiz işletim sistemi sürüm formatı. Lütfen sadece rakam ve nokta kullanın (örn. 15.0).",
        "unset_min_os": "Minimum işletim sistemi sürümü değişikliği sıfırlandı.",
        "set_min_os": "Minimum işletim sistemi sürümü **{os_version}** olarak ayarlanacak.",
        "unset_profile_removal": "Gömülü profil artık kaldırılmayacak.",
        "set_profile_removal": "Gömülü profil kaldırılacak.",
        "tweak_added_expecting_ipa": "Tweak eklendi: {file_name}. Şimdi uygulamak için IPA dosyasını gönderin.",
        "error_while_resetting": "Seçenekler sıfırlanırken bir hata oluştu: {error}."
    },
    "ru": {
        "save_error": "Не удалось сохранить {options}. Ошибка: {error}.",
        "update_error": "Не удалось обновить {options}. Ошибка: {error}.",
        "app_name_usage": "Использование: /name [новое название приложения]",
        "unset_app_name": "Изменение названия приложения сброшено.",
        "set_app_name": "Название приложения будет изменено на **{name}**.",
        "app_version_usage": "Использование: /version [новая версия]",
        "invalid_app_version": "Неверный формат версии. Используйте только цифры и точки (например, 1.2.3).",
        "unset_app_version": "Изменение версии приложения сброшено.",
        "set_app_version": "Версия приложения будет изменена на **{version}**.",
        "app_id_usage": "Использование: /id [новый идентификатор пакета]",
        "unset_app_id": "Изменение идентификатора пакета сброшено.",
        "set_app_id": "Идентификатор пакета будет изменен на **{id}**.",
        "min_os_usage": "Использование: /minos [версия]",
        "invalid_min_os": "Неверный формат версии ОС. Используйте только цифры и точки (например, 15.0).",
        "unset_min_os": "Изменение минимальной версии ОС сброшено.",
        "set_min_os": "Минимальная версия ОС будет установлена на **{os_version}**.",
        "unset_profile_removal": "Встроенный профиль больше не будет удаляться.",
        "set_profile_removal": "Встроенный профиль будет удален.",
        "tweak_added_expecting_ipa": "Твик добавлен: {file_name}. Теперь отправьте IPA-файл, чтобы применить его.",
        "error_while_resetting": "Произошла ошибка при сбросе настроек: {error}."
    },
    "de": {
        "save_error": "Konnte {options} nicht speichern. Fehler: {error}.",
        "update_error": "Konnte {options} nicht aktualisieren. Fehler: {error}.",
        "app_name_usage": "Verwendung: /name [neuer App-Name]",
        "unset_app_name": "Änderung des App-Namens wurde zurückgesetzt.",
        "set_app_name": "Der App-Name wird in **{name}** geändert.",
        "app_version_usage": "Verwendung: /version [neue Version]",
        "invalid_app_version": "Ungültiges Versionsformat. Bitte nur Zahlen und Punkte verwenden (z.B. 1.2.3).",
        "unset_app_version": "Änderung der App-Version wurde zurückgesetzt.",
        "set_app_version": "Die App-Version wird in **{version}** geändert.",
        "app_id_usage": "Verwendung: /id [neue Bundle-ID]",
        "unset_app_id": "Änderung der Bundle-ID wurde zurückgesetzt.",
        "set_app_id": "Die Bundle-ID wird in **{id}** geändert.",
        "min_os_usage": "Verwendung: /minos [Version]",
        "invalid_min_os": "Ungültiges Betriebssystem-Versionsformat. Bitte nur Zahlen und Punkte verwenden (z.B. 15.0).",
        "unset_min_os": "Änderung der Mindest-Betriebssystemversion wurde zurückgesetzt.",
        "set_min_os": "Die Mindest-Betriebssystemversion wird auf **{os_version}** gesetzt.",
        "unset_profile_removal": "Eingebettetes Profil wird nicht mehr entfernt.",
        "set_profile_removal": "Eingebettetes Profil wird entfernt.",
        "tweak_added_expecting_ipa": "Tweak hinzugefügt: {file_name}. Senden Sie jetzt die IPA-Datei, um ihn anzuwenden.",
        "error_while_resetting": "Beim Zurücksetzen der Optionen ist ein Fehler aufgetreten: {error}."
    }
}

# Plugins/sign.py
sign_strings = {
    "en": {
        "no_cert_selected": "Hello, {user_first_name}! Please select a certificate from the /start menu and try again. 🚀",
        "sign_error_retry": "An error occurred during signing, retrying... ({failed_sign_attempt}/{max_sign_attempt})",
        "signing_failed": "❌ Signing failed for {file_name}.",
        "unexpected_error": "An unexpected error occurred. If this issue persists, please contact support.",
        "ipa_ready": "✅ Your IPA has been signed and is ready.",
        "forgot_choice": "It seems you forgot to select a certificate. Please go to the /start menu to choose one.",
        "file_lost": "The file was lost during the signing process.",
        "value_error": "A value error occurred during the signing process.",
        "permission_error": "A permission error occurred during the signing process.",
        "signing_error": "The signing operation failed.",
        "unknown_error": "An unexpected error occurred during the signing process.",
        "select_certificate_button": "📝️ Select Certificate",
        "signing_in_progress": "📝 Signing...",
        "modifying_in_progress": "🔧 Modifying...",
        "executing_command": "Executing: {command}",
        "modify_retry_error": "An error occurred while modifying, retrying... ({failed_modify_attempt}/{max_modify_attempt})",
        "fnfe_err": "The file could not be found during the signing process.",
        "ve_err": "A value error occurred during the signing process.",
        "pe_err": "A permission error occurred during the signing process.",
        "unknown_sign_err": "An unknown error occurred during the signing process."
    },
    "tr": {
        "no_cert_selected": "Merhaba, {user_first_name}! Lütfen /start menüsünden bir sertifika seçin ve tekrar deneyin. 🚀",
        "sign_error_retry": "İmzalama sırasında bir hata oluştu, yeniden deneniyor... ({failed_sign_attempt}/{max_sign_attempt})",
        "signing_failed": "❌ {file_name} için imzalama başarısız oldu.",
        "unexpected_error": "Beklenmedik bir hata oluştu. Bu sorun devam ederse, lütfen destek ile iletişime geçin.",
        "ipa_ready": "✅ IPA'nız imzalandı ve hazır.",
        "forgot_choice": "Görünüşe göre bir sertifika seçmeyi unuttunuz. Lütfen bir tane seçmek için /start menüsüne gidin.",
        "file_lost": "Dosya imzalama işlemi sırasında kayboldu.",
        "value_error": "İmzalama işlemi sırasında bir değer hatası oluştu.",
        "permission_error": "İmzalama işlemi sırasında bir izin hatası oluştu.",
        "signing_error": "İmzalama işlemi başarısız oldu.",
        "unknown_error": "İmzalama işlemi sırasında beklenmedik bir hata oluştu.",
        "select_certificate_button": "📝️ Sertifika Seç",
        "signing_in_progress": "📝 İmzalanıyor...",
        "modifying_in_progress": "🔧 Düzenleniyor...",
        "executing_command": "Çalıştırılıyor: {command}",
        "modify_retry_error": "Düzenleme sırasında bir hata oluştu, yeniden deneniyor... ({failed_modify_attempt}/{max_modify_attempt})",
        "fnfe_err": "İmzalama işlemi sırasında dosya bulunamadı.",
        "ve_err": "İmzalama işlemi sırasında bir değer hatası oluştu.",
        "pe_err": "İmzalama işlemi sırasında bir izin hatası oluştu.",
        "unknown_sign_err": "İmzalama işlemi sırasında bilinmeyen bir hata oluştu."
    },
    "ru": {
        "no_cert_selected": "Здравствуйте, {user_first_name}! Пожалуйста, выберите сертификат в меню /start и попробуйте снова. 🚀",
        "sign_error_retry": "Произошла ошибка при подписании, повторная попытка... ({failed_sign_attempt}/{max_sign_attempt})",
        "signing_failed": "❌ Не удалось подписать {file_name}.",
        "unexpected_error": "Произошла непредвиденная ошибка. Если проблема не исчезнет, обратитесь в службу поддержки.",
        "ipa_ready": "✅ Ваш IPA подписан и готов.",
        "forgot_choice": "Кажется, вы забыли выбрать сертификат. Пожалуйста, перейдите в меню /start, чтобы выбрать его.",
        "file_lost": "Файл был утерян в процессе подписания.",
        "value_error": "В процессе подписания произошла ошибка значения.",
        "permission_error": "В процессе подписания произошла ошибка разрешений.",
        "signing_error": "Операция подписания не удалась.",
        "unknown_error": "В процессе подписания произошла непредвиденная ошибка.",
        "select_certificate_button": "📝️ Выбрать сертификат",
        "signing_in_progress": "📝 Подписание...",
        "modifying_in_progress": "🔧 Изменение...",
        "executing_command": "Выполнение: {command}",
        "modify_retry_error": "Произошла ошибка при изменении, повторная попытка... ({failed_modify_attempt}/{max_modify_attempt})",
        "fnfe_err": "Файл не найден в процессе подписания.",
        "ve_err": "В процессе подписания произошла ошибка значения.",
        "pe_err": "В процессе подписания произошла ошибка разрешений.",
        "unknown_sign_err": "В процессе подписания произошла неизвестная ошибка."
    },
    "de": {
        "no_cert_selected": "Hallo, {user_first_name}! Bitte wähle ein Zertifikat aus dem /start-Menü und versuche es erneut. 🚀",
        "sign_error_retry": "Beim Signieren ist ein Fehler aufgetreten, versuche erneut... ({failed_sign_attempt}/{max_sign_attempt})",
        "signing_failed": "❌ Signieren für {file_name} fehlgeschlagen.",
        "unexpected_error": "Ein unerwarteter Fehler ist aufgetreten. Wenn dieses Problem weiterhin besteht, wende dich bitte an den Support.",
        "ipa_ready": "✅ Deine IPA wurde signiert und ist fertig.",
        "forgot_choice": "Es scheint, du hast vergessen, ein Zertifikat auszuwählen. Bitte gehe zum /start-Menü, um eines auszuwählen.",
        "file_lost": "Die Datei ging während des Signiervorgangs verloren.",
        "value_error": "Während des Signiervorgangs ist ein Wertfehler aufgetreten.",
        "permission_error": "Während des Signiervorgangs ist ein Berechtigungsfehler aufgetreten.",
        "signing_error": "Der Signiervorgang ist fehlgeschlagen.",
        "unknown_error": "Während des Signiervorgangs ist ein unerwarteter Fehler aufgetreten.",
        "select_certificate_button": "📝️ Zertifikat auswählen",
        "signing_in_progress": "📝 Signiere...",
        "modifying_in_progress": "🔧 Ändere...",
        "executing_command": "Führe aus: {command}",
        "modify_retry_error": "Beim Ändern ist ein Fehler aufgetreten, versuche erneut... ({failed_modify_attempt}/{max_modify_attempt})",
        "fnfe_err": "Die Datei konnte während des Signiervorgangs nicht gefunden werden.",
        "ve_err": "Während des Signiervorgangs ist ein Wertfehler aufgetreten.",
        "pe_err": "Während des Signiervorgangs ist ein Berechtigungsfehler aufgetreten.",
        "unknown_sign_err": "Während des Signiervorgangs ist ein unbekannter Fehler aufgetreten."
    }
}

# Plugins/speedtest.py
speedtest_strings = {
    "en": {
        "speedtest_start": "🚀 Testing connection speed...",
        "network_error": "A network error occurred. Please check your connection and try again.",
        "timeout_error": "The request timed out. Please try again.",
        "unknown_error": "An unexpected error occurred. Please try again.",
    },
    "tr": {
        "speedtest_start": "🚀 Bağlantı hızı test ediliyor...",
        "network_error": "Bir ağ hatası oluştu. Lütfen bağlantınızı kontrol edip tekrar deneyin.",
        "timeout_error": "İstek zaman aşımına uğradı. Lütfen tekrar deneyin.",
        "unknown_error": "Beklenmedik bir hata oluştu. Lütfen tekrar deneyin.",
    },
    "ru": {
        "speedtest_start": "🚀 Тестирование скорости соединения...",
        "network_error": "Произошла сетевая ошибка. Пожалуйста, проверьте ваше соединение и попробуйте снова.",
        "timeout_error": "Время ожидания запроса истекло. Пожалуйста, попробуйте снова.",
        "unknown_error": "Произошла непредвиденная ошибка. Пожалуйста, попробуйте снова.",
    },
    "de": {
        "speedtest_start": "🚀 Verbindungsgeschwindigkeit wird getestet...",
        "network_error": "Ein Netzwerkfehler ist aufgetreten. Bitte überprüfe deine Verbindung und versuche es erneut.",
        "timeout_error": "Die Anfrage ist abgelaufen. Bitte versuche es erneut.",
        "unknown_error": "Ein unerwarteter Fehler ist aufgetreten. Bitte versuche es erneut.",
    }
}

# Plugins/start.py
start_strings = {
    "en": {
        "welcome_registered": "Hello, {name}!\nWelcome back. You can now send an IPA file to be signed.",
        "welcome_unregistered": "Hello, {name}!\nTo use this bot, you need to be a registered user. Please contact the administrator for access.",
        "select_certificate": "📝️ Select Certificate",
        "select_compression": "📚 Select Compression",
        "select_language": "🌐 Select Language",
        "approval_purchase": "Contact for Approval / Purchase",
        "settings_button": "⚙️ Settings",
        "settings_text": "Please choose a setting to configure:",
        "back_button": "🔙 Go Back",
    },
    "tr": {
        "welcome_registered": "Merhaba, {name}!\nTekrar hoş geldiniz. Şimdi imzalanacak bir IPA dosyası gönderebilirsiniz.",
        "welcome_unregistered": "Merhaba, {name}!\nBu botu kullanmak için kayıtlı bir kullanıcı olmanız gerekir. Erişim için lütfen yöneticiyle iletişime geçin.",
        "select_certificate": "📝️ Sertifika Seç",
        "select_compression": "📚 Sıkıştırma Seç",
        "select_language": "🌐 Dil Seç",
        "approval_purchase": "Onay / Satın Alma için İletişime Geçin",
        "settings_button": "⚙️ Ayarlar",
        "settings_text": "Lütfen yapılandırmak için bir ayar seçin:",
        "back_button": "🔙 Geri Dön",
    },
    "ru": {
        "welcome_registered": "Здравствуйте, {name}!\nС возвращением. Теперь вы можете отправить IPA-файл для подписи.",
        "welcome_unregistered": "Здравствуйте, {name}!\nЧтобы использовать этого бота, вам необходимо быть зарегистрированным пользователем. Пожалуйста, свяжитесь с администратором для получения доступа.",
        "select_certificate": "📝️ Выбрать сертификат",
        "select_compression": "📚 Выбрать сжатие",
        "select_language": "🌐 Выбрать язык",
        "approval_purchase": "Связаться для одобрения / покупки",
        "settings_button": "⚙️ Настройки",
        "settings_text": "Пожалуйста, выберите параметр для настройки:",
        "back_button": "🔙 Назад",
    },
    "de": {
        "welcome_registered": "Hallo, {name}!\nWillkommen zurück. Du kannst jetzt eine IPA-Datei zum Signieren senden.",
        "welcome_unregistered": "Hallo, {name}!\nUm diesen Bot zu verwenden, musst du ein registrierter Benutzer sein. Bitte kontaktiere den Administrator für den Zugriff.",
        "select_certificate": "📝️ Zertifikat auswählen",
        "select_compression": "📚 Komprimierung auswählen",
        "select_language": "🌐 Sprache auswählen",
        "approval_purchase": "Kontakt für Genehmigung / Kauf",
        "settings_button": "⚙️ Einstellungen",
        "settings_text": "Bitte wähle eine Einstellung zum Konfigurieren aus:",
        "back_button": "🔙 Zurück",
    }
}

# Plugins/user_management.py
user_management_strings = {
    "en": {
        "admin_only": "This command is for administrators only.",
        "invalid_command": "Invalid command format. Use /user [ID] or /premium [ID].",
        "user_not_found": "User with ID `{user_id}` was not found.",
        "user_added": "User `{user_id}` has been registered.",
        "user_removed": "User `{user_id}` has been unregistered.",
        "premium_added": "User `{user_id}` has been upgraded to premium. Expires on {expiry_date}.",
        "premium_removed": "Premium status has been removed for user `{user_id}`.",
        "premium_error": "An error occurred during the premium operation.",
        "premium_reg_error": "An error occurred while registering the premium user.",
        "premium_unreg_error": "An error occurred while unregistering the premium user.",
        "not_enough_arguments": "Please provide at least one user ID."
    },
    "tr": {
        "admin_only": "Bu komut sadece yöneticiler içindir.",
        "invalid_command": "Geçersiz komut formatı. /user [ID] veya /premium [ID] kullanın.",
        "user_not_found": "`{user_id}` ID'li kullanıcı bulunamadı.",
        "user_added": "`{user_id}` kullanıcısı kaydedildi.",
        "user_removed": "`{user_id}` kullanıcısının kaydı silindi.",
        "premium_added": "`{user_id}` kullanıcısı premium'a yükseltildi. Bitiş tarihi: {expiry_date}.",
        "premium_removed": "`{user_id}` kullanıcısının premium durumu kaldırıldı.",
        "premium_error": "Premium işlemi sırasında bir hata oluştu.",
        "premium_reg_error": "Premium kullanıcı kaydedilirken bir hata oluştu.",
        "premium_unreg_error": "Premium kullanıcının kaydı silinirken bir hata oluştu.",
        "not_enough_arguments": "Lütfen en az bir kullanıcı ID'si belirtin."
    },
    "ru": {
        "admin_only": "Эта команда только для администраторов.",
        "invalid_command": "Неверный формат команды. Используйте /user [ID] или /premium [ID].",
        "user_not_found": "Пользователь с ID `{user_id}` не найден.",
        "user_added": "Пользователь `{user_id}` зарегистрирован.",
        "user_removed": "Пользователь `{user_id}` снят с регистрации.",
        "premium_added": "Пользователь `{user_id}` повышен до премиума. Истекает {expiry_date}.",
        "premium_removed": "Статус премиум для пользователя `{user_id}` удален.",
        "premium_error": "Произошла ошибка во время операции с премиум.",
        "premium_reg_error": "Произошла ошибка при регистрации премиум-пользователя.",
        "premium_unreg_error": "Произошла ошибка при снятии с регистрации премиум-пользователя.",
        "not_enough_arguments": "Пожалуйста, укажите хотя бы один идентификатор пользователя."
    },
    "de": {
        "admin_only": "Dieser Befehl ist nur für Administratoren.",
        "invalid_command": "Ungültiges Befehlsformat. Verwende /user [ID] oder /premium [ID].",
        "user_not_found": "Benutzer mit ID `{user_id}` wurde nicht gefunden.",
        "user_added": "Benutzer `{user_id}` wurde registriert.",
        "user_removed": "Benutzer `{user_id}` wurde deregistriert.",
        "premium_added": "Benutzer `{user_id}` wurde auf Premium hochgestuft. Läuft am {expiry_date} ab.",
        "premium_removed": "Premium-Status für Benutzer `{user_id}` wurde entfernt.",
        "premium_error": "Bei der Premium-Operation ist ein Fehler aufgetreten.",
        "premium_reg_error": "Beim Registrieren des Premium-Benutzers ist ein Fehler aufgetreten.",
        "premium_unreg_error": "Beim Deregistrieren des Premium-Benutzers ist ein Fehler aufgetreten.",
        "not_enough_arguments": "Bitte gib mindestens eine Benutzer-ID an."
    }
}

# utils/certificate_handler.py
certificate_handler_strings = {
    "en": {
        "permission_denied": "You are not authorized to add new certificates.",
        "certificate_updated": "Certificate updated successfully: {file_name}",
        "unexpected_git_error": "An unexpected Git error occurred: {error}",
        "unexpected_error": "An unexpected error occurred: {error}",
    },
    "tr": {
        "permission_denied": "Yeni sertifika ekleme yetkiniz yok.",
        "certificate_updated": "Sertifika başarıyla güncellendi: {file_name}",
        "unexpected_git_error": "Beklenmedik bir Git hatası oluştu: {error}",
        "unexpected_error": "Beklenmedik bir hata oluştu: {error}",
    },
    "ru": {
        "permission_denied": "У вас нет прав на добавление новых сертификатов.",
        "certificate_updated": "Сертификат успешно обновлен: {file_name}",
        "unexpected_git_error": "Произошла непредвиденная ошибка Git: {error}",
        "unexpected_error": "Произошла непредвиденная ошибка: {error}",
    },
    "de": {
        "permission_denied": "Du bist nicht berechtigt, neue Zertifikate hinzuzufügen.",
        "certificate_updated": "Zertifikat erfolgreich aktualisiert: {file_name}",
        "unexpected_git_error": "Ein unerwarteter Git-Fehler ist aufgetreten: {error}",
        "unexpected_error": "Ein unerwarteter Fehler ist aufgetreten: {error}"
    }
}

# utils/gen_html.py
generate_html_strings = {
    "en": {
        "install_button": "Install",
        "installing": "Installing...",
        "download_button": "Download",
        "selected_certificate": "Selected Certificate",
        "unsupported_system": "Unsupported System",
        "credits": "Made with <i class=\"fa-solid fa-heart fa-beat\"></i> by AppleFavour",
        "system_info": "System Information",
        "requires_newer_OS": "Requires iOS {requiredOSVersion} or newer.",
    },
    "tr": {
        "title": "Favour Sign",
        "install_button": "Yükle",
        "installing": "Yükleniyor...",
        "download_button": "İndir",
        "selected_certificate": "Seçili Sertifika",
        "unsupported_system": "Desteklenmiyor",
        "credits": "<i class=\"fa-solid fa-heart fa-beat\"></i> ile AppleFavour tarafından yapıldı.",
        "system_info": "Sistem Bilgisi",
        "requires_newer_OS": "iOS {requiredOSVersion} veya daha yenisini gerektirir.",
    },
    "ru": {
        "install_button": "Установить",
        "installing": "Установка...",
        "download_button": "Скачать",
        "selected_certificate": "Выбранный сертификат",
        "unsupported_system": "Не поддерживается",
        "credits": "Сделано с <i class=\"fa-solid fa-heart fa-beat\"></i> от AppleFavour",
        "system_info": "Информация о системе",
        "requires_newer_OS": "Требуется iOS {requiredOSVersion} или новее.",
    },
    "de": {
        "install_button": "Installieren",
        "installing": "Installiere...",
        "download_button": "Herunterladen",
        "selected_certificate": "Ausgewähltes Zertifikat",
        "unsupported_system": "Nicht unterstützt",
        "credits": "Erstellt mit <i class=\"fa-solid fa-heart fa-beat\"></i> von AppleFavour",
        "system_info": "Systeminformationen",
        "requires_newer_OS": "Erfordert iOS {requiredOSVersion} oder neuer.",
    },
}

# utils/helpers.py
helpers_strings = {
    "en": {
        "create_folder_error": "Error creating folder: {error}",
        "hour_ETA": "{remaining_time}h",
        "minute_ETA": "{remaining_time}m",
        "second_ETA": "{remaining_time}s",
        "ETA": "ETA: {estimated_remaining_download_time}",
        "file_is_lost": "The file seems to have disappeared during the process.",
        "file_format_error": "The IPA file format is invalid or corrupted.",
        "file_size_unexpected": "Downloaded file size ({downloaded}) does not match the expected size ({expected}).",
        "exception_context": "Error: {exception}"
    },
    "tr": {
        "create_folder_error": "Klasör oluşturulurken hata: {error}",
        "hour_ETA": "{remaining_time}s",
        "minute_ETA": "{remaining_time}d",
        "second_ETA": "{remaining_time}sn",
        "ETA": "Tahmini Süre: {estimated_remaining_download_time}",
        "file_is_lost": "Dosya işlem sırasında kaybolmuş gibi görünüyor.",
        "file_format_error": "IPA dosya formatı geçersiz veya bozuk.",
        "file_size_unexpected": "İndirilen dosya boyutu ({downloaded}), beklenen boyutla ({expected}) eşleşmiyor.",
        "exception_context": "Hata: {exception}",
    },
    "ru": {
        "create_folder_error": "Ошибка при создании папки: {error}",
        "hour_ETA": "{remaining_time}ч",
        "minute_ETA": "{remaining_time}м",
        "second_ETA": "{remaining_time}с",
        "ETA": "Примерное время: {estimated_remaining_download_time}",
        "file_is_lost": "Файл, кажется, исчез в процессе обработки.",
        "file_format_error": "Формат файла IPA недействителен или поврежден.",
        "file_size_unexpected": "Размер загруженного файла ({downloaded}) не соответствует ожидаемому размеру ({expected}).",
        "exception_context": "Ошибка: {exception}"
    },
    "de": {
        "create_folder_error": "Fehler beim Erstellen des Ordners: {error}",
        "hour_ETA": "{remaining_time}h",
        "minute_ETA": "{remaining_time}m",
        "second_ETA": "{remaining_time}s",
        "ETA": "ETA: {estimated_remaining_download_time}",
        "file_is_lost": "Die Datei scheint während des Vorgangs verschwunden zu sein.",
        "file_format_error": "Das IPA-Dateiformat ist ungültig oder beschädigt.",
        "file_size_unexpected": "Die heruntergeladene Dateigröße ({downloaded}) stimmt nicht mit der erwarteten Größe ({expected}) überein.",
        "exception_context": "Fehler: {exception}"
    }
}

# utils/main_helper.py
main_helper_strings = {
    "en": {
        "unregistered_user": "You are not registered. Please contact an administrator for access.",
        "unsupported_file_type": "Unsupported file type: {file_extension}",
        "cooldown_wait": "Please wait {time_to_wait} seconds before sending another file.",
        "cooldown_update": "Please wait {time_to_wait} more seconds...",
        "download_starting": "⏳ Download starting...",
        "high_demand": "The bot is currently busy. Your request has been queued.",
        "reply_or_send_ipa_prompt": "Please reply to a message with an IPA file or a direct download URL."
    },
    "tr": {
        "unregistered_user": "Kayıtlı değilsiniz. Erişim için lütfen bir yöneticiyle iletişime geçin.",
        "unsupported_file_type": "Desteklenmeyen dosya türü: {file_extension}",
        "cooldown_wait": "Lütfen başka bir dosya göndermeden önce {time_to_wait} saniye bekleyin.",
        "cooldown_update": "Lütfen {time_to_wait} saniye daha bekleyin...",
        "download_starting": "⏳ İndirme başlıyor...",
        "high_demand": "Bot şu anda meşgul. İsteğiniz sıraya alındı.",
        "reply_or_send_ipa_prompt": "Lütfen bir IPA dosyası veya doğrudan indirme URL'si içeren bir mesaja yanıt verin."
    },
    "ru": {
        "unregistered_user": "Вы не зарегистрированы. Пожалуйста, свяжитесь с администратором для получения доступа.",
        "unsupported_file_type": "Неподдерживаемый тип файла: {file_extension}",
        "cooldown_wait": "Пожалуйста, подождите {time_to_wait} секунд перед отправкой следующего файла.",
        "cooldown_update": "Пожалуйста, подождите еще {time_to_wait} секунд...",
        "download_starting": "⏳ Начинается загрузка...",
        "high_demand": "Бот в настоящее время занят. Ваш запрос поставлен в очередь.",
        "reply_or_send_ipa_prompt": "Пожалуйста, ответьте на сообщение с файлом IPA или прямой ссылкой для скачивания."
    },
    "de": {
        "unregistered_user": "Du bist nicht registriert. Bitte kontaktiere einen Administrator für den Zugriff.",
        "unsupported_file_type": "Nicht unterstützter Dateityp: {file_extension}",
        "cooldown_wait": "Bitte warte {time_to_wait} Sekunden, bevor du eine weitere Datei sendest.",
        "cooldown_update": "Bitte warte noch {time_to_wait} Sekunden...",
        "download_starting": "⏳ Download startet...",
        "high_demand": "Der Bot ist derzeit beschäftigt. Deine Anfrage wurde in die Warteschlange gestellt.",
        "reply_or_send_ipa_prompt": "Bitte antworte auf eine Nachricht mit einer IPA-Datei oder einer direkten Download-URL."
    }
}

# utils/power_manager.py
restart_strings = {
    "en": {
        "restart_requested": "🔄 **Restart Requested** by {user_first_name} (@{username})\nPID: `{process_id}`",
        "restart_canceled": "🔄 Restart has been canceled.",
        "restart_aborted": "❌ Restart aborted.",
        "restart_awaiting": "⏳ Waiting for active tasks to finish...\nElapsed: {time_elapsed}",
        "restart_in_progress": "♻️ Restarting now... ({time_elapsed})",
        "restart_declined": "⛔ You are not authorized to restart the bot.",
        "shutdown_requested": "🛑 **Shutdown Requested** by {user_first_name} (@{username})\nPID: `{process_id}`",
        "shutdown_aborted": "🛑 Shutdown aborted.",
        "shutdown_awaiting": "⏳ Shutdown can be canceled within the next 10 seconds...\nElapsed: {time_elapsed}",
        "shutdown_in_progress": "♻️ Shutting down now... ({time_elapsed})",
        "shutdown_declined": "⛔ You are not authorized to shut down the bot.",
        "permission_declined": "⛔ Permission denied."
    },
    "tr": {
        "restart_requested": "🔄 **Yeniden Başlatma İstendi** bởi {user_first_name} (@{username})\nPID: `{process_id}`",
        "restart_canceled": "🔄 Yeniden başlatma iptal edildi.",
        "restart_aborted": "❌ Yeniden başlatma iptal edildi.",
        "restart_awaiting": "⏳ Aktif görevlerin bitmesi bekleniyor...\nGeçen süre: {time_elapsed}",
        "restart_in_progress": "♻️ Şimdi yeniden başlatılıyor... ({time_elapsed})",
        "restart_declined": "⛔ Botu yeniden başlatma yetkiniz yok.",
        "shutdown_requested": "🛑 **Kapatma İstendi** bởi {user_first_name} (@{username})\nPID: `{process_id}`",
        "shutdown_aborted": "🛑 Kapatma iptal edildi.",
        "shutdown_awaiting": "⏳ Kapatma önümüzdeki 10 saniye içinde iptal edilebilir...\nGeçen süre: {time_elapsed}",
        "shutdown_in_progress": "♻️ Şimdi kapatılıyor... ({time_elapsed})",
        "shutdown_declined": "⛔ Botu kapatma yetkiniz yok.",
        "permission_declined": "⛔ İzin reddedildi."
    },
    "ru": {
        "restart_requested": "🔄 **Запрошен перезапуск** от {user_first_name} (@{username})\nPID: `{process_id}`",
        "restart_canceled": "🔄 Перезапуск отменен.",
        "restart_aborted": "❌ Перезапуск прерван.",
        "restart_awaiting": "⏳ Ожидание завершения активных задач...\nПрошло: {time_elapsed}",
        "restart_in_progress": "♻️ Перезапускаюсь... ({time_elapsed})",
        "restart_declined": "⛔ У вас нет прав на перезапуск бота.",
        "shutdown_requested": "🛑 **Запрошено выключение** от {user_first_name} (@{username})\nPID: `{process_id}`",
        "shutdown_aborted": "🛑 Выключение прервано.",
        "shutdown_awaiting": "⏳ Выключение можно отменить в течение следующих 10 секунд...\nПрошло: {time_elapsed}",
        "shutdown_in_progress": "♻️ Выключаюсь... ({time_elapsed})",
        "shutdown_declined": "⛔ У вас нет прав на выключение бота.",
        "permission_declined": "⛔ Доступ запрещен."
    },
    "de": {
        "restart_requested": "🔄 **Neustart angefordert** von {user_first_name} (@{username})\nPID: `{process_id}`",
        "restart_canceled": "🔄 Neustart wurde abgebrochen.",
        "restart_aborted": "❌ Neustart abgebrochen.",
        "restart_awaiting": "⏳ Warte auf den Abschluss aktiver Aufgaben...\nVerstrichen: {time_elapsed}",
        "restart_in_progress": "♻️ Starte jetzt neu... ({time_elapsed})",
        "restart_declined": "⛔ Du bist nicht berechtigt, den Bot neu zu starten.",
        "shutdown_requested": "🛑 **Herunterfahren angefordert** von {user_first_name} (@{username})\nPID: `{process_id}`",
        "shutdown_aborted": "🛑 Herunterfahren abgebrochen.",
        "shutdown_awaiting": "⏳ Das Herunterfahren kann innerhalb der nächsten 10 Sekunden abgebrochen werden...\nVerstrichen: {time_elapsed}",
        "shutdown_in_progress": "♻️ Fahre jetzt herunter... ({time_elapsed})",
        "shutdown_declined": "⛔ Du bist nicht berechtigt, den Bot herunterzufahren.",
        "permission_declined": "⛔ Zugriff verweigert."
    }
}

# utils/run_cmd.py
run_cmd_strings = {
    "en": {
        "correct_usage": "Usage: /exec [command]",
        "admin_only_msg": "This command is for administrators only.",
        "exec_cmd_exception": "An error occurred while executing the command for {userID} (@{username}): {user_error_message}",
        "command_out": "**Output:**\n```\n{stdout}\n```",
        "command_err": "**Error:**\n```\n{stderr}\n```"
    },
    "tr": {
        "correct_usage": "Kullanım: /exec [komut]",
        "admin_only_msg": "Bu komut sadece yöneticiler içindir.",
        "exec_cmd_exception": "{userID} (@{username}) için komut çalıştırılırken bir hata oluştu: {user_error_message}",
        "command_out": "**Çıktı:**\n```\n{stdout}\n```",
        "command_err": "**Hata:**\n```\n{stderr}\n```"
    },
    "ru": {
        "correct_usage": "Использование: /exec [команда]",
        "admin_only_msg": "Эта команда только для администраторов.",
        "exec_cmd_exception": "Произошла ошибка при выполнении команды для {userID} (@{username}): {user_error_message}",
        "command_out": "**Вывод:**\n```\n{stdout}\n```",
        "command_err": "**Ошибка:**\n```\n{stderr}\n```"
    },
    "de": {
        "correct_usage": "Verwendung: /exec [Befehl]",
        "admin_only_msg": "Dieser Befehl ist nur für Administratoren.",
        "exec_cmd_exception": "Beim Ausführen des Befehls für {userID} (@{username}) ist ein Fehler aufgetreten: {user_error_message}",
        "command_out": "**Ausgabe:**\n```\n{stdout}\n```",
        "command_err": "**Fehler:**\n```\n{stderr}\n```"
    }
}