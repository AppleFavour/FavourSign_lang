# Plugins/announcements.py
announcements_strings = {
    "en": {
        "no_reply": "🔍 Please reply to a message to announce it.",
        "no_content": "🔍 The message you replied to has no content to announce.",
        "permission_denied": "🚫 You are not authorized to use this command.",
        "announcement_complete": "✅ Announcement sent successfully.\n\nTotal Recipients: {total}\nDelivered: {sent}\nFailed: {failed}",
    },
    "tr": {
        "no_reply": "🔍 Lütfen duyurmak için bir mesaja yanıt verin.",
        "no_content": "🔍 Yanıtladığınız mesajda duyurulacak bir içerik bulunmuyor.",
        "permission_denied": "🚫 Bu komutu kullanma yetkiniz yok.",
        "announcement_complete": "✅ Duyuru başarıyla gönderildi.\n\nToplam Alıcı: {total}\nUlaştırıldı: {sent}\nUlaştırılamadı: {failed}",
    },
    "ru": {
        "no_reply": "🔍 Пожалуйста, ответьте на сообщение, чтобы сделать объявление.",
        "no_content": "🔍 В сообщении, на которое вы ответили, нет содержимого для объявления.",
        "permission_denied": "🚫 У вас нет прав на использование этой команды.",
        "announcement_complete": "✅ Объявление успешно отправлено.\n\nВсего получателей: {total}\nДоставлено: {sent}\nНе доставлено: {failed}",
    },
    "de": {
        "no_reply": "🔍 Bitte antworte auf eine Nachricht, um sie anzukündigen.",
        "no_content": "🔍 Die Nachricht, auf die du geantwortet hast, hat keinen Inhalt zum Ankündigen.",
        "permission_denied": "🚫 Du bist nicht berechtigt, diesen Befehl zu verwenden.",
        "announcement_complete": "✅ Ankündigung erfolgreich gesendet.\n\nGesamtempfänger: {total}\nZugestellt: {sent}\nNicht zugestellt: {failed}"
    },
    "es": {
        "no_reply": "🔍 Por favor, responde a un mensaje para anunciarlo.",
        "no_content": "🔍 El mensaje al que respondiste no tiene contenido para anunciar.",
        "permission_denied": "🚫 No estás autorizado para usar este comando.",
        "announcement_complete": "✅ Anuncio enviado exitosamente.\n\nTotal de destinatarios: {total}\nEntregados: {sent}\nFallidos: {failed}",
    },
    "fr": {
        "no_reply": "🔍 Veuillez répondre à un message pour l'annoncer.",
        "no_content": "🔍 Le message auquel you avez répondu n'a pas de contenu à annoncer.",
        "permission_denied": "🚫 Vous n'êtes pas autorisé à utiliser cette commande.",
        "announcement_complete": "✅ Annonce envoyée avec succès.\n\nTotal des destinataires: {total}\nLivrés: {sent}\nÉchoués: {failed}",
    },
    "zh-cn": {
        "no_reply": "🔍 请回复一条消息来发布公告。",
        "no_content": "🔍 您回复的消息没有可公告的内容。",
        "permission_denied": "🚫 您无权使用此命令。",
        "announcement_complete": "✅ 公告发送成功.\n\n总接收者: {total}\n已送达: {sent}\n失败: {failed}",
    },
    "ar": {
        "no_reply": "🔍 الرجاء الرد على رسالة للإعلان عنها.",
        "no_content": "🔍 الرسالة التي رددت عليها لا تحتوي على محتوى للإعلان عنه.",
        "permission_denied": "🚫 غير مصرح لك باستخدام هذا الأمر.",
        "announcement_complete": "✅ تم إرسال الإعلان بنجاح.\n\nإجمالي المستلمين: {total}\nتم التسليم: {sent}\nفشل: {failed}",
    },
    "pt": {
        "no_reply": "🔍 Por favor, responda a uma mensagem para anunciá-la.",
        "no_content": "🔍 A mensagem à qual você respondeu não tem conteúdo para anunciar.",
        "permission_denied": "🚫 Você não está autorizado a usar este comando.",
        "announcement_complete": "✅ Anúncio enviado com sucesso.\n\nTotal de destinatários: {total}\nEntregues: {sent}\nFalhas: {failed}"
    },
    "it": {
        "no_reply": "🔍 Si prega di rispondere a un messaggio per annunciarlo.",
        "no_content": "🔍 Il messaggio a cui hai risposto non ha contenuto da annunciare.",
        "permission_denied": "🚫 Non sei autorizzato a usare questo comando.",
        "announcement_complete": "✅ Annuncio inviato con successo.\n\nDestinatari totali: {total}\nConsegnati: {sent}\nFalliti: {failed}"
    },
    "ja": {
        "no_reply": "🔍 アナウンスするにはメッセージに返信してください。",
        "no_content": "🔍 返信したメッセージにはアナウンスする内容がありません。",
        "permission_denied": "🚫 このコマンドを使用する権限がありません。",
        "announcement_complete": "✅ アナウンスが正常に送信されました。\n\n合計受信者数: {total}\n配信済み: {sent}\n失敗: {failed}"
    },
    "ko": {
        "no_reply": "🔍 공지하려면 메시지에 회신하십시오。",
        "no_content": "🔍 회신한 메시지에 공지할 내용이 없습니다。",
        "permission_denied": "🚫 이 명령을 사용할 권한이 없습니다。",
        "announcement_complete": "✅ 공지가 성공적으로 전송되었습니다。\n\n총 수신자: {total}\n전달됨: {sent}\n실패: {failed}"
    },
    "hi": {
        "no_reply": "🔍 कृपया घोषणा करने के लिए एक संदेश का जवाब दें।",
        "no_content": "🔍 आपके द्वारा जवाब दिए गए संदेश में घोषणा करने के लिए कोई सामग्री नहीं है।",
        "permission_denied": "🚫 आपको इस कमांड का उपयोग करने की अनुमति नहीं है।",
        "announcement_complete": "✅ घोषणा सफलतापूर्वक भेजी गई।\n\nकुल प्राप्तकर्ता: {total}\nवितरित: {sent}\nविफल: {failed}"
    },
    "vi": {
        "no_reply": "🔍 Vui lòng trả lời tin nhắn để thông báo.",
        "no_content": "🔍 Tin nhắn bạn đã trả lời không có nội dung để thông báo.",
        "permission_denied": "🚫 Bạn không được phép sử dụng lệnh này.",
        "announcement_complete": "✅ Thông báo đã được gửi thành công.\n\nTổng số người nhận: {total}\nĐã gửi: {sent}\nThất bại: {failed}"
    },
    "id": {
        "no_reply": "🔍 Mohon balas pesan untuk mengumumkannya.",
        "no_content": "🔍 Pesan yang Anda balas tidak memiliki konten untuk diumumkan.",
        "permission_denied": "🚫 Anda tidak diizinkan menggunakan perintah ini.",
        "announcement_complete": "✅ Pengumuman berhasil dikirim.\n\nTotal Penerima: {total}\nTerkirim: {sent}\nGagal: {failed}"
    },
    "pl": {
        "no_reply": "🔍 Proszę odpowiedzieć na wiadomość, aby ją ogłosić.",
        "no_content": "🔍 Wiadomość, na którą odpowiedziałeś, nie zawiera treści do ogłoszenia.",
        "permission_denied": "🚫 Nie masz uprawnień do używania tej komendy.",
        "announcement_complete": "✅ Ogłoszenie wysłane pomyślnie.\n\nCałkowita liczba odbiorców: {total}\nDostarczono: {sent}\nNiepowodzenia: {failed}"
    },
    "nl": {
        "no_reply": "🔍 Gelieve op een bericht te antwoorden om het aan te kondigen.",
        "no_content": "🔍 Het bericht waarop u hebt geantwoord, heeft geen inhoud om aan te kondigen.",
        "permission_denied": "🚫 U bent niet gemachtigd om dit commando te gebruiken.",
        "announcement_complete": "✅ Aankondiging succesvol verzonden.\n\nTotaal aantal ontvangers: {total}\nAfgeleverd: {sent}\nMislukt: {failed}"
    }
}
