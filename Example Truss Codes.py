#TRUSS 1:
TrialTruss = Truss([1, 2, 9], 1, 0.4)

TrialTruss.create_support([0, 0, 0], [0, 0, 0])
TrialTruss.create_support([0, 0, 8], [0, 0, 3.4])

TrialTruss.create_joint([0, 0, 1], [0, 0, 0.425])
TrialTruss.create_joint([0, 0, 2], [0, 0, 0.85])
TrialTruss.create_joint([0, 0, 3], [0, 0, 1.275])
TrialTruss.create_joint([0, 0, 4], [0, 0, 1.7])
TrialTruss.create_joint([0, 0, 5], [0, 0, 2.125])
TrialTruss.create_joint([0, 0, 6], [0, 0, 2.55])
TrialTruss.create_joint([0, 0, 7], [0, 0, 2.975])

TrialTruss.create_joint([0, 1, 1], [0, 0.4, 0.425])
TrialTruss.create_joint([0, 1, 2], [0, 0.4, 0.85])
TrialTruss.create_joint([0, 1, 3], [0, 0.4, 1.275])
TrialTruss.create_joint([0, 1, 4], [0, 0.4, 1.7])
TrialTruss.create_joint([0, 1, 5], [0, 0.4, 2.125])
TrialTruss.create_joint([0, 1, 6], [0, 0.4, 2.55])
TrialTruss.create_joint([0, 1, 7], [0, 0.4, 2.975])

for n in range(0, 8):
    TrialTruss.create_member([0, 0, n], [0, 0, n+1], 2)

for n in range(1, 8):
    TrialTruss.create_member([0, 0, n], [0, 1, n], 2)

for n in range(1, 7):
    TrialTruss.create_member([0, 1, n], [0, 1, n+1], 2)

TrialTruss.create_member([0, 0, 0], [0, 1, 1], 2)
TrialTruss.create_member([0, 1, 1], [0, 0, 2], 2)
TrialTruss.create_member([0, 0, 2], [0, 1, 3], 2)
TrialTruss.create_member([0, 1, 3], [0, 0, 4], 2)
TrialTruss.create_member([0, 0, 4], [0, 1, 5], 2)
TrialTruss.create_member([0, 1, 5], [0, 0, 6], 2)
TrialTruss.create_member([0, 0, 6], [0, 1, 7], 2)
TrialTruss.create_member([0, 1, 7], [0, 0, 8], 2)

#TRUSS 2: ARCH TRUSS (Flat Top)
TrialTruss = Truss([1, 2, 9], 1, 0.4)

TrialTruss.create_support([0, 0, 0], [0, 0, 0])
TrialTruss.create_support([0, 0, 8], [0, 0, 3.4])

TrialTruss.create_joint([0, 0, 1], [0, 0.2, 0.425])
TrialTruss.create_joint([0, 0, 2], [0, 0.35, 0.85])
TrialTruss.create_joint([0, 0, 3], [0, 0.45, 1.275])
TrialTruss.create_joint([0, 0, 4], [0, 0.5, 1.7])
TrialTruss.create_joint([0, 0, 5], [0, 0.45, 2.125])
TrialTruss.create_joint([0, 0, 6], [0, 0.35, 2.55])
TrialTruss.create_joint([0, 0, 7], [0, 0.2, 2.975])

TrialTruss.create_joint([0, 1, 0], [0, 0.6, 0])
TrialTruss.create_joint([0, 1, 1], [0, 0.6, 0.425])
TrialTruss.create_joint([0, 1, 2], [0, 0.6, 0.85])
TrialTruss.create_joint([0, 1, 3], [0, 0.6, 1.275])
TrialTruss.create_joint([0, 1, 4], [0, 0.6, 1.7])
TrialTruss.create_joint([0, 1, 5], [0, 0.6, 2.125])
TrialTruss.create_joint([0, 1, 6], [0, 0.6, 2.55])
TrialTruss.create_joint([0, 1, 7], [0, 0.6, 2.975])
TrialTruss.create_joint([0, 1, 8], [0, 0.6, 3.4])

for n in range(0, 9):
    TrialTruss.create_member([0, 0, n], [0, 1, n], 2)

