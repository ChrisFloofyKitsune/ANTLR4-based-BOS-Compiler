import tkinter



class RootTk(tkinter.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.option_add('*tearOff', tkinter.FALSE)

    def report_callback_exception(self, exc, val, tb):
        if exc == KeyboardInterrupt:
            exit(1)
        else:
            super().report_callback_exception(exc, val, tb)
