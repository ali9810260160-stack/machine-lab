<div align="center">

# ⚙️ Machine Lab

### Design custom CPU architectures · Define instruction sets · Assemble · Simulate

**A single-file, zero-dependency web workbench for building and running your own computer architectures — right in the browser.**

[![HTML](https://img.shields.io/badge/HTML-single--file-e34c26?logo=html5&logoColor=white)](#)
[![JavaScript](https://img.shields.io/badge/JavaScript-vanilla-f7df1e?logo=javascript&logoColor=black)](#)
[![Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)](#)
[![Build](https://img.shields.io/badge/build-none-blueviolet)](#)
[![License](https://img.shields.io/badge/license-MIT-6d5efc)](#)
[![Made for](https://img.shields.io/badge/Computer%20Structure%20%26%20Language-course-12b5a0)](#)

</div>

---

## 📖 Table of Contents

- [What is Machine Lab?](#-what-is-machine-lab)
- [✨ Feature Highlights](#-feature-highlights)
- [🚀 Quick Start](#-quick-start)
- [🧠 Concepts You Can Model](#-concepts-you-can-model)
- [🏗️ Designing a Machine](#️-designing-a-machine)
- [🧩 Instruction Formats](#-instruction-formats)
- [📝 The Operation Language](#-the-operation-language)
- [💾 Assembly Syntax](#-assembly-syntax)
- [🔬 Worked Examples from the Course](#-worked-examples-from-the-course)
  - [Example Machine 3 — Two-address, memory-direct / memory-indirect](#example-machine-3--two-address-memory-direct--memory-indirect)
  - [Example Machine 4 — Two-address with registers, 3 formats](#example-machine-4--two-address-with-registers-3-formats)
  - [Example Machine 5 — 2/3-address with indexed and immediate](#example-machine-5--23-address-with-indexed-and-immediate)
  - [Example Machine 6 — One-address accumulator machine](#example-machine-6--one-address-accumulator-machine)
- [📤 Output: The Listing Table](#-output-the-listing-table)
- [🎮 Simulation Mode](#-simulation-mode)
- [💾 Persistence & Themes](#-persistence--themes)
- [🗂️ File Layout](#️-file-layout)
- [🙏 Credits](#-credits)

---

## 🎯 What is Machine Lab?

**Machine Lab** is a self-contained browser application that lets you **invent a computer architecture from scratch**, describe its instruction set in a small algebraic notation, write assembly programs for it, and watch them turn into **hexadecimal machine code** and **execute step-by-step** in a live simulator.

It mirrors the exact exercise format used in *Computer Structure & Language* (Lecture 3 — Registers, Addressing Modes, Linker, Loader):

> *"In a 2-address machine, we have: main memory size = 2¹⁶ addressable units (each 8 bits), word size = 16 bits, unaligned, big endian, addressing modes: memory direct and memory indirect. The instruction format is shown below…"*

…followed by a table of opcodes, mnemonics, and operations, then a program, then its **machine-code translation** with addresses.

Machine Lab turns that whole workflow into a **live, editable, gorgeous UI** — no paper, no manual translation, no mistakes.

---

## ✨ Feature Highlights

| | |
|---|---|
| 🏭 **Fully parametric machines** | Memory cell width, address width, word size, endianness, register count, register width, name prefix, special registers — all editable, all visualised. |
| 🧱 **Unlimited instruction formats** | Each format is defined as a sequence of bit fields (`opcode`, `reg`, `addr`, `imm`) with a live bit-layout diagram (like the boxes in your handout). |
| 🧠 **Semantic operation language** | Every instruction has a behaviour written in a tiny expression language: `r1 <- r1 + M[r2]`, `if (r1 = 0) then PC <- addr`, and so on. Parsed and executed for real. |
| 📜 **Custom assembly** | Labels, `org`, `dw`, `N dup(?)`, decimal / hex / binary literals, comments — compiled by a two-pass assembler with a symbol table. |
| 🔢 **Hex-everything** | Addresses and machine codes are always shown in hexadecimal, formatted exactly like the course listing tables. |
| 🎛️ **Live listing table** | Address · Machine Code · Assembly, side-by-side, with per-field bit chips coloured by field type. |
| ▶️ **Real simulator** | Step / run, register file view, special registers, hex memory dump with PC highlight and changed-cell tracking, and an execution log. |
| 💾 **Persistence** | Machines are stored in `localStorage`. Create, duplicate, rename, delete — everything survives reloads. |
| 🌗 **Beautiful by default** | Persian RTL interface, Vazirmatn + JetBrains Mono fonts, dark/light themes, glassy sticky header, gradient accents. |
| 📦 **Single file** | Everything lives inside `machine-lab.html`. No npm, no bundler, no server. |

---

## 🚀 Quick Start

```bash
# 1. Download the file
curl -O https://raw.githubusercontent.com/<you>/machine-lab/main/machine-lab.html

# 2. Open it — that's it.
open machine-lab.html      # macOS
xdg-open machine-lab.html  # Linux
start machine-lab.html     # Windows
```

No installation, no build, no dependencies. It just runs.

The app ships with **three preloaded example machines** (Examples 3, 4 and 5 from the course handout) so you can start exploring immediately.

---

## 🧠 Concepts You Can Model

Machine Lab is expressive enough to describe everything from the lecture slides:

| Concept | How it's modelled |
|---|---|
| **Addressing modes** | *Direct* → `M[addr]` · *Indirect* → `M[M[addr]]` · *Register direct* → `r1` · *Register indirect* → `M[r2]` · *Immediate* → `#data` field type · *Indexed* → `M[addr + r2]` |
| **Multi-address machines** | One-address (accumulator), two-address, and 2/3-address machines — all achievable with different field layouts. |
| **Special registers** | Define any name in `sp`, e.g. `ACC:16, SP:16`, then use it directly in operations: `ACC <- ACC + M[addr]`. |
| **Stack-like calls** | Write `r1 <- PC` before updating `PC` to emulate `call r1, addr(r2)`. |
| **Variable-length formats** | Multiple formats with different total bit lengths coexist — the simulator selects by longest opcode prefix. |

---

## 🏗️ Designing a Machine

The **“۱ · Define Machine”** tab exposes every architectural knob:

| Parameter | Meaning | Example (Machine 3) |
|---|---|---|
| Name | Display name | `Example Machine 3` |
| Memory cell (bits) | Size of one addressable unit | `8` |
| Address width (bits) | Memory has `2ⁿ` cells | `16` → `2¹⁶` cells |
| Word size (bits) | Length of an integer word | `16` |
| Endianness | `big` or `little` | `big` |
| Register count | Number of general registers | `0` (Machine 3 has none) |
| Register width | Bits per register | `16` |
| Register prefix | Name prefix for registers | `R` |
| Special registers | `NAME:bits` list | `ACC:16` for accumulator machines |

Derived values are shown live as chips:

```
MAR = 16 bit   MBR = 16 bit   IR = 40 bit   PC = 16 bit   Memory = 2^16 × 8b
```

---

## 🧩 Instruction Formats

Each format is a row of **bit fields**. Just like the boxes in the handout:

```
┌──────────┬────────────────┬────────────────┐
│  Opcode  │     addr1      │     addr2      │
│  8 bits  │    16 bits     │    16 bits     │
└──────────┴────────────────┴────────────────┘
```

You define:

1. **The bit layout** — add/remove fields, choose each field’s name, width, and type (`opcode`, `reg`, `addr`, `imm`).
2. **The instructions** in that format — for each:
   - **Opcode** — binary (`00000000`) or hex (`0x00`).
   - **Mnemonic / Syntax** — e.g. `add addr1,(addr2)`.
   - **Operation** — a semantic program in the operation language.

> ⚠️ The **first field must be `opcode`**, and the **total bit width of every format must be a multiple of the memory cell size**. Machine Lab validates both — a red inline error tells you exactly what's wrong.

---

## 📝 The Operation Language

This is the heart of Machine Lab. It's a small expression language that describes *what an instruction does*, written in the same style as the **Operation** column of the lecture slides.

### Grammar at a glance

```ebnf
operation  ::= statement (";" statement)*
statement  ::= if-stmt | halt | assignment
if-stmt    ::= "if" "(" cond ")" "then" statement
halt       ::= "halt"
assignment ::= lvalue "<-" expression
lvalue     ::= FIELD | "M[" expr "]" | "R[" expr "]" | SPECIAL
```

### Operators

| Category | Operators |
|---|---|
| Assignment | `<-` or `←` |
| Arithmetic | `+  -  *` |
| Bitwise | `&  \|  ^  ~` (or `∧ ∨ ⊕`) |
| Comparison | `=  !=  <  >  <=  >=` (or `==`, `≠`, `≤`, `≥`) |
| Grouping | `( … )` |

All comparisons are **signed**.

### Operand types

| Syntax | Meaning |
|---|---|
| `r1`, `addr1`, `data` | A field of the current instruction. If it's a register field, it means the *contents* of that register. |
| `M[x]` or `M(x)` | Memory at address `x`. |
| `M[M[x]]` | **One level of indirection.** Chain for 2-level: `M[M[M[x]]]`. |
| `R[expr]` | Register whose number is `expr` (dynamic register indexing). |
| `PC`, `ACC`, … | Special registers declared on the machine. |
| `0x1F`, `1Fh`, `0b101`, `42` | Integer literals (hex, hex, binary, decimal). |

### Real examples straight from the handout

| Operation (as written in Machine Lab) | Meaning |
|---|---|
| `addr1 <- M[addr2]` | Direct memory load |
| `addr1 <- M[M[addr2]]` | One-level indirect load |
| `M[M[addr1]] <- M[addr2]` | Indirect store |
| `addr1 <- addr1 + addr2` | Memory-add |
| `addr1 <- addr1 + M[M[addr2]]` | Memory-add with indirection |
| `if (addr1 != 0) then PC <- addr2` | Conditional branch |
| `r1 <- r1 + r2` | Register add |
| `r <- M[addr]` | Load from memory |
| `M[addr] <- r` | Store to memory |
| `r1 <- M[addr + r2]` | **Indexed** load |
| `M[addr + r2] <- r1` | Indexed store |
| `r <- data` | Immediate load |
| `r1 <- r1 & data` | Immediate AND |
| `ACC <- ACC + M[addr]` | Accumulator machine add |
| `ACC <- M[M[addr]]` | Accumulator indirect load |
| `PC <- addr` | Unconditional jump |
| `r1 <- PC; PC <- addr + r2` | Emulate `call r1, addr(r2)` |

---

## 💾 Assembly Syntax

| Directive / Form | Meaning |
|---|---|
| `org 100h` | Set the assembly location counter. |
| `label:` | Declare a label at the current address. |
| `mnemonic arg1,arg2` | An instruction; matched against your format definitions. |
| `dw 1, 2, 3` | Define word(s) of data. |
| `dw 100 dup(?)` | Reserve 100 words (zero-filled in simulation). |
| `dw 10 dup(5)` | 10 copies of the value `5`. |
| `end` | End of program. |
| `; comment` | Anything after a semicolon is ignored. |
| `100`, `100h`, `0x64`, `0b1100100` | Decimal, hex, hex, binary literals. |
| `label` in an operand | Resolved to the label’s address. |

The assembler runs in **two passes**, exactly as the lecture describes:

1. **Pass 1** — record every label in the symbol table.
2. **Pass 2** — encode each instruction using the symbol table.

---

## 🔬 Worked Examples from the Course

All four examples below can be reproduced **exactly** in Machine Lab.

### Example Machine 3 — Two-address, memory-direct / memory-indirect

**Specifications**

| | |
|---|---|
| Memory | `2¹⁶` cells × 8 bits |
| Word | 16 bits, unaligned, big endian |
| Registers | none |
| Addressing | memory direct, memory indirect |
| Format | `Opcode (8)  ·  addr1 (16)  ·  addr2 (16)` |

**Instruction set (excerpt)**

| Opcode | Mnemonic | Operation |
|---|---|---|
| `00000000` | `mov addr1,addr2` | `addr1 <- M[addr2]` |
| `00000001` | `mov addr1,(addr2)` | `addr1 <- M[M[addr2]]` |
| `00000010` | `mov (addr1),addr2` | `M[M[addr1]] <- M[addr2]` |
| `00000011` | `add addr1,addr2` | `addr1 <- addr1 + addr2` |
| `00000100` | `sub addr1,addr2` | `addr1 <- addr1 - addr2` |
| `00000101` | `add addr1,(addr2)` | `addr1 <- addr1 + M[M[addr2]]` |
| `00000110` | `sub addr1,(addr2)` | `addr1 <- addr1 - M[M[addr2]]` |
| `10000000` | `jnz addr1,addr2` | `if (addr1 != 0) then PC <- addr2` |
| `10000001` | `jz addr1,addr2` | `if (addr1 = 0) then PC <- addr2` |
| `10000010` | `jneg addr1,addr2` | `if (addr1 < 0) then PC <- addr2` |
| `10000011` | `jpos addr1,addr2` | `if (addr1 > 0) then PC <- addr2` |

**Program — alternating Fibonacci sum**

```asm
org 0
loop: add sum,curr      ; add current element to sum
      sub sum,next      ; subtract next element from sum
      add curr,next     ; create the next element in curr
      add next,curr     ; create another next element in next
      sub count,one     ; reduce count by 1
      jnz count,loop    ; if not zero, go to loop
curr:  dw 0
next:  dw 1
sum:   dw 0
count: dw 50
one:   dw 1
end
```

**Listing produced by Machine Lab** (matching the handout exactly):

| Address | Machine Code | Assembly |
|---|---|---|
| `0000` | `030022001E` | `add sum,curr` |
| `0005` | `0400220020` | `sub sum,next` |
| `000A` | `03001E0020` | `add curr,next` |
| `000F` | `030020001E` | `add next,curr` |
| `0014` | `0400240026` | `sub count,one` |
| `0019` | `8000240000` | `jnz count,loop` |
| `001E` | `0000` | `curr:  dw 0` |
| `0020` | `0001` | `next:  dw 1` |
| `0022` | `0000` | `sum:   dw 0` |
| `0024` | `0032` | `count: dw 50` |
| `0026` | `0001` | `one:   dw 1` |

---

### Example Machine 4 — Two-address with registers, 3 formats

**Specifications**

| | |
|---|---|
| Memory | `2¹²` cells × 4 bits |
| Word | 16 bits, unaligned, big endian |
| Registers | `R0…R15`, each 16 bits |
| Addressing | direct, indirect, register direct, register indirect, immediate |

**Formats**

```
Format I    [ Opcode 4 | r1 4 | r2 4 ]
Format II   [ Opcode 4 | r  4 | addr 12 ]
Format III  [ Opcode 4 | r  4 | data 16 ]
```

**Program — vector addition `C ← A + B`**

```asm
org 0
      mov R0,#A        ; R0 points to array A
      mov R1,#B        ; R1 points to array B
      mov R2,#C        ; R2 points to array C
      mov R5,#10       ; loop counter
loop: mov R10,(R0)     ; element of A → R10
      mov R11,(R1)     ; element of B → R11
      add R10,R11      ; R10 ← R10 + R11
      mov (R2),R10     ; store into C
      add R0,#4        ; advance pointer A
      add R1,#4        ; advance pointer B
      add R2,#4        ; advance pointer C
      sub R5,#1        ; decrement counter
      jnz R5,loop      ; loop while counter ≠ 0
A:    dw 10 dup(?)
B:    dw 10 dup(?)
C:    dw 10 dup(?)
end
```

---

### Example Machine 5 — 2/3-address with indexed and immediate

**Specifications**

| | |
|---|---|
| Memory | `2¹⁶` cells × 8 bits |
| Word | 16 bits, unaligned, big endian |
| Registers | `R0…R63`, each 16 bits |
| Addressing | register direct, memory direct, immediate, indexed |

**Formats**

```
Format I    [ Opcode 4 | r1 6 | r2 6 ]
Format II   [ Opcode 4 | r1 6 | r2 6 | addr 16 ]
Format III  [ Opcode 10 | r 6 | data 16 ]
```

**Program — sum of an array of 100 elements**

```asm
org 100h
      xor R0,R0         ; accumulator = 0
      mov R1,R0         ; index register
      mov R2,#200       ; last index for loop control
loop: mov R3,A(R1)      ; load i-th element
      add R0,R3         ; accumulate
      add R1,#2         ; advance index
      jne R1,R2,loop    ; loop until index == 200
      mov sum,R0,R0     ; store result into sum
      call R0,0(R63)    ; return to OS (R63 holds return addr)
sum:  dw 0
A:    dw 100 dup(?)
end
```

Note how `mov r1,r2,addr` and `mov addr,r1,r2` pack *two* transfers into one instruction — Machine Lab handles these naturally because the operation language allows `;`-separated statements:

```
r1 <- r2; r2 <- M[addr]
```

---

### Example Machine 6 — One-address accumulator machine

**Specifications**

| | |
|---|---|
| Memory | `2¹⁶` cells × 4 bits |
| Word | 16 bits, unaligned, big endian |
| Special register | `ACC` (accumulator) |
| Addressing | implied, direct, indirect, immediate |
| Format | `Opcode (4) · addr/data (16)` |

**Instruction set (excerpt)**

| Opcode | Mnemonic | Operation |
|---|---|---|
| `0000` | `load #data` | `ACC <- data` |
| `0001` | `add #data` | `ACC <- ACC + data` |
| `0010` | `load addr` | `ACC <- M[addr]` |
| `0011` | `store addr` | `M[addr] <- ACC` |
| `1001` | `load (addr)` | `ACC <- M[M[addr]]` |
| `1010` | `store (addr)` | `M[M[addr]] <- ACC` |
| `1011` | `j addr` | `PC <- addr` |
| `1101` | `jnz addr` | `if (ACC != 0) then PC <- addr` |

Modelling this in Machine Lab is a matter of declaring a special register named `ACC` and writing operations like `ACC <- ACC + M[addr]`.

**Program — first 20 Fibonacci numbers**

```asm
org 0
loop: load (pointer_1)
      store sum
      load (pointer_2)
      add sum
      store (pointer_3)
      load pointer_1
      add #4
      store pointer_1
      load pointer_2
      add #4
      store pointer_2
      load pointer_3
      add #4
      store pointer_3
      load counter
      add #-1
      store counter
      jnz loop
      j OS_return_addr

pointer_1: dw array
pointer_2: dw array+4
pointer_3: dw array+8
counter:   dw 18
sum:       dw ?
array:     dw 0, 1, 18 dup(?)
end
```

---

## 📤 Output: The Listing Table

The **“۲ · Program & Compile”** tab shows two panes side by side:

1. **Assembly editor** (left) — monospace, LTR, with syntax-friendly hints below.
2. **Machine-code listing** (right) — the classic three-column table:

```
┌─────────┬──────────────────┬───────────────────────┐
│ Address │  Machine Code    │  Assembly Program     │
├─────────┼──────────────────┼───────────────────────┤
│ 0019    │ 8000240000       │ jnz count,loop        │
│         │ [Opcode:80]      │                       │
│         │ [addr1:0024]     │                       │
│         │ [addr2:0000]     │                       │
└─────────┴──────────────────┴───────────────────────┘
```

Under each machine-code word you get **coloured bit-field chips** — `Opcode` in purple, `reg` in mint, `addr` in peach, `imm` in blue — so you can visually decode every instruction, just like the boxes in the slides.

Below the listing there's a full **Symbol Table** with each label and its hex address.

Errors are shown **inline** with a red row background and a Persian explanation of exactly what went wrong.

---

## 🎮 Simulation Mode

The **“۳ · Simulator”** tab gives you a real machine:

- **Controls** — *Step*, *Run to completion* (with 100 000-step infinite-loop guard), *Reset*.
- **Special registers** — `PC`, `ACC`, `SP`, … rendered as live hex chips; `PC` is highlighted.
- **General registers** — the full register file in hex.
- **Memory dump** — an 8-column hex grid that:
  - highlights the cell the **PC** points to,
  - highlights cells that **changed since load** in teal.
- **Execution log** — the last 60 executed instructions, with address and source line.

Simulation stops cleanly when:
- The program runs off the end of the code segment → *“Program finished: PC is not on an instruction.”*
- An unknown opcode is fetched → *“Invalid opcode at address XXXX.”*
- An operation throws → *“Runtime error: …”*

---

## 💾 Persistence & Themes

- **Machines** are automatically saved to `localStorage` under the key `machinelab.v1`.
- The header lets you **create**, **duplicate**, **rename**, and **delete** machines, and switch between them with a dropdown.
- **Theme toggle** (🌓) cycles between light and dark, respecting `prefers-color-scheme` on first load.

---

## 🗂️ File Layout

```
machine-lab.html        ← the entire application
README.md               ← you are here
```

Everything — UI, CSS, assembler, simulator, storage — lives in the single HTML file. No bundler, no node_modules, no build step. Just open it.

---

## 🙏 Credits

<div align="center">

**Course:** Computer Structure & Language — Lecture 3: Registers, Addressing Modes, Linker, Loader
**Instructor:** Dr. Hamid Sarbazi-Azad
**Institution:** Sharif University of Technology (SUT)

</div>

Machine Lab was created as a study companion for the above course. It is an independent, unofficial project and is not affiliated with or endorsed by the university or the instructor. Its purpose is to turn the lecture's paper-based exercises — machine specification → instruction formats → assembly program → machine-code translation → simulation — into a live, editable, and verifiable browser experience.

Fonts by [Vazirmatn](https://github.com/rastikerdar/vazirmatn) and [JetBrains Mono](https://www.jetbrains.com/lp/mono/).

---

<div align="center">

**If Machine Lab helped you learn, star the repo ⭐**

*Design a machine. Write a program. Watch it run.*

</div>
```
