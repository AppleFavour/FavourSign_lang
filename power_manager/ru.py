class Russian:
    strings = {
        "restart_requested": "🔄 **Запрошен перезапуск** от {user_full_name} (@{username})\nPID: `{process_id}`",
        "restart_canceled": "🔄 Перезапуск отменен.",
        "restart_aborted": "❌ Перезапуск прервано.",
        "restart_awaiting": "⏳ Ожидание завершения активных задач...\nПрошло: {time_elapsed}",
        "restart_in_progress": "♻️ Перезапускаюсь... ({time_elapsed})",
        "restart_declined": "⛔ У вас нет прав на перезапуск бота.",
        "shutdown_requested": "🛑 **Запрошено выключение** от {user_full_name} (@{username})\nPID: `{process_id}`",
        "shutdown_aborted": "🛑 Выключение прервано.",
        "shutdown_awaiting": "⏳ Выключение можно отменить в течение следующих 10 секунд...\nПрошло: {time_elapsed}",
        "shutdown_in_progress": "♻️ Выключаюсь... ({time_elapsed})",
        "shutdown_declined": "⛔ У вас нет прав на выключение бота.",
        "permission_declined": "⛔ Доступ запрещен."
    }