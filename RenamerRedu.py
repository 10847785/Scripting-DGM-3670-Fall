import maya.cmds as cmds

def TextChange(name, count_start=1):
    sels=cmds.ls(sl=True)
    name_obj = []
    list_chars = name.count('#')
    title_area = name.partition('#' * list_chars)

    for index, sel in enumerate(sels, start=count_start):
        new_name = title_area[0] + str(index).zfill(list_chars) + title_area[2]
        new_name = cmds.rename(sel, new_name)
        name_obj.append(new_name)

    return name_obj

    print('Leg_##_Jnt' % name)
    return