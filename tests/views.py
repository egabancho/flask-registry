# -*- coding: utf-8 -*-
##
## This file is part of Flask-Registry
## Copyright (C) 2013 CERN.
##
## Flask-Registry is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Flask-Registry is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Flask-Registry; if not, write to the Free Software Foundation,
## Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
##
## In applying this licence, CERN does not waive the privileges and immunities
## granted to it by virtue of its status as an Intergovernmental Organization
## or submit itself to any jurisdiction.

"""
Test file for BlueprintAutoDiscoverRegistry testing
"""

from flask import Blueprint

blueprint = Blueprint('test', __name__)

blueprints = [
    Blueprint('test1', __name__),
    Blueprint('test2', __name__)
]


@blueprint.route("/", methods=['GET', ])
def index():
    from flask import current_app
    if current_app.config['USER_CFG'] and current_app.config['DEFAULT_CFG'] \
       and current_app.config['MOCKEXT']:
        return "Hello from Flask-Registry"
    else:
        return "Not everything loaded"
