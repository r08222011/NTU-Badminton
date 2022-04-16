# Booking NTU Badminton Courts with Python Selenium

Original author: **Yu-Tai, Lin**

---

### Prerequisites

1. [Python3](https://www.python.org)
2. Python package [selenium](https://selenium-python.readthedocs.io), can be installed with
   ```bash
   pip install selenium
   ```
   Need to be the latest version of `pip` and `selenium`, to upgrade, try
   ```bash
   pip install --upgrade pip
   pip install --upgrade selenium
   ```
3. [Chrome browser](https://www.google.com/chrome/)
4. [Homebrew](https://brew.sh). (Optional, for Mac users only.)

### Installations

For **Mac** users, you have two options, either install with `brew` or general method above.

- For **general**(non-Mac) users:
  1. Check your Chrome version. (see: [How to find which version of Google Chrome](https://www.businessinsider.com/what-version-of-google-chrome-do-i-have) or `chrome://settings/help`)
  2. Download [ChromeDriver](https://chromedriver.chromium.org/downloads) corresponds to your Chrome version.

- For **brew** users:
   1. Click the file `install.sh` and run with terminal.
   2. If it requires you to open ChromeDriver, just open it.

### Run Codes

1. Change the default values in `default.txt`
   **Warning**: You are NOT allowed to change the  order between lines or titles or delete them in `default.txt`

2. Just run with Python. 
   ```bash
   python main.py
   ```

### Notes For The Users

- You still need to fill in the verification image code by yourself at the last step.
- ChromeDriver will refresh until you are able to book the court.

### Acknowledgements

We thanks to the original author **Yu-Tai, Lin** for sharing his code to us.