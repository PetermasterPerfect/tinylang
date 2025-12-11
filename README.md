# TinyLang – Minimal Language Compiler with Static Analysis

TinyLang is a minimalistic programming language and compiler with a built-in **static program analysis framework**, inspired by the book:

> **Static Program Analysis**  
> Anders Møller & Michael I. Schwartzbach  
> Department of Computer Science, Aarhus University, Denmark

The **main goal of this project** was to implement the **Monotone Frameworks algorithm** (Chapter 5 of the book).  
Later, **LLVM-based compilation and execution** were added.

The language is intentionally designed to be **minimal**:
- Only **one numerical data type**
- **No pointers**
- **No records or complex data structures**
- **Static analysis is performed only as an equation solver and is not used directly for code transformation. Code optimization and modification are the responsibility of the LLVM compilation stage.**
---

## Features

- Monotone Frameworks static analysis implementation  
- Available Expressions Analysis  
- Live Variables Analysis  
- Reaching Definitions Analysis  
- Very Busy Expressions Analysis  
- Control Flow Graph (CFG) generation  
- LLVM IR generation and native execution  
- Benchmarks comparing different solvers

---

## Dependencies

The project depends only on:

- `antlr4-python3-runtime`
- `llvmlite`

---

##  Installation

```bash
git clone https://github.com/PetermasterPerfect/tinylang
cd tinylang
pip install .
python3 -m tinylang --help
usage: __main__.py [-h] {compile,monotone,time} ...

TinyLang toolchain

positional arguments:
  {compile,monotone,time}
    compile             Compile and execute
    monotone            Run monotone framework
    time                Benchmark monotone solvers

options:
  -h, --help            show this help message and exit
```

TinyLang supports three basic modes:

- compile - compile and execute a program
- monotone - run static analyses
- time - benchmark monotone framework solvers
## Example: Fibonacci Compilation

``` c
fib(n) {
    var a, b, i, t;
    a = 0;
    b = 1;
    i = 0;
    while (n > i) {
        t = a + b;
        a = b;
        b = t;
        i = i + 1;
    }
    return a;
}

main() {
    var n, x;
    input n;
    x = fib(n);
    return x;
}
```

``` bash
python3 -m tinylang compile examples/fibonacci
12
main(...) = 144.0
```
When add --print-module option llvm ir also will be shown.


------------------------------------------------------------------------

##  Example: Live Variables Analysis
In this example shows monotone framework for live variable analysis.
File:
```c
main() {
    var x, y, z;
    input x;
    while (x > 1) {
        y = x / 2;
        if (y > 3) { x = x - y; }
        z = x - 4;
        if (z > 0) { x = x / 2; }
        z = z - 1;
    }
    return x;
}
```


``` bash
python3 -m tinylang monotone examples/livevar
```

```
...
Analysis type:  <class 'tinylang.monotone_framework.LiveVariablesAnalysis'>
solution: 
 ["x=x-y - {'y', 'x'}", 
  "x=x/2 - {'x', 'z'}", 
  "y=x/2 - {'x'}", 
  "x - {'x'}", 
  "z=x-4 - {'x'}", 
  "z=z-1 - {'x', 'z'}", 
  "y>3 - {'y', 'x'}", 
  "input - {'x'}", 
  "z>0 - {'x', 'z'}", 
  "x>1 - {'x'}"]
...
```
From the Live Variables Analysis, a compiler can deduce that: 
- Variables y and z are never live at the same time
- The assignment:
  ```
  z = z - 1;
  ```
  writes a value that is never read.

------------------------------------------------------------------------

## Example: Benchmarking

``` bash
python3 -m tinylang time examples/big
```

```
Function  big
Analysis type:  <class 'tinylang.monotone_framework.AvailableExpressionsAnalysis'>
fixed point:  0.0022826194763183594
chaotic:  0.20209169387817383
simple worklist:  0.0018687248229980469
-------
Analysis type:  <class 'tinylang.monotone_framework.LiveVariablesAnalysis'>
fixed point:  0.002127408981323242
chaotic:  0.1031646728515625
simple worklist:  0.0005385875701904297
-------
Analysis type:  <class 'tinylang.monotone_framework.ReachingDefinitionsAnalysis'>
fixed point:  0.0009427070617675781
chaotic:  0.21620988845825195
simple worklist:  0.0014717578887939453
-------
Analysis type:  <class 'tinylang.monotone_framework.VeryBusyExpressionsAnalysis'>
fixed point:  0.0033855438232421875
chaotic:  0.14348173141479492
simple worklist:  0.0007200241088867188
-------
########
```
