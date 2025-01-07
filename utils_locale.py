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
    },
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
    }
}