for n in range(0, 8):
    TrialTruss.create_member([0, 0, n], [0, 0, n+1], 2)
    TrialTruss.create_member([0, 1, n], [0, 1, n + 1], 2)

for n in (0, 2, 4, 6):
    TrialTruss.create_member([0, 0, n], [0, 1, n+1], 2)

for n in (1, 3, 5, 7):
    TrialTruss.create_member([0, 1, n], [0, 0, n+1], 2)


#TRUSS 4: ARCHED TRUSS (Curved Top) For Truss 3, remove the excess diagonals
TrialTruss.create_support([0, 0, 0], [0, 0, 0])
TrialTruss.create_support([0, 0, 8], [0, 0, 3.4])

TrialTruss.create_joint([0, 0, 1], [0, 0.2, 0.425])
TrialTruss.create_joint([0, 0, 2], [0, 0.35, 0.85])
TrialTruss.create_joint([0, 0, 3], [0, 0.45, 1.275])
TrialTruss.create_joint([0, 0, 4], [0, 0.5, 1.7])
TrialTruss.create_joint([0, 0, 5], [0, 0.45, 2.125])
TrialTruss.create_joint([0, 0, 6], [0, 0.35, 2.55])
TrialTruss.create_joint([0, 0, 7], [0, 0.2, 2.975])

TrialTruss.create_joint([0, 1, 0], [0, 0.3, 0])
TrialTruss.create_joint([0, 1, 1], [0, 0.5, 0.425])
TrialTruss.create_joint([0, 1, 2], [0, 0.65, 0.85])
TrialTruss.create_joint([0, 1, 3], [0, 0.75, 1.275])
TrialTruss.create_joint([0, 1, 4], [0, 0.8, 1.7])
TrialTruss.create_joint([0, 1, 5], [0, 0.75, 2.125])
TrialTruss.create_joint([0, 1, 6], [0, 0.65, 2.55])
TrialTruss.create_joint([0, 1, 7], [0, 0.5, 2.975])
TrialTruss.create_joint([0, 1, 8], [0, 0.3, 3.4])

for n in range(0, 9):
    TrialTruss.create_member([0, 0, n], [0, 1, n], 2)

for n in range(0, 8):
    TrialTruss.create_member([0, 0, n], [0, 0, n+1], 2)
    TrialTruss.create_member([0, 1, n], [0, 1, n + 1], 2)

for n in (0, 2, 4, 6):
    TrialTruss.create_member([0, 0, n], [0, 1, n+1], 2)
    TrialTruss.create_member([0, 1, n], [0, 0, n + 1], 2)

for n in (1, 3, 5, 7):
    TrialTruss.create_member([0, 0, n], [0, 1, n + 1], 2)
    TrialTruss.create_member([0, 1, n], [0, 0, n+1], 2)

#Truss 5:
TrialTruss.create_support([0, 0, 0], [0, 0, 0])
TrialTruss.create_joint([0, 1, 0], [0.2, 0.3464, 0])
TrialTruss.create_support([1, 0, 0], [0.4, 0, 0])


TrialTruss.create_support([0, 0, 12], [0, 0, 3.4])

TrialTruss.create_joint([0, 0, 1], [0, 0.0, 0.4])
TrialTruss.create_joint([0, 0, 2], [0, 0.0, 0.8])
TrialTruss.create_joint([0, 0, 3], [0, 0.0, 1.1])
TrialTruss.create_joint([0, 0, 4], [0, 0.0, 1.4])
TrialTruss.create_joint([0, 0, 5], [0, 0.0, 1.55])
TrialTruss.create_joint([0, 0, 6], [0, 0.0, 1.7])
TrialTruss.create_joint([0, 0, 7], [0, 0.0, 1.85])
TrialTruss.create_joint([0, 0, 8], [0, 0.0, 2.0])
TrialTruss.create_joint([0, 0, 9], [0, 0.0, 2.3])
TrialTruss.create_joint([0, 0, 10], [0, 0.0, 2.6])
TrialTruss.create_joint([0, 0, 11], [0, 0.0, 3.0])

