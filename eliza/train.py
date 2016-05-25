import pickle
import model
import sys
import argparse

parser = argparse.ArgumentParser(description='options')
parser.add_argument('-i', required=True, help='input text file')
parser.add_argument('-o', required=True, help='output model file (.pickle)')
parser.add_argument('--iteration', type=int, default=1000, help='iteration times')
args = parser.parse_args()

lang = model.Lang(args.i)
lang.train(iterator=args.iteration)
with open(args.o, mode='wb') as f:
    pickle.dump(lang, f)
