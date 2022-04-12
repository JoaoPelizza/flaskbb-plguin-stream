# About this project

A simple videojs player plugin for streaming puroposes, you can define setting such as server ip, port and m3u3 path.
Based on [Flaskbb-plugin-portal](https://github.com/flaskbb/flaskbb-plugin-portal) so some things might be still a straight copy instead of the correct information.

As of now there is only the player on screen, I plan on merging one of my other projects with it, a [webassembly irc web client](https://github.com/JoaoPelizza/Webassembly-irc-client) so that streaming is as simple as installing this plugin and changing the settings.


# Stream Plugin for FlaskBB

This plugin provides a simple stream for FlaskBB.

In addition to the settings that can be changed via the management panel,
one setting has to be added (if desired) to your ``flaskbb.cfg``:
```python
PLUGIN_stream_URL_PREFIX="/yourstreamurlprefix"
```
This setting allows you to change the URL of the stream from the default
value of ``/stream`` to something else. Be sure to **not** change it to something that
could conflict with one of the ``URL_PREFIX``es of FlaskBB.


# Installation
Add to pip
```bash
pip install -e .
```

This plugin can be installed from PyPI via:
```bash
$ pip install flaskbb-plugin-stream
```

# Links

* [FlaskBB Website](https://flaskbb.org)
* [WebAssembly irc web client](https://github.com/JoaoPelizza/Webassembly-irc-client)
 