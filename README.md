# Filter Selection
Plugin for [Autodesk Flame software](http://www.autodesk.com/products/flame).

Search within a group of selected timelines to narrow down the selection.

## Compatibility
|Release Version|Flame Version|
|---|---|
|v2.X.X|Flame 2025 and up|
|v1.X.X|Flame 2021 up to 2024.2|

## Installation

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
