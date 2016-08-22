#!/usr/bin/env python
# Filename: car2mol2.py

from msmtmol.itfc_dict_table import atom_type_dict as attyp_dict
from msmtmol.readcar import read_carf, print_mol2f
from optparse import OptionParser

parser = OptionParser("Usage: car2mol2.py -i input_file -o output_file -r residue_name \n")
parser.add_option("-i", dest="infile", type='string',
                  help="Input file name")
parser.add_option("-o", dest="outfile", type='string',
                  help="Output file name")
parser.add_option("-r", dest="resname", type='string',
                  help="Residue name")
(options, args) = parser.parse_args()

mol, atids, resids = read_carf(options.infile)
print_mol2f(mol, atids, options.outfile, options.resname, attyp_dict)

