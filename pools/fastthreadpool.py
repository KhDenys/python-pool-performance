from pools import PoolTest
import fastthreadpool


class FastThreadPool(PoolTest):

    def init_pool(self, worker_count):
        return fastthreadpool.Pool(worker_count)

    def map(self, work_func, inputs):
        self.pool.map(work_func, inputs, unpack_args=False)
        # self.pool.shutdown()
        return self.pool.done

    def destroy_pool(self):
        self.pool.shutdown()
