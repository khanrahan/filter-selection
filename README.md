# Filter Selection
Plugin for [Autodesk Flame software](http://www.autodesk.com/products/flame).

Search within a group of selected timelines to narrow down the selection.

## Compatibility
|Release Version|Flame Version|
|---|---|
|v2.X.X|Flame 2025 and up|
|v1.X.X|Flame 2021 up to 2024.2|

## Installation

### Flame 2025 and newer
To make available to all users on the workstation, copy `apply_text_timeline_fx_to_segments.py` to `/opt/Autodesk/shared/python/`

For specific users, copy `apply_text_timeline_fx_to_segments.py` to the appropriate path below...
|Platform|Path|
|---|---|
|Linux|`/home/<user_name>/flame/python/`|
|Mac|`/Users/<user_name>/Library/Preferences/Autodesk/flame/python/`|

### Flame 2021 up to 2024.2
To make available to all users on the workstation, copy `filter_selection.py` to `/opt/Autodesk/shared/python/`

For specific users, copy `filter_selection.py` to `/opt/Autodesk/user/<user name>/python/`

### Last Step
Finally, inside of Flame, go to Flame (fish) menu `->` Python `->` Rescan Python Hooks

## Menus
- Right-click selected sequences on the Desktop `->` Select... `->` Filter Selection
- Right-click selected sequences in the Media Panel `->` Select... `->` Filter Selection

## Acknowledgements
UI Templates courtesy of [pyflame.com](http://www.pyflame.com)
