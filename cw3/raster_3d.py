import open3d
import numpy as np
import shapely

def draw_mesh(mesh: open3d.geometry.TriangleMesh):
    open3d.visualization.draw_geometries([mesh], mesh_show_back_face=True)


if __name__ == "__main__":
    mesh: open3d.geometry.TriangleMesh = open3d.geometry.TriangleMesh.create_sphere()
    mesh.compute_vertex_normals()
    # save mesh
    polygon = shapely.Polygon.from_bounds(0, 0, 10, 30)
    min_height, max_height = 0, 60
    wieszcholki = np.array(polygon.exterior.coords)

    xyz_min = np.hstack([
        wieszcholki,
        np.full(wieszcholki.shape[0], min_height)[:, np.newaxis]
    ])
    xyz_max = np.hstack([
        wieszcholki,
        np.full(wieszcholki.shape[0], max_height)[:, np.newaxis]
    ])

    xyz = np.vstack([xyz_min, xyz_max])

    triangles = []
    for i in range(1, wieszcholki.shape[0] - 1):
        triangles.append([i, i + 1, i + 1 + wieszcholki.shape[0]])
        triangles.append([i, i + 1 + wieszcholki.shape[0], i + wieszcholki.shape[0]])

    triangles.append([0, 1, 1 + wieszcholki.shape[0]])
    triangles.append([0, 1 + wieszcholki.shape[0], wieszcholki.shape[0]])
    # add podstawe
    for i in range(1, wieszcholki.shape[0] - 1):
        triangles.append([i, i + 1, 0])
        triangles.append([i + wieszcholki.shape[0], i + 1 + wieszcholki.shape[0], wieszcholki.shape[0]])

    mesh = open3d.geometry.TriangleMesh(
        open3d.utility.Vector3dVector(xyz),
        open3d.utility.Vector3iVector(triangles)
    )
    draw_mesh(mesh)

    open3d.io.write_triangle_mesh("sphere.obj", mesh)
