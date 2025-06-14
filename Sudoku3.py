import tkinter as tk
from tkinter import messagebox

M = 9

# --- Solver Functions ---
def is_valid(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[startRow + i][startCol + j] == num:
                return False
    return True

def solve_sudoku(grid, row=0, col=0):
    if row == M - 1 and col == M:
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return solve_sudoku(grid, row, col + 1)
    for num in range(1, M + 1):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid, row, col + 1):
                return True
            grid[row][col] = 0
    return False

# --- GUI Functions ---
def get_grid():
    grid = []
    for i in range(9):
        row = []
        for j in range(9):
            val = entries[i][j].get()
            try:
                val = int(val) if val else 0
                if not (0 <= val <= 9):
                    raise ValueError
            except ValueError:
                messagebox.showerror("Invalid Input", f"Cell ({i+1},{j+1}) must be 0–9.")
                return None
            row.append(val)
        grid.append(row)
    return grid

def set_grid(grid):
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(0, str(grid[i][j]))

def solve():
    grid = get_grid()
    if grid:
        if solve_sudoku(grid):
            set_grid(grid)
            messagebox.showinfo("Solved", "Sudoku solved successfully!")
        else:
            messagebox.showwarning("Failed", "No solution exists.")

def clear_grid():
    for row in entries:
        for cell in row:
            cell.delete(0, tk.END)

def on_arrow(event, row, col):
    if event.keysym == 'Up' and row > 0:
        entries[row - 1][col].focus_set()
    elif event.keysym == 'Down' and row < 8:
        entries[row + 1][col].focus_set()
    elif event.keysym == 'Left' and col > 0:
        entries[row][col - 1].focus_set()
    elif event.keysym == 'Right' and col < 8:
        entries[row][col + 1].focus_set()

# --- GUI Setup ---
root = tk.Tk()
root.title("Sudoku Solver")
root.configure(bg="#f8fafc", padx=20, pady=20)

entries = []
for i in range(9):
    row = []
    for j in range(9):
        bg_color = "#ffffff" if ((i//3 + j//3) % 2 == 0) else "#e2e8f0"  # Highlight 3x3 blocks
        e = tk.Entry(root, width=3, font=("Segoe UI", 16), justify="center", bd=1,
                     relief="solid", bg=bg_color)
        e.grid(row=i, column=j, ipadx=2, ipady=5, padx=1, pady=1)  # compact grid padding
        e.bind("<Up>", lambda e, x=i, y=j: on_arrow(e, x, y))
        e.bind("<Down>", lambda e, x=i, y=j: on_arrow(e, x, y))
        e.bind("<Left>", lambda e, x=i, y=j: on_arrow(e, x, y))
        e.bind("<Right>", lambda e, x=i, y=j: on_arrow(e, x, y))
        row.append(e)
    entries.append(row)

# --- Buttons ---
btn_frame = tk.Frame(root, pady=10, bg="#f8fafc")
btn_frame.grid(row=9, column=0, columnspan=9)

tk.Button(btn_frame, text="Solve", command=solve, font=("Segoe UI", 12),
          bg="#34d399", fg="black", width=10).pack(side="left", padx=10)

tk.Button(btn_frame, text="Clear", command=clear_grid, font=("Segoe UI", 12),
          bg="#f87171", fg="black", width=10).pack(side="left", padx=10)

root.mainloop()
