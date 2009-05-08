# -*- coding: utf-8 -*-
#
# File: api.py
#
# Copyright (c) InQuant GmbH
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

__author__ = """Hans-Peter Locher <hans-peter.locher@inquant.de>"""
__docformat__ = 'plaintext'


def add_recipient(api_url, list_id, email, columns=[]):
    """Add recipient to a list (only email key supported)
       api_url, list_id, email are required, optionally
       takes a list of dicts to define additional columns like
       [{'column_name':'State', 'column_value':'Germany'},]
       returns True or False
    """

    return True


def is_opted_in(api_url, list_id, email):
    """Is the specified email opted in to the list?
       api_url, list_id, email are required
       returns True or False
    """

    return True


def opt_out_recipient(api_url, list_id, email):
    """opt out a recipient from a list
       api_url, list_id, email are required
       returns True or False
    """

    return True


def select_recipient_data(api_url, list_id, email, columns=[]):
    """get the recipients data
       api_url, list_id, email are required
       returns a string (xml)
    """

    return '<tobedone>foo</tobedone>'


def xml_request(api_url, xml):
    """submit a custom xml request
       api_url, xml, are required
       returns a string (xml)
    """

    return '<tobedone>foo</tobedone>'

# vim: set ft=python ts=4 sw=4 expandtab :
