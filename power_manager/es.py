class Spanish:
    strings = {
        "restart_requested": "🔄 **Reinicio solicitado** por {user_full_name} (@{username})\nPID: `{process_id}`",
        "restart_canceled": "🔄 El reinicio ha sido cancelado.",
        "restart_aborted": "❌ Reinicio abortado.",
        "restart_awaiting": "⏳ Esperando que terminen las tareas activas...\nTiempo transcurrido: {time_elapsed}",
        "restart_in_progress": "♻️ Reiniciando ahora... ({time_elapsed})",
        "restart_declined": "⛔ No estás autorizado para reiniciar el bot.",
        "shutdown_requested": "🛑 **Apagado solicitado** por {user_full_name} (@{username})\nPID: `{process_id}`",
        "shutdown_aborted": "🛑 Apagado abortado.",
        "shutdown_awaiting": "⏳ El apagado se puede cancelar en los próximos 10 segundos...\nTiempo transcurrido: {time_elapsed}",
        "shutdown_in_progress": "♻️ Apagando ahora... ({time_elapsed})",
        "shutdown_declined": "⛔ No estás autorizado para apagar el bot.",
        "permission_declined": "⛔ Permiso denegado."
    }
