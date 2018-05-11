#!/usr/bin/env python3
"""
Settings contains different setting parametres to be used
throughout the system
"""

DBSettings = {
    "dbtype": "MongoDB",
    "connection": {
        "host": "<HOST>",
        "port": "<PORT>"
    },

    # Credentials: the username for read-only access 
    "readonly": {
        "username": "KeepCurrent_1_RO",
        "password": "<PASSWRORD>"
    },

    # Credentials: the username for read-write access 
    "readwrite": {
        "username": "KeepCurrent_1_RW",
        "password": "<PASSWRORD>"
    }
}
