class Japanese:
    strings = {
        "restart_requested": "🔄 **再起動要求** {user_full_name} (@{username})より\nPID: `{process_id}`",
        "restart_canceled": "🔄 再起動はキャンセルされました。",
        "restart_aborted": "❌ 再起動は中止されました。",
        "restart_awaiting": "⏳ Active tasks remaining: {remaining_tasks}\nWaiting for finish...",
        "restart_in_progress": "♻️ 今すぐ再起動中...",
        "restart_declined": "⛔ ボットを再起動する権限がありません。",
        "shutdown_requested": "🛑 **シャットダウン要求** {user_full_name} (@{username})より\nPID: `{process_id}`",
        "shutdown_aborted": "🛑 シャットダウンは中止されました。",
        "shutdown_awaiting": "⏳ シャットダウンは次の10秒以内にキャンセルできます...",
        "shutdown_in_progress": "♻️ 今すぐシャットダウン中...",
        "shutdown_declined": "⛔ ボットをシャットダウンする権限がありません。",
        "permission_declined": "⛔ 権限が拒否されました。"
    }
