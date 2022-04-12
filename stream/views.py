# -*- coding: utf-8 -*-
"""
    flaskbb.plugins.stream.views
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the stream view.

    :copyright: (c) 2014 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
from flask import Blueprint, current_app, flash, request
from flask_babelplus import gettext as _
from flask_login import current_user

from flaskbb.utils.helpers import render_template
from flaskbb.forum.models import Topic, Post, Forum
from flaskbb.user.models import User, Group
from flaskbb.plugins.models import PluginRegistry
from flaskbb.utils.helpers import time_diff, get_online_users
from flaskbb.utils.settings import flaskbb_config

stream = Blueprint("stream", __name__, template_folder="templates")


@stream.route("/")
def index():
    plugin = PluginRegistry.query.filter_by(name="stream").first()
    if plugin and not plugin.settings:
        flash(
            _(
                "Please install the plugin first to configure the forums "
                "which should be displayed."
            ),
            "warning",
        )

    stream_ip = str(plugin.settings["stream_ip"])
    stream_port = str(plugin.settings["stream_port"])
    stream_path = str(plugin.settings["hls_path"])

    if(stream_path[0] == '/'):
        stream_path = stream_path[1:]

    return render_template(
        "index.html",
        stream_ip=stream_ip,
        stream_port=stream_port,
        stream_path=stream_path
    )
