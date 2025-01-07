# utils/certificate_handler.py
certificate_handler_strings = {
    "EN": {},
    "TR": {},
    "RU": {},
}
# utils/helpers.py
helpers_strings = {
    "EN": {},
    "TR": {},
    "RU": {},
}
# utils/main_helper.py
main_helper_strings = {
    "EN": {},
    "TR": {},
    "RU": {},
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
