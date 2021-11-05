import maya.cmds as cmds

def Renamer(naming):
    listNames = cmds.ls(sl=True)


    for sel in Naming:
        txt = "Leg_##_Jnt"
        c = "#"
        print(txt.find(c))

        x = txt.partition("##")
        print(x)

        x = txt.rpartition("##")
        print(x)

        x = txt.replace("##", "01")
        print(x)

        part[0] + str(x).zfill() + x[2]


txt = "Leg_##_Jnt"
c = "#"
print(txt.find(c))

txt.partition("##")
print(x)

x = txt.rpartition("##")
print(x)

x = txt.replace("##", "01")
print(x)

part[0] + str(x).zfill(find) + x[2]

txt.partition("##")
print(txt)