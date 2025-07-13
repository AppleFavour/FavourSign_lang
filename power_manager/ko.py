class Korean:
    strings = {
        "restart_requested": "🔄 **재시작 요청** {user_full_name} (@{username})님으로부터\nPID: `{process_id}`",
        "restart_canceled": "🔄 재시작이 취소되었습니다.",
        "restart_aborted": "❌ 재시작이 중단되었습니다.",
        "restart_awaiting": "⏳ 활성 작업 완료 대기 중...\n경과 시간: {time_elapsed}",
        "restart_in_progress": "♻️ 지금 재시작 중... ({time_elapsed})",
        "restart_declined": "⛔ 봇을 재시작할 권한이 없습니다.",
        "shutdown_requested": "🛑 **종료 요청** {user_full_name} (@{username})님으로부터\nPID: `{process_id}`",
        "shutdown_aborted": "🛑 종료가 중단되었습니다.",
        "shutdown_awaiting": "⏳ 종료는 다음 10초 이내에 취소할 수 있습니다...\n경과 시간: {time_elapsed}",
        "shutdown_in_progress": "♻️ 지금 종료 중... ({time_elapsed})",
        "shutdown_declined": "⛔ 봇을 종료할 권한이 없습니다.",
        "permission_declined": "⛔ 권한이 거부되었습니다."
    }
