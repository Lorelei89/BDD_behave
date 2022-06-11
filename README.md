# BDD project
_BDD tests_ for https://jules.app/sign-in

📚 
**_Technologies:_** 
* **BDD** (Behaviour Driven Development):
   * _features_ folder 
   * _steps_ folder
* Behave Library
* Gherkin 
* Python & PyCharm
* **POM** (Page Object Model) in _pages_ folder

📝 
Commands in **cmd** file for **Behave** and **Selenium**
* pip install -u selenium
* pip install behave
* pip install behave-html-formatter
* pip install webdriver-manager
* _To run the BDD tests use in **Terminal**_: 
     * **behave -f html -o behave-report.html  --tags=signin** for sign_in BDD tests
     * **behave -f html -o behave-report.html  --tags=forgot_password** for forgot_password BDD tests
     * **behave -f html -o behave-report.html  --tags=forgot_password** for sign_up BDD tests

➡️
**_Gherkin syntax keywords:_**
* Feature
* Given, When, Then, And, But for steps (or *)
* Background
* Scenario 
* Scenario Outline - data in tables + Examples 

➡️
**_POM:_**
- classes, objects, methods
- OOP: Inheritance principle 

➡️
_Report BDD for **forgot_password.feature**_
![image](https://user-images.githubusercontent.com/70057309/173138871-550b4b52-51ce-4169-bf63-931b08431d40.png)

_Report BDD for **sign_up.feature**_
![image](https://user-images.githubusercontent.com/70057309/173138638-088fc8e2-6289-4649-943f-17cdc69690f0.png)

⏩
**_Steps to download the repository:_
*** Navigate to the upper level of the project;
* Click on the blue ‘Code’ button;
* Choose either ‘Open with Github Desktop’ if you have installed ‘Github Desktop’ on your computer or ‘Download ZIP’ to download as ZIP document
* Make sure you use _PyCharm_ with this repository
* Install the commands from _cmd_ file 
* Run the test with:
     * **behave -f html -o behave-report.html  --tags=signin** for sign_in BDD tests
     * **behave -f html -o behave-report.html  --tags=forgot_password** for forgot_password BDD tests
     * **behave -f html -o behave-report.html  --tags=forgot_password** for sign_up BDD tests


