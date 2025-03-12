"""
Script Name: Filter Selection
Written by: Kieran Hanrahan

Script Version: 1.0.0
Flame Version: 2022

URL: http://www.github.com/khanrahan/filter-selection

Creation Date: 03.07.25
Update Date: 04.07.25

Description:

    Filter the current selection in the Media Panel.

Menus:

    Right-click selected items on the Desktop -> Select... -> Filter Selection
    Right-click selected items in the Media Hub -> Select... -> Filter Selection
    Right-click selected items in the Media Panel -> Select... -> Filter Selection

To Install:

    For all users, copy this file to:
    /opt/Autodesk/shared/python

    For a specific user, copy this file to:
    /opt/Autodesk/user/<user name>/python
"""

from typing import Optional

import flame
from PySide2 import QtCore, QtWidgets

TITLE = 'Filter Selection'
VERSION_INFO = (1, 0, 0)
VERSION = '.'.join([str(num) for num in VERSION_INFO])
TITLE_VERSION = f'{TITLE} v{VERSION}'
MESSAGE_PREFIX = '[PYTHON]'


class FlameButton(QtWidgets.QPushButton):
    """
    Custom Qt Flame Button Widget v2.1

    button_name: button text [str]
    connect: execute when clicked [function]
    button_color: (optional) normal, blue [str]
    button_width: (optional) default is 150 [int]
    button_max_width: (optional) default is 150 [int]

    Usage:

        button = FlameButton(
            'Button Name', do_something__when_pressed, button_color='blue')
    """

    def __init__(self, button_name, connect, button_color='normal', button_width=150,
                 button_max_width=150):
        super().__init__()

        self.setText(button_name)
        self.setMinimumSize(QtCore.QSize(button_width, 28))
        self.setMaximumSize(QtCore.QSize(button_max_width, 28))
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clicked.connect(connect)
        if button_color == 'normal':
            self.setStyleSheet("""
                QPushButton {
                    color: rgb(154, 154, 154);
                    background-color: rgb(58, 58, 58);
                    border: none;
                    font: 14px "Discreet"}
                QPushButton:hover {
                    border: 1px solid rgb(90, 90, 90)}
                QPushButton:pressed {
                    color: rgb(159, 159, 159);
                    background-color: rgb(66, 66, 66);
                    border: 1px solid rgb(90, 90, 90)}
                QPushButton:disabled {
                    color: rgb(116, 116, 116);
                    background-color: rgb(58, 58, 58);
                    border: none}
                QToolTip {
                    color: rgb(170, 170, 170);
                    background-color: rgb(71, 71, 71);
                    border: 10px solid rgb(71, 71, 71)}""")
        elif button_color == 'blue':
            self.setStyleSheet("""
                QPushButton {
                    color: rgb(190, 190, 190);
                    background-color: rgb(0, 110, 175);
                    border: none;
                    font: 12px "Discreet"}
                QPushButton:hover {
                    border: 1px solid rgb(90, 90, 90)}
                QPushButton:pressed {
                    color: rgb(159, 159, 159);
                    border: 1px solid rgb(90, 90, 90)
                QPushButton:disabled {
                    color: rgb(116, 116, 116);
                    background-color: rgb(58, 58, 58);
                    border: none}
                QToolTip {
                    color: rgb(170, 170, 170);
                    background-color: rgb(71, 71, 71);
                    border: 10px solid rgb(71, 71, 71)}""")


