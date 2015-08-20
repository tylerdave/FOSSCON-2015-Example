import click

@click.command()
def cli():
    click.echo("I'm a click CLI.")

if __name__ == '__main__':
    cli()
