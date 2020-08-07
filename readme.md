# What this script is
This is a simple DNS Update script for [Sitelutions](http://sitelutions.com). This one is written in python and gets its settings from a config file. The code is relatively simple and does just about the minimum it can. I threw this together one evening to have a dynamic DNS updater that fit my needs.

# How to use it
Take the example config file and replace the placeholders with your details. You then place it in ~/.config/slup.conf 

If the script won't run, it's probably because you don't have requests installed. You can install it one of a few ways:
* With pip: `pip install requests`
* With easy_install: `easy_install requests`
* With your OS package manger. In Debian/Ubuntu: `apt-get install python3-requests`

The rest of the libraries are part of the standard library. Given the simplicity of the script, I didn't include setuptools or other packages to make this into a stand-alone python package.

This script would ideally be run by cron to update your DNS regularly. If you do run it in cron, you won't have automatic shell expansion or $HOME availble so you should provide the full path to the config file. 

## Cron file
For example, your cron may look like this:
```
*/5 * * * * /home/automation/bin/slup.py /home/automation/.config/slup.conf
```