class FlameLabel(QtWidgets.QLabel):
    """
    Custom Qt Flame Label Widget v2.1

    label_name:  text displayed [str]
    label_type:  (optional) select from different styles:
                 normal, underline, background. default is normal [str]
    label_width: (optional) default is 150 [int]

    Usage:

        label = FlameLabel('Label Name', 'normal', 300)
    """

    def __init__(self, label_name, label_type='normal', label_width=150):
        super().__init__()

        self.setText(label_name)
        self.setMinimumSize(label_width, 28)
        self.setMaximumHeight(28)
        self.setFocusPolicy(QtCore.Qt.NoFocus)

        # Set label stylesheet based on label_type

        if label_type == 'normal':
            self.setStyleSheet("""
                QLabel {
                    color: rgb(154, 154, 154);
                    font: 14px "Discreet"}
                QLabel:disabled {
                    color: rgb(106, 106, 106)}""")
        elif label_type == 'underline':
            self.setAlignment(QtCore.Qt.AlignCenter)
            self.setStyleSheet("""
                QLabel {
                    color: rgb(154, 154, 154);
                    border-bottom: 1px inset rgb(40, 40, 40);
                    font: 14px "Discreet"}
                QLabel:disabled {
                    color: rgb(106, 106, 106)}""")
        elif label_type == 'background':
            self.setStyleSheet("""
                QLabel {
                    color: rgb(154, 154, 154);
                    background-color: rgb(30, 30, 30);
                    padding-left: 5px;
                    font: 14px "Discreet"}
                QLabel:disabled {
                    color: rgb(106, 106, 106)}""")


class FlameLineEdit(QtWidgets.QLineEdit):
    """
    Custom Qt Flame Line Edit Widget v2.1

    Main window should include this: window.setFocusPolicy(QtCore.Qt.StrongFocus)

    text: text show [str]
    width: (optional) width of widget. default is 150. [int]
    max_width: (optional) maximum width of widget. default is 2000. [int]

    Usage:

        line_edit = FlameLineEdit('Some text here')
    """

    def __init__(self, text, width=150, max_width=2000):
        super().__init__()

        self.setText(text)
        self.setMinimumHeight(28)
        self.setMinimumWidth(width)
        self.setMaximumWidth(max_width)
        self.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.setStyleSheet("""
            QLineEdit {
                color: rgb(154, 154, 154);
                background-color: rgb(55, 65, 75);
                selection-color: rgb(38, 38, 38);
                selection-background-color: rgb(184, 177, 167);
                border: 1px solid rgb(55, 65, 75);
                padding-left: 5px;
                font: 14px "Discreet"}
            QLineEdit:focus {background-color: rgb(73, 86, 99)}
            QLineEdit:hover {border: 1px solid rgb(90, 90, 90)}
            QLineEdit:disabled {
                color: rgb(106, 106, 106);
                background-color: rgb(55, 55, 55);
                border: 1px solid rgb(55, 55, 55)}
            QToolTip {
                color: rgb(170, 170, 170);
                background-color: rgb(71, 71, 71);
                border: none}""")


class FlameListWidget(QtWidgets.QListWidget):
    """
    Custom Qt Flame List Widget

    FlameListWidget([min_width=200, max_width=2000, min_height=250, max_height=2000])

    Example:
        list_widget = FlameListWidget()
    """

    def __init__(
            self, min_width: Optional[int] = 200, max_width: Optional[int] = 2000,
            min_height: Optional[int] = 250, max_height: Optional[int] = 2000):
        super().__init__()

        # Check argument types

        if not isinstance(min_width, int):
            raise TypeError('FlameListWidget: min_width must be integer.')
        if not isinstance(max_width, int):
            raise TypeError('FlameListWidget: max_width must be integer.')
        if not isinstance(min_height, int):
            raise TypeError('FlameListWidget: min_height must be integer.')
        if not isinstance(max_height, int):
            raise TypeError('FlameListWidget: max_height must be integer.')

        # Build list widget

        self.setMinimumWidth(min_width)
        self.setMaximumWidth(max_width)
        self.setMinimumHeight(min_height)
        self.setMaximumHeight(max_height)
        self.spacing()
        self.setUniformItemSizes(True)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.setAlternatingRowColors(True)
        self.setStyleSheet("""
            QListWidget {
                color: rgb(154, 154, 154);
                background-color: rgb(30, 30, 30);
                alternate-background-color: rgb(36, 36, 36);
                outline: 3px rgb(0, 0, 0);
                font: 14px "Discreet"}
            QListWidget::item:selected {
                color: rgb(217, 217, 217);
                background-color: rgb(102, 102, 102);
                border: 1px solid rgb(102, 102, 102)}
            QScrollBar {
                background: rgb(61, 61, 61)}
            QScrollBar::handle {
                background: rgb(31, 31, 31)}
            QScrollBar::add-line:vertical {
                border: none;
                background: none;
                width: 0px;
                height: 0px}
            QScrollBar::sub-line:vertical {
                border: none;
                background: none;
                width: 0px;
                height: 0px}
            QScrollBar {
                background: rgb(61, 61, 61)}
            QScrollBar::handle {
                background: rgb(31, 31, 31)}
            QScrollBar::add-line:horizontal {
                border: none;
                background: none;
                width: 0px;
                height: 0px}
            QScrollBar::sub-line:horizontal {
                border: none;
                background: none;
                width: 0px;
                height: 0px}
            QToolTip {
                color: rgb(170, 170, 170);
                background-color: rgb(71, 71, 71);
                border: 10px solid rgb(71, 71, 71)}""")


