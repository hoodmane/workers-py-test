"""CLI entry point for pywrangler."""

import click
from rich.console import Console

from . import __version__

console = Console()


@click.group()
@click.version_option(version=__version__, prog_name="pywrangler")
@click.option("--debug", is_flag=True, help="Enable debug mode")
def app(debug: bool) -> None:
    """Pywrangler - Python tooling for Cloudflare Workers (test dummy)."""
    if debug:
        console.print("[yellow]Debug mode enabled[/yellow]")


@app.command()
def sync() -> None:
    """Sync Python packages for Workers."""
    console.print("[green]Syncing packages...[/green]")
    console.print("[green]Done![/green]")


@app.command()
def types() -> None:
    """Generate Python type stubs from wrangler config."""
    console.print("[green]Generating type stubs...[/green]")
    console.print("[green]Done![/green]")


@app.command()
def info() -> None:
    """Show environment information."""
    from workers import __version__ as sdk_version

    console.print(f"pywrangler version: {__version__}")
    console.print(f"workers-runtime-sdk version: {sdk_version}")


@app.command()
def status() -> None:
    """Show current deployment status."""
    console.print("[bold]Deployment Status[/bold]")
    console.print("  Workers: [green]healthy[/green]")
    console.print("  Runtime: [green]ready[/green]")
