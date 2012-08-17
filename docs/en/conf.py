# -*- coding: utf-8 -*-
import os
import sys

language_dir = os.path.realpath(os.path.dirname(__file__))
sys.path = [os.path.abspath(os.path.join(language_dir, '..'))] + sys.path

from common import *

#
# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'
