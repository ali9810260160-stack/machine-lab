<div align="center">

# ⚙️ Machine Lab

**Design your own machine, write assembly for it, and watch it run — all in a single HTML file.**

**English** · [فارسی](README.fa.md)

![version](https://img.shields.io/badge/version-1.2.0-6d5efc)
![license](https://img.shields.io/badge/license-MIT-blue)
![runtime](https://img.shields.io/badge/runtime-browser-12b5a0)
![dependencies](https://img.shields.io/badge/dependencies-none-success)
![ui](https://img.shields.io/badge/UI-English%20%7C%20فارسی-orange)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="pics/main-page-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="pics/main-page-light.png">
  <img alt="Machine Lab — the Define machine tab" src="pics/main-page-light.png" width="920">
</picture>

</div>

## Table of contents

1. [Overview](#overview)
2. [Features and versions](#features-and-versions)
3. [Getting started](#getting-started)
4. [Interface tour](#interface-tour)
5. [Defining a machine](#defining-a-machine)
6. [The Operation language](#the-operation-language)
7. [The assembly language](#the-assembly-language)
8. [Simulator](#simulator)
9. [Graphic simulation (CPU animation and memory lab)](#graphic-simulation-cpu-animation-and-memory-lab)
10. [Slide export (PNG)](#slide-export-png)
11. [Export / Import](#export--import)
12. [SQLite storage](#sqlite-storage)
13. [Bundled machines](#bundled-machines)
14. [Walkthrough: a one-address machine](#walkthrough-a-one-address-machine)
15. [Architecture](#architecture)
16. [Limitations](#limitations)
17. [Troubleshooting / FAQ](#troubleshooting--faq)
18. [Changelog](#changelog)
19. [Contributing](#contributing)
20. [License](#license)

---

## Overview

**Machine Lab** is a teaching tool for *Computer Structure and Language* courses. Such courses usually introduce a hypothetical machine ("Example Machine 3/4/5/6"): memory size, word size, registers, instruction formats, and a table of instructions. Students then write assembly by hand and translate it to machine code on paper.

Machine Lab automates exactly that workflow:

- **You define the machine.** Parameters, any number of instruction formats, and for every format its instructions: opcode, syntax and behaviour.
- **The Operation column is executable.** The behaviour of an instruction (e.g. `M[addr1] <- M[addr1] + M[addr2]`) is written in a small language that the app parses and runs.
- **You write assembly for *your* machine** and see, right next to it, the address and the machine code of every line, **in hexadecimal**, laid out like the tables in the lecture notes.
- **You run the program step by step**, watching registers, memory and the PC change.
- **You watch the machine work** *(new in 1.2.0)*: an animated CPU with MAR, MBR, the memory decoder, PC, IR, CU and ALU shows every fetch, decode and execute phase, together with the six internal paths of the von Neumann model.
- **You export lecture-style slides** (PNG), export/import machines as JSON, or persist everything in a SQLite file.

The whole app is one file, `machine-lab.html`. It has no dependencies and needs no build step (only the web fonts come from Google Fonts, with local fallbacks).

> **Verified against the lecture.** For Example Machine 3, the first line of the sample program (`add sum,curr`) assembles to `030022001E` at address `0000`, exactly as in the course slides; Machines 4 and 5 reproduce the slides too. Every bundled sample program was also assembled and run headlessly to check its result (see [Bundled machines](#bundled-machines)).

---

## Features and versions

| Feature | Description | Since |
|---|---|:---:|
| Custom machines | Memory unit, address width, word size, big/little endian, number and size of registers, register prefix, special registers (e.g. `ACC:16`) | 1.0.0 |
| Unlimited instruction formats | Each format is a list of named fields with a bit width and a type (`opcode`, `reg`, `addr`, `imm`) | 1.0.0 |
| Instruction tables | Opcode, Mnemonic/Syntax and Operation columns with live validation | 1.0.0 |
| Operation language | Parsed and executed: assignment, memory, conditions, arithmetic and logic | 1.0.0 |
| Two-pass assembler | Labels, `org`, `dw`, `dup`, `?`, `end`, simple expressions, symbol table | 1.0.0 |
| Hex output | Address / Machine Code / Assembly Program columns with colour-coded fields | 1.0.0 |
| Format diagrams | Proportional field boxes, like the lecture slides | 1.0.0 |
| Simulator | Step / Run / Reload, registers, hex memory view, instruction log | 1.0.0 |
| Machine management | New, copy, delete, switch; automatic saving in `localStorage` | 1.0.0 |
| Lecture machines | Example Machine 3, 4 and 5 with sample programs | 1.0.0 |
| Light / dark theme | Follows the system setting, with a manual toggle | 1.0.0 |
| Slide export (PNG) | English slides: machine overview, one slide per format with its instruction table, and a register-size slide with explanations | 1.1.0 |
| Bilingual UI | Switch between Persian and English | 1.1.0 |
| Famous machines | IBM 360/370, Intel 8086/8088, RISC-V RV32I, an educational GPU core | 1.1.0 |
| Export / Import | Save and restore a machine (with its program) as JSON | 1.1.0 |
| SQLite persistence | `server.py` keeps a `machines.db` file next to the app and saves continuously | 1.1.0 |
| Several opcode fields per format | For ISAs such as RISC-V and x86 (`funct3`/`funct7`, ModRM) | 1.1.0 |
| Custom register names | e.g. `AX,CX,DX,BX,SP,BP,SI,DI` | 1.1.0 |
| Hardwired zero register | For architectures like RISC-V (`x0 = 0`) | 1.1.0 |
| `sext(x,n)` in Operation | Sign extension of immediates | 1.1.0 |
| `$` in assembly | Current address, for relative jumps | 1.1.0 |
| **Simulator view modes** | The Simulator tab now has three views: Table, CPU animation, Memory lab | **1.2.0** |
| **Animated instruction cycle** | Fetch → decode → execute drawn on a CPU diagram (PC, IR, CU, ALU, registers, MAR, MBR, memory decoder), with data packets travelling along the buses | **1.2.0** |
| **Von Neumann paths 1–6** | Every path is colour-coded, lit while it is in use, explained in a side panel, and can be replayed on its own | **1.2.0** |
| **Memory lab** | Lecture-style memory with MAR, MBR, decoder and Read/Write lamps; Write/Read of any address, the slide examples `M10 ← (M12)` and `M(M0) ← (M0) + (M(M4))` | **1.2.0** |
| **Micro-step, pause, speed** | Advance every data movement with one click, pause, run continuously, skip to the end, 0.25×–3× speed | **1.2.0** |
| **Execution trace** | The engine records which registers, memory cells and ALU operations each instruction touches, which drives the animation | **1.2.0** |
| **Fully bilingual graphics** | Every label, explanation and button of the new views follows the EN / فا switch | **1.2.0** |

---

## Getting started

### Option A — browser only

Open `machine-lab.html` in a modern browser. Data is kept in the browser's `localStorage`.

> `localStorage` belongs to a browser *and* an address. Opening the file directly (`file://…`) and opening it through `http://localhost:8000` give two separate stores. Use [Export / Import](#export--import) to move machines between them.

### Option B — with the SQLite database (since 1.1.0)

Requires Python 3 (standard library only — nothing to install).

```bash
# machine-lab.html and server.py must sit in the same folder
python server.py        # on Windows you can also use:  py server.py
# then open  http://localhost:8000
```

`machines.db` is created next to `server.py` and updated automatically after every change. When the server is reachable, a **SQLite ✓** badge appears in the toolbar.

<div align="center">

![Folder layout: machine-lab.html, machines.db and server.py in one folder](pics/sqlite-and-python-runner.png)

*The three files side by side — the database (`machines`, shown without its `.db` extension by the file manager) is created by the server.*

</div>

Recommended repository layout:

```text
.
├── machine-lab.html   # the whole app (UI + assembler + simulator + animations)
├── server.py          # optional tiny local server that stores data in SQLite
├── machines.db        # generated by server.py — add it to .gitignore
├── pics/              # screenshots used by this README
├── README.md
├── README.fa.md
└── LICENSE
```

---

## Interface tour

The interface has three tabs; the toolbar holds the machine selector and tools.

| Tab | Purpose |
|---|---|
| **1 · Define machine** | Parameters, formats, fields and instruction tables. Format diagrams and the register sizes (MAR, MBR, IR, PC) update live. |
| **2 · Program & compile** | Assembly editor on one side, hex listing and symbol table on the other. Recompiles as you type. |
| **3 · Simulator** | Three views of the running program: a **Table** (registers, memory, log), a **CPU animation** and a **Memory lab**. |

| Toolbar control | Action |
|---|---|
| Machine selector | Switch between saved machines |
| `+ New machine` | Create an empty machine with one sample format |
| `Copy` / `Delete` | Duplicate or remove the current machine (at least one machine always remains) |
| 🌓 | Toggle light / dark theme |
| `EN` / `فا` | Switch the UI language |
| `⬇ Export` / `⬆ Import` | JSON export / import |
| `🖼 Slides` | Generate PNG slides |

**Light and dark themes** (the theme follows your OS; 🌓 overrides it):

<table>
<tr>
<td width="50%"><img src="pics/main-page-dark.png" alt="Dark theme"></td>
<td width="50%"><img src="pics/main-page-light.png" alt="Light theme"></td>
</tr>
</table>

**Bilingual interface** — the same screen in English (the Persian version is shown above):

<div align="center">

<img src="pics/two-lang-Persian%20%26%20English.png" alt="The English interface, with the language toggle in the toolbar" width="860">

</div>

> The layout switches between right-to-left (Persian) and left-to-right (English) automatically. Code, hex values and field names are always left-to-right. Since 1.2.0 the graphic simulation views are translated as well.

---

## Defining a machine

### Parameters

| Parameter | Meaning | Example (Machine 4) |
|---|---|---|
| Machine name | Display name; also used on the slides | `Example Machine 4` |
| Memory unit size | Bits per addressable memory unit | `4` |
| Address width | Address bits; memory has 2ⁿ units | `12` |
| Word size | Bits per word; must be a multiple of the unit size | `16` |
| Byte order | `big` or `little` (how words are read/written in memory) | `big` |
| General registers | May be `0` | `16` |
| Register size | Bits per general register | `16` |
| Register prefix | Registers are written `prefix + number` (e.g. `R5`). An empty prefix means plain numbers (IBM style) | `R` |
| Special registers | `name:bits` list, e.g. `ACC:16, SP:16`. `PC` always exists | — |
| Register names *(1.1.0)* | When filled in, replaces prefix-based naming; registers are named in list order (e.g. `AX,CX,DX,BX,SP,BP,SI,DI`) | — |
| Hardwired zero register *(1.1.0)* | If `1`, register 0 is reset to zero after every instruction (like RISC-V `x0`) | `0` |

The register sizes of the machine are computed and displayed automatically (the same reasoning as in the lecture):

| Register | Size | Why |
|---|---|---|
| **MAR** | address width | holds a memory address |
| **MBR** | word size | holds one word transferred per memory access |
| **IR** | longest instruction format | must hold the longest instruction |
| **PC** | address width | points to the next instruction in memory |
| **R0…Rn** | register size | one operand |

### Formats and fields

An instruction format is an ordered list of **fields** (left to right, most significant bit first). Each field has:

| Property | Description |
|---|---|
| Name | e.g. `r1`, `addr2`, `data`. Used in the Syntax and Operation columns |
| Bits | Field width |
| Type | `opcode`, `reg` (register number), `addr` (address / label), `imm` (immediate value) |

Rules:

- Every format needs at least one `opcode` field.
- **The total width of a format must be a multiple of the memory unit size.** With 4-bit units, a 20-bit format occupies 5 units.
- Since 1.1.0 a format may contain **several `opcode` fields**; the instruction's opcode value is the **concatenation of those fields in order** (e.g. `funct7 | funct3 | opcode` in RISC-V).
- `addr` and `imm` behave identically in the assembler (number or label); the difference is conceptual and shown by colour in the diagram.

### Instructions

Every instruction has three columns:

| Column | Content | Example |
|---|---|---|
| **Opcode** | A binary string (`00000101`) or hex with `0x` (`0x05`). It must fit the combined width of the opcode fields | `00000101` |
| **Mnemonic / Syntax** | The template used to write the instruction in assembly | `add addr1,(addr2)` |
| **Operation** | The behaviour, in the [Operation language](#the-operation-language) | `M[addr1] <- M[addr1] + M[M[addr2]]` |

#### Writing the Syntax

1. The first word is the mnemonic (case-insensitive).
2. Any identifier that equals the name of a **non-opcode field** is an **operand**.
3. Every other character (`#`, `(`, `)`, `,`) must appear **literally** in the program. This is how addressing modes are expressed.
4. Whitespace inside operands is ignored.

| Syntax | Addressing mode | Written in a program as |
|---|---|---|
| `mov r1,r2` | Register direct | `mov R1,R2` |
| `mov r,addr` | Memory direct | `mov R1,var` |
| `mov r1,(r2)` | Register indirect | `mov R10,(R0)` |
| `mov addr1,(addr2)` | Memory indirect | `mov a,(p)` |
| `mov r,#data` | Immediate | `mov R5,#10` |
| `mov r1,addr(r2)` | Indexed | `mov R3,A(R1)` |
| `L r1,d2(x2,b2)` | Base + index + displacement | `L 2,NUM(0,0)` |

> When several syntaxes could match one source line, the one with the **most literal characters** wins, provided its operands are valid (a real register, a number, or a defined label). That is why `mov R1,R2` is never confused with `mov r,addr`.

---

## The Operation language

The Operation column is a small language. It is parsed when you define the instruction (errors appear under the row) and executed by the simulator.

### Statements

```text
statement ; statement ; ...
```

| Kind | Form | Example |
|---|---|---|
| Assignment | `target <- expression` (or `←`) | `r1 <- r1 + r2` |
| Conditional | `if condition then statement` (`then` optional) | `if (r != 0) then PC <- addr` |
| Halt | `halt` | `halt` |

### Targets (left of `<-`)

| Target | Meaning |
|---|---|
| a `reg`-type field name | that register (e.g. `r1`) |
| `R[expr]` | the register whose number is computed |
| `M[expr]` or `M(expr)` | one **word** of memory at the given address |
| `PC` | the program counter |
| a special register | e.g. `ACC` |

### Expressions

| Element | Description |
|---|---|
| number | decimal `42`, hex `0x2A` or `2Ah` (must start with a digit) |
| `reg` field name | the **contents** of that register (e.g. `r2`) |
| `addr` / `imm` field name | the numeric value of the field in the instruction |
| `M[e]` | the word stored at address `e` |
| `R[e]` | contents of register number `e` |
| `PC`, special register | its contents |
| `sext(x,n)` | *(1.1.0)* sign-extend `x`, treating it as an `n`-bit signed value |
| `( … )` | grouping; the lecture style `(r1)+(r2)` is valid too |

**Operators** (highest to lowest precedence):

| Precedence | Operator |
|:---:|---|
| 1 | `-` (unary), `~` |
| 2 | `*` |
| 3 | `+`, `-` |
| 4 | `&` (or `∧`) |
| 5 | `^` (or `⊕`) |
| 6 | `\|` (or `∨`) |

**Conditions** use `=`, `==`, `!=` (or `≠`), `<`, `>`, `<=`, `>=`. Comparisons are **signed**, using the machine's word size. A condition that is just an expression means "not zero". A parenthesised comparison evaluates to `1` or `0` and can be assigned:

```text
ZF <- (rm = 0)
```

### Execution rules

- **The PC already points to the next instruction while an instruction executes.** So `r1 <- PC` (a `call`) saves the return address, and PC-relative jumps are computed from the updated PC.
- Results are truncated to the size of the target: general registers to the register size, `M[..]` to the word size, `PC` to the address width, special registers to their declared size.
- Negative values are stored in two's complement.
- Unknown names, assignments to non-register fields and unbalanced parentheses are reported when the instruction is defined.

### Examples

| Instruction | Operation |
|---|---|
| `mov addr1,(addr2)` (Machine 3) | `M[addr1] <- M[M[addr2]]` |
| `jnz addr1,addr2` | `if (M[addr1] != 0) then PC <- addr2` |
| `mov r1,r2,addr` (Machine 5) | `r1 <- r2; r2 <- M[addr]` |
| `call r1,addr(r2)` | `r1 <- PC; PC <- addr + r2` |
| `xor r1,r2` | `r1 <- r1 ⊕ r2` |
| `addi rd,rs1,imm` (RISC-V) | `rd <- rs1 + sext(imm,12)` |
| `jnz disp` (8086) | `if (ZF = 0) then PC <- PC + sext(disp,8)` |

---

## The assembly language

### Line format

```text
[label:] [instruction or directive] [; comment]
```

- At most one label per line; a label may stand alone on its line.
- Labels are case-insensitive.
- Everything after `;` is a comment.

### Directives

| Directive | Effect | Example |
|---|---|---|
| `org address` | sets the location counter | `org 100h` |
| `dw value, ...` | defines one or more **words** | `dw 1,2,3` |
| `dw N dup(value)` | N words with the same value | `dw 10 dup(5)` |
| `?` | undefined value (stored as zero, shown as `????`) | `dw 100 dup(?)` |
| `end` | stops assembly | `end` |

> `dw` always reserves **one machine word**. On Machine 4 (16-bit word, 4-bit unit) each `dw` takes 4 units.

### Numbers and expressions

| Form | Example |
|---|---|
| decimal | `200` |
| hex with `h` suffix (must start with a digit) | `100h`, `0Ah` |
| hex with `0x` prefix | `0x64` |
| binary | `0b101` |
| label | `loop`, `A` |
| current address *(1.1.0)* | `$` |

`addr` / `imm` operands may be sums and differences of numbers, labels and `$`, such as `array+4` or `L1-$-2`. The value must fit the field (from `-2^(b-1)` to `2^b-1`); negative values are encoded in two's complement, otherwise a "does not fit" error is reported.

### How it assembles (two passes)

1. **Pass 1** — collects labels (building the symbol table), decides the size and address of every line, and determines which syntax each instruction line matches.
2. **Pass 2** — evaluates the fields, concatenates them, converts to **hex** and writes the memory image.

### Output

| Column | Content |
|---|---|
| **Address** | hex address, padded to the machine's address width |
| **Machine Code** | hex machine code; the fields are shown below it as colour-coded chips (`opcode` / `reg` / `addr` / `imm`) |
| **Assembly Program** | the source line; an error message appears under it when something is wrong |
| **Symbol Table** | every label with its hex address, as in the lecture notes |

### Worked example — IBM 360/370

<div align="center">

<img src="pics/coding-and-assembling.png" alt="Assembly source on the right and the hex listing with symbol table on the left" width="900">

</div>

Reading the listing:

- `L 2,NUM(0,0)` is an **RX** instruction (4 bytes): `58 | 2 | 0 | 0 | 012` → `58200012`. The `012` is the address of `NUM`, taken from the symbol table.
- `AR 2,3` is an **RR** instruction (2 bytes): `1A | 2 | 3` → `1A23`. Notice that the next instruction starts at `00000A`, not `00000C`.
- `NUM: dw 41` becomes `00000029` (41 in hex) at address `000012`, and `RES: dw ?` shows `????????`.
- The coloured chips under each machine code word show how the bits split into fields.

---

## Simulator

The **Simulator** tab has three views, chosen with the buttons at its top. All of them run the same engine on the same program and machine state, so you can switch between them freely; the animation views continue from the current machine state.

| View | What it is for |
|---|---|
| **📋 Table** | Fast execution with registers, hex memory and an instruction log |
| **🎬 CPU · memory · paths animation** | Watching one instruction at a time travel through the machine |
| **🧪 Memory lab** | Understanding MAR, MBR, the decoder and the Read/Write signals on a small memory |

### Table view

- **↺ Reload** compiles the program again, loads it into memory, clears the registers and puts the PC on the first instruction.
- **Step ▸** executes one instruction.
- **Run ⏵** runs until the program stops (capped at 100,000 steps to catch infinite loops).

**Execution cycle.** The instruction is **fetched from memory** and decoded by its opcode — not taken from the source text. That is why self-modifying code works (like the slide-16 example of the lecture that edits an address field).

**Stop conditions:**

- the PC is not on the start of an assembled instruction (end of program — "return to the OS");
- a `halt` statement runs;
- the opcode is invalid, or a runtime error occurs;
- 100,000 steps are exceeded.

<div align="center">

<img src="pics/memory-simulation.png" alt="The simulator after three steps: PC, registers, memory dump and executed instructions" width="900">

</div>

The screenshot shows the IBM 360/370 sample after **3 steps**:

- the log lists the three executed instructions (`L 2,NUM(0,0)`, `L 3,ONE(0,0)`, `AR 2,3`);
- the **PC** is `00000A`, and the memory cell it points to (`5A`, the opcode of `A`) is highlighted;
- **R2 = 0000002A** (41 + 1) and **R3 = 00000001**;
- cells that differ from the initial memory image are coloured, and the memory table shows 8 units per row (at most 1024 units around the program).

---

## Graphic simulation (CPU animation and memory lab)

*(since 1.2.0)* Based on the von Neumann model of the lecture (memory access through MAR/MBR, instruction format, and the internal paths of the machine).

### 🎬 CPU · memory · paths animation

The stage shows, for the selected machine:

- **CPU:** the control unit (CU) with its decoder and the current instruction split into its colour-coded fields, **PC**, **IR**, the **ALU** with inputs A / B and a result register, the general-register file (first 16 registers drawn) and the special registers.
- **Memory interface:** **MAR** and **MBR**, the address bus, the data bus and the **decoder** that turns an address into one selected memory unit.
- **Main memory:** a 12-unit window that follows the active address, showing hex values, labels and instructions beside the cells, the **READ / WRITE** lamps, and the selected row lit by the decoder.
- **I/O devices** connected through paths 3, 5 and 6.

Press **▶ Run one instruction** and the app animates the whole cycle for the instruction at the PC. Small coloured packets carry values along the wires while the explanation panel narrates each step and the step log keeps a history:

1. **Fetch** — `MAR ← (PC)`; the address goes to the decoder; **Read**; the word travels to MBR and then to IR. An instruction longer than the access width is fetched in several accesses. Finally `PC ← PC + length`.
2. **Decode** — the opcode is matched against the instruction table; CU shows the mnemonic, the operation, the format, the length, the addressing mode, and the fields with their values.
3. **Execute** — follows exactly what the Operation column does: register and special-register operands go to the ALU, immediates come straight from IR (path 4), memory operands are read through MAR → decoder → Read → MBR → ALU (direct and indirect modes are shown, including the extra memory read of indirect addressing and the ALU computing an effective address), CU sends the command to the ALU (path 3), and the result is written back to a register, to PC, or to memory through MBR → Write.

| Control | Action |
|---|---|
| **▶ Run one instruction** | Animates one complete instruction |
| **⏵ Run continuously** / **⏹ Stop** | Keeps executing instructions until the program ends or you stop it |
| **⏸ Pause / ▶ Resume** | Freezes the animation without losing its place |
| **Micro-step** + **Next micro-step ▸** | Each data movement waits for your click |
| **⏩ Skip to end** | Runs the rest of the program instantly (no animation) |
| **↺ Reset** | Reloads the program |
| **Speed** slider | 0.25× – 3× |

#### The six internal paths

The panel next to the stage lists the paths of the von Neumann model, each with its own colour and number. A path lights up (wires, badge and panel entry) whenever the animation uses it, and every entry has a **▶ Show path** button that replays it on its own without changing the machine state.

| # | Path | What happens |
|:---:|---|---|
| 1 | Fetching instructions | memory → MBR → IR / CU; address from PC via MAR |
| 2 | Data access | memory ↔ MBR ↔ ALU / registers |
| 3 | Command / status communication | CU → ALU (operation code), CU ↔ I/O (command, status) |
| 4 | Special data access (immediate) | IR / CU → ALU, no memory access |
| 5 | I/O data via the CPU | device ↔ CPU registers (in / out) |
| 6 | I/O data by DMA | device ↔ memory directly, the CPU stays free |

> Paths 5 and 6 are shown for completeness: the bundled machines have no I/O instructions, so these two are only visible through **Show path**.

### 🧪 Memory lab

A small standalone memory (8, 16 or 32 units of 16 bits, chosen by *address width*) reproducing the lecture's memory examples:

- **Write** — enter an address and a datum: `MAR ← address`, `MBR ← datum`, the decoder selects the unit, the **Write** lamp lights and the value is stored.
- **Read** — `MAR ← address`, decoder, **Read** lamp, the content flows into MBR.
- **Slide examples** — `M10 ← (M12)` (a read followed by a write) and `M(M0) ← (M0) + (M(M4))` (two reads, an indirect read through MBR → MAR, the ALU, and a write to an address that came from memory). The notation line under the figure shows the current operation in lecture notation.
- Click any memory unit to edit its value. Micro-step, pause and speed work here too.

The initial memory contents are `M[i] = 10 + i`.

---

## Slide export (PNG)

*(since 1.1.0)* The **🖼 Slides** button builds lecture-style slides in **English** for the current machine:

| Slide | Content |
|---|---|
| 1 | Machine name, specification (memory, word, registers, special registers) and a diagram of every format |
| 2 … N-1 | One slide per format: the format diagram and the Opcode / Mnemonic / Operation table |
| N (last) | Sizes of MAR, MBR, IR, PC, general and special registers, **each with the reason for its value** |

<div align="center">

<img src="pics/save-as-some-slides-with-png-type.png" alt="The slide preview overlay showing the first slide of the IBM 360/370 machine" width="900">

</div>

Click a slide to download it, or use **Download all (PNG)** (1280×720 images). If your browser blocks multiple downloads, allow them for the page.

Notes:

- Operator symbols are drawn in lecture style: `<-` → `←`, `!=` → `≠`, `&` → `∧`, `|` → `∨`, `^` → `⊕`.
- Slide 1 always says `unaligned`: machines in this app always have unaligned memory.
- Formats with more than about 11 instructions get a smaller table font automatically.
- Slides are drawn with `canvas.roundRect`, so a reasonably recent browser is required.

---

## Export / Import

*(since 1.1.0)*

- **⬇ Export** saves the current machine, including its program, as `<name>.machine.json`. Characters other than letters, digits and `_` in the name become `_` (see [Troubleshooting](#troubleshooting--faq)).
- **⬆ Import** reads a JSON file containing **one machine** or **an array of machines**. Machines are always added with a fresh id, so nothing is overwritten.

<div align="center">

<img src="pics/import-and-export-machines.png" alt="After clicking Export, the browser shows the downloaded IBM_360_370.machine.json" width="860">

</div>

File format:

```jsonc
{
  "name": "Example Machine 3",
  "u": 8,            // memory unit size (bits)
  "a": 16,           // address width (bits)
  "w": 16,           // word size (bits)
  "en": "big",       // "big" | "little"
  "rc": 0,           // number of general registers
  "rb": 16,          // register size (bits)
  "rp": "R",         // register prefix
  "rn": "",          // register names (optional)
  "z": 0,            // hardwired zero register: 0 | 1
  "sp": "",          // special registers, e.g. "ACC:16"
  "fm": [
    {
      "n": "Format I",
      "f": [ { "n": "Opcode", "b": 8,  "t": "opcode" },
             { "n": "addr1",  "b": 16, "t": "addr"   } ],
      "i": [ { "o": "00000000", "s": "mov addr1,addr2", "op": "M[addr1] <- M[addr2]" } ]
    }
  ],
  "code": "org 0\n..."
}
```

> Real JSON has no comments — the `//` notes above are only for explanation.

---

## SQLite storage

| Mode | Where data lives | When |
|---|---|---|
| Browser | `localStorage`, key `machinelab.v1` | the HTML file is opened directly |
| Server | the `machines.db` file (plus `localStorage`) | started with `python server.py` |

`server.py` exists because a web page cannot write files next to itself for security reasons; this tiny local server does it on the page's behalf.

**Tables:**

```sql
machines(id TEXT PRIMARY KEY, name TEXT, pos INTEGER, data TEXT)  -- data = the machine as JSON
settings(k TEXT PRIMARY KEY, v TEXT)                             -- k='cur' → active machine
```

**How it works.** On start-up the page calls `GET /api/state`. If the server answers, the **SQLite ✓** badge appears; a non-empty database is loaded, otherwise the default machines are written into it. Every change is stored about 300 ms later with `PUT /api/state`. If the server is not reachable the app silently keeps using `localStorage`.

**Notes:**

- The server listens on `127.0.0.1:8000` only (not reachable from the network). To change the port, edit the last line of `server.py`.
- The UI language is stored in `localStorage`, not in the database.
- Each save rewrites the whole `machines` table, so with two tabs open the last save wins.
- Machines created in plain-browser mode are not migrated automatically — export them and import them in server mode.
- The animation state (selected simulator view, speed, memory-lab contents) is not saved.

---

## Bundled machines

| Machine | Since | Description | Verified sample result |
|---|:---:|---|---|
| Example Machine 3 | 1.0.0 | Two-address, 2¹⁶×8 memory, 16-bit word, memory direct/indirect, conditional jumps. Sample: alternating Fibonacci | first instruction `030022001E` @ `0000` |
| Example Machine 4 | 1.0.0 | 4-bit units, 16 registers, three formats, register/memory direct and indirect, immediate. Sample: vector add `C = A + B` | `D00041` @ `0000`; vector `C` computed |
| Example Machine 5 | 1.0.0 | 64 registers, indexed addressing, three formats (4- and 10-bit opcodes), `call`. Sample: sum of a 100-element array | first instructions `5000`, `0040` @ `0100`, `0102` |
| IBM 360/370 | 1.1.0 | 24-bit addresses, 32-bit word, 16 registers; RR (`LR`, `AR`, `SR`) and RX (`L`, `ST`, `A`, `S`) with `D2(X2,B2)` | `RES` = `0000002B` (R2 = 2B) |
| Intel 8086/8088 (simplified) | 1.1.0 | registers `AX…DI`, `ZF` flag, ModRM encoding for `mov/add/sub`, `inc/dec`, relative `jz/jnz` | `AX` = `000F`, `ZF` = 1 |
| RISC-V RV32I (subset) | 1.1.0 | 32 registers `x0..x31` with `x0 = 0`; R, I and U formats | `addi x1,x0,5` → `00500093`; `x5` = `0001E240` |
| GPU core (SIMT, educational) | 1.1.0 | an educational core with `fma`, `tid`, `ld/st` and `bnz` | `R4` = `00000028` |

> Machine 6 (the one-address ACC machine of the lecture) is not bundled, but it can be defined with this tool — see the next section.

### Accuracy notes for the 1.1.0 machines

- **IBM 360/370:** the rule "register 0 as base/index means *no register*" is not implemented; the contents of R0 (zero at start-up) are used.
- **8086/8088:** a simplified subset. Immediates are encoded big-endian (the real chip is little-endian) and memory segmentation is not modelled.
- **RISC-V:** only the R, I and U formats. S/B/J instructions (`sw`, `beq`, `jal`, …) are missing because their immediates are split across several fields, which the current engine cannot express. Instruction bytes are laid out big-endian, and the hex shown is the 32-bit instruction word as printed in the ISA manual.
- **GPU:** not a real ISA; it has no warps or parallel lanes and behaves like a single-threaded core.

---

## Walkthrough: a one-address machine

A subset of the lecture's *Example Machine 6* (an accumulator machine).

**1. Parameters** (`+ New machine`):

| Parameter | Value |
|---|---|
| Memory unit | `4` |
| Address width | `16` |
| Word | `16` |
| General registers | `0` |
| Special registers | `ACC:16` |

**2. One format** with the fields `Opcode` (4 bits, `opcode`) and `addr` (16 bits, `addr`) — 20 bits in total, i.e. 5 units.

**3. Instructions:**

| Opcode | Syntax | Operation |
|---|---|---|
| `0000` | `load #addr` | `ACC <- addr` |
| `0001` | `add #addr` | `ACC <- ACC + addr` |
| `0010` | `load addr` | `ACC <- M[addr]` |
| `0011` | `store addr` | `M[addr] <- ACC` |
| `0100` | `add addr` | `ACC <- ACC + M[addr]` |
| `1101` | `jnz addr` | `if (ACC != 0) then PC <- addr` |

**4. Program** (sums 5+4+3+2+1):

```asm
org 0
loop:  load sum        ; ACC <- sum
       add  cnt        ; ACC <- ACC + cnt
       store sum
       load cnt
       add  #-1        ; cnt - 1 (two's complement)
       store cnt
       jnz  loop       ; repeat while ACC != 0
sum:   dw 0
cnt:   dw 5
end
```

**5. Run** it in the **Simulator** tab. When it stops, `sum` holds `000F` (15) — the stop happens because the PC leaves the last instruction and enters the data area. The first listing line is `20023` at address `0000`: opcode `2` followed by the address of `sum` (`0023`). Switch to **🎬 CPU animation** and run the first instruction to watch `load sum` fetch itself, decode, read `sum` through MAR/decoder/MBR and load it into `ACC`.

---

## Architecture

The app is a single HTML file with no framework and no build step:

| Part | Role |
|---|---|
| `prep(m)` | prepares the instructions: builds a regex per syntax, parses opcodes, parses Operation into an AST |
| `parseOp` | tokenizer and recursive-descent parser of the Operation language |
| `ev` / `exec` | expression evaluation and statement execution on the machine state; while an instruction runs they also append events (register / special-register / memory reads and writes, ALU operations, branches) to an **execution trace** |
| `compile(m)` | the two-pass assembler; produces listing rows, the symbol table and the memory image |
| `step1` | fetch, decode (from memory) and execute; stores the last instruction and its trace for the animation |
| `slides(m)` | draws the slides on a `<canvas>` |
| `cpuSVG` / `labSVG` | build the SVG scenes (CPU, memory interface, lab) |
| `fetchPhase` / `decodePhase` / `execPhase` | replay one instruction as a sequence of micro-steps, driven by the trace |
| `mkEng` / `micro` / `guard` | animation engine: pause, micro-step gate, speed, cancellation, flying data packets (`fly`) |
| `demo(p)` | plays one of the six paths on its own |
| `L(fa, en)` | picks the Persian or English text according to the UI language |
| `render` / event handlers | UI, tab state and persistence |

Implementation notes:

- Instruction encoding uses `BigInt`, so long formats are no problem.
- Memory is a sparse `Map` from address to unit value; 32-bit address spaces cost nothing.
- The animation never calls the engine twice: `step1` runs the instruction once, and the animation then *replays* the recorded trace on a copy of the state ("VM"), so what you see always matches what the simulator did.
- The optional server exposes just two routes: `GET` and `PUT /api/state`.

---

## Limitations

- For **simulation**, words and registers are limited to 32 bits (bitwise operators work on 32 bits). Assembling and hex output are less restricted.
- A format's length must be a multiple of the memory unit. Instruction sets with **variable-length encodings inside one format** cannot be expressed; define each length as its own format instead.
- An operand split across several non-contiguous fields (split immediates) is not supported.
- Instruction bits are always laid out big-endian (most significant bit first). Only `dw` data follows the machine's byte order.
- Flags are not automatic; model them with a special register and the Operation column (like `ZF`).
- No macros, `db`, `equ`, interrupts, I/O or segments.
- One label per source line.
- SQLite mode is meant for a single user on a local machine.
- **Graphic views:** the CPU stage draws at most 16 general registers and 8 special registers (the rest still work, but are not drawn; registers beyond the 16th appear in the last slot while they are being used), and the memory window shows 12 units around the active address. The memory lab is a fixed 16-bit-word memory with 8, 16 or 32 units. Paths 5 and 6 are demonstration-only because no bundled machine has I/O instructions.

---

## Troubleshooting / FAQ

**My exported file is called `_.machine.json`.**
The file name is built from the machine name, replacing every character that is not a Latin letter, digit or `_`. Names written only in Persian therefore become `_`. Use a Latin name (or rename the file) — the name stored *inside* the JSON is unaffected.

**The machines I made are gone after switching to `python server.py`.**
`file://` and `http://localhost:8000` have separate `localStorage`. Export the machines in the old mode and import them in the new one.

**The "SQLite ✓" badge doesn't show.**
Open the app through `http://localhost:8000` (not by double-clicking the HTML file) and make sure `server.py` is running in the same folder as `machine-lab.html`.

**"Address already in use" when starting the server.**
Another program uses port 8000. Change the port in the last line of `server.py`.

**"Download all" saves only some slides.**
Allow multiple downloads for the page in your browser settings.

**My instruction line says no syntax matches.**
Check that the opcode fields, syntax and register names agree: operands must be real registers (e.g. `R0`…`Rn`, or the names in *Register names*), numbers, or defined labels, and the literal characters (`#`, `(`, `)`, `,`) must match the syntax exactly.

**The animation view is empty / the CPU stage looks small on my phone.**
The stage is a wide diagram: scroll it horizontally, or use a larger screen. If it is empty, make sure the program compiles without errors (a warning is shown above the stage).

**The animation is too fast or too slow.**
Use the **Speed** slider, or turn on **Micro-step** to advance every data movement with a click.

**The English view still shows some Persian text.**
Since 1.2.0 the graphic views are fully translated. Use the `EN` button in the toolbar; text you typed yourself (machine names, comments) is never translated.

---

## Changelog

### v1.2.0
**Added**
- Three views in the Simulator tab: Table, CPU animation, Memory lab
- Animated instruction cycle on a CPU diagram: fetch (MAR, decoder, Read, MBR, IR, PC update), decode (opcode lookup, fields, addressing mode) and execute (registers, immediates, direct/indirect memory access, ALU, write-back)
- The six internal paths of the von Neumann model, colour-coded, lit while in use, explained, and replayable with **Show path**
- Memory lab reproducing the lecture's memory examples (MAR / MBR / decoder / Read / Write), including `M10 ← (M12)` and `M(M0) ← (M0) + (M(M4))`
- Micro-step mode, pause, continuous run, skip to end and a speed slider
- Execution trace recorded by the engine (registers, memory, ALU, branches) used to drive the animation
- Persian / English text for every label, explanation and button in the new views

**Changed**
- The original simulator view became the **Table** view; its behaviour is unchanged
- `step1` now also records the executed instruction and its trace (no change to execution results)

### v1.1.0
**Added**
- English PNG slide export (overview, one slide per format, register sizes with reasons)
- Bilingual UI (Persian / English)
- Default machines: IBM 360/370, Intel 8086/8088 (simplified), RISC-V RV32I (subset), GPU core (educational)
- Machine export / import as JSON
- SQLite persistence through `server.py` (`machines.db`)
- Several `opcode` fields per format (concatenated in order)
- Custom register names and a hardwired zero register
- `sext(x,n)` and the comma token in the Operation language
- `$` (current address) in assembly
- Instruction decoding based on all opcode fields, regardless of position

**Changed**
- The first field of a format no longer has to be `opcode`; at least one opcode field is required.

### v1.0.0
- Initial release: machine definition, formats and instructions, Operation language, two-pass assembler with hex output and symbol table, simulator, format diagrams, `localStorage` persistence, Example Machines 3/4/5, light/dark theme

---

## Contributing

Bug reports and ideas are welcome through **Issues**; code improvements through **Pull Requests**. When reporting a problem, please attach the machine's export (JSON) and the source line that fails.

Ideas for the future: split immediates (RISC-V S/B/J instructions), little-endian instruction encoding, automatic flags, PDF slide export, I/O and DMA instructions that exercise paths 5 and 6, animated cache and pipeline views, screenshots of the animation views for this README.

## License

Released under the **MIT License** — see the [`LICENSE`](LICENSE) file.
