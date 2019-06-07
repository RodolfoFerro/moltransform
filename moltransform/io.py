"""

"""

def read_xyz(filename):
    """Utility function to read a xyz file.
    It returns a numpy matrix for a posterior transformation.
    """
    xyz = open(filename, "r")
    n_lns = int(xyz.readline())
    p_mat = np.zeros((20, 3))
    for l in range(n_lns + 1):
        ps = xyz.readline().split(" ")
        if l > 0:
            ps[-1] = ps[-1][:-1]
            ps = list(filter(lambda x: x != "" and x != "\n", ps))
            p_mat[l - 1] = np.array([float(ps[1]), float(ps[2]), float(ps[3])])
    xyz.close()
    return p_mat


def write_xyz(filename, p_mat):
    """
    Utility function to write a xyz file.
    """
    xyz = open(filename, "w")
    xyz.write("{}\n".format(len(p_mat)))
    xyz.write("\n")
    for line in range(len(p_mat)):
        xyz.write("C\t\t {: .5f}\t {: .5f}\t {: .5f}\n".format(
            p_mat[line, 0], p_mat[line, 1], p_mat[line, 2]))
    xyz.close()