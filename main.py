#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test docstring for main module.
"""
from abaqus import session

class odb(object):
    """
    A wrapper for odbs.
    """
    
    def __init__(self, path):
        self.path = path
        self.odb = None
        
    def open(self):
        """Open an odb. """
        self.odb = session.openOdb(self.path)
        return self.odb
    
    def close(self):
        """Close the odb."""
        self.odb.close()
        self.odb = None
        
