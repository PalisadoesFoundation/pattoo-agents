#!/usr/bin/env python3
"""Test the files module."""

# Standard imports
import unittest
import os
import sys

# Try to create a working PYTHONPATH
EXEC_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(
    os.path.abspath(os.path.join(
        os.path.abspath(os.path.join(
            EXEC_DIR, os.pardir)), os.pardir)), os.pardir))
if EXEC_DIR.endswith(
        '/pattoo-agents/tests/test_pattoo_agents/os') is True:
    # We need to prepend the path in case PattooShared has been installed
    # elsewhere on the system using PIP. This could corrupt expected results
    sys.path.insert(0, ROOT_DIR)
else:
    print('''\
This script is not installed in the \
"pattoo-agents/tests/test_pattoo_agents/os" directory. Please fix.''')
    sys.exit(2)

# Pattoo imports
from tests.libraries.configuration import UnittestConfig

from pattoo_agents.os.constants import PATTOO_AGENT_OS_SPOKED_API_PREFIX
from pattoo_agents.os.constants import PATTOO_AGENT_OS_SPOKED
from pattoo_agents.os.constants import PATTOO_AGENT_OS_SPOKED_PROXY
from pattoo_agents.os.constants import PATTOO_AGENT_OS_AUTONOMOUSD
from pattoo_agents.os.constants import PATTOO_AGENT_OS_HUBD


class TestConstants(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test_constants(self):
        """Testing constants."""
        # Test agent constants
        self.assertEqual(
            PATTOO_AGENT_OS_SPOKED_API_PREFIX, '/pattoo-agent-os')
        self.assertEqual(
            PATTOO_AGENT_OS_SPOKED, 'pattoo_agent_os_spoked')
        self.assertEqual(
            PATTOO_AGENT_OS_SPOKED_PROXY,
            '{}-gunicorn'.format(PATTOO_AGENT_OS_SPOKED))
        self.assertEqual(
            PATTOO_AGENT_OS_AUTONOMOUSD, 'pattoo_agent_os_autonomousd')
        self.assertEqual(
            PATTOO_AGENT_OS_HUBD, 'pattoo_agent_os_hubd')



if __name__ == '__main__':
    # Make sure the environment is OK to run unittests
    UnittestConfig().create()

    # Do the unit test
    unittest.main()