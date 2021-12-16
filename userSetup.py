import maya.cmds as cmds

if not cmds.commandPort(":4434", query=True):
    cmds.commandPort(name=":4434")

if 'C:\MayaPython' not in sys.path:
    sys.path.append('C:\MayaPython')