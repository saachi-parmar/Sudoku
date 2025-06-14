# Sudoku
# 🧩 Sudoku Solver Collection

A collection of Python programs to solve 9×9 Sudoku puzzles using the backtracking algorithm. The repository includes three progressively enhanced versions:

- ✅ **Sudoku1**: Basic solver with a fixed puzzle
- 📥 **Sudoku2**: Console-based input from user
- 🖥️ **Sudoku3**: Interactive GUI with tkinter

---

## 🔢 About Sudoku

Sudoku is a logic-based, combinatorial number-placement puzzle. The objective is to fill a 9×9 grid so that each column, each row, and each of the nine 3×3 boxes contains the digits from **1 to 9** exactly once.

---

## 📂 Files

### 1. Sudoku1.py — Basic Solver  
- Solves a **hardcoded puzzle** using recursion and backtracking  
- Outputs the result in the console

### 2. Sudoku2.py — Console Input Version  
- Accepts **user input from the terminal** (row-by-row)
- Includes **input validation** for correct formatting  
- Solves and prints the final grid

### 3. Sudoku3.py — GUI-based Solver  
- Built with **Tkinter**
- Supports:
  - ✅ Grid input via GUI
  - 🖱️ Click and arrow-key navigation
  - 🎯 Highlighting 3×3 subgrids
  - 🧼 Clear grid button
  - 📛 Error handling and alerts if unsolvable or invalid
