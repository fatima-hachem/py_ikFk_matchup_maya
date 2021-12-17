import maya.cmds as cmds

if 'myWin' in globals():
    if cmds.window(myWin, exists=True):
        cmds.deleteUI(myWin, window=True)
        
myWin = cmds.window(title='FK IK Align / Match', menuBar=True)

#https://download.autodesk.com/us/maya/2009help/CommandsPython/columnLayout.html
cmds.columnLayout(width=300, columnAlign='center', columnAttach=['both', 10])

cmds.button(label='Match FK to IK', command='matchFkToIk()')
cmds.button(label='Match IK to FK', command='matchIkToFk()')

cmds.setParent('..')

cmds.showWindow(myWin)


#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#                                             WHERE THE MAGIC HAPPENS
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------


# to select an object in a group: group_name|object_name ex:grp_orient_constraint|jnt_FK_01
def matchFkToIk():
    print 'match fk to ik has been triggered!'
    


def matchIkToFk():
    print 'match ik to fk has been triggered!'