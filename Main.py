import numpy as np
from vis2 import MeshVisual
np.set_printoptions(threshold=np.inf)
import time as time

tension_array = np.asarray([26.6, 39.8, 53.1, 106.3, 119.5, 159.4, 212.5, 332.0, 478.1])
compression_array = np.asarray([[15.1, 39.8, 53.1, 106.3, 119.5, 159.4, 212.5, 332.0, 478.1],
                                [6.7, 30.1, 53.1, 106.3, 119.5, 159.4, 212.5, 332.0, 478.1],
                                [3.8, 16.9, 30.1, 60.2, 119.5, 159.4, 212.5, 332.0, 478.1],
                                [2.4, 10.8, 19.3, 38.6, 97.6, 159.4, 212.5, 332.0, 478.1],
                                [1.7, 7.5, 13.4, 26.8, 67.8, 120.5, 212.5, 332.0, 478.1],
                                [1.2, 5.5, 9.8, 19.7, 49.8, 88.5, 157.4, 332.0, 478.1],
                                [0.9, 4.2, 7.5, 15.1, 38.1, 67.8, 120.5, 294.1, 478.1],
                                [0.7, 3.3, 5.9, 11.9, 30.1, 53.5, 95.2, 232.4, 478.1],
                                [0.6, 2.7, 4.8, 9.6, 24.4, 43.4, 77.1, 188.2, 390.4],
                                [0.5, 2.2, 4.0, 8.0, 20.2, 35.8, 63.7, 155.6, 322.6],
                                [0.4, 1.9, 3.3, 6.7, 16.9, 30.1, 53.5, 130.7, 271.1],
                                [0.3, 1.4, 2.5, 4.9, 12.4, 22.1, 39.3, 96.0, 199.2],
                                [0.3, 1.2, 2.1, 4.3, 10.8, 19.3, 34.3, 83.7, 173.5],
                                [0.2, 1.1, 1.9, 3.8, 9.5, 16.9, 30.1, 73.5, 152.5],
                                [0.2, 0.9, 1.7, 3.3, 8.4, 15.0, 26.7, 65.1, 135.1],
                                [0.2, 0.8, 1.5, 3.0, 7.5, 13.4, 23.8, 58.1, 120.5],
                                [0.2, 0.8, 1.3, 2.7, 6.8, 12.0, 21.4, 52.1, 108.1]])




class Joint:
    def __init__(self, position, uid):
        self.pos = np.asarray(position, dtype=float)
        self.connections = []
        self.load = np.zeros(3, dtype=float)
        self.uid = uid
        self.support = False

    def attach(self, spring):
        self.connections.append(spring)

    def load(self, load):
        self.load = load


class Support(Joint):
    def __init__(self, position, uid):
        super().__init__(position, uid)
        self.reactions = np.asarray([0, 0, 0], dtype=float)
        self.support = True
        self.load = self.reactions

    def support_reactions(self, reactions):
        self.reactions = np.asarray(reactions)
        self.load = self.reactions


class Member:
    def __init__(self, joint_1, joint_2, type, unique_id):
        self.type = type
        self.joint_1 = joint_1
        self.joint_2 = joint_2
        self.length = np.linalg.norm(self.joint_2.pos - self.joint_1.pos) * 10
        self.uid = unique_id
        self.force = None
        self.fos = None

        self.max_tension = tension_array[type-1]

        int_l = int(self.length * 2) - 2
        int_h = int_l + 1
        length_l = (int_l) * 0.5 + 1
        comp_l = compression_array[int_l, type - 1]
        comp_h = compression_array[int_h, type - 1]
        comp_slope = (comp_h -  comp_l) / 0.5
        diff_length = self.length - length_l
        self.max_compression = comp_l + diff_length * comp_slope



