# t1.py
import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, BasicAer
from qiskit.visualization import plot_state_city


def upkeep(in1, in2, in3, in4):
    # This handles the progression of the pet if not fed or watered
    q = QuantumRegister(6, 'q')
    circ = QuantumCircuit(q)
    c = ClassicalRegister(6, 'c')
    meas = QuantumCircuit(q, c)

    if int(in1) == 1:
        circ.x(q[2])
    if int(in2) == 1:
        circ.x(q[3])
    if int(in3) == 1:
        circ.x(q[4])
    if int(in4) == 1:
        circ.x(q[5])
    # check health 001
    circ.reset(q[0])
    circ.reset(q[1])
    circ.cx(q[4], q[1])
    circ.cx(q[2], q[0])
    circ.cx(q[3], q[0])
    circ.ccx(q[3], q[2], q[0])
    circ.cx(q[5], q[0])
    circ.x(q[0])
    circ.ccx(q[0], q[1], q[5])

    # check health 010
    circ.reset(q[0])
    circ.reset(q[1])
    circ.cx(q[3], q[1])
    circ.cx(q[2], q[0])
    circ.cx(q[4], q[0])
    circ.ccx(q[4], q[2], q[0])
    circ.cx(q[5], q[0])
    circ.x(q[0])
    circ.ccx(q[0], q[1], q[5])

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
    circ.x(q[1])
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
    circ.x(q[0])
    circ.cx(q[2], q[1])
    circ.cx(q[3], q[0])
    circ.cx(q[4], q[0])
    circ.ccx(q[3], q[4], q[0])
    circ.ccx(q[0], q[1], q[2])
    circ.ccx(q[0], q[1], q[3])

    # control block for 110->100
    circ.reset(q[0])
    circ.reset(q[1])
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
    # print(counts)
    # plot_state_city(outputstate)
    data = str(counts)
    data = data[2:6]
    return data


def feed(in1, in2, in3):
    # this circuit handles feeding the pet
    q = QuantumRegister(5, 'q')
    circ = QuantumCircuit(q)
    c = ClassicalRegister(5, 'c')
    meas = QuantumCircuit(q, c)

    if int(in1) == 1:
        circ.x(q[2])
    if int(in2) == 1:
        circ.x(q[3])
    if int(in3) == 1:
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

    # control block for 100->101
    circ.reset(q[0])
    circ.reset(q[1])
    circ.cx(q[2], q[1])
    circ.x(q[0])
    circ.cx(q[3], q[0])
    circ.cx(q[4], q[0])
    circ.ccx(q[4], q[3], q[0])
    circ.ccx(q[0], q[1], q[4])

    # control block for 110,111->101
    circ.reset(q[0])
    circ.reset(q[1])
    circ.ccx(q[3], q[2], q[1])
    circ.cx(q[1], q[0])
    circ.reset(q[1])
    circ.cx(q[2], q[1])
    circ.ccx(q[4], q[2], q[1])
    circ.x(q[1])
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