TrialTruss.create_joint([0, 1, 1], [0, 0.3, 0.4])
TrialTruss.create_joint([0, 1, 2], [0, 0.4, 0.8])
TrialTruss.create_joint([0, 1, 3], [0, 0.4, 1.1])
TrialTruss.create_joint([0, 1, 4], [0, 0.4, 1.4])
TrialTruss.create_joint([0, 1, 5], [0, 0.2, 1.55])
TrialTruss.create_joint([0, 1, 6], [0, 0.2, 1.7])
TrialTruss.create_joint([0, 1, 7], [0, 0.2, 1.85])
TrialTruss.create_joint([0, 1, 8], [0, 0.4, 2.0])
TrialTruss.create_joint([0, 1, 9], [0, 0.4, 2.3])
TrialTruss.create_joint([0, 1, 10], [0, 0.4, 2.6])
TrialTruss.create_joint([0, 1, 11], [0, 0.3, 3.0])

TrialTruss.create_joint([0, 2, 5], [0, 0.4, 1.55])
TrialTruss.create_joint([0, 2, 6], [0, 0.4, 1.7])
TrialTruss.create_joint([0, 2, 7], [0, 0.4, 1.85])

for n in range(0, 12):
    TrialTruss.create_member([0, 0, n], [0, 0, n+1], 2)

for n in range(1, 12):
    TrialTruss.create_member([0, 0, n], [0, 1, n], 2)

for n in (1, 2, 3):
    TrialTruss.create_member([0, 1, n], [0, 1, n+1], 2)
    TrialTruss.create_member([0, 1, n], [0, 0, n + 1], 2)

for n in (8, 9, 10):
    TrialTruss.create_member([0, 1, n], [0, 1, n + 1], 2)
    TrialTruss.create_member([0, 0, n], [0, 1, n + 1], 2)

TrialTruss.create_member([0, 0, 0], [0, 1, 1], 2)
TrialTruss.create_member([0, 1, 11], [0, 0, 12], 2)

TrialTruss.create_member([0, 1, 5], [0, 2, 5], 2)
TrialTruss.create_member([0, 1, 6], [0, 2, 6], 2)
TrialTruss.create_member([0, 1, 7], [0, 2, 7], 2)

TrialTruss.create_member([0, 1, 4], [0, 2, 5], 2)
TrialTruss.create_member([0, 2, 5], [0, 2, 6], 2)
TrialTruss.create_member([0, 2, 6], [0, 2, 7], 2)
TrialTruss.create_member([0, 2, 7], [0, 1, 8], 2)


TrialTruss.create_member([0, 1, 5], [0, 1, 4], 2)
TrialTruss.create_member([0, 1, 5], [0, 0, 4], 2)

TrialTruss.create_member([0, 1, 6], [0, 2, 5], 2)
TrialTruss.create_member([0, 1, 6], [0, 0, 5], 2)

TrialTruss.create_member([0, 1, 7], [0, 1, 8], 2)
TrialTruss.create_member([0, 1, 7], [0, 0, 8], 2)

TrialTruss.create_member([0, 1, 6], [0, 2, 7], 2)
TrialTruss.create_member([0, 1, 6], [0, 0, 7], 2)



TrialTruss = Truss([2, 2, 11], 1, 0.4, "TrussReport8.txt")


TrialTruss.create_support([0, 0, 0], [0, 0, 0])
TrialTruss.create_joint([0, 1, 0], [0.2, 0.3464, 0])
TrialTruss.create_support([1, 0, 0], [0.4, 0, 0])

n = 11
size = 3.4/(n-1)

for i in range(1, n-1):
    TrialTruss.create_joint([0, 0, i], [0, 0, size*i])
    TrialTruss.create_joint([0, 1, i], [0.2, 0.3464, size*i])
    TrialTruss.create_joint([1, 0, i], [0.4, 0, size*i])

    TrialTruss.create_member([0, 0, i-1], [0, 0, i], 1)
    TrialTruss.create_member([0, 0, i - 1], [0, 1, i], 3)
    TrialTruss.create_member([0, 0, i - 1], [1, 0, i-1], 3)
    TrialTruss.create_member([0, 0, i - 1], [0, 1, i - 1], 1)


    TrialTruss.create_member([0, 1, i - 1], [0, 1, i], 1)
    TrialTruss.create_member([0, 1, i - 1], [1, 0, i], 3)
    TrialTruss.create_member([0, 1, i - 1], [1, 0, i - 1], 3)
    TrialTruss.create_member([0, 1, i - 1], [0, 0, i], 1)

    TrialTruss.create_member([1, 0, i-1], [1, 0, i], 1)
    TrialTruss.create_member([1, 0, i - 1], [0, 1, i], 1)



    #TrialTruss.create_member([0, 1, i - 1], [0, 1, i], 1)
    #TrialTruss.create_member([0, 1, i - 1], [0, 0, i], 1)


    #TrialTruss.create_member([1, 0, i - 1], [1, 0, i], 1)




