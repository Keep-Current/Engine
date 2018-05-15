#!/usr/bin/python3
# -*- coding: utf-8 -*-
from abc import ABC

class DbUserBase(ABC):

    def get_user_details(self, user_guid):
        """
        Retrieves user's data according to the guid: email, name, etc.
        """
        raise NotImplementedError