
def parse_command(full_command: str) -> dict:
    """
    Parse telegram command format for Jarvis

    Examples:
    1. Simple command example:
    >>> parse_command('/idea Test jarvis #link Notion Assistant #blue #important')
    {'command': '/idea', 'text': 'Test jarvis', 'tags': {'link': 'Notion Assistant', 'blue': None, 'important': None}}

    2. Text only
    >>> parse_command('Just text with tags #link Notion Assistant #blue #important')
    {'command': None, 'text': 'Just text with tags', 'tags': {'link': 'Notion Assistant', 'blue': None, 'important': None}}
    """
    output = {}

    # parse command
    if full_command.startswith('/'):
        command, message = full_command.split(None, 1)
        output['command'] = command.rstrip()
    else:
        message = full_command
        output['command'] = None


    text, *tags = message.split('#')

    # parse text
    text = text.strip()
    if '\n' in text.strip():
        # text with content, for example in
        # /idea Make tests
        # So that everything is tested
        # #Important
        text, content = text.split('\n', 1)
        output['text'] = text
        output['content'] = content
    else:
        output['text'] = text

    # parse tags
    tags = [[part.rstrip() for part in tag.split(None, 1)] for tag in tags]
    output['tags'] = dict([(tag + [None] if len(tag) == 1 else tag) for tag in tags])

    return output


if __name__ == "__main__":
    import doctest
    doctest.testmod()
