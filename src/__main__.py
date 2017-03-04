#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Main file to execute, contains all the stuff to start the application properly
"""

# Libraries
import os
import sys
import platform
import logging
import core.log

from cli.arguments.parser import DEFAULT_PARSER
from cli.arguments.constants import *


# Constants
LOGGER = logging.getLogger(__name__)

# variables
"""
Arguments namespace
"""
args = None


# Functions
def parseArguments(parser, args=None):
    """
    Takes the system arguments vector and tries to parse the arguments in it
    given the argument parser specified and returns the namespace generated

    Args:
        parser(): the ArgumentParser objects to use to parse the arguments
        args(): arguments to parse (default is sys.argv)

    Returns:
        namespace of parsed arguments
    """
    return parser.parse_args(args)


if __name__ == "__main__":
    # Prepare coding
    if platform.system() == "Windows":
        os.system("chcp 65001")
    args = parseArguments(DEFAULT_PARSER)
    # Switching log level
    root_logger = logging.getLogger()
    root_logger.setLevel(LOGS_LEVELS[LOGS.index(args.log_level)])
    # Welcome
    LOGGER.info("Welcome !")
    # Exiting
    LOGGER.info("Bye !")
