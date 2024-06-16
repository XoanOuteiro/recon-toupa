from rich.console import Console
from rich.text import Text

class HeaderPrinter:
    currentVersion = "Alpha 0.1.34"

    logoAscii = """    ____                            ______                       
   / __ \\___  _________  ____      /_  __/___  __  ______  ____ _
  / /_/ / _ \\/ ___/ __ \\/ __ \\______/ / / __ \\/ / / / __ \\/ __ `/
 / _, _/  __/ /__/ /_/ / / / /_____/ / / /_/ / /_/ / /_/ / /_/ / 
/_/ |_|\\___/\\___/\\____/_/ /_/     /_/  \\____/\\__,_/ .___/\\__,_/  
                                                 /_/             """
    
    header = f"""
    ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰

        >>Developed by: @XoanOuteiro
        >>Version:      {currentVersion}

    ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰
"""

    def __init__(self):
        self.console = Console()

    def print_stylized_text(self, text, primary_color="bright_yellow", secondary_color="yellow", segment_length=8):
        styled_text = Text()
        for i, char in enumerate(text):
            color = primary_color if (i // segment_length) % 2 == 0 else secondary_color
            styled_text.append(char, style=color)
        self.console.print(styled_text)

    def print_header_and_logo(self):
        self.print_stylized_text(self.logoAscii, primary_color="bright_yellow", secondary_color="yellow")
        print(self.header)