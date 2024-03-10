"""
Move Tab

Plugin for Sublime Text to move tabs around

Copyright (c) 2012 Frédéric Massart - FMCorz.net

Licensed under The MIT License
Redistributions of files must retain the above copyright notice.

http://github.com/FMCorz/MoveTab
"""

from __future__ import annotations

import sublime_plugin


class MoveTabCommand(sublime_plugin.WindowCommand):

    def run(self, position: str | int, cycle=False) -> None:
        if not (view := self.window.active_view()):
            return
        group, index = self.window.get_view_index(view)
        if index < 0:
            return
        count = len(self.window.views_in_group(group))

        if isinstance(position, str):
            if position[0] in '-+':
                position = (index + int(position))
                if cycle:
                    position %= count
            else:
                position = int(position)
        elif position < 0:
            position = count - position

        position = max(0, min(position, count - 1))

        # Avoid flashing tab when moving to same index
        if position != index:
            self.window.set_view_index(view, group, position)
            self.window.focus_view(view)

    def is_enabled(self) -> bool:
        if not (view := self.window.active_view()):
            return False
        (group, index) = self.window.get_view_index(view)
        return -1 not in (group, index) and len(self.window.views_in_group(group)) > 1
