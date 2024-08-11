"""
Library for interaction with generic parts of the Notion Glow template

Namely, core databases - Todos, Notes and Bookmarks

And core item types
    - Application
    - Process
    - Project
    - Context

    - Working session
"""
from notion_assistant.jarvis.enhanced_notion_client import EnhancedNotionClient


class GlowEnhancedNotionClient(EnhancedNotionClient):

    def find_page(self, query, context=None):
        pass
        # todo: support shortcuts
        # todo: narrow search to main item types

        # todo: fancy dynamic heuristics
        # dynamically expand/narrow search based on # of results

        # request additional info from user via telegram