class Truss:
    def __init__(self, dim, connection_type, truss_thickness, filename):
        self.m = np.empty(dim, dtype=object)
        self.joint_list = []
        self.member_list = []
        self.diagram = None
        self.connection_type = connection_type
        self.joint_num = 0
        self.support_num = 0
        self.truss_thickness = truss_thickness
        self.unique_id = 0
        self.unique_joint_id = 0
        self.truss_text = open(filename, "w+")


    def create_joint(self, slot, position):
        self.m[tuple(slot)] = Joint(position , self.unique_joint_id)
        self.unique_joint_id = self.unique_joint_id + 1
        self.joint_num = self.joint_num + 1
        self.joint_list.append(self.m[tuple(slot)])

    def create_support(self, slot, position):
        self.m[tuple(slot)] = Support(position, self.unique_joint_id)
        self.unique_joint_id = self.unique_joint_id + 1
        self.support_num = self.joint_num + 1
        self.joint_list.append(self.m[tuple(slot)])

    def create_member(self, slot_1, slot_2, type):
        joint_1, joint_2 = self.m[tuple(slot_1)], self.m[tuple(slot_2)]
        self.member_list.append(Member(joint_1, joint_2, type, self.unique_id))
        self.unique_id = self.unique_id + 1
        joint_1.attach(self.member_list[-1])
        joint_2.attach(self.member_list[-1])

    def load(self, load, load_slot, support1_slot, support2_slot, support3_slot, support4_slot):
        self.m[tuple(load_slot)].load = np.asarray(load)
        #self.m[tuple(support1_slot)].load = np.asarray(load)/-4
        #self.m[tuple(support2_slot)].load = np.asarray(load)/-4
        #self.m[tuple(support3_slot)].load = np.asarray(load) / -4
        #self.m[tuple(support4_slot)].load = np.asarray(load) / -4

    def force_balance(self):
        self.force_matrix = []
        self.force_answers = []

        force_balance_y = np.zeros(len(self.member_list) + 4)
        for r in range(1, 5):
            force_balance_y[-1 * r] = 1
        self.force_matrix.append(force_balance_y)
        self.force_answers.append(22.0312)

        moment_balance_y = np.zeros(len(self.member_list) + 4)
        moment_balance_y[-1] = -1.7
        moment_balance_y[-2] = -1.7
        moment_balance_y[-3] = 1.7
        moment_balance_y[-4] = 1.7
        self.force_matrix.append(moment_balance_y)
        self.force_answers.append(0)


        n=-1
        for joint in self.joint_list:
            new_force_x = np.zeros(len(self.member_list)+4)
            new_force_y = np.zeros(len(self.member_list)+4)
            new_force_z = np.zeros(len(self.member_list)+4)

            if joint.support == True:
                new_force_y[n] = 1
                n = n - 1

            for member in joint.connections:
                if joint.uid == member.joint_1.uid:
                    orient_vector = member.joint_2.pos - member.joint_1.pos
                elif joint.uid == member.joint_2.uid:
                    orient_vector = member.joint_1.pos - member.joint_2.pos
                else:
                    print("you done goofed")
                orient_norm = np.linalg.norm(orient_vector)
                orient_unit_vector = orient_vector / orient_norm
                new_force_x[member.uid] = orient_unit_vector[2]
                new_force_y[member.uid] = orient_unit_vector[1]
                new_force_z[member.uid] = orient_unit_vector[0]
            self.force_matrix.append(new_force_x)
            self.force_answers.append(-1*joint.load[2])
            self.force_matrix.append(new_force_y)
            self.force_answers.append(-1*joint.load[1])
            self.force_matrix.append(new_force_z)
            self.force_answers.append(-1*joint.load[0])


        #size_diff = np.shape(self.force_matrix)[0] - np.shape(self.force_matrix)[1]
        #adjucator = np.zeros([np.shape(self.force_matrix)[0], size_diff])
        #self.adj_force_matrix = np.concatenate((self.force_matrix, adjucator), 1)


        self.force_matrix = np.asarray(self.force_matrix)
        print(np.shape(self.force_matrix))
        print(np.shape(self.force_answers))
        self.internal_forces = np.linalg.lstsq(self.force_matrix, self.force_answers, rcond=None)[0]
        self.internal_forces = np.around(self.internal_forces, 2)
        member = 0
        for force in self.internal_forces:
            if member < len(self.member_list):
                self.member_list[member].force = force
                member = member + 1

    def check_results(self):

        self.truss_text.write("TRUSS REPORT \n \n")
        self.truss_text.write("Reactions (in Fx Fy Fz): \n")
        supports = [0, 1, 5, 6]
        for j in range(1, 5):
            self.truss_text.write(f"Reaction at {supports[j-1]}: ({0, self.internal_forces[-1*j], 0} \n")

        self.truss_text.write("UID \t Joint 1 \t \t Joint 2 \t \t Length \t Force \t \t Max T/C Force \t FOS \t \n")
        for member in self.member_list:

            if member.force > 0:
                member.fos = np.abs(member.max_tension/member.force)
                self.truss_text.write(f"{member.joint_1.uid}-{member.joint_2.uid}: \t ({member.joint_1.pos[2]:.3f}, {member.joint_1.pos[1]:.3f}, {member.joint_1.pos[0]:.3f}) "
                                      f"\t ({member.joint_2.pos[2]:.3f}, {member.joint_2.pos[1]:.3f}, {member.joint_2.pos[0]:.3f}) \t {member.length:.3f} \t \t {member.force:.3f} (T) "
                                      f"\t {member.max_tension:.3f}  \t {np.abs(member.max_tension/member.force):.3f}\t ")
                if np.abs(member.max_tension/member.force) >= 2:
                    self.truss_text.write(f"VALID")
                else:
                    self.truss_text.write(f"INVALID")


            if member.force < 0:
                member.fos = np.abs(member.max_compression/member.force)
                self.truss_text.write(f"{member.joint_1.uid}-{member.joint_2.uid}: \t ({member.joint_1.pos[2]:.3f}, {member.joint_1.pos[1]:.3f}, {member.joint_1.pos[0]:.3f}) "
                                      f"\t ({member.joint_2.pos[2]:.3f}, {member.joint_2.pos[1]:.3f}, {member.joint_2.pos[0]:.3f}) \t {member.length:.3f} \t \t {member.force:.3f} (C) "
                                      f"\t {member.max_compression:.3f}  \t {np.abs(member.max_compression/member.force):.3f}\t ")
                if np.abs(member.max_compression/member.force) >= 2:
                    self.truss_text.write(f"VALID")
                else:
                    self.truss_text.write(f"INVALID")

            if member.force == 0:
                member.fos = -99
                self.truss_text.write(f"{member.joint_1.uid}-{member.joint_2.uid}: \t ({member.joint_1.pos[2]:.3f}, {member.joint_1.pos[1]:.3f}, {member.joint_1.pos[0]:.3f}) "
                                      f"\t ({member.joint_2.pos[2]:.3f}, {member.joint_2.pos[1]:.3f}, {member.joint_2.pos[0]:.3f}) \t {member.length:.3f} "
                                      f"\t \t 0.000   \t N/A \t \t Inf  \t ZERO-FORCE ")




            self.truss_text.write('\n')




    def visual(self):
        self.diagram = MeshVisual(self, 4)
        while 1:
            self.diagram.update()

    def compute_cost(self):
        self.truss_text.write("\n \n")
        self.truss_text.write("Cost Analysis: \n")
        airplane_glue = 7500
        print(f"Airplane Glue, costs 7500")
        self.truss_text.write("Airplane Glue: $7500 \n")
        strip_lengths = np.zeros(3, dtype=float)
        strip_comp = np.array([[2, 0, 0],
                      [3, 0, 0],
                      [0, 1, 0],
                      [0, 2, 0],
                      [0, 0, 1],
                      [0, 3, 0],
                      [0, 4, 0],
                      [1, 3, 4],
                      [0, 0, 4]])
        strip_costs = np.array([1000, 3500, 7000])
        strip_cost = 0
        for member in self.member_list:
            strip_lengths = strip_lengths + (member.length)*strip_comp[member.type-1]
        print(f"Front and Back 2D Trusses, and Thickness Connections:")
        for n in range(1, 4):
            strip_count = strip_lengths[n-1] // 36
            if strip_lengths[n-1] % 36 != 0:
                strip_count = strip_count + 1
            print(f"Strip Type {n}: {strip_count} 36-inch strips needed, costs {strip_count*strip_costs[n-1]}")
            self.truss_text.write(f"Strip Type {n}: {strip_count} 36-inch strips needed, costs ${strip_count*strip_costs[n-1]} \n")
            strip_cost = strip_cost + strip_count*strip_costs[n-1]
        self.truss_text.write(r"Type 1: 1/16 Strip | Type 2: 1/8 Strip | Type 3: 3/16 Strip ")


        #Assuming 1 inch square gusset plates:
        #Each 2 x 36 gusset sheet can hold 72 gusset plates
        gusset_num = (self.joint_num + self.support_num)
        gusset_sheet_num = gusset_num // 72
        if gusset_num % 72 !=0:
            gusset_sheet_num = gusset_sheet_num + 1
        print(f"Gusset Plate Sheets: {gusset_sheet_num} needed, costs {gusset_sheet_num * 5000}")
        self.truss_text.write(f"\nGusset Plate Sheets {gusset_sheet_num} needed, costs ${gusset_sheet_num * 5000} \n")
        gusset_cost = gusset_sheet_num * 5000
        total_cost = airplane_glue + strip_cost + gusset_cost
        print(f"Total Cost: {total_cost}")
        self.truss_text.write(f"Total Cost: ${total_cost}")
        self.truss_text.close()










