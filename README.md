# Adversarial Search on Tic-Tac-Toe

This repository implements adversarial search methods (Minimax and Alpha-Beta pruning) on a generalised version of tic-tac-toe.

A discussions of these methods can be found in [Russel and Norvig, 1995](https://zoo.cs.yale.edu/classes/cs470/materials/aima2010.pdf).

---

## Contents of repository

2. The `Methods` directory contains scripts for:

  1. Minimax on a generalised version of tic-tac-toe.

  2. Alpha-beta pruning on a generalised version of tic-tac-toe.

The generalised version of tic-tac-toe extends tic-tac-toe to boards of dimensions
m by n where the winner has k consecutive Xs (or Os) diagonally, vertically or
horizontally.

---

## Prerequisites

Before you begin, ensure that you have the following:

- Python 3.8 or higher
- Virtualenv (optional, but recommended)

---

## Setting up a virtual environment

It is recommended to use a virtual environment to keep the dependencies for this project separate from other projects on your system. To set up a virtual environment:

1. If you don't have virtualenv installed, run `pip install virtualenv`
2. Navigate to the project directory and create a virtual environment by running `virtualenv env`
3. Activate the virtual environment by running `source env/bin/activate`

---

## Installing dependencies

To install the dependencies for this project, run the following command:

'pip install -r requirements.txt'

This will install all of the packages listed in the `requirements.txt` file.

---

## Cloning the repository

To clone this repository, run the following command:

`git clone https://github.com/user/repo.git`
