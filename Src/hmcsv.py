"""
Home Made CSV File Reader
-------------------------
By Sean Dahan
26.11.2020
"""

from .Classes import Types


def read(file_path,deli = ","):
    
    return Types.Reader(file_path,deli=deli)