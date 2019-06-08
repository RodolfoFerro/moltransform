# moltransform 💻⚗️

![PyPI - License](https://img.shields.io/pypi/l/moltransform.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/moltransform.svg)
![PyPI](https://img.shields.io/pypi/v/moltransform.svg)
![PyPI - Format](https://img.shields.io/pypi/format/moltransform.svg)
![GitHub top language](https://img.shields.io/github/languages/top/RodolfoFerro/moltransform.svg)


Molecular transformations for graphic displaying using Cartesian coordinates.

## How to use it

#### Generalities:
This package aims to transform `(x, y, z)` coordinates of molecules by reading and writing directly from a `.xyz` file and specifying the transformation vector. For each transformation function in the `transform` module, a `verbose` flag can be set `True` to print the transformation matrix to be applied for all `(x, y, z)` coordinates.

### Opening a file

To load a file, we will use the `read_xyz` function by passing to it the path to the corresponding file to be opened.

An example on how to load a `.xyz` file:
```bash
>>> from moltransform.io import read_xyz
>>> positions_matrix = read_xyz("path/to/file.xyz")
```

### Centering coordinates

Center the molecules' coordinates by finding the center position of all `(x, y, z)` coordinates.
```bash
>>> from moltransform.transform import center
>>> centered_positions = center(positions_matrix)
```

### Translating coordinates

Translate a molecule using a specific vector `(a, b, c)`. This implies:
<center>
	<img src="https://latex.codecogs.com/svg.latex?\fn_cm&space;\hspace*{-18}&space;x&space;\rightarrow&space;x&space;&plus;&space;a,\newline&space;y&space;\rightarrow&space;y&space;&plus;&space;b,\newline&space;z&space;\rightarrow&space;z&space;&plus;&space;c" title="\hspace*{-18} x \rightarrow x + a,\newline y \rightarrow y + b,\newline z \rightarrow z + c" />
</center>

```bash
>>> from moltransform.transform import translate
>>> translated_positions = translate(positions_matrix, [a, b, c])
```


### Scaling coordinates

Scale the molecule along the 3-axis by a vector `(a, b, c)`. This implies:
<center>
	<img src="https://latex.codecogs.com/svg.latex?\fn_cm&space;\hspace*{-18}&space;x&space;\rightarrow&space;ax,\newline&space;y&space;\rightarrow&space;by,\newline&space;z&space;\rightarrow&space;cz" title="\hspace*{-18} x \rightarrow ax,\newline y \rightarrow by,\newline z \rightarrow cz" />
</center>

```bash
>>> from moltransform.transform import scale
>>> scaled_positions = scale(positions_matrix, [a, b, c])
```

### Saving into a file

To save transformed coordinates into a file, we will use the `write_xyz` function by passing to it the path to the corresponding file to be **created**.

An example on how to save into a `.xyz` file:
```bash
>>> from moltransform.io import write_xyz
>>> write_xyz("path/to/file.xyz", positions_matrix)
```