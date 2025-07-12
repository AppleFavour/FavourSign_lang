# Plugins/speedtest.py
speedtest_strings = {
    "en": {
        "speedtest_start": "🚀 Testing connection speed...",
        "network_error": "A network error occurred. Please check your connection and try again.",
        "timeout_error": "The request timed out. Please try again.",
        "unknown_error": "An unexpected error occurred. Please try again.",
    },
    "tr": {
        "speedtest_start": "🚀 Bağlantı hızı test ediliyor...",
        "network_error": "Bir ağ hatası oluştu. Lütfen bağlantınızı kontrol edip tekrar deneyin.",
        "timeout_error": "İstek zaman aşımına uğradı. Lütfen tekrar deneyin.",
        "unknown_error": "Beklenmedik bir hata oluştu. Lütfen tekrar deneyin.",
    },
    "ru": {
        "speedtest_start": "🚀 Тестирование скорости соединения...",
        "network_error": "Произошла сетевая ошибка. Пожалуйста, проверьте ваше соединение и попробуйте снова.",
        "timeout_error": "Время ожидания запроса истекло. Пожалуйста, попробуйте снова.",
        "unknown_error": "Произошла непредвиденная ошибка. Пожалуйста, попробуйте снова.",
    },
    "de": {
        "speedtest_start": "🚀 Verbindungsgeschwindigkeit wird getestet...",
        "network_error": "Ein Netzwerkfehler ist aufgetreten. Bitte überprüfe deine Verbindung und versuche es erneut.",
        "timeout_error": "Die Anfrage ist abgelaufen. Bitte versuche es erneut.",
        "unknown_error": "Ein unerwarteter Fehler ist aufgetreten. Bitte versuche es erneut.",
    },
    "es": {
        "speedtest_start": "🚀 Probando velocidad de conexión...",
        "network_error": "Ocurrió un error de red. Por favor, verifica tu conexión e inténtalo de nuevo.",
        "timeout_error": "La solicitud ha caducado. Por favor, inténtalo de nuevo.",
        "unknown_error": "Ocurrió un error inesperado. Por favor, inténtalo de nuevo.",
    },
    "fr": {
        "speedtest_start": "🚀 Test de la vitesse de connexion...",
        "network_error": "Une erreur réseau est survenue. Veuillez vérifier votre connexion et réessayer.",
        "timeout_error": "La requête a expiré. Veuillez réessayer.",
        "unknown_error": "Une erreur inattendue est survenue. Veuillez réessayer.",
    },
    "zh-cn": {
        "speedtest_start": "🚀 正在测试连接速度...",
        "network_error": "发生网络错误。请检查您的连接并重试。",
        "timeout_error": "请求超时。请重试。",
        "unknown_error": "发生未知错误。请重试。",
    },
    "ar": {
        "speedtest_start": "🚀 جاري اختبار سرعة الاتصال...",
        "network_error": "حدث خطأ في الشبكة. الرجاء التحقق من اتصالك والمحاولة مرة أخرى.",
        "timeout_error": "انتهت مهلة الطلب. الرجاء المحاولة مرة أخرى.",
        "unknown_error": "حدث خطأ غير متوقع. الرجاء المحاولة مرة أخرى.",
    },
    "pt": {
        "speedtest_start": "🚀 Testando velocidade de conexão...",
        "network_error": "Ocorreu um erro de rede. Por favor, verifique sua conexão e tente novamente.",
        "timeout_error": "A solicitação expirou. Por favor, tente novamente.",
        "unknown_error": "Ocorreu um erro inesperado. Por favor, tente novamente.",
    },
    "it": {
        "speedtest_start": "🚀 Test della velocità di connessione...",
        "network_error": "Si è verificato un errore di rete. Controlla la tua connessione e riprova.",
        "timeout_error": "La richiesta è scaduta. Riprova.",
        "unknown_error": "Si è verificato un errore imprevisto. Riprova.",
    },
    "ja": {
        "speedtest_start": "🚀 接続速度をテスト中...",
        "network_error": "ネットワークエラーが発生しました。接続を確認して再試行してください。",
        "timeout_error": "リクエストがタイムアウトしました。もう一度お試しください。",
        "unknown_error": "予期しないエラーが発生しました。もう一度お試しください。",
    },
    "ko": {
        "speedtest_start": "🚀 연결 속도 테스트 중...",
        "network_error": "네트워크 오류가 발생했습니다. 연결을 확인하고 다시 시도하십시오.",
        "timeout_error": "요청 시간이 초과되었습니다. 다시 시도하십시오.",
        "unknown_error": "예기치 않은 오류가 발생했습니다. 다시 시도하십시오.",
    },
    "hi": {
        "speedtest_start": "🚀 कनेक्शन की गति का परीक्षण कर रहा है...",
        "network_error": "एक नेटवर्क त्रुटि हुई। कृपया अपना कनेक्शन जांचें और पुनः प्रयास करें।",
        "timeout_error": "अनुरोध का समय समाप्त हो गया। कृपया पुनः प्रयास करें।",
        "unknown_error": "एक अप्रत्याशित त्रुटि हुई। कृपया पुनः प्रयास करें।",
    },
    "vi": {
        "speedtest_start": "🚀 Đang kiểm tra tốc độ kết nối...",
        "network_error": "Đã xảy ra lỗi mạng. Vui lòng kiểm tra kết nối của bạn và thử lại.",
        "timeout_error": "Yêu cầu đã hết thời gian chờ. Vui lòng thử lại.",
        "unknown_error": "Đã xảy ra lỗi không mong muốn. Vui lòng thử lại.",
    },
    "id": {
        "speedtest_start": "🚀 Menguji kecepatan koneksi...",
        "network_error": "Terjadi kesalahan jaringan. Harap periksa koneksi Anda dan coba lagi.",
        "timeout_error": "Permintaan waktu habis. Silakan coba lagi.",
        "unknown_error": "Terjadi kesalahan tak terduga. Silakan coba lagi.",
    },
    "pl": {
        "speedtest_start": "🚀 Testowanie prędkości połączenia...",
        "network_error": "Wystąpił błąd sieci. Sprawdź połączenie i spróbuj ponownie.",
        "timeout_error": "Limit czasu żądania został przekroczony. Spróbuj ponownie.",
        "unknown_error": "Wystąpił nieoczekiwany błąd. Spróbuj ponownie.",
    },
    "nl": {
        "speedtest_start": "🚀 Verbindingssnelheid testen...",
        "network_error": "Er is een netwerkfout opgetreden. Controleer uw verbinding en probeer het opnieuw.",
        "timeout_error": "De aanvraag is verlopen. Probeer het opnieuw.",
        "unknown_error": "Er is een onverwachte fout opgetreden. Probeer het opnieuw.",
    }
}
