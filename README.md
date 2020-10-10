# android-web-test
Functional, Integration and System tests to a mobile & web application of an embedded system

## Commands

### START FRONTEND
npx serve -s build

### GRAPHWALKER PATH GENERATION
java -jar /Users/user/Desktop/DevTools/graphwalker-cli-4.2.0.jar offline --start-element v_Start --model Desktop/yEd_Models/unlock.graphml "random(edge_coverage(100))" >> /Users/user/Desktop/yEd_Paths/unlock_ec100.json

### TEST A PATH
python3 Helper/test_scenario_parser.py

### MANUEL SYSTEM TEST
python3 -m pytest System_Test/system_test.py::TestMobileApp::test_open_the_door_sys -s --alluredir /Users/user/Desktop/DemoReports
python3 -m pytest System_Test/system_test.py::TestMobileApp::test_lock_the_door_sys -s --alluredir /Users/user/Desktop/DemoReports
python3 -m pytest System_Test/system_test.py::TestMobileApp::test_click_on_the_open_the_door_button_once -s --alluredir /Users/user/Desktop/DemoReports
python3 -m pytest System_Test/system_test.py::TestMobileApp::test_click_on_the_open_the_door_button_twice -s --alluredir /Users/user/Desktop/DemoReports
python3 -m pytest System_Test/system_test.py::TestMobileApp::test_click_on_the_lock_the_door_button_once -s --alluredir /Users/user/Desktop/DemoReports
python3 -m pytest System_Test/system_test.py::TestMobileApp::test_click_on_the_lock_the_door_button_twice -s --alluredir /Users/user/Desktop/DemoReports

### MANUEL EMBEDDED-WEB TEST
python3 -m pytest Integration_Test/embedded_web::TestDoorStatus::test_door_status -s --alluredir /Users/user/Desktop/DemoReports

### ALLURE REPORT GENERATION
allure generate <path>