#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np

# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, transpile, Aer, IBMQ
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from ibm_quantum_widgets import *
from qiskit.providers.aer import QasmSimulator
IBMQ.save_account('ff29d6e2acca3b3f5083c0b430f55fe4209fbe3d444368f324cba0304615e90badc2e35f725690581c5df553562fbc232d495646242112203760831061917639')
# Loading your IBM Quantum account(s)
provider = IBMQ.load_account()


# In[10]:


qc = QuantumCircuit(2,2)
qc.h(0)
qc.cx(0,1)
qc.measure(range(2),range(2))
qc.draw()


# In[16]:


backend = Aer.get_backend('qasm_simulator')
job_simulator = backend.run(transpile(qc, backend), shots=1024)
result_simulator = job_simulator.result()
counts = result_simulator.get_counts(qc)
print(counts)


# In[17]:


from qiskit.visualization import plot_histogram
plot_histogram(counts)


# In[18]:


provider.backends()


# In[29]:


backend = provider.get_backend('ibmq_qasm_simulator')


# In[ ]:





# In[ ]:





# In[ ]:




