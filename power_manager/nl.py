class Dutch:
    strings = {
        "restart_requested": "🔄 **Herstart aangevraagd** door {user_full_name} (@{username})\nPID: `{process_id}`",
        "restart_canceled": "🔄 Herstart is geannuleerd.",
        "restart_aborted": "❌ Herstart afgebroken.",
        "restart_awaiting": "⏳ Active tasks remaining: {remaining_tasks}\nWaiting for finish...",
        "restart_in_progress": "♻️ Nu opnieuw opstarten...",
        "restart_declined": "⛔ U bent niet gemachtigd om de bot opnieuw te starten.",
        "shutdown_requested": "🛑 **Afsluiten aangevraagd** door {user_full_name} (@{username})\nPID: `{process_id}`",
        "shutdown_aborted": "🛑 Afsluiten afgebroken.",
        "shutdown_awaiting": "⏳ Afsluiten kan binnen de volgende 10 seconden worden geannuleerd...",
        "shutdown_in_progress": "♻️ Nu afsluiten...",
        "shutdown_declined": "⛔ U bent niet gemachtigd om de bot af te sluiten.",
        "permission_declined": "⛔ Toegang geweigerd."
    }
