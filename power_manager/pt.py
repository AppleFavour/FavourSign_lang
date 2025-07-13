class Portuguese:
    strings = {
        "restart_requested": "🔄 **Reinicialização Solicitada** por {user_full_name} (@{username})\nPID: `{process_id}`",
        "restart_canceled": "🔄 Reinicialização foi cancelada.",
        "restart_aborted": "❌ Reinicialização abortada.",
        "restart_awaiting": "⏳ Aguardando a conclusão das tarefas ativas...\nTempo decorrido: {time_elapsed}",
        "restart_in_progress": "♻️ Reiniciando agora... ({time_elapsed})",
        "restart_declined": "⛔ Você não está autorizado a reiniciar o bot.",
        "shutdown_requested": "🛑 **Desligamento Solicitado** por {user_full_name} (@{username})\nPID: `{process_id}`",
        "shutdown_aborted": "🛑 Desligamento abortado.",
        "shutdown_awaiting": "⏳ O desligamento pode ser cancelado nos próximos 10 segundos...\nTempo decorrido: {time_elapsed}",
        "shutdown_in_progress": "♻️ Desligando agora... ({time_elapsed})",
        "shutdown_declined": "⛔ Você não está autorizado a desligar o bot.",
        "permission_declined": "⛔ Permissão negada."
    }