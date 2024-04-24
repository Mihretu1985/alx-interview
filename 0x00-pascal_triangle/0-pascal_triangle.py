def generate_pascal_triangle(num_rows):
    triangle = []
    for i in range(num_rows):
        row = [None for _ in range(i + 1)]
        row[0], row[-1] = 1, 1  # Set the first and last elements of the row to 1
        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

def print_pascal_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(len(triangle[-1]) * 3))

# Example usage:
num_rows = 5
triangle = generate_pascal_triangle(num_rows)
print_pascal_triangle(triangle)
This code defines a function generate_pascal_triangle that generates Pascal's triangle up to a specified number of rows and a function print_pascal_triangle to print the triangle nicely formatted. You can adjust the num_rows variable to generate Pascal's triangle with a different number of rows.

If you have any specific requirements or questions about Pascal's triangle or the implementation, feel free to ask!








