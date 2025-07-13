class English:
    strings = {
        "restart_requested": "🔄 **Restart Requested** by {user_full_name} (@{username})\nPID: `{process_id}`",
        "restart_canceled": "🔄 Restart has been canceled.",
        "restart_aborted": "❌ Restart aborted.",
        "restart_awaiting": "⏳ Waiting for active tasks to finish...\nElapsed: {time_elapsed}",
        "restart_in_progress": "♻️ Restarting now... ({time_elapsed})",
        "restart_declined": "⛔ You are not authorized to restart the bot.",
        "shutdown_requested": "🛑 **Shutdown Requested** by {user_full_name} (@{username})\nPID: `{process_id}`",
        "shutdown_aborted": "🛑 Shutdown aborted.",
        "shutdown_awaiting": "⏳ Shutdown can be canceled within the next 10 seconds...\nElapsed: {time_elapsed}",
        "shutdown_in_progress": "♻️ Shutting down now... ({time_elapsed})",
        "shutdown_declined": "⛔ You are not authorized to shut down the bot.",
        "permission_declined": "⛔ Permission denied."
    }
