import pytest
from parse import parse_command


class TestParseCommand:
    def test_full(self):
        output = parse_command('/idea Test jarvis #link Notion Assistant #blue #important')
        correct_output = {'command': '/idea',
                          'text': 'Test jarvis',
                          'tags': {'link': 'Notion Assistant', 'blue': None, 'important': None}}

        assert output == correct_output

    def test_no_tags(self):
        output = parse_command('/idea Test jarvis ')
        correct_output = {'command': '/idea', 'text': 'Test jarvis'}

        assert output == correct_output

    def test_few_tags(self):
        output = parse_command('/idea Test jarvis #blue')
        correct_output = {'command': '/idea', 'text': 'Test jarvis', 'tags': {'blue': None}}

        assert output == correct_output