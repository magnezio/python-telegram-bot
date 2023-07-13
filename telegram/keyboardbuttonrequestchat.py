#!/usr/bin/env python
# pylint: disable=R0903
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2022
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
"""This module contains an object that represents a type of a Telegram Poll."""
from typing import Any

from telegram import TelegramObject


class KeyboardButtonRequestChat(TelegramObject):

    __slots__ = ('type', 'request_id', 'chat_is_channel', 'chat_is_forum', 'chat_has_username', 'chat_is_created',
                 'user_administrator_rights', 'bot_administrator_rights', 'bot_is_member', '_id_attrs')

    def __init__(self, request_id: int = None, chat_is_channel: bool = None, chat_is_forum: bool = None,
                 chat_has_username: bool = None, chat_is_created: bool = None,
                 user_administrator_rights = None, bot_administrator_rights = None, bot_is_member: bool = None,
                 **_kwargs: Any):  # pylint: disable=W0622
        self.request_id = request_id
        self.chat_is_channel = chat_is_channel
        self.chat_is_forum = chat_is_forum
        self.chat_has_username = chat_has_username
        self.chat_is_created = chat_is_created
        self.user_administrator_rights = user_administrator_rights
        self.bot_administrator_rights = bot_administrator_rights
        self.bot_is_member = bot_is_member
        self._id_attrs = (self.request_id, self.chat_is_channel, self.chat_is_forum, self.chat_has_username,
                          self.chat_is_created, self.user_administrator_rights, self.bot_administrator_rights,
                          self.bot_is_member)
