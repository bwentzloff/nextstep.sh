import click
import json
from nextstep.agent import AIProjectAgent


@click.group()
def cli():
    """Nextstep.sh - AI-powered project assistant"""
    pass


@cli.command()
@click.argument("goal")
def generate(goal):
    """Generate project tasks based on the given goal"""
    agent = AIProjectAgent()
    click.echo(f"Generating tasks for: {goal}")

    tasks = agent.generate_tasks(goal)
    click.echo(json.dumps(tasks, indent=4))


if __name__ == "__main__":
    cli()
