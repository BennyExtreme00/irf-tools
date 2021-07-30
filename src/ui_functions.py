from main import *

class UIFunctions(MainWindow):

    def selectMenu(getStyle):
        select = getStyle + ("QPushButton { border-left: 6px solid rgb(24, 125, 193); background-color: rgba(22, 33, 63, 180); }")
        return select

    def deselectMenu(getStyle):
        deselect = getStyle.replace("QPushButton { border-left: 6px solid rgb(24, 125, 193); background-color: rgba(22, 33, 63, 180); }", "")
        return deselect

    def selectStandardMenu(self, widget):
        for w in self.ui.leftBar.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    def resetStyle(self, widget):
        for w in self.ui.leftBar.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))


