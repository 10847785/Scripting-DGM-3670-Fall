import maya.cmds as cmds

def renamer(numName):
    numName.partition("##")
    numRun = cmds.ls(sl=True)
    for count, object in enumerate(numRun.selected_objects, 1):
        numName.count("#")
        numName[0] + str(count).zfill(2) + x[2]
    renamer("Leg_##_Jnt")

