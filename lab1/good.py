#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           ��T��@���O<KA9�A���u�":�P@�G��ˊג����i�],<keM]�dMAz�bA��V�"v2������V�$5�:-)�WI,M�=�3`�NEu"�`!���.��c~�!�e"�-"""
from hashlib import sha256

if sha256(blob).hexdigest() == '0e0cce862ff0a3f265408d231446d15294f9f0615d4894836f8ba64fc31a4f25':
    print 'I come in peace.'
else:
    print 'Prepare to be destroyed!'
