# vim: ts=4:sw=4:expandtab
# -*- coding: UTF-8 -*-

# BleachBit
# Copyright (C) 2008-2025 Andrew Ziem
# https://www.bleachbit.org
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""
Test case for module SystemInformation
"""

from tests import common
from bleachbit.SystemInformation import get_system_information, get_version


class SystemInformationTestCase(common.BleachbitTestCase):
    """Test Case for module SystemInformation"""

    def test_get_system_information(self):
        """Test get_system_information"""
        # at least it does not crash
        ret = get_system_information()
        self.assertIsString(ret)

    def test_get_version(self):
        """Test get_version"""
        ret = get_version()
        self.assertIsString(ret)
        # check it is in a.b.c.d or a.b.c format
        self.assertRegex(ret, r'^\d+\.\d+\.\d+(\.\d+)?$')
        ret = get_version(four_parts=True)
        self.assertIsString(ret)
        # check it is in a.b.c.d format
        self.assertRegex(ret, r'^\d+\.\d+\.\d+\.\d+$')
