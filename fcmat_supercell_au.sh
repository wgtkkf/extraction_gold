#!/bin/bash
python file_clear.py                    # added
python coordinate_extraction.py         # added
python split_au_c.py
pyhton coordinate_generic_extraction.py # added
python coordinate_au_c.py
python mat_construction_au_KLR.py
python copy_rename_au.py
python unit_conversion_L_au.py
python unit_conversion_R_au.py
python mass_matrices_au_supercell.py

python mat_construction_au_LCR.py
python unit_conversion_C_au.py