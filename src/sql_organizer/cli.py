import typer

from other import Model
from sql_organizer.main import echo


def main():
    Model()
    typer.run(echo)


if __name__ == "__main__":
    main()
