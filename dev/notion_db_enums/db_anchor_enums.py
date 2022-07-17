import os
import enum
import re
from notion_client import Client


def get_enums_from_db(notion_client: Client, db_id: str) -> dict:
    ''' gets all enums in all columns of type "select" in a database
    :param notion_client: ready-to-use client
    :param db_id: id of a database
    :return: {'col1': ['enumvalue1', 'enumvalue2', ...], ...}
    '''
    response = notion_client.databases.retrieve(db_id)
    cols_and_enums = {}

    for db_column in response['properties']:
        if response['properties'][db_column]['type'] != 'select':
            continue

        this_column_enums = [opt['name'] for opt in response['properties'][db_column]['select']['options']]
        cols_and_enums[db_column] = this_column_enums

    return cols_and_enums


def change_all_nonletters_to_underscores(data: str) -> str:
    return re.sub('[^0-9a-zA-Z]+', '_', data)


class S_Status(enum.Enum):
    Cancelled = 'Cancelled'
    Done = 'Done'
    In_progress = 'In progress'
    Focus = 'Focus'
    Todo = 'Todo'


class S_Priority(enum.Enum):
    Lowest = '1 - Lowest'
    Low = '2 - Low'
    Medium = '3 - Medium'
    High = '4 - High'
    Highest = '5 - Highest'


class C_Type(enum.Enum):
    Disposable = 'Disposable'
    Idea = 'Idea'
    Todo = 'Todo'
    Context_Project = 'Context/Project'
    App_Process = 'App/Process'


class S_Area(enum.Enum):
    Home = 'Home'
    Work = 'Work'
    Wellbeing = 'Wellbeing'
    For_Others = 'For Others'
    Meta = 'Meta'
    Life = 'Life',
    Unclear = 'Unclear'

