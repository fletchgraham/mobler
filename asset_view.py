'''Define a custom widget for viewing a grid of assets with images.'''

from tkinter import *
from tkinter.ttk import *

class AssetView(Canvas):
    def __init__(self, parent, **options):
        Canvas.__init__(self, parent, options)
        self.parent = parent
        self.columns = IntVar()
        self.columns.set(5)
        self.assets = []
        self.bind('<Configure>', self.draw_assets)

    def clear(self):
        self.assets = []

    def add_assets(self, list_of_assets):
        self.clear()
        for i in list_of_assets:
            self.assets.append(i)

    def draw_assets(self, *args):
        self.delete('all')
        for index, asset in enumerate(self.assets):
            self.draw_single_asset(index, asset)

    def draw_single_asset(self, index, asset):
        self.update()
        width = self.winfo_width()
        cols = self.columns.get()
        w = width / cols
        x1 = (index % cols) * (w)
        y1 = (index // cols) * (w)
        x2 = x1 + w
        y2 = y1 + w
        self.create_rectangle(x1, y1, x2, y2)
        self.create_text(x1 + w / 2, y1 + w / 2, text=asset)


def main():
    root = Tk()
    TEST_MODEL = ['asset_' + str(x) for x in range(500)]
    asset_view = AssetView(root, bg='white')
    asset_view.add_assets(TEST_MODEL)
    asset_view.pack(fill=BOTH, expand=True)
    asset_view.draw_assets()
    root.mainloop()

if __name__ == '__main__':
    main()
