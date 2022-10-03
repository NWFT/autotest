import os
import sys
import unittest
from BeautifulReport import BeautifulReport

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from api.utils.path_handler import cases_dir, reports_dir


# Retrieve test cases
s = unittest.TestLoader().discover(cases_dir)

# generate reports
br = BeautifulReport(s)
br.report("unittest login API report", "report_.html", reports_dir)