TrialTruss.create_support([0, 0, n-1], [0, 0, 3.4])
TrialTruss.create_joint([0, 1, n-1], [0.2, 0.3464, 3.4])
TrialTruss.create_support([1, 0, n-1], [0.4, 0, 3.4])

TrialTruss.create_member([0, 0, 9], [0, 0, 10], 1)
TrialTruss.create_member([0, 0, 9], [0, 1, 10], 1)
TrialTruss.create_member([0, 0, 9], [1, 0, 9], 1)
TrialTruss.create_member([0, 0, 9], [0, 1, 9], 1)

TrialTruss.create_member([0, 1, 9], [0, 1, 10], 1)
TrialTruss.create_member([0, 1, 9], [1, 0, 10], 1)
TrialTruss.create_member([0, 1, 9], [1, 0, 9], 1)
TrialTruss.create_member([0, 1, 9], [0, 0, 10], 1)

TrialTruss.create_member([1, 0, 9], [1, 0, 10], 1)
TrialTruss.create_member([1, 0, 9], [0, 1, 10], 1)

TrialTruss.create_member([0, 1, 10], [1, 0, 10], 1)
TrialTruss.create_member([0, 1, 10], [0, 0, 10], 1)
TrialTruss.create_member([0, 0, 10], [1, 0, 10], 1)


#Convert 98 N to 22 lbf, then half for each of the two face trusses
TrialTruss.load([0, -22.0312, 0], [0, 1, 4], [0, 0, 0], [1, 0, 0], [0, 0, 8], [1, 0, 8])


#TRUSS 8: Triangular, 9 Sections, Diagonals have Joints
#---------------------------------------------------------------------
TrialTruss = Truss([2, 3, 9], 1, 0.4, "TrussReport10.txt")

#Building Joints:
#ORIGIN SIDE
#Two Supports
TrialTruss.create_support([0, 0, 0], [0, 0, 0])
TrialTruss.create_support([1, 0, 0], [0.4, 0, 0])

#Top of the Triangle
TrialTruss.create_joint([0, 2, 0], [0.2, 0.3464, 0])

#Diagonal Joints
TrialTruss.create_joint([0, 1, 0], [0.1, 0.173, 0.2125])
TrialTruss.create_joint([1, 1, 0], [0.3, 0.173, 0.2125])

#OPPOSITE SIDE
#Two Supports
TrialTruss.create_support([0, 0, 8], [0, 0, 3.4])
TrialTruss.create_support([1, 0, 8], [0.4, 0, 3.4])

#Top of the Triangle
TrialTruss.create_joint([0, 2, 8], [0.2, 0.3464, 3.4])

#Auto-builder for piece 1-7
size = 0.425
for n in range(1, 8):
    # Two Bottom Joints
    TrialTruss.create_joint([0, 0, n], [0, 0, 0 + size*n])
    TrialTruss.create_joint([1, 0, n], [0.4, 0, 0 + size*n])

    # Top of the Triangle
    TrialTruss.create_joint([0, 2, n], [0.2, 0.3464, 0 + size*n])

    # Diagonal Joints
    TrialTruss.create_joint([0, 1, n], [0.1, 0.173, 0.2125 + size*n])
    TrialTruss.create_joint([1, 1, n], [0.3, 0.173, 0.2125 + size*n])

