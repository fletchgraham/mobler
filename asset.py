'''Define the Asset class.

What is an Asset?

An Asset is a folder containing the necessary files to realize a specific idea.
The most common assets are nouns (like: chair, table, lamp) but this definition
is not so limiting. An asset could also be a entire scene, or something less
concrete, like a sky, or lighting setup. Here are some examples:

    "morning_sky" could be an asset folder containing an hdri, a jpg preview,
    and a 3d file with the settings all dialed in.

    "lounge_chair" could be an asset folder containing an obj file, a blend file,
    and a folder of texture maps.

    "walnut_floor" could be an asset folder containing a diffuse map and a
    normal map.

In the Code:
An Asset is represented as a Dictionary.
'''

class Asset(dict):
    '''The basic unit of the asset library.'''
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        print("Asset created!")


def main():
    asset = Asset
if __name__ == '__main__':
    main()
