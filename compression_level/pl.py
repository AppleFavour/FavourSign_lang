class Polish:
    strings = {
        "compression_prompt": (
            "📁 **Select Compression Level**\n\n"
            "This setting affects the signing speed and the final file size.\n\n"
            "**0**: Fastest signing, largest file size.\n"
            "**9**: Slowest signing, smallest file size.\n\n"
            "Currently selected: **{selected}**"
        ),
        "already_selected": "⚠️ This level is already selected.",
        "save_error": "Could not save the compression level.",
        "db_error": "A database error occurred. Please try again.",
        "compression_selected": "📌 Compression level set to **{selected}**.",
        "selected_notification": "📌 Selected: {selected}",
        "generic_error": "⚠️ An unexpected error occurred.",
        "back_button": "🔙 Go Back",
    }
