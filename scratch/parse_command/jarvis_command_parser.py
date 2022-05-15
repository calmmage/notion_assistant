
def parse_command(full_command):
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
        command, message = full_command.split(' ', 1)
        output['command'] = command.rstrip()
    else:
        message = full_command
        output['command'] = None

    # parse text
    if '#' not in message:
        output['text'] = message.rstrip()
    else:
        text, message = message.split('#', 1)
        output['text'] = text.rstrip()

        # parse tags
        output['tags'] = {}
        tags = message.split('#')
        for tag in tags:
            tagparts = tag.split(' ', 1)
            if len(tagparts) == 1 or len(tagparts[1]) == 0:
                output['tags'][f'{tagparts[0]}'] = None
            else:
                output['tags'][f'{tagparts[0]}'] = tagparts[1].rstrip()

    return output


if __name__ == "__main__":
    import doctest
    doctest.testmod()
