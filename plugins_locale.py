# Plugins/announcements.py
announcements_strings = {
    "EN": {
        "no_reply": "🔍 Announcement message not found. Please reply to a message and try again.",
        "no_content": "🔍 Announcement content not found. Please reply to a message with text or a file.",
        "permission_denied": "🚫 You do not have permission to perform this action.",
        "announcement_complete": "✅ Announcement completed.\n\nTotal users: {total}\nSent: {sent}\nFailed: {failed}",
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
}
# Plugins/download.py
download_strings = {
    "EN": {
        "download_pending": "**Download pending**",
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
        "download_pending": "**İndirme bekleniyor**",
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
        "download_pending": "**Ожидание загрузки**",
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
}
# Plugins/language_select.py
language_select_strings = {
    "EN": {
        "select_language": "Select a language",
        "selected": "Selected",
        "already_selected": "You have already selected the current language.",
        "save_failed": "Failed to save the language.",
        "new_language_selected": "New language selected",
        "error_in_language_selection": "An error occurred during language selection.",
        "saving_language_pref": "Saving language preference...",
        "language_already_saved": "Language {lang} already saved for user {userID}",
        "language_saved_successfully": "Language {lang} saved successfully for user {userID}",
        "database_error": "A database error occurred. Please try again later.",
        "no_language_found": "No language preference found for the user",
        "using_default_language": "Default language (EN) will be used",
        "back_button": "Go Back 🔙",
    },
    "TR": {
        "select_language": "Dil seçiniz",
        "selected": "Seçilen",
        "already_selected": "Zaten seçili dili seçtiniz.",
        "save_failed": "Dil kaydedilemedi.",
        "new_language_selected": "Yeni dil seçildi",
        "error_in_language_selection": "Dil seçiminde bir hata oluştu.",
        "saving_language_pref": "Dil tercihi kaydediliyor...",
        "language_already_saved": "Dil zaten kaydedildi",
        "language_saved_successfully": "Dil başarıyla kaydedildi",
        "database_error": "Veritabanı hatası oluştu. Lütfen daha sonra tekrar deneyin.",
        "no_language_found": "Kullanıcı için dil tercihi bulunamadı",
        "using_default_language": "Varsayılan dil (TR) kullanılacak",
        "back_button": "Geri Dön 🔙",
    },
    "RU": {
        "select_language": "Выберите язык",
        "selected": "Выбранный",
        "already_selected": "Вы уже выбрали текущий язык.",
        "save_failed": "Не удалось сохранить язык.",
        "new_language_selected": "Новый язык выбран",
        "error_in_language_selection": "Произошла ошибка при выборе языка.",
        "saving_language_pref": "Сохранение предпочтений языка...",
        "language_already_saved": "Язык {lang} уже сохранен для пользователя {userID}",
        "language_saved_successfully": "Язык {lang} успешно сохранен для пользователя {userID}",
        "database_error": "Произошла ошибка базы данных. Пожалуйста, попробуйте позже.",
        "no_language_found": "Предпочтение языка не найдено для пользователя",
        "using_default_language": "Будет использован язык по умолчанию (RU)",
        "back_button": "Назад 🔙",
    }
}
# Plugins/modifier.py **to-do**
modifier_strings = {
    "EN": {},
    "TR": {},
    "RU": {},
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
        "modify_retry_error": "An error occurred while modifying, retrying... ({failed_modify_attempt}/{max_modify_attempt})"
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
        "modify_retry_error": "Düzenleme sırasında hata oluştu, tekrar deneniyor... ({failed_modify_attempt}/{max_modify_attempt})"
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
        "modify_retry_error": "Произошла ошибка при модификации, повторная попытка... ({failed_modify_attempt}/{max_modify_attempt})"
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
        "premium_unreg_error": "Error occurred during premium removal. Please try again."
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
        "premium_unreg_error": "Premium üyelik iptali sırasında bir hata oluştu. Lütfen tekrar deneyin."
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
        "premium_unreg_error": "Произошла ошибка при удалении премиум. Пожалуйста, попробуйте снова."
    },
}
