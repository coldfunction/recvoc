import sys
import climenu
from shutil import copyfile
from input_voc import *
from recite import *

backup_level1 = "1_level.txt"
backup_level2 = "2_level.txt"
tmp_level1    = ".1_level.tmp"
tmp_level2    = ".2_level.tmp"

copyfile(backup_level1, tmp_level1)
copyfile(backup_level2, tmp_level2)

@climenu.menu()
def build_voc():
    '''Create voc'''
    rval = input_vocabulary(backup_level1) 
    print('Create', rval, 'ok!\n')

@climenu.menu()
def build_recite():
    '''Recite'''
    if recite_voc(tmp_level1, tmp_level2) :
        copyfile(tmp_level1, backup_level1)	
        copyfile(tmp_level2, backup_level2)		
	

if __name__ == '__main__':
    climenu.run()
