import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Test cases dir
cases_dir = os.path.join(base_dir, "testCases")
# Test data dir
data_dir = os.path.join(base_dir, "testData")
# Test report dir
reports_dir = os.path.join(base_dir, "output", "reports")
# Test logs dir
logs_dir = os.path.join(base_dir, "output", "logs")
# configuration dir
conf_dir = os.path.join(base_dir, "config")
