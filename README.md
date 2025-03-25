# Vector Editor (CLI)

A simple console-based vector editor for working with geometric shapes.

## Features

- Create shapes:
  - 📍 Point (by coordinates)
  - 📏 Line segment (by two points)
  - ⭕ Circle (center and radius)
  - ⬛ Square (base point and side length)
- Manage shapes:
  - View list of all created objects
  - Delete shapes by ID
- Input parameter validation
- Automatic ID generation for shapes
- Interactive help (use the `help` command)

## Installation and Launch

1. Ensure Python 3.10 or newer is installed.
2. Download the editor files:
   ```bash
   git clone https://github.com/Rust-it/CLI_shapes.git
   cd CLI_shapes
   ```
3. Run the program:
   ```bash
   python main.py
   ```

## Usage

### Basic Commands

|Command|Description|
|-|-|
|create <тип> [args]|Create a shape|
|delete <id>|Delete a shape by ID|
|list|Show all shapes|
|help|Display command help|
|exit|Exit the program|

### Creating Shapes

```bash
create point <x> <y>
create line <x1> <y1> <x2> <y2>
create circle <cx> <cy> <radius>
create square <x> <y> <side>
```

Examples:
```bash
> create point 10.5 20
Создана точка с ID 1.

> create circle 50 50 30
Создан круг с ID 2.
```

### Viewing Shapes

```bash
> list
Созданные фигуры:
  ID 1: Точка (10.5, 20)
  ID 2: Круг с центром в (50, 50) и радиусом 30
```

### Deleting a Shape

```bash
> delete 2
Фигура с ID 2 удалена.
```

## Development

### Project Structure

* Shape: Base class for all shapes
* Subclasses:
   * Point
   * Line
   * Circle
   * Square
* ShapeManager: Manager for handling shapes

### Requirements

* Python 3.10+
