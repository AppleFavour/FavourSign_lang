class French:
    strings = {
        "restart_requested": "🔄 **Redémarrage demandé** par {user_full_name} (@{username})\nPID: `{process_id}`",
        "restart_canceled": "🔄 Le redémarrage a été annulé.",
        "restart_aborted": "❌ Redémarrage annulé.",
        "restart_awaiting": "⏳ En attente de la fin des tâches activas...\nTemps écoulé: {time_elapsed}",
        "restart_in_progress": "♻️ Redémarrage en cours... ({time_elapsed})",
        "restart_declined": "⛔ Vous n'êtes pas autorisé à redémarrer le bot.",
        "shutdown_requested": "🛑 **Arrêt demandé** par {user_full_name} (@{username})\nPID: `{process_id}`",
        "shutdown_aborted": "🛑 Arrêt annulé.",
        "shutdown_awaiting": "⏳ L'arrêt peut être annulé dans les 10 prochaines secondes...\nTemps écoulé: {time_elapsed}",
        "shutdown_in_progress": "♻️ Arrêt en cours... ({time_elapsed})",
        "shutdown_declined": "⛔ Vous n'êtes pas autorisé à arrêter le bot.",
        "permission_declined": "⛔ Permission refusée."
    }