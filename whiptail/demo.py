# stdlib
import sys

# this package
from whiptail import Whiptail

sys.path.append("../..")
sys.path.append("..")
sys.path.append(".")

w = Whiptail(title="This is the title", backtitle="This is the backtitle")

prompt = w.prompt("Enter some text:")[0]
print(f"You entered: '{prompt}'!")

prompt_default = w.prompt("Enter some text:", "Some Text ;)")[0]
print(f"You entered: '{prompt_default}'!")

prompt_password = w.prompt("Enter a (pretend) password:", password=True)[0]
print(f"Your password is: '{prompt_password}'!")

alert = w.alert("This is an alert!")  # type: ignore
print(f"Alert doesn't return anything, see: {alert}")

# view_file

menu = w.menu("This is a menu.", ["Option 1", "Option 2", "Option 3", "Option 4"])[0]
print(f"You selected '{menu}'")

menu_descriptions = w.menu(
		"This is a menu with descriptions.", [("Option 1", "Does Something"), ("Option 2", "Does Something Else")]
		)[0]
print(f"You selected '{menu_descriptions}'")

radiolist = w.radiolist("Choose One", ["Spam, spam, spam, spam", "Egg", "Chips"])[0]
print(f"You selected: '{radiolist}'!")

checklist = w.checklist("Choose Multiple", ["Spam, spam, spam, spam", "Egg", "Chips"])[0]
checklist_str = "' and '".join(checklist)
print(f"You selected: '{checklist_str}'!")
