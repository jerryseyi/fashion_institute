import shelve, sys

"""
    mcb.py - Saves and loads pieces of text to the cliboard
    Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
           py.exe mcb.pyw <keyword> - Loads keyword to clipboard
           py.exe mcb.pyw list - Loads all keywords to clipboard 
"""

mcbShelf = shelve.open('mcb')


mcbShelf.close()