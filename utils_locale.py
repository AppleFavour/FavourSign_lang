# utils/certificate_handler.py
certificate_handler_strings = {
    "en-US": {},
    "tr-TR": {},
    "ru-RU": {},
}
# utils/gen_html.py
gen_html_strings = {
    "en-US": {},
    "tr-TR": {},
    "ru-RU": {},
}
# utils/gen_plist.py
gen_plist_strings = {
    "en-US": {},
    "tr-TR": {},
    "ru-RU": {},
}
# utils/helpers.py
helpers_strings = {
    "en-US": {},
    "tr-TR": {},
    "ru-RU": {},
}
# utils/janitor.py
jan_strings = {
    "en-US": {},
    "tr-TR": {},
    "ru-RU": {},
}
# utils/logger.py
keyboard_strings = {
    "en-US": {},
    "tr-TR": {},
    "ru-RU": {},
}
# utils/main_helper.py
main_strings = {
    "en-US": {},
    "tr-TR": {},
    "ru-RU": {},
}
# utils/plugin_manager.py
plist_strings = {
    "en-US": {},
    "tr-TR": {},
    "ru-RU": {},
}
# utils/restart.py
restart_strings = {
    "en-US": {
        "restart_declined": "Sorry, only admins can restart bot. (Permission denied)",
        "restart_requested": "Restart requested by {userID} - @{username}",
        "shutdown_declined": "Sorry, only admins can shutdown bot. (Permission denied)",
        "shutdown_requested": "Shutdown requested by {userID} - @{username}",
        "restart_awaiting": "⚠️ Some directories still remain in {web_path}.\nWaiting for cleanup to complete...\n⌛️ Elapsed: {calculate_process_time((time.time() - start_time))}.",
        "restart_in_progress": "🔁 Bot is restarting...\n⌛️ Total elapsed: {calculate_process_time((time.time() - start_time))}."
    },
    "tr-TR": {
        "restart_declined": "Uzgunum, sadece adminler botu yeniden baslatabilir. (İzin reddedildi)",
        "restart_requested": "Yeniden baslatma talebi - @{username}",
        "shutdown_declined": "Uzgunum, sadece adminler botu kapatabilir. (İzin reddedildi)",
        "shutdown_requested": "Kapatma talebi - @{username}",
        "restart_awaiting": "⚠️ {web_path} Temizlenme tamamlanana kadar bekleniyor...\n⌛️ Gecen sure: {calculate_process_time((time.time() - start_time))}.",
        "restart_in_progress": "🔁 Bot Yeniden başlatiliyor...\n⌛️ Toplam süre: {calculate_process_time((time.time() - start_time))}."
    },
    "ru-RU": {
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
    "en-US": {
        "correct_usage": "Usage: /exec <command>",
        "admin_only_msg": "Sorry, only admins can execute commands. (Permission denied)",
        "exec_cmd_exception": "{userID} {username} - Error while executing command: {user_error_message}",
        "command_out": "Command output:\n{stdout}\n",
        "command_err": "Command error:\n{stderr}\n"
    },
    "tr-TR": {
        "correct_usage": "Kullanim: /exec <komut>",
        "admin_only_msg": "Sorry, only admins can execute commands. (Permission denied)",
        "exec_cmd_exception": "{userID} {username} - Komut calistirirken hata olustu: {user_error_message}",
        "command_out": ":\n{stdout}\n",
        "command_err": ":\n{stderr}\n"
    },
    "ru-RU": {
        "correct_usage": "",
        "admin_only_msg": "",
        "exec_cmd_exception": "{userID} {username} - : {user_error_message}",
        "command_out": ":\n{stdout}\n",
        "command_err": ":\n{stderr}\n"
    }
}
# utils/update.py
update_strings = {
    "en-US": {},
    "tr-TR": {},
    "ru-RU": {},
}
