class Polish:
    strings = {
        "restart_requested": "🔄 **Żądanie ponownego uruchomienia** przez {user_full_name} (@{username})\nPID: `{process_id}`",
        "restart_canceled": "🔄 Ponowne uruchomienie zostało anulowane.",
        "restart_aborted": "❌ Ponowne uruchomienie przerwane.",
        "restart_awaiting": "⏳ Oczekiwanie na zakończenie aktywnych zadań...\nUpłynęło: {time_elapsed}",
        "restart_in_progress": "♻️ Ponowne uruchamianie... ({time_elapsed})",
        "restart_declined": "⛔ Nie masz uprawnień do ponownego uruchomienia bota.",
        "shutdown_requested": "🛑 **Żądanie wyłączenia** przez {user_full_name} (@{username})\nPID: `{process_id}`",
        "shutdown_aborted": "🛑 Wyłączenie przerwane.",
        "shutdown_awaiting": "⏳ Wyłączenie można anulować w ciągu następnych 10 sekund...\nUpłynęło: {time_elapsed}",
        "shutdown_in_progress": "♻️ Wyłączanie... ({time_elapsed})",
        "shutdown_declined": "⛔ Nie masz uprawnień do wyłączenia bota.",
        "permission_declined": "⛔ Odmowa dostępu."
    }