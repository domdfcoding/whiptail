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

prompt = w.inputbox("Input box messages can take multiple lines of text.\nNow, enter some text:")[0]
print(f"You entered: '{prompt}'!")
assert prompt == "Hello World"

prompt_default = w.inputbox("Now, enter some text:", "-- Some Text ;)")[0]
print(f"You entered: '{prompt_default}'!")
assert prompt_default == "-- Some Text ;)"

prompt_password = w.inputbox(
		"This input box is to show an example of text wrapping. This is additional text to ensure that we are actually testing the wrapping. And more wrapping. Is this enough wrapping? Surprise! New line:\nNow, enter a (pretend) password:",
		password=True
		)[0]
print(f"Your password is: '{prompt_password}'!")
assert prompt_password == "Password"

msgbox = w.msgbox(
		"This is an msgbox, which originally had issues with newlines and wrapping. As a result, here are 4 new lines before the prompt.\n\n\n\nNow, just hit enter!"
		)  # type: ignore[func-returns-value]
print(f"msgbox doesn't return anything, see: {msgbox}")

# view_file

menu = w.menu(
		"This is a menu testing multple new lines.\n\n\n\nChoose option 3.",
		["Option 1", "Option 2", "Option 3", "Option 4"]
		)[0]
print(f"You selected '{menu}'")
assert menu == "Option 3"

menu_descriptions = w.menu(
		"This is a menu with description, which also faced issues. So here is more copy to ensure it wraps on all sorts of monitors.Let's hope that's enoiugh. After a new line, lets try centering text.\n\n\n                              Centered text. Choose option 2.",
		[("Option 1", "Does Something"), ("Option 2", "Does Something Else")]
		)[0]
print(f"You selected '{menu_descriptions}'")
assert menu_descriptions == "Option 2"

radiolist = w.radiolist("Choose One", ["Spam, spam, spam, spam", "Egg", "Chips"])[0]
print(f"You selected: '{radiolist}'!")
assert radiolist == ["Chips"]

checklist = w.checklist("Choose Multiple", ["Spam, spam, spam, spam", "Egg", "Chips"])[0]
checklist_str = "' and '".join(checklist)
print(f"You selected: '{checklist_str}'!")
print(checklist)
assert checklist == ["Spam, spam, spam, spam", "Egg"]

print("Tests passed successfully!")
