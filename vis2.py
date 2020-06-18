import numpy as np
import tkinter as tk

def setup_graphics(width, height, name="Mesh Visual"):
    gui = tk.Tk()
    gui.geometry("{}x{}".format(width, height))
    gui.resizable(0, 0)
    gui.title(name)
    canvas = tk.Canvas(gui, width=width, height=height, bg='#000000', highlightthickness=0, borderwidth=0)
    canvas.pack(fill="both")
    canvas.create_rectangle(0, 0, width, height, fill="#000")
    canvas.configure(scrollregion=canvas.bbox("ALL"))
    return gui, canvas


class SpaceCanvasMap:
    def __init__(self, scale, window_width, window_height, window_center, mesh_center):
        self.scale = scale
        self.window_height = np.asarray(window_height)
        scaled_mesh_center = 50 * self.scale * np.asarray(mesh_center)
        self.center_transform = np.asarray(window_center) - scaled_mesh_center

    def space_to_canvas(self, point):
        old_point = point
        point = np.flip(point[1:], axis=0)
        scaled_point = [50*self.scale*coord for coord in point]
        centered_point = scaled_point + self.center_transform
        centered_point[1] = self.window_height - centered_point[1]
        if old_point[0] != 0:
            centered_point[0] = centered_point[0] + 80*old_point[0]
            centered_point[1] = centered_point[1] - 40*old_point[0]
        return centered_point


class MeshVisual:
    def __init__(self, mesh, scale_factor=1, window_width=800, window_height=800, point_radius=4, fill="#FFF"):
        self.full_mesh = mesh
        self.mesh = mesh.m[0, :, :]
        self.spring_list = mesh.member_list
        self.elem_y, self.elem_x = self.mesh.shape
        self.window_center = [window_width/2, window_height/2]
        self.mesh_center = [1.7, 0]

        self.gui, self.canvas = setup_graphics(window_width, window_height)
        self.space_canvas_map = SpaceCanvasMap(scale_factor, window_width, window_height, self.window_center, self.mesh_center)

        self.point_radius = point_radius
        self.fill = fill
        self.handles = []
        self.rigids_list = []
        self.shandles = []

        for rigid in np.nditer(self.full_mesh.m, flags=["refs_ok"]):
            rigid = rigid.item()
            if rigid is not None:
                canvas_x, canvas_y = self.space_canvas_map.space_to_canvas(rigid.pos)

                if rigid.support == 1:

                    handle = self.canvas.create_rectangle(
                        canvas_x - self.point_radius,
                        canvas_y - self.point_radius,
                        canvas_x + self.point_radius,
                        canvas_y + self.point_radius,
                        fill=self.fill)


                else:

                    handle = self.canvas.create_oval(
                        canvas_x - self.point_radius,
                        canvas_y - self.point_radius,
                        canvas_x + self.point_radius,
                        canvas_y + self.point_radius,
                        fill=self.fill)
                self.canvas.create_text(canvas_x + 0.5 * (canvas_x - canvas_x),
                                         canvas_y + 0.5 * (canvas_y - canvas_y) + 100, fill="white", text=str(rigid.uid))
                self.handles.append(handle)
                self.rigids_list.append(rigid)

        for spring in self.spring_list:
            canvas_xn, canvas_yn = self.space_canvas_map.space_to_canvas(spring.joint_1.pos)
            canvas_xp, canvas_yp = self.space_canvas_map.space_to_canvas(spring.joint_2.pos)
            if spring.fos == -99:
                shandle = self.canvas.create_line(canvas_xn, canvas_yn, canvas_xp, canvas_yp, dash=(2, 2),
                                                  fill='blue')
            elif spring.fos < 1:
                shandle = self.canvas.create_line(canvas_xn, canvas_yn, canvas_xp, canvas_yp, dash=(2, 2),
                                                  fill='red')
            elif spring.fos < 2:
                shandle = self.canvas.create_line(canvas_xn, canvas_yn, canvas_xp, canvas_yp, dash=(2, 2),
                                                  fill='yellow')
            elif spring.fos > 3:
                shandle = self.canvas.create_line(canvas_xn, canvas_yn, canvas_xp, canvas_yp, dash=(2, 2),
                                              fill='purple')
            else:
                shandle = self.canvas.create_line(canvas_xn, canvas_yn, canvas_xp, canvas_yp, dash=(2, 2),
                                                  fill='white')


            #self.canvas.create_text(canvas_xn + 0.5 * (canvas_xp - canvas_xn),
                                    #canvas_yn + 0.5 * (canvas_yp - canvas_yn) - 200, fill="white", text=str(spring.uid))
            self.shandles.append(shandle)


    def update(self):
        for rigid, handle in zip(self.rigids_list, self.handles):
            canvas_x, canvas_y = self.space_canvas_map.space_to_canvas(rigid.pos)
            self.canvas.coords(
                handle,
                canvas_x - self.point_radius,
                canvas_y - self.point_radius,
                canvas_x + self.point_radius,
                canvas_y + self.point_radius
            )
            self.canvas.itemconfig(handle, fill=self.fill)

        for spring, shandle in zip(self.spring_list, self.shandles):
            canvas_xn, canvas_yn = self.space_canvas_map.space_to_canvas(spring.joint_1.pos)
            canvas_xp, canvas_yp = self.space_canvas_map.space_to_canvas(spring.joint_2.pos)
            self.canvas.coords(shandle, canvas_xn, canvas_yn, canvas_xp, canvas_yp)


        self.gui.update()
