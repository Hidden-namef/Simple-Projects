import subprocess
import os

class Lab:
    '''
    A class to represent a laboratory for running automated tests on a specified Python script.
    
    Attributes:
        path_file (str): The absolute path to the Python file to be tested.
        test_cases (int): The number of test cases to run.
        conditions (list): A list of conditions, each containing a description and expected output.
        input_values (list): A list of input values to provide during the tests.
        results (list): A list of boolean values indicating whether each test passed.

    Methods:
        add_condition(condition):
            Adds a test condition to the `conditions` attribute.
        
        add_input_value(value):
            Adds an input value to the `input_values` attribute.
        
        execute_file(input_values=None):
            Executes the specified Python file with optional input data.
        
        run_cases():
            Runs all test cases and evaluates their results.
    '''

    def __init__(self):
        '''
        Initializes the Lab instance with default values.
        
        Attributes:
            - `path_file (str)`: The default file path. Modify this path as per your environment.
            - `test_cases (int)`: Default number of test cases, set to 1.
            - `conditions (list)`: Initially empty, stores conditions for the tests.
            - `input_values (list)`: Initially empty, stores input values for the tests.
            - `results (list)`: Initially empty, stores boolean results of test cases.
        '''

        self.path_file = "D:\Visual Studio Code\Python\Test\Python.py"   # This is my path. You have to modify for yours own path
        self.test_cases = 1     # The number of test cases, you can modify this for your own preferences
        self.conditions = []
        self.input_values = []
        self.results = []
    
    def add_condition(self, condition):
        '''
        Adds a test condition to the `conditions` list.

        Args:
            condition (list): A list containing two elements:
                - Description (str): A brief description of the condition.
                - Expected value (any): The expected output of the test case.
        
        Requirements:
            - The `condition` argument must be a list of exactly two elements.
            - The first element must be a string (description).
            - The second element can be of any type (expected value).

        Example:
            lab.add_condition(["Check addition", 5])
        '''

        if not isinstance(condition, list) or len(condition) != 2:
            print('Condition not match the required parameters.')
            return
        
        self.conditions.append({'Description': condition[0], 'Expected_value': str(condition[1])})
    
    def add_input_value(self, value):
        '''
        Adds an input value to the `input_values` list for use during test execution.

        Args:
            value (str): The input value to provide to the script.

        Example:
            lab.add_input_value("5")
        '''

        self.input_values.append(value)
    
    def execute_file(self, input_values=None):
        '''
        Executes the specified Python script with optional input values.

        Args:
            input_values (list, optional): A list of input values to provide to the script. 
                                Defaults to None, in which case `self.input_values` is used.

        Returns:
            list: A list of outputs produced by the script for each test case.
        
        Notes:
            - Verifies the file exists before execution.
            - Ensures the number of conditions and input values matches `self.test_cases`.
        '''

        if not os.path.exists(self.path_file):
            print('Error: The specified file path does not exist. Please check the path and try again.')
            return []
        
        with open(self.path_file) as file:
            if file.readlines() == '':
                print('Error: The specified file is empty.')  # Make you sure that the file you want to probe is not in blank
                return []
        
        input_values = self.input_values    # Automatically, I select the input data
        if len(self.conditions) != self.test_cases or len(input_values) != self.test_cases:
            print('Error: The number of conditions or input values does not match the number of test cases.')
            return []
        
        outputs = []
        for i in range(self.test_cases):
            input_ = input_values[i]
            output = subprocess.run(f'python "{self.path_file}"', input=input_, capture_output=True, text=True, encoding='utf-8')
            outputs.append(output.stdout.strip())
        return outputs
        
    def run_cases(self):
        '''
        Runs all test cases and evaluates their results.

        Returns:
            list: A list of boolean values indicating whether each test case passed.
        
        Workflow:
            - Executes the script for all test cases using `execute_file`.
            - Compares the actual output to the expected value for each condition.
        '''

        outputs = self.execute_file()
        
        for i in range(len(outputs)):
            self.results.append(outputs[i] == self.conditions[i]['Expected_value'])
        return self.results


# Create an instance of the Lab class
lab = Lab()

# Conditions and values. Make you sure them have an argument
try:
    lab.add_condition()
    lab.add_input_value()
except TypeError:
    print('The functions "add_condition" and "add_input_value" in class "Lab" require an argument.')

# Run the test
results = lab.run_cases()

# Print the results
for i, result in enumerate(results):
    status = 'Passed ✅' if result == True else 'Failed ❌'
    print(f'Test {i}. {lab.conditions[i]["Description"]}: {status}')
    print(f'Expected value: {lab.conditions[i]["Expected_value"]}, Got: {result}')

# Print the summary of passed tests
passed_average = results.count(True)
print(f'Passed: {passed_average}/{len(results)}')