#Building Members:
#Auto-connector for 0-1, 1-2, etc to 7-8
for n in range(0, 8):
    #FLAT MEMBERS:

    #Close flat
    TrialTruss.create_member([0, 0, n], [0, 0, n+1], 1)
    #Far flat
    TrialTruss.create_member([1, 0, n], [1, 0, n + 1], 1)
    #Top flat
    TrialTruss.create_member([0, 2, n], [0, 2, n + 1], 7)
    #Side fltas

    #TRIANGULAR X-SECTION MEMBERS:
    #Close to top
    TrialTruss.create_member([0, 0, n], [0, 2, n], 1)
    #Top to far
    TrialTruss.create_member([0, 2, n], [1, 0, n], 1)
    #Far to close
    TrialTruss.create_member([1, 0, n], [0, 0, n], 1)

    #DIAGONAL MEMBERS, CLOSE SIDE:
    #Close to close Xjoint
    TrialTruss.create_member([0, 0, n], [0, 1, n], 2)
    #Close Xjoint to next close
    TrialTruss.create_member([0, 1, n], [0, 0, n+1], 2)
    #Top to close Xjoint
    TrialTruss.create_member([0, 2, n], [0, 1, n], 2)
    #Close Xjoint to next top
    TrialTruss.create_member([0, 1, n], [0, 2, n+1], 2)

    #DIAGONAL MEMBERS, FAR SIDE:
    #Far to far Xjoint
    TrialTruss.create_member([1, 0, n], [1, 1, n], 2)
    #Far Xjoint to next far
    TrialTruss.create_member([1, 1, n], [1, 0, n + 1], 2)
    #Top to far Xjoint
    TrialTruss.create_member([0, 2, n], [1, 1, n], 2)
    #Far Xjoint to next top
    TrialTruss.create_member([1, 1, n], [0, 2, n + 1], 2)

#LAST END MEMBERS (LAST TRIANGLE X-SECTION)
TrialTruss.create_member([0, 0, 8], [0, 2, 8], 1)
TrialTruss.create_member([0, 2, 8], [1, 0, 8], 1)
TrialTruss.create_member([1, 0, 8], [0, 0, 8], 1)

#Convert 98 N to 22 lbf
TrialTruss.load([0, -22.0312, 0], [0, 2 , 4], [0, 0, 0], [1, 0, 0], [0, 0, 8], [1, 0, 8])


TrialTruss.force_balance()
TrialTruss.check_results()
TrialTruss.compute_cost()

TrialTruss.visual()


#Load the top of the center of the mesh (slot [



TrialTruss = Truss([2, 3, 9], 1, 0.4, "TrussReport10.txt")

#Building Joints:
#ORIGIN SIDE
#Two Supports
TrialTruss.create_support([0, 0, 0], [0, 0, 0])
TrialTruss.create_support([1, 0, 0], [0.4, 0, 0])

#Top of the Triangle
TrialTruss.create_joint([0, 2, 0], [0.2, 0.3464, 0])

#Half Top of the Triangle
TrialTruss.create_joint([1, 2, 0], [0.2, 0.3464, 0.2125])

#Diagonal Joints
TrialTruss.create_joint([0, 1, 0], [0.1, 0.173, 0.2125])
TrialTruss.create_joint([1, 1, 0], [0.3, 0.173, 0.2125])

#OPPOSITE SIDE
#Two Supports
TrialTruss.create_support([0, 0, 8], [0, 0, 3.4])
TrialTruss.create_support([1, 0, 8], [0.4, 0, 3.4])

#Top of the Triangle
TrialTruss.create_joint([0, 2, 8], [0.2, 0.3464, 3.4])



#Auto-builder for piece 1-7
size = 0.425
for n in range(1, 8):
    # Two Bottom Joints
    TrialTruss.create_joint([0, 0, n], [0, 0, 0 + size*n])
    TrialTruss.create_joint([1, 0, n], [0.4, 0, 0 + size*n])

    # Top of the Triangle
    TrialTruss.create_joint([0, 2, n], [0.2, 0.3464, 0 + size*n])

    # Half Top of the Triangle
    TrialTruss.create_joint([1, 2, n], [0.2, 0.3464, 0.2125 + size*n])

    # Diagonal Joints
    TrialTruss.create_joint([0, 1, n], [0.1, 0.173, 0.2125 + size*n])
    TrialTruss.create_joint([1, 1, n], [0.3, 0.173, 0.2125 + size*n])

#FIRST END MEMBERS (FIRST TRIANGLE X-SECTION)
TrialTruss.create_member([0, 0, 0], [0, 2, 0], 1)
TrialTruss.create_member([0, 2, 0], [1, 0, 0], 1)
TrialTruss.create_member([1, 0, 0], [0, 0, 0], 1)

