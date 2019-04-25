import json
from os import path as p

class Model(dict):
    '''Manage library data.'''
    def __init__(self):
        self['libraries'] = {}
        self['assets'] = []

    def set_library_folder(self, path):
        if not p.exists(path):
            print(path + ' is not a path')
            return
        self.library_folder = path

    def get_assets(self):
        return self['assets']

    def add_asset(self, asset):
        self['assets'].append(asset)

    def save(self, dst):
        out_dict = {}
        out_dict['library_folder'] = self.library_folder
        out_dict['assets'] = self.assets
        with open(dst, 'w') as outfile:
            json.dump(out_dict, outfile, indent=4)

    def load(self, src):
        in_dict = {}
        with open(src, 'r') as infile:
            in_dict = json.load(infile)
        self.library_folder = in_dict.get('library_folder')
        self.assets = in_dict.get('assets')

    def create_test_data(self):
        for i in ['asset_' + str(x) for x in range(500)]:
            self.add_asset(i)


def main():
    pass

if __name__ == '__main__':
    main()
