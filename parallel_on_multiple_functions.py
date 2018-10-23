"""
Program to test out how Python handles parallel execution.
Different threads/processes run different functions.
"""

import random, time
from multiprocessing import Pool as MultiProcessPool
from multiprocessing.dummy import Pool as MultiThreadPool


class ParallelismTest():
    """
    Parallel execution testing class.

    To run threading as parallel processes, set "use_dummy_version" var to False.
    To run threading as parallel threads on a single process, set "use_dummy_version" var to True.
    """

    def __init__(self, use_dummy_version=False):
        print('')
        self.thread_number = 0

        # Check for parallel processes (standard) VS parallel threads (dummy).
        if use_dummy_version:
            print('Executing Parallel Threading Test:')
            thread_pool = MultiThreadPool(10)
        else:
            print('Executing Parallel Processing Test:')
            thread_pool = MultiProcessPool(10)

        # Run parallel execution.
        thread_a_results = thread_pool.map_async(self.parallel_function_a, [1, 2, 3])
        thread_b_results = thread_pool.map_async(self.parallel_function_b, [1, 2])
        thread_c_results = thread_pool.map_async(self.parallel_function_c, [1])
        thread_pool.close()
        thread_pool.join()

    def get_random_float(self):
        """
        Gets a random float between 0 and 2 seconds.
        :return: A random float.
        """
        random_float = float(random.randrange(0, 200))/100
        return random_float

    def parallel_function_a(self, *args):
        this_thread_number = self.thread_number
        self.thread_number += 1

        print('   Thread {0} starting function A.'.format(this_thread_number))
        time.sleep(self.get_random_float())
        print('   Thread {0} ending function A.'.format(this_thread_number))

    def parallel_function_b(self, *args):
        this_thread_number = self.thread_number
        self.thread_number += 1

        print('   Thread {0} starting function B.'.format(this_thread_number))
        time.sleep(self.get_random_float())
        print('   Thread {0} ending function B.'.format(this_thread_number))

    def parallel_function_c(self, *args):
        this_thread_number = self.thread_number
        self.thread_number += 1

        print('   Thread {0} starting function C.'.format(this_thread_number))
        time.sleep(self.get_random_float())
        print('   Thread {0} ending function C.'.format(this_thread_number))


if __name__ == "__main__":
    print("Starting program.")

    # Test as parallel threads.
    parallel_thread_start_time = time.time()
    ParallelismTest(use_dummy_version=True)
    parallel_thread_end_time = time.time()

    # Test as parallel processes.
    parallel_process_start_time = time.time()
    ParallelismTest(use_dummy_version=False)
    parallel_process_end_time = time.time()

    print('')
    print('Final Results')
    print('Parallel Thread Execution Time: {0}'.format(parallel_thread_end_time - parallel_thread_start_time))
    print('Parallel Process Execution Time: {0}'.format(parallel_process_end_time - parallel_process_start_time))
    print('')

    print("Terminating Program.")
