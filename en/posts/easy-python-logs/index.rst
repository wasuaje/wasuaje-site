.. title: Demystifying the Python logs
.. slug: easy-python-logs
.. date: 2018-05-16 23:59:59 UTC-03:30
.. tags: python, logs, easy
.. author: Wuelfhis Asuaje
.. link: http://wasuaje.com/
.. description:
.. category: python

.. figure:: /images/logging-logs-516678.jpg   
   :class: bookfig
   :alt: It's good to have a good logging strategy ;)

Intro
-----

One of the most important aspects, and at the same time weakest I found in python:
It was the handling of the logs. It seemed strange to me to see how the programs were 
full of **prints** that essentially served two purposes: debugging and as exit of the
process or program in execution. In a work project came the issue of how to handle the 
logs in an orderly and standard manner and of course, after some research I found a way
to achieve just what I wanted: Output by console and at the same time write to disk, 
in a file of my preference of the output of the program: Using only the `Python <https://python.org>`__ 
`logging <https://docs.python.org/2/library/logging.html>`__ library is enough to 
achieve a more than decent output of our code result.


Inicio
------
We are using only 2 python's standard library modules.

.. code-block:: python

  import time
  import logging


Basic Config
------------
We define the basic configuration, which is the one that will be used to write to disk, 
notice we use **asctime**, **levelname** (log level) and our message. We also 
configure the default "level" and the name of the output file (can have a relative or absolute path)


.. code-block:: python
  
  logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S',
                    filename='output.log',
                    level=logging.DEBUG)



Console
-------
Now comes the configuration of the console: instead of **basicConfig** we use **StreamHandler ()** 
and the default level to **INFO**. Use exactly the same output format, maybe you want 
to use a different one for each. You can see better how `logging <https://docs.python.org/2/library/logging.html>`__ 
works in the documentation.

Then we add the **handler** to the **logging** so that both happen at the same time. That is, write to disk and display in console.

.. code-block:: python

  console = logging.StreamHandler()
  console.setLevel(logging.INFO)
  
  formatter = logging.Formatter(
      '%(asctime)s %(levelname)-8s: %(message)s')
  
  console.setFormatter(formatter)
  
  logging.getLogger('').addHandler(console)


Example
-------
I'll show some examples of use, note that we must manually set the level of log we want to show, 
that is, the library itself can not determine when it is an error or an info or whatever. 
We must do it by ourselves depending on the possible behavior of a block of code, notice:

.. code-block:: python
  
  a = 'a string'
  try:
      b = a + 1
  except TypeError as e:  
      logging.error('OH! There has been an error: {}'.format(e))


Ah! and the output?
-------------------

Finally, this is what the output of our newly configured log looks like.

.. listing:: output.log console


The Code
--------

Here the complete piece of code:

.. listing:: logging_sample_en.py python


