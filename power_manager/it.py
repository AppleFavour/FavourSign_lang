class Italian:
    strings = {
        "restart_requested": "🔄 **Riavvio richiesto** da {user_full_name} (@{username})\nPID: `{process_id}`",
        "restart_canceled": "🔄 Riavvio annullato.",
        "restart_aborted": "❌ Riavvio interrotto.",
        "restart_awaiting": "⏳ In attesa del completamento delle attività attive...\nTempo trascorso: {time_elapsed}",
        "restart_in_progress": "♻️ Riavvio in corso... ({time_elapsed})",
        "restart_declined": "⛔ Non sei autorizzato a riavviare il bot.",
        "shutdown_requested": "🛑 **Spegnimento richiesto** da {user_full_name} (@{username})\nPID: `{process_id}`",
        "shutdown_aborted": "🛑 Spegnimento interrotto.",
        "shutdown_awaiting": "⏳ Lo spegnimento può essere annullato entro i prossimi 10 secondi...\nTempo trascorso: {time_elapsed}",
        "shutdown_in_progress": "♻️ Spegnimento in corso... ({time_elapsed})",
        "shutdown_declined": "⛔ Non sei autorizzato a spegnere il bot.",
        "permission_declined": "⛔ Permesso negato."
    }