#TRUSS FINAL: Triangular, 9 Sections, Diagonals have Joints, ALL members SAVED
#---------------------------------------------------------------------
TrialTruss = Truss([2, 3, 9], 1, 0.4, "TrussFinal.txt")

#Building Joints:
#ORIGIN SIDE
#Two Supports
TrialTruss.create_support([0, 0, 0], [0, 0, 0])
TrialTruss.create_support([1, 0, 0], [0.4, 0, 0])

#Top of the Triangle
TrialTruss.create_joint([0, 2, 0], [0.2, 0.4, 0])

#Diagonal Joints
TrialTruss.create_joint([0, 1, 0], [0.1, 0.2, 0.2125])
TrialTruss.create_joint([1, 1, 0], [0.3, 0.2, 0.2125])

#OPPOSITE SIDE
#Two Supports
TrialTruss.create_support([0, 0, 8], [0, 0, 3.4])
TrialTruss.create_support([1, 0, 8], [0.4, 0, 3.4])

#Top of the Triangle
TrialTruss.create_joint([0, 2, 8], [0.2, 0.4, 3.4])

#Auto-builder for piece 1-7
size = 0.425
for n in range(1, 8):
    # Two Bottom Joints
    TrialTruss.create_joint([0, 0, n], [0, 0, 0 + size*n])
    TrialTruss.create_joint([1, 0, n], [0.4, 0, 0 + size*n])

    # Top of the Triangle
    TrialTruss.create_joint([0, 2, n], [0.2, 0.4, 0 + size*n])

    # Diagonal Joints
    TrialTruss.create_joint([0, 1, n], [0.1, 0.2, 0.2125 + size*n])
    TrialTruss.create_joint([1, 1, n], [0.3, 0.2, 0.2125 + size*n])

