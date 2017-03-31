# -*- coding: utf-8 -*-

import uuid


class UUIDTools(object):
    """UUID Helper"""

    @staticmethod
    def uuid1_hex():
        """return uuid1 hex string, eg: 23f87b528d0f11e696a7f45c89a84eed"""
        return uuid.uuid1().hex