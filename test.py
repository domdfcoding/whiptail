"""
Test Routine
---------------

#. Enter "Hello World" and press ``Enter``.
#. ``Tab`` to ``<OK>`` and press ``Enter``.
#. Enter "Password", ``Tab`` to ``<OK>`` and press ``Enter``.
#. Press ``Enter``.
#. Highlight ``Option 3`` and press ``Enter``.
#. Highlight ``Option 2``, ``Tab`` to ``<OK>`` and press ``Enter``.
#. Highlight ``Chips``, press ``Space``, and press ``Enter``.
#. Highlight ``Spam, spam, spam, spam``, press ``Space``,
	highlight ``Egg``, press ``Space``, then ``Tab`` to ``<OK>`` and press ``Enter``.

"""

# stdlib
import sys

# isort: off
sys.path.append("../..")
sys.path.append("..")
sys.path.append('.')

# this package
from whiptail import Whiptail
# isort: on

w = Whiptail(title="This is the title", backtitle="This is the backtitle", auto_exit=True)

prompt = w.inputbox("This is the first line. \n Newline test. Now, enter some text:")[0]
print(f"You entered: '{prompt}'!")
assert prompt == "Hello World"

prompt_default = w.inputbox("This is the first line. \n Newline test. Now, enter some text:", "-- Some Text ;)")[0]
print(f"You entered: '{prompt_default}'!")
assert prompt_default == "-- Some Text ;)"

prompt_password = w.inputbox(
		"This is the first line. \n Newline test. Now, enter a (pretend) password:",
		password=True,
		)[0]
print(f"Your password is: '{prompt_password}'!")
assert prompt_password == "Password"

msgbox = w.msgbox("This is a msgbox! \n This is a new line!")  # type: ignore[func-returns-value]
print(f"msgbox doesn't return anything, see: {msgbox}")

# view_file

menu = w.menu(
		"This is a menu. \n This is a new line in the menu",
		["Option 1", "Option 2", "Option 3", "Option 4"],
		)[0]
print(f"You selected '{menu}'")
assert menu == "Option 3"

menu_descriptions = w.menu(
		"This is a menu with descriptions. The rest of this is a very long string to test wrapping within the whiptail box. Here is more string to ensure it wraps on even the widest of monitors.",
		[("Option 1", "Does Something"), ("Option 2", "Does Something Else")],
		)[0]
print(f"You selected '{menu_descriptions}'")
assert menu_descriptions == "Option 2"

radiolist = w.radiolist(
		"This is the first line. \n Newline test. Choose One",
		["Spam, spam, spam, spam", "Egg", "Chips"],
		)[0]
print(f"You selected: '{radiolist}'!")
assert radiolist == ["Chips"]

checklist = w.checklist(
		"This is the first line. \n Newline test. Choose Multiple",
		["Spam, spam, spam, spam", "Egg", "Chips"],
		)[0]
checklist_str = "' and '".join(checklist)
print(f"You selected: '{checklist_str}'!")
print(checklist)
assert checklist == ["Spam, spam, spam, spam", "Egg"]

print("Tests passed successfully!")
