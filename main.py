"""
Program to test out how Python handles parallel execution.

Notes:
    According to http://chriskiehl.com/article/parallelism-in-one-line/, it seems that using multiprocessing.dummy is
    generally more efficient (both from "code length" and "execution time" standpoints) than manually creating your own
    threading management.

    Furthermore, according to both https://stackoverflow.com/questions/2846653/how-to-use-threading-in-python
    and python docs, multiprocessing.dummy and multiprocessing both have the same api.

    The main difference is that multiprocessing.dummy executes as multiple threads while standard multiprocessing
    executes as multiple processes on a single thread.

    Finally, it's worth noting that Python seems to have "the GIL" or "Global Interpreter Lock" which explicitly
    prevents any two threads from running at the same time. Because of this, standard multiprocessing (which runs
    parallel processes) is good for CPU intensive work where multiprocessing.dummy (which runs parallel threads on a
    single process) is good for IO intensive work. Having the same API to interchange between the two is very powerful.
"""

import random, time
from multiprocessing import Pool as ThreadPool
from multiprocessing.dummy import Pool as DummyThreadPool


class ParallelismTest():
    """
    Parallel execution testing class.

    To run threading as parallel processes, set "use_dummy_version" var to False.
    To run threading as parallel threads on a single process, set "use_dummy_version" var to True.
    """

    def __init__(self, print_array, use_dummy_version=False, sleep=True):
        print('')

        self.thread_number = 0
        self.print_array = []

        # Since our threading method requires more than one arg, we need to pack the array with tuples.
        for arg in print_array:
            self.print_array.append((arg, sleep))

        # Check for parallel processes (dummy) VS parallel threads (standard).
        if use_dummy_version:
            print('Executing Parallel Threading Test:')
            thread_pool = DummyThreadPool(10)
        else:
            print('Executing Parallel Processing Test:')
            thread_pool = ThreadPool(10)

        # Run parallel execution.
        thread_results = thread_pool.map(self.thread_wrapper, self.print_array)
        thread_pool.close()
        thread_pool.join()
        print('   Threading Results: {0}'.format(thread_results))

    def thread_wrapper(self, args):
        """
        This is necessary to pass multiple args into a called thread method.
        If we were only passing one arg per thread, then we can skip this and call that method directly.
        :param args: Tuple of args to pass into method.
        :return: The returned value from our desired thread method.
        """
        return self.print_item(*args)

    def print_item(self, item, sleep):
        """
        Prints out the given item after a random time.
        :param item: Item to print.
        :param sleep: Dictates if sleep values should be used.
        """
        this_thread_number = self.thread_number
        self.thread_number += 1
        print('   Started Thread #{0}'.format(this_thread_number))

        if sleep:
            sleep_time = self.get_random_float()
            time.sleep(sleep_time)
        else:
            sleep_time = 0

        print('   Thread #{0} Recieved Item: {1}'.format(this_thread_number, item))
        return (item, sleep_time)

    def get_random_float(self):
        """
        Gets a random float between 0 and 2 seconds.
        :return: A random float.
        """
        random_float = float(random.randrange(0, 200))/100
        return random_float


if __name__ == "__main__":
    print("Starting program.")

    print_array =[
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '1', '2', '3', '4', '5', '6', '7', '8', '9',
    ]

    # Test as parallel threads.
    parallel_thread_start_time = time.time()
    ParallelismTest(print_array, sleep=False, use_dummy_version=True)
    parallel_thread_end_time = time.time()

    # Test as parallel processes.
    parallel_process_start_time = time.time()
    ParallelismTest(print_array, sleep=False, use_dummy_version=False)
    parallel_process_end_time = time.time()

    print('')
    print('Final Results')
    print('Parallel Thread Execution Time: {0}'.format(parallel_thread_end_time - parallel_thread_start_time))
    print('Parallel Process Execution Time: {0}'.format(parallel_process_end_time - parallel_process_start_time))
    print('')

    print("Terminating Program.")