#Building Members:
#Auto-connector for 0-1, 1-2, etc to 7-8
bottomfl_types = [1, 1, 2, 3, 3, 2, 1, 1]
top_flat_types = [4, 6, 6, 7, 7, 6, 6, 4]
xsection_types = [3, 1, 1, 1, 3, 1, 1, 1]


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


for n in range(0, 3):
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

for n in range(3, 4):
    #DIAGONAL MEMBERS, CLOSE SIDE:
    #Close to close Xjoint
    TrialTruss.create_member([0, 0, n], [0, 1, n], 4)
    #Close Xjoint to next close
    TrialTruss.create_member([0, 1, n], [0, 0, n+1], 1)
    #Top to close Xjoint
    TrialTruss.create_member([0, 2, n], [0, 1, n], 1)
    #Close Xjoint to next top
    TrialTruss.create_member([0, 1, n], [0, 2, n+1], 4)

    #DIAGONAL MEMBERS, FAR SIDE:
    #Far to far Xjoint
    TrialTruss.create_member([1, 0, n], [1, 1, n], 4)
    #Far Xjoint to next far
    TrialTruss.create_member([1, 1, n], [1, 0, n + 1], 1)
    #Top to far Xjoint
    TrialTruss.create_member([0, 2, n], [1, 1, n], 1)
    #Far Xjoint to next top
    TrialTruss.create_member([1, 1, n], [0, 2, n + 1], 4)

for n in range(4, 5):
    #DIAGONAL MEMBERS, CLOSE SIDE:
    #Close to close Xjoint
    TrialTruss.create_member([0, 0, n], [0, 1, n], 1)
    #Close Xjoint to next close
    TrialTruss.create_member([0, 1, n], [0, 0, n+1], 4)
    #Top to close Xjoint
    TrialTruss.create_member([0, 2, n], [0, 1, n], 4)
    #Close Xjoint to next top
    TrialTruss.create_member([0, 1, n], [0, 2, n+1], 1)

    #DIAGONAL MEMBERS, FAR SIDE:
    #Far to far Xjoint
    TrialTruss.create_member([1, 0, n], [1, 1, n], 1)
    #Far Xjoint to next far
    TrialTruss.create_member([1, 1, n], [1, 0, n + 1], 4)
    #Top to far Xjoint
    TrialTruss.create_member([0, 2, n], [1, 1, n], 4)
    #Far Xjoint to next top
    TrialTruss.create_member([1, 1, n], [0, 2, n + 1], 1)

for n in range(5, 8):
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
