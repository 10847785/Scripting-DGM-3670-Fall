import maya.cmds as cmds
import importlib

class ToolUI():
    def __init__(self):
        self.m_window = 'colorUIWindow'
        self.name_txtfield = ''
        self.name_txtfieldrename_grp = ''


    def create(self):
        self.delete()

        self.m_window = cmds.window(self.m_window,
                                    title="Menu",
                                    widthHeight=(100, 25))
        m_column = cmds.columnLayout(parent=self.m_window,
                                     adjustableColumn=True)

        ##Text Field
        self.name_txtfield = cmds.textField(parent=m_column)
        cmds.button(parent=m_column, label='Rename', command=lambda x: self.text_change_cmd())
        self.name_txtfieldrename_grp = cmds.textFieldButtonGrp(parent=m_column,
                                                            label='Name',
                                                            buttonLabel='Change',
                                                            buttonCommand=lambda *x: self.txtfieldbtn_cmd())

        ##Controls
        cmds.button(parent=m_column, label='Sphere', command='cmds.polySphere()')
        cmds.button(parent=m_column, label='Joint', command='cmds.joint()')
        cmds.button(parent=m_column, label='Control', command='cmds.circle()')
        cmds.button(parent=m_column, label='Contraint', command='cmds.parentConstraint()')

        ##Color Buttons
        m_column = cmds.gridLayout(parent=self.m_window,
                                   numberOfColumns=8,
                                   cellWidthHeight=(80, 80))

        cmds.button(parent=m_column, label='Default', command=lambda x: self.color_icon(0))
        cmds.button(parent=m_column, label='Red', command=lambda x: self.color_icon(1))
        cmds.button(parent=m_column, label='Gray', command=lambda x: self.color_icon(2))
        cmds.button(parent=m_column, label='Silver', command=lambda x: self.color_icon(3))
        cmds.button(parent=m_column, label='Magenta', command=lambda x: self.color_icon(4))
        cmds.button(parent=m_column, label='Dark Blue', command=lambda x: self.color_icon(5))
        cmds.button(parent=m_column, label='Blue', command=lambda x: self.color_icon(6))
        cmds.button(parent=m_column, label='Green', command=lambda x: self.color_icon(7))
        cmds.button(parent=m_column, label='Purple', command=lambda x: self.color_icon(8))
        cmds.button(parent=m_column, label='Pink', command=lambda x: self.color_icon(9))
        cmds.button(parent=m_column, label='Wood', command=lambda x: self.color_icon(10))
        cmds.button(parent=m_column, label='Brown', command=lambda x: self.color_icon(11))
        cmds.button(parent=m_column, label='Red-Brown', command=lambda x: self.color_icon(12))
        cmds.button(parent=m_column, label='Bright Red', command=lambda x: self.color_icon(13))
        cmds.button(parent=m_column, label='Light Green', command=lambda x: self.color_icon(14))
        cmds.button(parent=m_column, label='Sea Blue', command=lambda x: self.color_icon(15))
        cmds.button(parent=m_column, label='White', command=lambda x: self.color_icon(16))
        cmds.button(parent=m_column, label='Yellow', command=lambda x: self.color_icon(17))
        cmds.button(parent=m_column, label='Sky Blue', command=lambda x: self.color_icon(18))
        cmds.button(parent=m_column, label='Blue-Green', command=lambda x: self.color_icon(19))
        cmds.button(parent=m_column, label='Skin', command=lambda x: self.color_icon(20))
        cmds.button(parent=m_column, label='Tan', command=lambda x: self.color_icon(21))
        cmds.button(parent=m_column, label='Light Yellow', command=lambda x: self.color_icon(22))
        cmds.button(parent=m_column, label='Light-Dark Green', command=lambda x: self.color_icon(23))
        cmds.button(parent=m_column, label='Gold', command=lambda x: self.color_icon(24))
        cmds.button(parent=m_column, label='Dark Yellow', command=lambda x: self.color_icon(25))
        cmds.button(parent=m_column, label='Yellow-Green', command=lambda x: self.color_icon(26))
        cmds.button(parent=m_column, label='Swamp Green', command=lambda x: self.color_icon(27))
        cmds.button(parent=m_column, label='Light Blue', command=lambda x: self.color_icon(28))
        cmds.button(parent=m_column, label='Navy Blue', command=lambda x: self.color_icon(29))
        cmds.button(parent=m_column, label='Bright Purple', command=lambda x: self.color_icon(30))
        cmds.button(parent=m_column, label='Dark Pink', command=lambda x: self.color_icon(31))

        cmds.showWindow(self.m_window)

    def delete(self):
        if cmds.window(self.m_window, exists=True):
                cmds.deleteUI(self.m_window)

    def txtfieldbtn_cmd(self):
        import RenamerRedu
        importlib.reload(RenamerRedu)
        txt_data = cmds.textFieldButtonGrp(self.name_txtfieldrename_grp, q=True, text=True)
        RenamerRedu.TextChange(txt_data)
        return

    def text_change_cmd(self):
        import RenamerRedu
        importlib.reload(RenamerRedu)
        txt_data = cmds.textField(self.name_txtfield, q=True, text=True)
        RenamerRedu.TextChange(txt_data)
        return

    def color_icon(self, color):
        import ColorChange
        importlib.reload(ColorChange)
        ColorChange.colorChange(color)
        return

myUI = ToolUI()
myUI.create()