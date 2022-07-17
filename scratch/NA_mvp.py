
# --------------------------------------
# config
# --------------------------------------

# prod: DB_Actionable
# todos_database = 'https://www.notion.so/lavrovs/2290411c436848479b4826e63d740c63?v=f50c1eebf2ba4441a922d523587b6b66'

# test: DB_test_notion_assistant
todos_database = 'https://www.notion.so/lavrovs/d96416324b44433a9d378f0767627301?v=877e567e513a4583b9e4614d1b059ba1'


# --------------------------------------
# utils
# --------------------------------------

def extract_database_id(database_link):
    """
    :param database_link: url to the database page
    :type database_link: str
    :return: Id of the database for use in Notion API
    """
    return database_link.rsplit('/', 1)[-1].split('?', 1)[0]



# --------------------------------------
# main
# --------------------------------------

# Telegram bot


# Notion API

