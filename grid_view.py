'''Define a custom widget for viewing a grid of items with images.'''

from tkinter import *
from tkinter.ttk import *

class GridView(Canvas):
    '''Display a grid of items.'''
    def __init__(self, parent, **options):
        Canvas.__init__(self, parent, options)
        self.parent = parent
        self.columns = IntVar()
        self.columns.set(5)
        self.items = []
        self.bind('<Configure>', self.draw_items)
        self.bind('<Enter>', self.bind_to_scroll)
        self.bind('<Leave>', self.unbind_to_scroll)

    def roll_wheel(self, event):
        print(event)
        self.yview('scroll', -event.delta//100, 'units')

        self.limit_scroll()

    def bind_to_scroll(self, event):
        print(event)
        self.bind('<MouseWheel>', self.roll_wheel)

    def unbind_to_scroll(self, event):
        self.unbind('<4>')
        self.unbind('<5>')

    def clear(self):
        self.items = []

    def add_items(self, list_of_items):
        self.clear()
        for i in list_of_items:
            self.items.append(i)

    def draw_items(self, *args):
        self.delete('all')
        for index, item in enumerate(self.items):
            self.draw_single_item(index, item)

    def draw_single_item(self, index, item):
        self.update()
        x1, y1, w = self.get_item_coords(index)
        x2 = x1 + w
        y2 = y1 + w
        self.create_rectangle(x1, y1, x2, y2)
        self.create_text(x1 + w / 2, y1 + w / 2, text=item)

    def get_bottom(self):
        last = len(self.items)
        x, y, w = self.get_item_coords(last)
        bottom = y + w
        return bottom

    def get_item_coords(self, index):
        """Return x, y, w at a given item index."""
        width = self.winfo_width()
        cols = self.columns.get()
        w = width / cols
        x = (index % cols) * (w)
        y = (index // cols) * (w)
        return(x, y, w)

    def limit_scroll(self):
        offset = self.canvasy(0)
        h = self.winfo_height()
        extent = self.canvasy(h)
        if offset <= 0:
            self.yview_moveto(0)

        b = self.get_bottom()
        if extent >= b:
            print(f'BOTTOM: {b-h}')
            self.yview_moveto(b)

def main():
    root = Tk()
    TEST_MODEL = ['item_' + str(x) for x in range(500)]
    item_view = GridView(root, bg='white')
    item_view.add_items(TEST_MODEL)
    item_view.pack(fill=BOTH, expand=True)
    item_view.draw_items()
    root.mainloop()

if __name__ == '__main__':
    main()
