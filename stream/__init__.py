# -*- coding: utf-8 -*-
"""
    flaskbb.plugins.stream
    ~~~~~~~~~~~~~~~~~~~~~~

    A stream Plugin for FlaskBB.

    :copyright: (c) 2014 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
import os

from pluggy import HookimplMarker
from flask_babelplus import gettext as _

from flaskbb.display.navigation import NavigationLink
from flaskbb.forum.models import Forum
from flaskbb.utils.forms import SettingValueType

from .views import stream

__version__ = "1.2.0"


hookimpl = HookimplMarker("flaskbb")


def available_forums():
    forums = Forum.query.order_by(Forum.id.asc()).all()
    return [(forum.id, forum.title) for forum in forums]


@hookimpl
def flaskbb_load_migrations():
    return os.path.join(os.path.dirname(__file__), "migrations")


@hookimpl
def flaskbb_load_translations():
    return os.path.join(os.path.dirname(__file__), "translations")


@hookimpl
def flaskbb_load_blueprints(app):
    app.register_blueprint(
        stream, url_prefix=app.config.get("PLUGIN_stream_URL_PREFIX", "/stream")
    )


@hookimpl
def flaskbb_tpl_navigation_before():
    return NavigationLink(
        endpoint="stream.index",
        name=_("Stream"),
        icon="fas fa-broadcast-tower",
    )


SETTINGS = {
    "stream_ip": {
        "value": "127.0.0.1",
        "value_type": SettingValueType.string,
        "name": "Strean IP",
        "description": (
            "IP of HLS server"
        ),
        "extra": {},
    },
    "stream_port": {
        "value": "8080",
        "value_type": SettingValueType.integer,
        "name": "Stream PORT",
        "description": (
            "PORT of HLS server"
        ),
        "extra": {"min": 1, "max": 65535},
    },
    "hls_path": {
        "value": "/hls/test.m3u3",
        "value_type": SettingValueType.string,
        "name": ".m3u3 path",
        "description": (
            "Path to .m3u3 file"
        ),
        "extra": {},
    },
}
