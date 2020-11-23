# stdlib
import sys

# isort: off
sys.path.append("../..")
sys.path.append("..")
sys.path.append('.')

# this package
from whiptail import Whiptail
# isort: on

w = Whiptail(title="This is the title", backtitle="This is the backtitle")

prompt = w.inputbox("Enter some text:")[0]
print(f"You entered: '{prompt}'!")

prompt_default = w.inputbox("Enter some text:", "Some Text ;)")[0]
print(f"You entered: '{prompt_default}'!")

prompt_password = w.inputbox("Enter a (pretend) password:", password=True)[0]
print(f"Your password is: '{prompt_password}'!")

msgbox = w.msgbox("This is an msgbox!")  # type: ignore
print(f"msgbox doesn't return anything, see: {msgbox}")

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

textbox = w.textbox(__file__)  # type: ignore
print(textbox)
