
def parse_command(full_command):
    """
    Parse telegram command format for Jarvis

    Examples:
    1. Simple command example:
    >>> parse_command('/idea Test jarvis #link Notion Assistant #blue #important')
    {'command': '/idea', 'text': 'Test jarvis', 'tags': {'link': 'Notion Assistant', 'blue': None, 'important': None}}

    2. Text only
    TODO
    """
    output = {}

    # parse command
    command, full_command = full_command.split(' ', 1)
    output['command'] = command.rstrip()

    # parse text
    if '#' not in full_command:
        output['text'] = full_command.rstrip()
    else:
        text, full_command = full_command.split('#', 1)
        output['text'] = text.rstrip()

        # parse tags
        output['tags'] = {}
        tags = full_command.split('#')
        for tag in tags:
            tagparts = tag.split(' ', 1)
            if len(tagparts) == 1 or len(tagparts[1]) == 0:
                output['tags'][f'{tagparts[0]}'] = None
            else:
                output['tags'][f'{tagparts[0]}'] = tagparts[1].rstrip()

    return output
