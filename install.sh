brew uninstall chromedriver
brew install --cask chromedriver
chromedriver=$(which chromedriver)
echo $chromedriver
spctl --add $chromedriver
open $chromedriver