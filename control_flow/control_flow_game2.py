#!usr/bin/python3

#import argparse
from staticfg import CFGBuilder

#parser = argparse.ArgumentParser(description='Generate the control flow graph\
# of a Python program')
#parser.add_argument('input_file', help='Path to a file containing a Python\
# program for which the CFG must be generated')
#parser.add_argument('output_file', help='Path to a file where the produced\
# visualisation of the CFG must be saved')

#args = parser.parse_args()
#cfg_name = args.input_file.split('/')[-1]
cfg = CFGBuilder().build_from_file('game2', './game2.py')
cfg.build_visual('game2CFG', format='png', calls=True)