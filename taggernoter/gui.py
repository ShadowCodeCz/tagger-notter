from PyQt6.QtGui import QDoubleValidator, QFont
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

from . import core
from . import notificator


def clear_layout(layout):
    if layout:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                clear_layout(item.layout())


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        cfg = core.container.cfg

        self.notifier = core.container.notifier()
        self.main_layout = QVBoxLayout(self)

        scroll_area = QScrollArea(self)
        scroll_area.setObjectName("ScrollArea")
        scroll_area.setStyleSheet("#ScrollArea {border: 0px solid black}")
        scroll_area.setWidgetResizable(True)

        self.main_layout.addWidget(scroll_area)
        self.setLayout(self.main_layout)
        self.resize(cfg.window.open_width(), cfg.window.open_height())
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        render_cfg = core.container.cfg.render.main_window
        # self.setStyleSheet(f"background-color:{render_cfg.background_color()}")

    def keyPressEvent(self, event):
        modifier = ''
        if event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            modifier += 'Ctrl+'
        if event.modifiers() & Qt.KeyboardModifier.ShiftModifier:
            modifier += 'Shift+'
        if event.modifiers() & Qt.KeyboardModifier.AltModifier:
            modifier += 'Alt+'

        # key = event.text().upper()
        # if not key:
        key = Qt.Key(event.key()).name

        notification = notificator.Notification(notificator.Messages.key_event)
        notification.key = f"{modifier}{key}"
        self.notifier.notify(notification)

        super().keyPressEvent(event)
