# Prasanna kumari
Here are some commonly asked Tosca Basics Interview Questions and Answers that are useful for entry-level and intermediate interviews. These topics appear frequently in Tosca interview preparation guides and practitioner discussions.

1. What is Tricentis Tosca?

Answer:
Tosca is a model-based test automation tool used for functional, regression, API, mobile, and end-to-end testing. It provides scriptless automation, reducing the need for programming knowledge.

2. What are the key features of Tosca?

Answer:

Model-based testing
Scriptless automation
Risk-based testing
Test data management
API testing
Cross-browser testing
CI/CD integration
3. What are the main components of Tosca?

Answer:

Tosca Commander – Design and manage tests
Modules – Store scanned controls/objects
TestCases – Business test scenarios
ExecutionLists – Execute tests
Repository/Workspace – Store artifacts
4. What is Model-Based Testing?

Answer:
Instead of writing scripts, Tosca creates reusable models (Modules) of application controls. Test cases are built using these models, making maintenance easier.

5. What is XScan?

Answer:
XScan is Tosca's object identification tool. It scans application elements and creates Modules for automation.

6. What is a Module in Tosca?

Answer:
A Module contains scanned controls (buttons, text fields, dropdowns, etc.) from the application under test and is reused across multiple test cases.

7. What is a TestCase?

Answer:
A TestCase is a collection of test steps used to validate a business process or application functionality.

8. What is a TestStep?

Answer:
A TestStep is a single action performed on a control, such as entering text or clicking a button.

9. What is an ExecutionList?

Answer:
ExecutionLists organize and execute multiple test cases together. They help manage regression suites efficiently.

10. What is ScratchBook?

Answer:
ScratchBook is used for debugging and executing test cases quickly during development.

11. What is a Buffer in Tosca?

Answer:
Buffers temporarily store values during execution and allow those values to be reused later in the test.

12. What is Test Data Management (TDM)?

Answer:
TDM is Tosca's feature for creating, managing, and supplying test data for automated tests.

13. What is TQL?

Answer:
Tosca Query Language (TQL) is used to search and filter objects within the Tosca repository.

14. What is a Template in Tosca?

Answer:
A Template is a reusable blueprint used to generate multiple test case instances with different data sets.

15. What is Test Case Instantiation?

Answer:
Instantiation creates multiple test case instances from a template using different test data values.

16. What is Synchronization in Tosca?

Answer:
Synchronization ensures Tosca waits for an application event or condition before continuing execution, preventing timing issues.

17. What is the difference between Business Parameters and Buffers?

Answer:

Business Parameters: Pass data between test cases.
Buffers: Store values during execution within a test run.
18. What are the advantages of Tosca over Selenium?

Answer:

Scriptless automation
Faster test creation
Built-in reporting
Better support for multiple technologies
Lower maintenance through model-based testing
19. Can Tosca perform API testing?

Answer:
Yes. Tosca supports API/Web Service testing without requiring coding.

20. How does Tosca integrate with CI/CD?

Answer:
Tosca can integrate with tools like Jenkins and other CI/CD platforms to automate test execution during builds and deployments.

For many real interviews, expect questions on:

XScan
Modules
TestCase Design
Templates & Instantiation
Buffers
TDM
ExecutionLists
Recovery Scenarios
API Testing
CI/CD Integration

These are among the most frequently discussed Tosca topics by interviewers and practitioners.

Also, here is a video that walks through many Tosca interview questions:
