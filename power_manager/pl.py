class Polish:
    strings = {
        "restart_requested": "🔄 **Żądanie ponownego uruchomienia** przez {user_full_name} (@{username})\nPID: `{process_id}`",
        "restart_canceled": "🔄 Ponowne uruchomienie zostało anulowane.",
        "restart_aborted": "❌ Ponowne uruchomienie przerwane.",
        "restart_awaiting": "⏳ Active tasks remaining: {remaining_tasks}\nWaiting for finish...",
        "restart_in_progress": "♻️ Ponowne uruchamianie...",
        "restart_declined": "⛔ Nie masz uprawnień do ponownego uruchomienia bota.",
        "shutdown_requested": "🛑 **Żądanie wyłączenia** przez {user_full_name} (@{username})\nPID: `{process_id}`",
        "shutdown_aborted": "🛑 Wyłączenie przerwane.",
        "shutdown_awaiting": "⏳ Wyłączenie można anulować w ciągu następnych 10 sekund...",
        "shutdown_in_progress": "♻️ Wyłączanie...",
        "shutdown_declined": "⛔ Nie masz uprawnień do wyłączenia bota.",
        "permission_declined": "⛔ Odmowa dostępu."
    }
