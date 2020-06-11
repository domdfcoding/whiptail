#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  __init__.py
"""
Use whiptail to display dialog boxes from Python scripts
"""
#  Copyright (c) 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#  Copyright (c) 2013 Marwan Alsabbagh and contributors.
#  All rights reserved.
#  Licensed under the BSD License. See LICENSE file for details.
#
#  Docstrings based on the whiptail manpage
#  https://manpages.debian.org/buster/whiptail/whiptail.1.en.html
#  Written by
#     Savio Lam (lam836@cs.cuhk.hk) - version 0.3
#     Stuart Herbert (S.Herbert@sheffield.ac.uk) - patch for version 0.4
#     Enrique Zanardi (ezanard@debian.org)
#     Alastair McKinstry (mckinstry@debian.org)
#

__author__ = "Dominic Davis-Foster"
__copyright__ = "2020 Dominic Davis-Foster"

__license__ = "BSD"
__version__ = "0.3.1dev"
__email__ = "dominic@davis-foster.co.uk"

# stdlib
import itertools
import os
import pathlib
import shlex
import sys
from collections import namedtuple
from subprocess import PIPE, Popen
from typing import AnyStr, Iterable, List, Optional, Sequence, Tuple, Union

# 3rd party
from domdf_python_tools.terminal import get_terminal_size

# TODO:
# --default-item string
#    Set the default item in a menu box. Normally the first item in the box is the default.
# --fb, --fullbuttons
#     Use full buttons. (By default, whiptail uses compact buttons).
# --nocancel
#     The dialog box won't have a Cancel button.
# --yes-button text
#     Set the text of the Yes button.
# --no-button text
#     Set the text of the No button.
# --ok-button text
#     Set the text of the Ok button.
# --cancel-button text
#     Set the text of the Cancel button.
# --noitem
#     The menu, checklist and radiolist widgets will display tags only, not the item strings. The menu widget still needs some items specified, but checklist and radiolist expect only tag and status.
# --notags
#     Don't display tags in the menu, checklist and radiolist widgets.
# --infobox text height width
#     An info box is basically a message box. However, in this case, whiptail will exit immediately
#     after displaying the message to the user. The screen is not cleared when whiptail exits,
#     so that the message will remain on the screen until the calling shell script clears it later.
#     This is useful when you want to inform the user that some operations are carrying on that may
#     require some time to finish.
# --gauge text height width percent
#     A gauge box displays a meter along the bottom of the box. The meter indicates a percentage.
#     New percentages are read from standard input, one integer per line. The meter is updated to
#     reflect each new percentage. If stdin is XXX, the first following line is a percentage and
#     subsequent lines up to another XXX are used for a new prompt. The gauge exits when EOF is
#     reached on stdin.


class Response(namedtuple('__BaseResponse', 'returncode value')):
	"""
	Namedtuple to store the returncode and value returned by a whiptail dialog.

	:param returncode: The returncode
	:param value: The value returned from the dialog. Values are as follows:

		* ``0``: The ``Yes`` or ``OK`` button was pressed.
		* ``1``: The ``No`` or ``Cancel`` button was pressed.
		* ``255``: The user pressed the ``ESC`` key, or an error occurred.
	"""

	returncode: int
	value: str

	def __new__(cls, returncode: int, value: AnyStr):
		if isinstance(value, bytes):
			val = value.decode("UTF-8")
		else:
			val = value
		return super().__new__(cls, returncode, val)


def flatten(data):
	return list(itertools.chain.from_iterable(data))


