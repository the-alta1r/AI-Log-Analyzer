from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, RichLog, Input, Static
from textual.binding import Binding


class CyberConsole(App):

    CSS = """
    Screen {
        background: black;
    }

    RichLog {
        border: solid green;
        color: green;
        background: black;
    }

    Input {
        border: solid green;
        color: green;
        background: black;
    }

    #banner {
        color: green;
        text-style: bold;
    }
    """

    BINDINGS = [
        Binding("ctrl+c", "quit", "Quit")
    ]

    def compose(self) -> ComposeResult:

        yield Header()

        with Vertical():

            yield Static("""
 █████╗ ██╗
██╔══██╗██║
███████║██║
██╔══██║██║
██║  ██║██║
╚═╝  ╚═╝╚═╝

AI SECURITY CONSOLE
""", id="banner")

            yield RichLog(id="logs",
                            highlight=True,
                            markup=True,
                            auto_scroll=True)

            yield Input(
                placeholder="msf-ai > ",
                id="command"
            )

        yield Footer()

    def on_mount(self):

        logs = self.query_one("#logs", RichLog)

        logs.write("[green]System initialized[/green]")
        logs.write("[green]Ollama connected[/green]")
        logs.write("[red]Monitoring started[/red]")

    async def on_input_submitted(self, event):

        command = event.value

        logs = self.query_one("#logs", RichLog)

        logs.write(f"[green]msf-ai > {command}[/green]")

        if command == "help":
            logs.write("""
Commands:
- scan
- analyze
- clear
- exit
""")

        elif command == "scan":
            logs.write("[red]Scanning logs...[/red]")
            logs.write("[yellow]Potential brute force attack[/yellow]")

        elif command == "clear":
            logs.clear()

        elif command == "exit":
            self.exit()

        else:
            logs.write("[red]Unknown command[/red]")

        self.query_one(Input).value = ""


if __name__ == "__main__":
    app = CyberConsole()
    app.run()