
"""
If you want to use this framework,
Here are API test steps with Unittest:

0. Prepare all test data in one file
1. Read test data from -testData excel-files
    (use 'excel_file_handler')
2. Define a TestClass
    eg.: class AddPosts(unitterst.TestCase)
3. Define the pre/after-conditions for this test suite
4. Make test cases
    (following unittest rules, def test_XXX())
    4-1 Replace "#MARK#" with dynamic values
        (use 'replace_test_data_values_handler')
    4-2 Send requests
    4-3 Get response data
    4-4 Assert response with expected results
"""