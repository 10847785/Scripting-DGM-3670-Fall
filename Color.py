import maya.cmds as cmds

def control(shapeName, position):
    suffix = '_Ctrl'
    sels = cmds.ls(sl=True)
    if not sels:
        circle = cmds.circle(nr=(0, 1, 0), c=(0, 0, 0))
    else:
        for sel in sels:

            circle = cmds.circle(nr=(0, 1, 0), c=(0, 0, 0))
            print (str(circle[0]))
            bbox = cmds.exactWorldBoundingBox(sel)
            xmax = bbox[3]
            xmin = bbox[0]
            size = (xmax-xmin)
            print(size)
            scale = 1 + size
            cmds.matchTransform(circle, sel)
            cmds.scale(scale,scale,scale)
            cmds.listRelatives(circle[0], shapes=True)
            cmds.setAttr(circle[0]+".overrideEnabled", 1)
            cmds.setAttr(circle[0]+".overrideColor", 6)
            name = sel+suffix
            cmds.rename(circle[0],name)
            cmds.group(n=circle[0])
            cmds.group(em=True, n=circle[0])
            cmds.parent(sel, circle[0])



control('01', 'Leg')
def naming():
    control('01', 'Leg')