def drink(in1, in2, in3):
    # this circuit handles watering the pet
    q = QuantumRegister(5, 'q')
    circ = QuantumCircuit(q)
    c = ClassicalRegister(5, 'c')
    meas = QuantumCircuit(q, c)

    if int(in1) == 1:
        circ.x(q[2])
    if int(in2) == 1:
        circ.x(q[3])
    if int(in3) == 1:
        circ.x(q[4])

    # 001,010,100->111
    circ.reset(q[0])
    circ.reset(q[1])
    circ.cx(q[2], q[1])
    circ.cx(q[3], q[1])
    circ.cx(q[4], q[1])
    circ.cx(q[2], q[0])
    circ.x(q[0])
    circ.ccx(q[0], q[1], q[2])
    circ.reset(q[0])
    circ.cx(q[3], q[0])
    circ.x(q[0])
    circ.ccx(q[0], q[1], q[3])
    circ.reset(q[0])
    circ.cx(q[4], q[0])
    circ.x(q[0])
    circ.ccx(q[0], q[1], q[4])

    # control block for 110->100
    circ.reset(q[0])
    circ.reset(q[1])
    circ.ccx(q[3], q[2], q[1])
    circ.cx(q[4], q[0])
    circ.x(q[0])
    circ.ccx(q[0], q[1], q[3])

    # control block for 011,101->110
    circ.reset(q[0])
    circ.reset(q[1])
    circ.ccx(q[4], q[2], q[1])
    circ.ccx(q[3], q[4], q[1])
    circ.cx(q[1], q[0])
    circ.reset(q[1])
    circ.ccx(q[4], q[2], q[1])
    circ.ccx(q[1], q[0], q[3])
    circ.ccx(q[1], q[0], q[4])
    circ.reset(q[1])
    circ.cx(q[2], q[1])
    circ.x(q[1])
    circ.ccx(q[0], q[1], q[4])
    circ.ccx(q[0], q[1], q[2])


    # control block for 000->110
    circ.reset(q[0])
    circ.reset(q[1])
    circ.x(q[1])
    circ.cx(q[2], q[1])
    circ.cx(q[3], q[1])
    circ.cx(q[4], q[1])
    circ.cx(q[1], q[0])
    circ.ccx(q[3], q[2], q[0])
    circ.ccx(q[4], q[2], q[0])
    circ.ccx(q[4], q[3], q[0])
    circ.ccx(q[0], q[1], q[2])
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
    # print(counts)
    # plot_state_city(outputstate)
    data = str(counts)
    data = data[2:5]
    return data


def test_feed():
    # tests that the feed circuit works correctly
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


def test_upkeep():
    # tests that the upkeep circuit works correctly
    print("000")
    print(upkeep(0, 0, 0))
    print("001")
    print(upkeep(0, 0, 1))
    print("010")
    print(upkeep(0, 1, 0))
    print("011")
    print(upkeep(0, 1, 1))
    print("100")
    print(upkeep(1, 0, 0))
    print("101")
    print(upkeep(1, 0, 1))
    print("110")
    print(upkeep(1, 1, 0))
    print("111")
    print(upkeep(1, 1, 1))


def test_drink():
    # tests that the drink circuit works correctly
    print("000")
    print(drink(0, 0, 0))
    print("001")
    print(drink(0, 0, 1))
    print("010")
    print(drink(0, 1, 0))
    print("011")
    print(drink(0, 1, 1))
    print("100")
    print(drink(1, 0, 0))
    print("101")
    print(drink(1, 0, 1))
    print("110")
    print(drink(1, 1, 0))
    print("111")
    print(drink(1, 1, 1))


def status_info(status):
    if str(status)[:1] == "0":
        print("Your pet is healthy")
        if status[1:] == "111" or status[1:] == "010":
            print("They are hungry though")
        if status[1:] == "000" or status[1:] == "100":
            print("They are thirsty though")
        if status[1:] == "110" or status[1:] == "010":
            print("They are going to be thirsty soon")
        if status[1:] == "100" or status[1:] == "001":
            print("They are going to be hungry soon")
    else:
        print("Your pet is sick! please feed and water it!")


def main_loop():
    # This is the main loop of the game

    status = "0101"
    loop = True
    while loop:
        status_info(status)
        print("To feed your pet, enter 0. To water your pet, enter 1. To play with your pet, enter 2")
        print("To exit, enter 3.")
        choice = input()

        try:
            if int(choice) == 0:
                if str(status)[:1] == "0":
                    status = str(status[:1]) + str(feed(status[3:], status[2:3], status[1:2]))
                else:
                    status = "0000"
            elif int(choice) == 1:
                if str(status)[:1] == "0":
                    status = status[:1] + str(drink(status[3:], status[2:3], status[1:2]))
                else:
                    status = "0111"
            elif int(choice) == 2:
                status = upkeep(status[3:], status[2:3], status[1:2], status[:1])
                if str(status)[:1] == "0":
                    print("your pet is very happy to be played with")
                else:
                    print("Your pet is too sick to play!")
            elif int(choice) == 3:
                loop = False
            else:
                print("Sorry, that is not a valid input")
        except:
            print("invalid input")


    print("Thanks for playing the game!")


main_loop()

