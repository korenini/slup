This is a simple DNS Update script for Sitelutions. This one is written in python and gets its settings from a config file. The code is relatively simple and does just about the minimum it can. I threw this together one evening to have a dynamic DNS updater that fit my needs.

Take the example config file and replace the placeholders with your details. You then place it in ~/.config/slup.conf 

This script would ideally be run by cron to update your DNS regularly. If you do run it in cron, you won't have automatic shell expansion or $HOME availble so you should provide the full path to the config file. For example, your cron may look like this:
```
*/5 * * * * /home/automation/bin/slup.py /home/automation/.config/slup.conf
```