class FlamePushButton(QtWidgets.QPushButton):
    """Custom Qt Flame Push Button Widget v2.1

    button_name: text displayed on button [str]
    button_checked: True or False [bool]
    connect: execute when button is pressed [function]
    button_width: (optional) default is 150. [int]

    Usage:
        pushbutton = FlamePushButton('Button Name', False)
    """
    def __init__(self, button_name, button_checked, connect=None, button_width=150):
        super().__init__()

        self.setText(button_name)
        self.setCheckable(True)
        self.setChecked(button_checked)
        self.setMinimumSize(button_width, 28)
        self.setMaximumSize(button_width, 28)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clicked.connect(connect)
        self.setStyleSheet("""
            QPushButton {
                color: rgb(154, 154, 154);
                background-color: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 0,
                    stop: .93 rgb(58, 58, 58),
                    stop: .94 rgb(44, 54, 68));
                text-align: left;
                border-top: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 0,
                    stop: .93 rgb(58, 58, 58),
                    stop: .94 rgb(44, 54, 68));
                border-bottom: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 0,
                    stop: .93 rgb(58, 58, 58),
                    stop: .94 rgb(44, 54, 68));
                border-left: 1px solid rgb(58, 58, 58);
                border-right: 1px solid rgb(44, 54, 68);
                padding-left: 5px; font: 14px 'Discreet'}
            QPushButton:checked {
                color: rgb(217, 217, 217);
                background-color: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 0,
                    stop: .93 rgb(71, 71, 71),
                    stop: .94 rgb(50, 101, 173));
                text-align: left;
                border-top: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 0,
                    stop: .93 rgb(71, 71, 71),
                    stop: .94 rgb(50, 101, 173));
                border-bottom: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 0,
                    stop: .93 rgb(71, 71, 71),
                    stop: .94 rgb(50, 101, 173));
                border-left: 1px solid rgb(71, 71, 71);
                border-right: 1px solid rgb(50, 101, 173);
                padding-left: 5px;
                font: italic}
            QPushButton:hover {
                border: 1px solid rgb(90, 90, 90)}
            QPushButton:disabled {
                color: #6a6a6a;
                background-color: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 0,
                    stop: .93 rgb(58, 58, 58),
                    stop: .94 rgb(50, 50, 50));
                font: light;
                border: none}
            QToolTip {
                color: rgb(170, 170, 170);
                background-color: rgb(71, 71, 71);
                border: 10px solid rgb(71, 71, 71)}""")


