#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test docstring for main module.
"""
from abaqus import session

class odb(object):
    """
    A wrapper for odbs.

    Attributes
    ----------
    path : str
        Path to the underlying odb.
    odb : Abaqus odb object or None
        The open odb, if one is open.

    """

    def __init__(self, path):
        self.path = path
        self.odb = None

    def open(self):
        """
        Open an odb.

        Returns
        -------
        odb : Abaqus odb object.

        """
        self.odb = session.openOdb(self.path)
        return self.odb

    def close(self):
        """
        Close the odb.

        Returns
        -------
        None

        """
        self.odb.close()
        self.odb = None

