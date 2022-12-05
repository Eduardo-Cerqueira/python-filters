import rich
import time
from rich.console import Console
from rich.theme import Theme
from rich.progress import track, Progress
from rich.live import Live
from rich.table import Table
from rich import print
from rich.layout import Layout
from rich.panel import Panel


def console_print(message,style_):
    custom_theme = Theme({
        "info": "dim cyan",
        "warning": "magenta",
        "danger": "bold red"
    })
    console = Console(theme=custom_theme)
    console.print("This is information", style=style_)
    #console.print("[warning]The pod bay doors are locked[/warning]")
    #console.print("Something terrible happened!", style="danger")

def working_bar():
    rich.progress_bar.ProgressBar(total=100, completed=0)
    for i in track(range(100), description="Processing..."):
        time.sleep(0.01)  # Simulate work being done

def panel_rich():
    print(Panel("Hello, [red]World!"))

def panel_rich2():
    rich.console.ConsoleDimensions(500,500)
    print(Panel("Hello, [red]World!", title="Welcome", subtitle="Thank you"))

def panel_rich3():
    print(Panel("Hello, [red]World!", title="Welcome", subtitle="Thank you"))

def progress_rich():
    with Progress() as progress:
        task1 = progress.add_task("[red]Downloading...", total=1000)
        task2 = progress.add_task("[green]Processing...", total=1000)
        task3 = progress.add_task("[cyan]Cooking...", total=1000)

        while not progress.finished:
            progress.update(task1, advance=0.5)
            progress.update(task2, advance=0.3)
            progress.update(task3, advance=0.9)
            time.sleep(0.02)

def tab():
    table = Table()
    table.add_column("Row ID")
    table.add_column("Description")
    table.add_column("Level")

    with Live(table, refresh_per_second=4):  # update 4 times a second to feel fluid
        for row in range(12):
            time.sleep(0.4)  # arbitrary delay
            # update the renderable internally
            table.add_row(f"{row}", f"description {row}", "[red]ERROR")

def layout_1top_2bottom(content_left,content_top,content_right):
    layout = Layout()
    layout.split_column(
    Layout(name="heigher"),
    Layout(name="lower")
    )
    layout["lower"].split_row(
    Layout(name="left"),
    Layout(name="right"),
    )
    layout["right"].update(
        Layout(Panel("Hello"))
    )
    layout["left"].update(
    Layout(Panel("The mystery of life isn't a problem to solve, but a reality to experience."))
    )
    layout["heigher"].update(
        Layout(Panel(content_top))
    )
    print(layout)

#layout_1top_2bottom("oof","oof","oof")
#update_right("oof")