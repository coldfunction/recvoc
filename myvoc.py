import sys
import climenu
from input_voc import *
from recite import *


@climenu.menu()
def build_voc():
    '''Create voc'''
    # TODO: Call the build scripts here!
    rval = input_vocabulary() 
    print('Create', rval, 'ok!\n')

@climenu.menu()
def build_recite():
    '''Recite'''
    # TODO: Call the build scripts here!
    recite_voc()

if __name__ == '__main__':
    climenu.run()