#Building Members:
#Auto-connector for 0-1, 1-2, etc to 7-8
for n in range(0, 8):
    #FLAT MEMBERS:

    #Close flat
    TrialTruss.create_member([0, 0, n], [0, 0, n+1], 1)
    #Far flat
    TrialTruss.create_member([1, 0, n], [1, 0, n + 1], 1)
    #Top flat first 1/2
    TrialTruss.create_member([0, 2, n], [1, 2, n], 3)
    # Top flat second 1/2
    TrialTruss.create_member([1, 2, n], [0, 2, n + 1], 3)
    #Side fltas


    #TRIANGULAR SLANT PYRAMID MEMBERS:
    #Close to top
    TrialTruss.create_member([0, 0, n], [1, 2, n], 1)
    TrialTruss.create_member([1, 0, n], [1, 2, n], 1)
    #Top to far
    TrialTruss.create_member([1, 2, n], [1, 0, n+1], 1)
    TrialTruss.create_member([1, 2, n], [0, 0, n+1], 1)
    #Far to close
    #TrialTruss.create_member([1, 0, n], [0, 0, n], 1)

    #DIAGONAL MEMBERS, CLOSE SIDE:
    #Close to close Xjoint
    TrialTruss.create_member([0, 0, n], [0, 1, n], 2)
    #Close Xjoint to next close
    TrialTruss.create_member([0, 1, n], [0, 0, n+1], 2)
    #Top to close Xjoint
    TrialTruss.create_member([0, 2, n], [0, 1, n], 2)
    #Close Xjoint to next top
    TrialTruss.create_member([0, 1, n], [0, 2, n+1], 2)

    #DIAGONAL MEMBERS, FAR SIDE:
    #Far to far Xjoint
    TrialTruss.create_member([1, 0, n], [1, 1, n], 2)
    #Far Xjoint to next far
    TrialTruss.create_member([1, 1, n], [1, 0, n + 1], 2)
    #Top to far Xjoint
    TrialTruss.create_member([0, 2, n], [1, 1, n], 2)
    #Far Xjoint to next top
    TrialTruss.create_member([1, 1, n], [0, 2, n + 1], 2)

#LAST END MEMBERS (LAST TRIANGLE X-SECTION)
TrialTruss.create_member([0, 0, 8], [0, 2, 8], 1)
TrialTruss.create_member([0, 2, 8], [1, 0, 8], 1)
TrialTruss.create_member([1, 0, 8], [0, 0, 8], 1)

#Convert 98 N to 22 lbf
TrialTruss.load([0, -22.0312, 0], [0, 2 , 4], [0, 0, 0], [1, 0, 0], [0, 0, 8], [1, 0, 8])


TrialTruss.force_balance()
TrialTruss.check_results()
TrialTruss.compute_cost()

TrialTruss.visual()


#Load the top of the center of the mesh (slot [



#TRUSS 12: Triangular, 9 Sections, Diagonals have Joints, ALL members SAVED
#---------------------------------------------------------------------
TrialTruss = Truss([2, 3, 9], 1, 0.4, "TrussReport12.txt")

#Building Joints:
#ORIGIN SIDE
#Two Supports
TrialTruss.create_support([0, 0, 0], [0, 0, 0])
TrialTruss.create_support([1, 0, 0], [0.4, 0, 0])

#Top of the Triangle
TrialTruss.create_joint([0, 2, 0], [0.2, 0.3464, 0])

#Diagonal Joints
TrialTruss.create_joint([0, 1, 0], [0.1, 0.173, 0.2125])
TrialTruss.create_joint([1, 1, 0], [0.3, 0.173, 0.2125])

#OPPOSITE SIDE
#Two Supports
TrialTruss.create_support([0, 0, 8], [0, 0, 3.4])
TrialTruss.create_support([1, 0, 8], [0.4, 0, 3.4])

#Top of the Triangle
TrialTruss.create_joint([0, 2, 8], [0.2, 0.3464, 3.4])

