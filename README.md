# ig_follower_refactor

ig_follower is the python-based application that helps to track the Instagram account you like and 
discover and follow automatically all its followers. This use case is specially applicable for marketing 
specialties who require to run marketing campaign using Instagram and increase the number of followers 
for their client IG account in an automated fashion.


## Preview

![preview](https://user-images.githubusercontent.com/74083216/171606565-b5b630bc-8a2f-49ba-8605-45bfc85a69ff.png)

## Quick-start

You can run ig_follower on your local Windows/Mac/Linux environmemt with Python3+ installed. 

We can categorize the use scenarios of ig_follower into 2 cases. 
1.	Normal Flow 
2.	UnitTest Flow (Whitebox testing)

### Normal Flow 

a. This repo has contained the ver99 of Chrome driver for Windows, so Windows user can directly 
use it or find out more details of other versions from https://chromedriver.chromium.org/downloads)

b. If you're using other OSes like Mac/Linux, please download the latest version for your OS 
from https://chromedriver.chromium.org/downloads)

c. All the global parameters for running ig_follower are stored in **config.ini**, such as your *IG 
account name* and *password* and also  *target_account*, from which is for IG account you want to discover 
its followers by ig_follower. Please modify them according to your needs before running ig-follower. 

d. In your OS command prompt, enter 
```
$ python src\run_ig_follower.py
```

e. The selenium process will be run to invoke the Chrome browser windows and then start the automation process of 
digging out and following the followers from the target account.

d. Since IG website often updates its HTML structure, ig_follower reserves users the ability of adjusting the XPath 
of the key HTML elements that selenium is accessing for the IG following process. You can modify the arguments, 
such as *follower_xpath* or *ig_login_path* …etc. in the sector of IGARGUMENTS in **config.ini** 

### UnitTest/Pytest Flow
a.	In your OS command prompt, enter 
```
$ pytest tests\test_ig_follower.py
```

b.	Python UnitTest to verify each methods of InstaFollower class will be run to report PASS/FAILED results. 

Notes: 

- In some situations, to make pytest work, you will need to create a new Variable called 
**PYTHONPATH** in your OS, for example in Windows:
```
set PYTHONPATH=src
```

- The current version of **tests\test_ig_follower.py** is only worked in the local. For Github CI workflow, we suggests 
users to use **tests\test_ci.py**. Please refer to the details of **.github\workflows\python-app.yml**

## Python Dependencies

Please refer to requirements.txt and install all the required packages by 
```
$ pip install -r requirements.txt
```

## License

Distributed under the Apache License. See LICENSE.txt for more information.

## Contact

Kana Kunikata

## Acknowledgments

Angela's 100 Days of Code: The Complete Python Pro Bootcamp for 2022 in Udemy
