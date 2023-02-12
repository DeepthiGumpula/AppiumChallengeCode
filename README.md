### Appium-Python-Challenge

#### This is coding challenge for interview

###  Appium ENV Setup on mac OS
Note: Make sure you have full permissions to the file system

1. Java
java -version
2. Git
git --version
3. ruby
ruby -v
4. brew
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
brew -v
5. node
brew install node
6. npm
npm -v
7. appium
npm install -g appium
appium -v
8. wd
npm install -g wd
9. pip & selenium
sudo easy_install pip
pip install -U selenium
10. update "~/.bash_profile"
Add ANDROID_HOME and JAVA_HOM
source .bash_profile
11. Install Appium Python Client
pip install appium-python-client
12. appium-doctor
npm install -g appium-doctor
appium-doctor (Check appium environment)
13. BDD
(sudo su)
pip install behave

#### How to run this script
First download image from email and save it as test.png (Note : for now its hardcoded in the script)

./run.sh

or 

behave -f allure_behave.formatter:AllureFormatter -o ./reports/report/ ./features/
allure serve ./reports/report/


