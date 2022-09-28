
import unittest
from BeautifulReport import BeautifulReport

from api.utils.handle_path import cases_dir, reports_dir


# Retrieve test cases
s = unittest.TestLoader().discover(cases_dir)

# generate reports
br = BeautifulReport(s)
br.report("unittest login API report", "report_.html", reports_dir)
