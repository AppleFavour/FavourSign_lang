class Chinese:
    strings = {
        "restart_requested": "🔄 **重启请求** 由 {user_full_name} (@{username})\nPID: `{process_id}`",
        "restart_canceled": "🔄 重启已取消。",
        "restart_aborted": "❌ 重启中止。",
        "restart_awaiting": "⏳ Active tasks remaining: {remaining_tasks}\nWaiting for finish...",
        "restart_in_progress": "♻️ 正在重启...",
        "restart_declined": "⛔ 您无权重启机器人。",
        "shutdown_requested": "🛑 **关机请求** 由 {user_full_name} (@{username})\nPID: `{process_id}`",
        "shutdown_aborted": "🛑 关机中止。",
        "shutdown_awaiting": "⏳ 关机可在接下来的 10 秒内取消...",
        "shutdown_in_progress": "♻️ 正在关机...",
        "shutdown_declined": "⛔ 您无权关闭机器人。",
        "permission_declined": "⛔ 权限被拒绝。"
    }
