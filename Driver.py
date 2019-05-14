# t1.py
import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, BasicAer
from qiskit.visualization import plot_state_city


def upkeep(in1, in2, in3):

    q = QuantumRegister(5, 'q')
    circ = QuantumCircuit(q)
    c = ClassicalRegister(5, 'c')
    meas = QuantumCircuit(q, c)

    if in1 == 1:
        circ.x(q[2])
        print("1")
    if in2 == 1:
        circ.x(q[3])
        print("2")
    if in3 == 1:
        circ.x(q[4])
        print("3")

    # control block for 111->010
    circ.reset(q[0])
    circ.reset(q[1])
    circ.ccx(q[3], q[2], q[1])
    circ.cx(q[4], q[0])
    circ.ccx(q[0], q[1], q[2])
    circ.ccx(q[0], q[1], q[4])

    # control block for 000->001
    circ.reset(q[0])
    circ.reset(q[1])
    circ.cx(q[2], q[1])
    circ.cx(q[3], q[1])
    circ.x(q[1])
    circ.cx(q[1], q[0])
    circ.ccx(q[1], q[2], q[0])
    circ.reset(q[1])
    circ.cx(q[4], q[1])
    circ.ccx(q[0], q[1], q[4])

    # control block for 011->001
    circ.reset(q[0])
    circ.reset(q[1])
    circ.ccx(q[4], q[3], q[1])
    circ.cx(q[2], q[1])
    circ.swap(q[0], q[1])
    circ.cx(q[2], q[0])
    circ.cx(q[0], q[3])

    # control block for 101->011
    circ.reset(q[0])
    circ.reset(q[1])
    circ.x(q[0])
    circ.ccx(q[2], q[4], q[1])
    circ.cx(q[3], q[0])
    circ.ccx(q[0], q[1], q[2])
    circ.ccx(q[0], q[1], q[3])

    # control block for 100->010
    circ.reset(q[0])
    circ.reset(q[1])
    circ.cx(q[2], q[1])
    circ.ccx(q[2], q[3], q[1])
    circ.cx(q[1], q[0])
    circ.ccx(q[2], q[4], q[0])
    circ.ccx(q[4], q[3], q[0])
    circ.cx(q[0], q[2])
    circ.cx(q[0], q[3])

    # control block for 110->100
    circ.x(q[0])
    circ.ccx(q[3], q[2], q[1])
    circ.ccx(q[4], q[2], q[0])
    circ.ccx(q[0], q[1], q[3])

    meas.barrier(q)
    meas.measure(q, c)
    qc = circ + meas
    qc.draw()

    circ.draw()
    backend = BasicAer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1)
    result = job.result()
    counts = result.get_counts(qc)
    print(counts)
    # plot_state_city(outputstate)
    data = str(counts)
    data = data[2:5]
    return data


def feed(in1, in2, in3):
    q = QuantumRegister(5, 'q')
    circ = QuantumCircuit(q)
    c = ClassicalRegister(5, 'c')
    meas = QuantumCircuit(q, c)

    if in1 == 1:
        circ.x(q[2])
    if in2 == 1:
        circ.x(q[3])
    if in3 == 1:
        circ.x(q[4])

    # control block for 0xx->000
    circ.reset(q[0])
    circ.reset(q[1])
    circ.x(q[1])
    circ.cx(q[2], q[1])
    circ.cx(q[1], q[0])
    circ.cx(q[3], q[0])
    circ.x(q[0])
    circ.ccx(q[0], q[1], q[3])
    circ.reset(q[0])
    circ.cx(q[1], q[0])
    circ.cx(q[4], q[0])
    circ.x(q[0])
    circ.ccx(q[0], q[1], q[4])

    # control block for 101->011
    circ.reset(q[0])
    circ.reset(q[1])
    circ.x(q[0])
    circ.ccx(q[4], q[2], q[1])
    circ.cx(q[3], q[0])
    circ.ccx(q[0], q[1], q[2])
    circ.ccx(q[0], q[1], q[3])

    # control block for 100,110,111->101
    circ.reset(q[0])
    circ.reset(q[1])
    circ.ccx(q[3], q[2], q[1])
    circ.cx(q[1], q[0])
    circ.reset(q[1])
    circ.cx(q[2], q[1])
    circ.ccx(q[4], q[3], q[1])
    circ.cx(q[1], q[0])
    circ.reset(q[1])
    circ.cx(q[3], q[1])
    circ.ccx(q[0], q[1], q[3])
    circ.reset(q[1])
    circ.cx(q[4], q[1])
    circ.x(q[1])
    circ.ccx(q[0], q[1], q[4])

    meas.barrier(q)
    meas.measure(q, c)
    qc = circ + meas
    qc.draw()

    circ.draw()
    backend = BasicAer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1)
    result = job.result()
    counts = result.get_counts(qc)
    # print(counts)
    # plot_state_city(outputstate)
    data = str(counts)
    data = data[2:5]
    return data


print("000")
print(feed(0, 0, 0))
print("001")
print(feed(0, 0, 1))
print("010")
print(feed(0, 1, 0))
print("011")
print(feed(0, 1, 1))
print("100")
print(feed(1, 0, 0))
print("101")
print(feed(1, 0, 1))
print("110")
print(feed(1, 1, 0))
print("111")
print(feed(1, 1, 1))
