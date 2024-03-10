# Move Tab

Plugin for Sublime Text to move tabs around.

## Usage

The following commands are accessible via the command palette:

- Move Tab: To the left
- Move Tab: To the right
- Move Tab: To first position
- Move Tab: To last position

The default shortcuts are:

- Linux/Windows: <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>Page up</kbd>/<kbd>Page down</kbd>
- MacOS X: <kbd>Command</kbd><kbd>Alt</kbd><kbd>Shift</kbd><kbd>Left</kbd>/<kbd>Right</kbd>

*Shortcuts to move to first or last position
are suggested but disabled by default.*

### Commands

This package provides the `move_tab` command
which requires a parameter named `position`
and optionaly accepts a parameter `cycle`
to move the currently active tab to a new position.

- To move the tab to an absolute position,
  e.g. the first,
  specify `position` as an integer.
  The position is 0-based.
  Negative integers start counting from the end of the group,
  so a position of `-1` would be the last in the group.
- To move the tab relatively,
  specify `position` as a string
  prefixed with either `+` or `-`.
- To start cycling the position of the tab
  when reaching the end or the beginning,
  set `cycle` to `true`
  (the default is `false`, i.e. it does not cycle).


## Installation

Use the Package Control.

1. Open the Command Palette.
2. Select `Package Control: Install Package`.
3. Select `MoveTab`.

Alternatively, simply clone this repository into the Packages directory
(found via *Preferences > Browse Packages...*).

## License

Licensed under the [MIT License](http://www.opensource.org/licenses/mit-license.php)
