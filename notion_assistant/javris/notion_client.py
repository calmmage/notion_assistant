import logging
from functools import cached_property

import notion_client


class NotionClient:  # todo: make a factory, forbid duplication
    def __init__(self, token):
        self.client = notion_client.Client(auth=token)

    def get_db(self, id):
        return NotionDB(id=id, client=self)

    def find_db(self, name):
        res = self.client.search(query=name)['results']
        if len(res) != 1:
            raise RuntimeError(f"Ambiguous search results: {res}")  # todo: format pretty
        return self.get_db(res[0]['id'])

    def get_page(self, id):
        return NotionPage(id=id, client=self)

    def find_page(self, name):
        res = self.client.search(query=name)['results']
        if len(res) > 1:
            logging.warning(f"Ambiguous search results: {res}")  # todo: format pretty
        elif len(res) == 0:
            raise RuntimeError("No results")
        return self.get_page(res[0]['id'])

    @property
    def workspace_name(self):
        return "lavrovs"  # todo: implement properly
    # @property
    # def dbs(self) -> Dict[str, NotionDB]:
    #     pass

    # todo map

    # todo dot-access


NOTION_LINK_TEMPLATE = "https://www.notion.so/{id}"


class NotionObject:
    def __init__(self, id, client: NotionClient):
        self.id = id
        self.client = client

    @property
    def url(self):
        raise NOTION_LINK_TEMPLATE.format(id=self.id)


class NotionDB(NotionObject):
    # def __init__(self, id, client: Notion):
    #     self.id = id
    #     self.client = client

    def add_item(self, item):
        # todo: verify item, patch if issues
        # todo: check that response is the page address
        return self.client.client.pages.create(parent={"database_id": self.id}, **item)

    @cached_property  # todo: refresh cache from time to time?
    def metadata(self):
        return self.client.client.databases.retrieve(self.id)

    # todo: summary. Recently edited pages + Big pages

    # todo: suggestions - __dir__, dot-access


class NotionPage(NotionObject):
    # def __init__(self, id,  client: Notion):
    #     self.id = id
    #     self.client = client

    @cached_property  # todo: just remove? requests are cheap
    def metadata(self):
        return self.client.client.pages.retrieve(self.id)
