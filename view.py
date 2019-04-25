from tkinter import *
#from tkinter.ttk import *
from tkinter.filedialog import askdirectory

from grid_view import GridView

class View():
    def __init__(self, model):
        self.model = model
        self.model.create_test_data()
        self.root = Tk()
        self.create_widgets()
        self.root.title("Mobler Asset Browser")
        self.root.mainloop()

    def create_widgets(self):
        self.create_the_top_bar()
        self.create_the_grid_view()
        self.create_the_footer()

    def create_the_top_bar(self):
        # Container
        toolbar = Frame(self.root)
        toolbar.pack(fill=X)

        # Search bar
        self.search_entry_var = StringVar()
        self.search_entry = Entry(
            toolbar, textvariable=self.search_entry_var)
        self.search_entry.pack(side=LEFT, fill=X, expand=True)

        # Buttons
        buttons = [
            Button(toolbar, text="Search"),
            Button(toolbar, text="Save Images"),
            Button(toolbar, text="Open"),
            Button(toolbar, text="Refresh"),
            Button(toolbar, text="-", command=self.decrease_thumb_size),
            Button(toolbar, text="+", command=self.increase_thumb_size)
            ]

        for b in buttons:
            b.configure(relief=FLAT)
            b.pack(side=LEFT)

    def create_the_grid_view(self):
        self.grid_view = GridView(self.root, bg='white')
        self.grid_view.pack(fill=BOTH, expand=True)
        self.grid_view.add_items(self.model.get_assets())

    def create_the_footer(self):
        # Container
        footer = Frame(self.root)
        footer.pack(fill=X)

        # library Path Editor
        self.library_path_var = StringVar()
        self.library_path_var.set("Click to set a library path.")
        Button(footer, textvariable=self.library_path_var,
            command=self.change_library, relief=FLAT).pack(side=RIGHT)

    # COMMANDS

    def decrease_thumb_size(self):
        self.grid_view.columns.set(self.grid_view.columns.get() + 1)
        self.grid_view.draw_items()

    def increase_thumb_size(self):
        self.grid_view.columns.set(self.grid_view.columns.get() - 1)
        self.grid_view.draw_items()

    def change_library(self):
        new_path = askdirectory()
        if not new_path:
            return
        self.model.set_library_folder(new_path)
        self.library_path_var.set(self.model.get_library_folder())


if __name__ == '__main__':
    from model import Model
    model = Model()
    view = View(model)
