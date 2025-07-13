class Chinese:
    strings = {
        "restart_requested": "🔄 **重启请求** 由 {user_full_name} (@{username})\nPID: `{process_id}`",
        "restart_canceled": "🔄 重启已取消。",
        "restart_aborted": "❌ 重启中止。",
        "restart_awaiting": "⏳ 正在等待活动任务完成...\n已用时间: {time_elapsed}",
        "restart_in_progress": "♻️ 正在重启... ({time_elapsed})",
        "restart_declined": "⛔ 您无权重启机器人。",
        "shutdown_requested": "🛑 **关机请求** 由 {user_full_name} (@{username})\nPID: `{process_id}`",
        "shutdown_aborted": "🛑 关机中止。",
        "shutdown_awaiting": "⏳ 关机可在接下来的 10 秒内取消...\n已用时间: {time_elapsed}",
        "shutdown_in_progress": "♻️ 正在关机... ({time_elapsed})",
        "shutdown_declined": "⛔ 您无权关闭机器人。",
        "permission_declined": "⛔ 权限被拒绝。"
    }