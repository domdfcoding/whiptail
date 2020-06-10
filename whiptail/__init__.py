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

__author__ = "Dominic Davis-Foster"
__copyright__ = "2020 Dominic Davis-Foster"

__license__ = "GNU Lesser General Public License v3 or later (LGPLv3+)"
__version__ = "0.3.0dev"
__email__ = "dominic@davis-foster.co.uk"

# stdlib
import itertools
import shlex
import sys
from collections import namedtuple
from subprocess import PIPE, Popen
from typing import AnyStr, List, Optional, Sequence, Tuple

# 3rd party
from domdf_python_tools.terminal import get_terminal_size


class Response(namedtuple('__BaseResponse', 'returncode value')):
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
	:param title: The text to show at the top of the dialog.
	:type title: str
	:param backtitle: The text to show on the top left of the background.
	:type backtitle: str
	:param height: The height of the dialog. Default is 2-5 characters shorter than the terminal window
	:param width: The height of the dialog. Default is approx. 10 characters narrower than the terminal window
	:param auto_exit: Whether to call :func:`sys.exit` if the user selects cancel in a dialog. Default ``False``
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

	def run(self, control, msg: str, extra=(), exit_on: Sequence[int] = (1, 255)) -> Response:
		"""

		:param control:
		:type control:
		:param msg:
		:type msg: str
		:param extra:
		:type extra:
		:param exit_on:

		:return:
		:rtype:
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
				f'--{control}',
				str(msg),
				str(height),
				str(width),
				*list(extra),
				]

		p = Popen(cmd, stderr=PIPE)
		out, err = p.communicate()

		if self.auto_exit and p.returncode in exit_on:
			print('User cancelled operation.')
			sys.exit(p.returncode)

		return Response(p.returncode, err)

	def prompt(self, msg: str, default: str = '', password: bool = False) -> Tuple[str, int]:
		"""

		:param msg:
		:type msg: str, optional
		:param default: A default value for the text
		:type default: str, optional
		:param password: Whether the text being entered is a password, and should be replaced by ``*``. Default ``False``
		:type password: bool, optional

		:return:
		:rtype:
		"""
		control = 'passwordbox' if password else 'inputbox'
		returncode, val = self.run(control, msg, [default])
		return val, returncode

	def confirm(self, msg: str, default='yes') -> int:
		"""

		:param msg:
		:type msg: str

		:param default:
		:type default:

		:return:
		:rtype:
		"""

		if default == "no":
			defaultno = '--defaultno'
		else:
			defaultno = ''

		return self.run('yesno', msg, [defaultno], [255]).returncode

	def alert(self, msg: str) -> None:
		"""

		:param msg:
		:type msg: str

		:return:
		:rtype:
		"""

		self.run('msgbox', msg)

	def view_file(self, path):
		"""

		:param path:
		:type path:

		:return:
		:rtype:
		"""

		returncode, val = self.run('textbox', path, ['--scrolltext'])
		return val, returncode

	def calc_height(self, msg: str) -> List[str]:
		"""

		:param msg:
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

	def menu(self, msg: str = '', items: Sequence = (), prefix: str = ' - ') -> Tuple[str, int]:
		"""

		:param msg:
		:type msg: str, optional
		:param items:
		:param prefix:
		:type prefix:  str

		:return:
		:rtype:
		"""

		if isinstance(items[0], str):
			items = [(i, '') for i in items]
		else:
			items = [(k, prefix + v) for k, v in items]

		extra = self.calc_height(msg) + flatten(items)
		returncode, val = self.run('menu', msg, extra)
		return val, returncode

	def showlist(self, control, msg: str, items: Sequence, prefix: str) -> Tuple[List[str], int]:
		"""

		:param control:
		:type control:
		:param msg:
		:type msg: str
		:param items:
		:param prefix:
		:type prefix:  str

		:return:
		:rtype:
		"""

		if isinstance(items[0], str):
			items = [(i, '', 'OFF') for i in items]
		else:
			items = [(k, prefix + v, s) for k, v, s in items]

		extra = self.calc_height(msg) + flatten(items)
		returncode, val = self.run(control, msg, extra)
		return shlex.split(val), returncode

	def radiolist(self, msg: str = '', items: Sequence = (), prefix: str = ' - ') -> Tuple[List[str], int]:
		"""

		:param msg:
		:type msg: str, optional
		:param items:
		:param prefix:
		:type prefix:  str

		:return:
		:rtype:
		"""

		return self.showlist('radiolist', msg, items, prefix)

	def checklist(self, msg: str = '', items: Sequence = (), prefix: str = ' - ') -> Tuple[List[str], int]:
		"""

		:param msg:
		:type msg: str, optional
		:param items:
		:param prefix:
		:type prefix:  str

		:return:
		:rtype:
		"""

		return self.showlist('checklist', msg, items, prefix)
