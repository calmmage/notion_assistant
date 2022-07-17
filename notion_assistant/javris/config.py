from defaultenv import env

# Jarvis
notion_token = env("JARVIS_NOTION_TOKEN")
db_logs = env("JARVIS_SIMPLE_LOG_TABLE")
db_structured_logs = env("JARVIS_STUCTURED_LOG_TABLE")
jarvis_env = env("JARVIS_ENV")  # prod or dev

# Jarvis Input Bot
telegram_input_token = env("JARVIS_TELEGRAM_INPUT_TOKEN")
db_todos = env("JARVIS_DB_TODOS")
db_notes = env("JARVIS_DB_NOTES")
db_bookmarks = env("JARVIS_DB_BOOKMARKS")

# Jarvis Output Bot
telegram_token = env("JARVIS_TELEGRAM_TOKEN")

# Simple task Selector
telegram_sts_token = env("JARVIS_TELEGRAM_STS_TOKEN")

# Simple task repeater
db_str = env("JARVIS_DB_STR")
