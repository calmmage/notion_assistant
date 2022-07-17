import pytest
import os
import json
from pathlib import Path
from notion_client import Client

from db_anchor_enums import get_enums_from_db, change_all_nonletters_to_underscores
import db_anchor_enums


class TestParseCommand:
    def test_anchor_db(self):
        secrets_path = Path('../secrets.json')
        secrets = json.load(secrets_path.open())
        notion = Client(auth=secrets["notion_token"])

        enums = get_enums_from_db(notion, "2290411c436848479b4826e63d740c63")

        for col in enums:
            assert hasattr(db_anchor_enums, change_all_nonletters_to_underscores(col)), f'No enum for {col=} in out code'

            n_option_in_col_ours = len(getattr(db_anchor_enums, change_all_nonletters_to_underscores(col)))
            n_option_in_col_remote = len(enums[col])
            assert n_option_in_col_ours == n_option_in_col_remote, f'Number of options in enum {col} differ: {n_option_in_col_ours} != {n_option_in_col_remote}.\n {getattr(db_anchor_enums, change_all_nonletters_to_underscores(col))}\n{enums[col]}'