class Whiptail:
	"""
	Display dialog boxes in the terminal from Python scripts.

	:param title: The text to show at the top of the dialog.
	:type title: str
	:param backtitle: The text to show on the top left of the background.
	:type backtitle: str
	:param height: The height of the dialog. Default is 2-5 characters shorter than the terminal window
	:param width: The height of the dialog. Default is approx. 10 characters narrower than the terminal window
	:param auto_exit: Whether to call :func:`sys.exit` if the user selects cancel in a dialog. Default :py:obj:`False`
	:type auto_exit: bool
	"""

	def __init__(
			self,
			title: str = '',
			backtitle: str = '',
			height: Optional[int] = None,
			width: Optional[int] = None,
			auto_exit: bool = False,
			):

		self.title: str = str(title)
		self.backtitle: str = str(backtitle)
		self.height: Optional[int] = height
		self.width: Optional[int] = width
		self.auto_exit: bool = auto_exit

	def run(
			self,
			control: str,
			msg: str,
			extra_args: Sequence[str] = (),
			extra_values: Sequence[str] = (),
			exit_on: Sequence[int] = (1, 255)
			) -> Response:
		"""

		:param control: The name of the control to run. One of ``"yesno"``, ``"msgbox"``, ``"infobox"``,
			``"inputbox"``, ``"passwordbox"``, ``"textbox"``, ``"menu"``, ``"checklist"``,
			``"radiolist"`` or ``"gauge"``
		:type control: str
		:param msg: The message to display in the dialog box
		:type msg: str
		:param extra_args: A sequence of extra arguments to pass to the control
		:param extra_values: A sequence of extra values to pass to the control
		:param exit_on: A sequence of return codes that will cause program execution to stop if
			:attr:`Whiptail.auto_exit` is :py:obj:`True`

		:return: The response returned by whiptail
		"""

		width = self.width
		height = self.height

		if self.height is None or self.width is None:
			w, h = get_terminal_size()

			if self.width is None:
				width = w - 10
				width = width - (width % 10)

			if self.height is None:
				height = h - 2
				height = height - (height % 5)

		cmd = [
				'whiptail',
				'--title',
				self.title,
				'--backtitle',
				self.backtitle,
				*list(extra_args),
				f'--{control}',
				"--",
				str(msg),
				str(height),
				str(width),
				*list(extra_values),
				]

		p = Popen(cmd, stderr=PIPE)
		out, err = p.communicate()

		if self.auto_exit and p.returncode in exit_on:
			print('User cancelled operation.')
			sys.exit(p.returncode)

		return Response(p.returncode, err)

	def inputbox(self, msg: str, default: str = '', password: bool = False) -> Tuple[str, int]:
		"""
		An input box is useful when you want to ask questions that require the user to input a string as the answer.
		If ``default`` is supplied it is used to initialize the input string.
		When inputting the string, the ``BACKSPACE`` key can be used to correct typing errors. If the input string
		is longer than the width of the dialog box, the input field will be scrolled.

		If ``password`` is :py:obj:`True`, the text the user enters is not displayed.
		This is useful when prompting for passwords or other sensitive information.
		Be aware that if anything is passed in "init", it will be visible in the system's
		process table to casual snoopers. Also, it is very confusing to the user to provide
		them with a default password they cannot see. For these reasons, using "init" is highly discouraged.

		:param msg: The message to display in the dialog box
		:type msg: str, optional
		:param default: A default value for the text
		:type default: str, optional
		:param password: Whether the text being entered is a password, and should be replaced by ``*``. Default :py:obj:`False`
		:type password: bool, optional

		:return: The value entered by the user, and the return code
		"""

		control = 'passwordbox' if password else 'inputbox'
		returncode, val = self.run(control, msg, extra_values=[default])
		return val, returncode

	def yesno(self, msg: str, default='yes') -> bool:
		"""
		A yes/no dialog box will be displayed.
		The string specified by ``msg`` is displayed inside the dialog box.
		If this string is too long to be fit in one line, it will be automatically
		divided into multiple lines at appropriate places.
		The text string may also contain the newline character ``\n`` to control line breaking explicitly.

		This dialog box is useful for asking questions that require the user to answer either yes or no.
		The dialog box has a ``Yes`` button and a ``No`` button, in which the user can switch between
		by pressing the ``TAB`` key.

		:param msg: The message to display in the dialog box
		:type msg: str

		:param default: The default button to select, either ``"yes"`` or ``"no"``. Default ``"yes"``
		:type default: str, optional.

		:return: :py:obj:`True` if the user selected ``yes``. :py:obj:`False` otherwise.
		:rtype: bool
		"""

		if default.lower() == "no":
			defaultno = '--defaultno'
		else:
			defaultno = ''

		return bool(self.run('yesno', msg, extra_args=[defaultno], exit_on=[255]).returncode)

	def msgbox(self, msg: str) -> None:
		"""
		A message box is very similar to a yes/no box. The only difference between a message box
		and a yes/no box is that a message box has only a single ``OK`` button.

		You can use this dialog box to display any message you like.
		After reading the message, the user can press the ENTER key so that whiptail will exit
		and the calling script can continue its operation.

		:param msg: The message to display in the dialog box
		:type msg: str
		"""

		self.run('msgbox', msg)

	def textbox(self, path: Union[str, pathlib.Path, os.PathLike]) -> int:
		"""
		A text box lets you display the contents of a text file in a dialog box.
		It is like a simple text file viewer. The user can move through the file by using
		the ``UP``/``DOWN``, ``PGUP``/``PGDN`` and ``HOME``/``END`` keys available on most keyboards.
		If the lines are too long to be displayed in the box, the ``LEFT``/``RIGHT`` keys can be used
		to scroll the text region horizontally. For more convenience, forward and backward searching
		functions are also provided.

		:param path: The file to display the contents of

		:return: The return code
		:rtype: int
		"""

		if not isinstance(path, pathlib.Path):
			path = pathlib.Path(path)

		return self.run('textbox', str(path), extra_args=['--scrolltext']).returncode

	def calc_height(self, msg: str) -> List[str]:
		"""

		:param msg: The message to display in the dialog box
		:type msg: str

		:return:
		:rtype:
		"""

		height_offset = 8 if msg else 7

		if self.height is None:
			width, height = get_terminal_size()
			height = height - 2
			height = height - (height % 5)
		else:
			height = self.height

		return [str(height - height_offset)]

	def menu(
			self,
			msg: str = '',
			items: Union[Sequence[str], Sequence[Iterable[str]]] = (),
			prefix: str = ' - ',
			) -> Tuple[str, int]:
		"""
		As its name suggests, a menu box is a dialog box that can be used to present a
		list of choices in the form of a menu for the user to choose.

		Each menu entry consists of a tag string and an item string.
		The tag gives the entry a name to distinguish it from the other entries in the menu.
		The item is a short description of the option that the entry represents.
		The user can move between the menu entries by pressing the ``UP``/``DOWN`` keys,
		the first letter of the tag as a hot-key. There are menu-height entries displayed
		in the menu at one time, but the menu will be scrolled if there are more entries than that.

		:param msg: The message to display in the dialog box
		:type msg: str, optional
		:param items: A sequence of items to display in the menu
		:param prefix:
		:type prefix:  str

		:return: The tag of the selected menu item, and the return code
		"""

		if isinstance(items[0], str):
			parsed_items = [(i, '') for i in items]
		else:
			parsed_items = [(k, prefix + v) for k, v in items]

		extra = self.calc_height(msg) + flatten(parsed_items)
		returncode, val = self.run('menu', msg, extra_values=extra)
		return val, returncode

	def showlist(
			self,
			control,
			msg: str,
			items: Union[Sequence[str], Sequence[Iterable[str]]],
			prefix: str,
			) -> Tuple[List[str], int]:
		"""
		Helper function to display radio- and check-lists.

		:param control: The name of the control to run. Either ``"checklist"`` or ``"radiolist"``
		:type control: str
		:param msg: The message to display in the dialog box
		:type msg: str
		:param items: A sequence of items to display in the list
		:param prefix:
		:type prefix:  str

		:return: A list of the tags strings that were selected, and the return code
		"""

		if isinstance(items[0], str):
			parsed_items = [(i, '', 'OFF') for i in items]
		else:
			parsed_items = [(k, prefix + v, s) for k, v, s in items]

		extra = self.calc_height(msg) + flatten(parsed_items)
		returncode, val = self.run(control, msg, extra_values=extra)
		return shlex.split(val), returncode

	def radiolist(
			self,
			msg: str = '',
			items: Union[Sequence[str], Sequence[Iterable[str]]] = (),
			prefix: str = ' - '
			) -> Tuple[List[str], int]:
		"""
		A radiolist box is similar to a menu box.
		The only difference is that you can indicate which entry is currently selected,
		by setting its status to on.

		:param msg: The message to display in the dialog box
		:type msg: str, optional
		:param items: A sequence of items to display in the radiolist
		:param prefix:
		:type prefix:  str

		:return: A list of the tags strings that were selected, and the return code
		"""

		return self.showlist('radiolist', msg, items, prefix)

	def checklist(
			self,
			msg: str = '',
			items: Union[Sequence[str], Sequence[Iterable[str]]] = (),
			prefix: str = ' - '
			) -> Tuple[List[str], int]:
		"""
		checklist box is similar to a menu box in that there are multiple entries presented in the form of a menu.
		You can select and deselect items using the SPACE key.
		The initial on/off state of each entry is specified by status.

		:param msg: The message to display in the dialog box
		:type msg: str, optional
		:param items: A sequence of items to display in the checklist
		:param prefix:
		:type prefix:  str

		:return: A list of the tag strings of those entries that are turned on, and the return code
		"""

		return self.showlist('checklist', msg, items, prefix)
