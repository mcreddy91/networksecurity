#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           ��T��@���O<KA9�A���u�":�P@�G��ˊג����i�],<keM]�dMAz�bA��V�"v2������V�$5�:-)�WI,M�=�3`�NEu"�`!���.��c~�!�e"�-"""
from hashlib import sha256
print sha256(blob).hexdigest()