class FilterSelection:
    """Take the selection and filter it, to create a smaller more specific selection."""

    def __init__(self, selection):
        """Create instance."""
        self.message(TITLE_VERSION)
        self.message(f'Script called from {__file__}')

        self.selection = selection
        self.selection_list = None

        self.main_window()

    @staticmethod
    def message(string):
        """Print message to shell window and append global MESSAGE_PREFIX."""
        print(' '.join([MESSAGE_PREFIX, string]))

    def get_names(self):
        """Get the object names of everything that is selected."""
        return [item.name.get_value() for item in self.selection]

    def process_selection(self):
        """Update the selection in Flame."""
        for item in self.selection:
            if item.name.get_value() not in self.selection_list:
                item.selected = False

    def main_window(self):
        """Enter search terms, view results, then confirm the selection."""

        def okay_button():
            """Close window and process the artist's selected subdirectory."""
            self.window.close()
            self.process_selection()
            self.message('Done!')

        def cancel_button():
            """Do when cancel button is pressed."""
            self.window.close()
            self.message('Cancelled!')

        def filter_list():
            """Updates the results list when anything is typed in the Find bar."""
            for num in range(self.list_scroll.count()):
                if self.find.text() in self.list_scroll.item(num).text():
                    self.list_scroll.item(num).setHidden(False)
                else:
                    self.list_scroll.item(num).setHidden(True)

        def invert_selection(self):
            """Self explanitory."""
            for num in range(self.list_scroll.count()):
                if self.list_scroll.item(num).isSelected():
                    self.list_scoll.item(num).setSelected(False)
                else:
                    self.list_scroll.item(num).setSelected(True)

        def update_selection_list():
            """Pass selection in the PySide window back to a class attribute."""
            self.selection_list = [self.list_scroll.item(num).text() for num in
                    range(self.list_scroll.count()) if
                        not self.list_scroll.item(num).isHidden()]

        def find_updated():
            """Execute when the Find field is updated."""
            filter_list()
            update_selection_list()

        self.window = QtWidgets.QWidget()

        self.window.setMinimumSize(600, 600)
        self.window.setStyleSheet('background-color: #272727')
        self.window.setWindowTitle(TITLE_VERSION)

        # Mac needs this to close the window
        self.window.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # FlameLineEdit class needs this
        self.window.setFocusPolicy(QtCore.Qt.StrongFocus)

        # Center Window
        resolution = QtWidgets.QDesktopWidget().screenGeometry()

        self.window.move(
                (resolution.width() / 2) - (self.window.frameSize().width() / 2),
                (resolution.height() / 2) - (self.window.frameSize().height() / 2))

        # Label
        self.find_label = FlameLabel('Find')

        # Line Edit
        self.find = FlameLineEdit('')
        self.find.textChanged.connect(find_updated)

        # List Widget
        self.list_scroll = FlameListWidget(min_width=500)
        self.list_scroll.addItems(self.get_names())
        self.list_scroll.sortItems()
        self.list_scroll.itemDoubleClicked.connect(okay_button)

        # Buttons
        self.invert_btn = FlameButton('Invert', connect=invert_selection)
        self.ok_btn = FlameButton('Ok', okay_button, button_color='blue')
        self.ok_btn.setAutoDefault(True)  # doesnt make Enter key work

        self.cancel_btn = FlameButton('Cancel', cancel_button)

        # Layout
        self.grid = QtWidgets.QGridLayout()
        self.grid.setHorizontalSpacing(10)
        self.grid.setVerticalSpacing(10)

        self.grid.addWidget(self.find_label, 0, 0)
        self.grid.addWidget(self.find, 0, 1)

        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.list_scroll)
        self.hbox.addWidget(self.invert_btn)
        self.hbox.addStretch(1)

        self.hbox2 = QtWidgets.QHBoxLayout()
        self.hbox2.addStretch(1)
        self.hbox2.addWidget(self.cancel_btn)
        self.hbox2.addWidget(self.ok_btn)

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.setMargin(20)
        self.vbox.addLayout(self.grid)
        self.vbox.addSpacing(20)
        self.vbox.addLayout(self.hbox)
        self.vbox.addSpacing(20)
        self.vbox.addLayout(self.hbox2)

        self.window.setLayout(self.vbox)

        self.window.show()
        return self.window


def scope_sequence(selection):
    """Ensure selection only contains the objects this script is inteneded for."""
    valid_objects = (
            flame.PyClip,
            flame.PySegment,
    )

    return all(isinstance(item, valid_objects) for item in selection)


def get_media_panel_custom_ui_actions():
    """Add right click menu."""
    return [{'name': 'Select...',
             'actions': [{'name': 'Filter Selection',
                          'isVisible': scope_sequence,
                          'execute': FilterSelection,
                          'minimumVersion': '2022.0.0.0'}]
            }]
