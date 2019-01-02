
# Python - Threading Test

## Author
Brandon Rodriguez

## About This Program
This program has three main files. Simply run each as a standalone Python file.

Note for the first two: The numbering print out for multiprocessing currently does not work properly. To resolve this,
there needs to be a lock around the number counter, which was excluded to make code simpler.

* **parallel_on_one_function** - Tests parallelization where each thread/process runs an instance of the same
function.

* **parallel_on_multiple_function** Tests parallelization where each thread/process can run an instance
of different functions.

* **parallel_on_one_function_shared** - Works the same as "parallel_on_one_function", but with the added benefit of
sharing locks and a variable between threads. Slightly more complicated code as result.

## Notes About Python Parallelization
According to [the top google result as of Oct 2018](http://chriskiehl.com/article/parallelism-in-one-line/), it seems
that using multiprocessing.dummy is generally more efficient (both from "code length" and "execution time" standpoints)
than manually creating custom threading management.

### Multiprocessing Vs Multiprocessing.dummy
Furthermore, according to both
[stack overflow](https://stackoverflow.com/questions/2846653/how-to-use-threading-in-python) and
[the python docs](https://docs.python.org/3.5/library/multiprocessing.html#all-platforms), multiprocessing.dummy and
multiprocessing both have the same api.

The main difference is that multiprocessing.dummy executes as multiple threads while standard multiprocessing executes
as multiple processes on a single thread.

### GIL
Finally, it's worth noting that Python has
["the GIL" or "Global Interpreter Lock"](https://wiki.python.org/moin/GlobalInterpreterLock) which explicitly prevents
any two threads from running at the same time. Because of this, standard multiprocessing (which runs parallel processes)
is good for CPU intensive work where multiprocessing.dummy (which runs parallel threads on a single process) is good for
IO intensive work. Having the same API to interchange between the two is very beneficial in this regard.
