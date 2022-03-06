"""Console script for ping_pong_paradox."""
import sys
import click

import ping_pong_paradox

@click.command()
def main(args=None):
    """Console script for ping_pong_paradox."""
    click.echo("Starting Ping Pong Paradox")
    ping_pong_paradox.main()
    click.echo("Shutting Ping Pong Paradox down. Thanks for playing 😊👋")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
