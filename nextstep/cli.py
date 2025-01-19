import click


@click.group()
def cli():
    """Nextstep.sh - AI-powered project assistant"""
    pass


@cli.command()
@click.argument("goal")
def generate(goal):
    """Generate tasks for a given goal"""
    click.echo(f"Generating tasks for: {goal}")


if __name__ == "__main__":
    cli()