#Auto-builder for piece 1-7
size = 0.425
for n in range(1, 8):
    # Two Bottom Joints
    TrialTruss.create_joint([0, 0, n], [0, 0, 0 + size*n])
    TrialTruss.create_joint([1, 0, n], [0.4, 0, 0 + size*n])

    # Top of the Triangle
    TrialTruss.create_joint([0, 2, n], [0.2, 0.3464, 0 + size*n])

    # Diagonal Joints
    TrialTruss.create_joint([0, 1, n], [0.1, 0.173, 0.2125 + size*n])
    TrialTruss.create_joint([1, 1, n], [0.3, 0.173, 0.2125 + size*n])

#Building Members:
#Auto-connector for 0-1, 1-2, etc to 7-8
bottomfl_types = [1, 1, 2, 3, 3, 2, 1, 1]
top_flat_types = [6, 6, 7, 7, 7, 7, 6, 6]
xsection_types = [3, 1, 1, 1, 4, 1, 1, 1]


for n in range(0, 8):
    #FLAT MEMBERS:

    #Close flat
    TrialTruss.create_member([0, 0, n], [0, 0, n+1], bottomfl_types[n])
    #Far flat
    TrialTruss.create_member([1, 0, n], [1, 0, n + 1], bottomfl_types[n])
    #Top flat
    TrialTruss.create_member([0, 2, n], [0, 2, n + 1], top_flat_types[n])
    #Side fltas

    #TRIANGULAR X-SECTION MEMBERS:
    #Close to top
    TrialTruss.create_member([0, 0, n], [0, 2, n], xsection_types[n])
    #Top to far
    TrialTruss.create_member([0, 2, n], [1, 0, n], xsection_types[n])
    #Far to close
    TrialTruss.create_member([1, 0, n], [0, 0, n], xsection_types[n])


for n in range(0, 4):
    #DIAGONAL MEMBERS, CLOSE SIDE:
    #Close to close Xjoint
    TrialTruss.create_member([0, 0, n], [0, 1, n], 3)
    #Close Xjoint to next close
    TrialTruss.create_member([0, 1, n], [0, 0, n+1], 1)
    #Top to close Xjoint
    TrialTruss.create_member([0, 2, n], [0, 1, n], 1)
    #Close Xjoint to next top
    TrialTruss.create_member([0, 1, n], [0, 2, n+1], 3)

    #DIAGONAL MEMBERS, FAR SIDE:
    #Far to far Xjoint
    TrialTruss.create_member([1, 0, n], [1, 1, n], 3)
    #Far Xjoint to next far
    TrialTruss.create_member([1, 1, n], [1, 0, n + 1], 1)
    #Top to far Xjoint
    TrialTruss.create_member([0, 2, n], [1, 1, n], 1)
    #Far Xjoint to next top
    TrialTruss.create_member([1, 1, n], [0, 2, n + 1], 3)


for n in range(4, 8):
    #DIAGONAL MEMBERS, CLOSE SIDE:
    #Close to close Xjoint
    TrialTruss.create_member([0, 0, n], [0, 1, n], 1)
    #Close Xjoint to next close
    TrialTruss.create_member([0, 1, n], [0, 0, n+1], 3)
    #Top to close Xjoint
    TrialTruss.create_member([0, 2, n], [0, 1, n], 3)
    #Close Xjoint to next top
    TrialTruss.create_member([0, 1, n], [0, 2, n+1], 1)

    #DIAGONAL MEMBERS, FAR SIDE:
    #Far to far Xjoint
    TrialTruss.create_member([1, 0, n], [1, 1, n], 1)
    #Far Xjoint to next far
    TrialTruss.create_member([1, 1, n], [1, 0, n + 1], 3)
    #Top to far Xjoint
    TrialTruss.create_member([0, 2, n], [1, 1, n], 3)
    #Far Xjoint to next top
    TrialTruss.create_member([1, 1, n], [0, 2, n + 1], 1)



#LAST END MEMBERS (LAST TRIANGLE X-SECTION)
TrialTruss.create_member([0, 0, 8], [0, 2, 8], 3)
TrialTruss.create_member([0, 2, 8], [1, 0, 8], 3)
TrialTruss.create_member([1, 0, 8], [0, 0, 8], 3)

#Convert 98 N to 22 lbf
TrialTruss.load([0, -22.0312, 0], [0, 2 , 4], [0, 0, 0], [1, 0, 0], [0, 0, 8], [1, 0, 8])


TrialTruss.force_balance()
TrialTruss.check_results()
TrialTruss.compute_cost()

TrialTruss.visual()