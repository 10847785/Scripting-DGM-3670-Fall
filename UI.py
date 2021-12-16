window = cmds.window( title="Joints", iconName="JointName", widthHeight=(10,5))
m_column = cmds.columnLayout(parent=window)
cmds.button(parent=m_column, label='Joint', command='cmds.joint()')
cmds.button(parent=m_column, label='control', command='cmds.circle()')
cmds.button(parent=m_column, label='contraint', command='cmds.parentConstraint()')
cmds.button(parent=m_column, label='move1', command='cmds.move(2,6,3)')
cmds.button(parent=m_column, label='move2', command='cmds.move(10,2,5)')
cmds.button(parent=m_column, label='move3', command='cmds.move(13,3,7)')

cmds.showWindow(window)

