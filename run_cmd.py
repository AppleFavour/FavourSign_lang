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
    },
    "es": {
        "correct_usage": "Uso: /exec [comando]",
        "admin_only_msg": "Este comando es solo para administradores.",
        "exec_cmd_exception": "Ocurrió un error al ejecutar el comando para {userID} (@{username}): {user_error_message}",
        "command_out": "**Salida:**\n```\n{stdout}\n```",
        "command_err": "**Error:**\n```\n{stderr}\n```"
    },
    "fr": {
        "correct_usage": "Utilisation: /exec [commande]",
        "admin_only_msg": "Cette commande est réservée aux administrateurs.",
        "exec_cmd_exception": "Une erreur est survenue lors de l'exécution de la commande pour {userID} (@{username}): {user_error_message}",
        "command_out": "**Sortie:**\n```\n{stdout}\n```",
        "command_err": "**Erreur:**\n```\n{stderr}\n```"
    },
    "zh-cn": {
        "correct_usage": "用法: /exec [命令]",
        "admin_only_msg": "此命令仅供管理员使用。",
        "exec_cmd_exception": "为 {userID} (@{username}) 执行命令时发生错误: {user_error_message}",
        "command_out": "**输出:**\n```\n{stdout}\n```",
        "command_err": "**错误:**\n```\n{stderr}\n```"
    },
    "ar": {
        "correct_usage": "الاستخدام: /exec [الأمر]",
        "admin_only_msg": "هذا الأمر للمسؤولين فقط.",
        "exec_cmd_exception": "حدث خطأ أثناء تنفيذ الأمر لـ {userID} (@{username}): {user_error_message}",
        "command_out": "**الإخراج:**\n```\n{stdout}\n```",
        "command_err": "**خطأ:**\n```\n{stderr}\n```"
    },
    "pt": {
        "correct_usage": "Uso: /exec [comando]",
        "admin_only_msg": "Este comando é apenas para administradores.",
        "exec_cmd_exception": "Ocorreu um erro ao executar o comando para {userID} (@{username}): {user_error_message}",
        "command_out": "**Saída:**\n```\n{stdout}\n```",
        "command_err": "**Erro:**\n```\n{stderr}\n```"
    },
    "it": {
        "correct_usage": "Uso: /exec [comando]",
        "admin_only_msg": "Questo comando è solo per gli amministratori.",
        "exec_cmd_exception": "Si è verificato un errore durante l'esecuzione del comando per {userID} (@{username}): {user_error_message}",
        "command_out": "**Output:**\n```\n{stdout}\n```",
        "command_err": "**Errore:**\n```\n{stderr}\n```"
    },
    "ja": {
        "correct_usage": "使用法: /exec [コマンド]",
        "admin_only_msg": "このコマンドは管理者のみが使用できます。",
        "exec_cmd_exception": "{userID} (@{username}) のコマンド実行中にエラーが発生しました: {user_error_message}",
        "command_out": "**出力:**\n```\n{stdout}\n```",
        "command_err": "**エラー:**\n```\n{stderr}\n```"
    },
    "ko": {
        "correct_usage": "사용법: /exec [명령]",
        "admin_only_msg": "이 명령은 관리자 전용입니다.",
        "exec_cmd_exception": "{userID} (@{username})에 대한 명령 실행 중 오류가 발생했습니다: {user_error_message}",
        "command_out": "**출력:**\n```\n{stdout}\n```",
        "command_err": "**오류:**\n```\n{stderr}\n```"
    },
    "hi": {
        "correct_usage": "उपयोग: /exec [कमांड]",
        "admin_only_msg": "यह कमांड केवल प्रशासकों के लिए है।",
        "exec_cmd_exception": "{userID} (@{username}) के लिए कमांड निष्पादित करते समय एक त्रुटि हुई: {user_error_message}",
        "command_out": "**आउटपुट:**\n```\n{stdout}\n```",
        "command_err": "**त्रुटि:**\n```\n{stderr}\n```"
    },
    "vi": {
        "correct_usage": "Cách dùng: /exec [lệnh]",
        "admin_only_msg": "Lệnh này chỉ dành cho quản trị viên.",
        "exec_cmd_exception": "Đã xảy ra lỗi khi thực thi lệnh cho {userID} (@{username}): {user_error_message}",
        "command_out": "**Đầu ra:**\n```\n{stdout}\n```",
        "command_err": "**Lỗi:**\n```\n{stderr}\n```"
    },
    "id": {
        "correct_usage": "Penggunaan: /exec [perintah]",
        "admin_only_msg": "Perintah ini hanya untuk administrator.",
        "exec_cmd_exception": "Terjadi kesalahan saat mengeksekusi perintah untuk {userID} (@{username}): {user_error_message}",
        "command_out": "**Output:**\n```\n{stdout}\n```",
        "command_err": "**Error:**\n```\n{stderr}\n```"
    },
    "pl": {
        "correct_usage": "Użycie: /exec [komenda]",
        "admin_only_msg": "To polecenie jest tylko dla administratorów.",
        "exec_cmd_exception": "Wystąpił błąd podczas wykonywania polecenia dla {userID} (@{username}): {user_error_message}",
        "command_out": "**Wyjście:**\n```\n{stdout}\n```",
        "command_err": "**Błąd:**\n```\n{stderr}\n```"
    },
    "nl": {
        "correct_usage": "Gebruik: /exec [commando]",
        "admin_only_msg": "Dit commando is alleen voor beheerders.",
        "exec_cmd_exception": "Er is een fout opgetreden tijdens het uitvoeren van het commando voor {userID} (@{username}): {user_error_message}",
        "command_out": "**Output:**\n```\n{stdout}\n```",
        "command_err": "**Fout:**\n```\n{stderr}\n```"
    }
}
