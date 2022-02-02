import click


@click.group(short_help="custom_theme CLI.")
def custom_theme():
    """custom_theme CLI.
    """
    pass


@custom_theme.command()
@click.argument("name", default="custom_theme")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [custom_theme]
