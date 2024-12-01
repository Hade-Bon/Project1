from tkinter import *
import cmd2


class Cli(cmd2.Cmd):

    prompt = ">>$ "

# Aqui hacemos el codigo que me permitira integrar la CLI a Tkinter: (GUI)
    def __init__(self,screen_widget):
        super().__init__()
        self.screen_widget = screen_widget


    def do_take(self, line):
        output = self.screen_widget.get(1.4,END)
        print(output)

    def do_clear(self, line):
        self.screen_widget.delete(1.4,END)

    def update_scren(self):
        self.screen_widget.insert(END, "\n" + self.prompt)
    
    def postcmd(self, stop, line):
        self.update_screen()
        return stop

myshell = Tk()

myshell.title("Shell")

interface = Frame(myshell)
interface.pack()

screen = Text(interface, foreground="green")
screen.pack()

def take_write():
    taked = screen.get(1.4,END).strip()
    if taked:
        cli_instance.onecmd(taked)
    #print(taked)
    
Button(interface, text="SEND", command=take_write).pack()

cli_instance = Cli(screen) # Together with this code se integra la CLI a Tkinter

screen.insert(END,cli_instance.prompt)

myshell.mainloop()
