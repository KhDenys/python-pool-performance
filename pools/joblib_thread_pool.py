from joblib import Parallel, delayed

from pools import PoolTest


class JoblibThreadPool(PoolTest):

    def init_pool(self, worker_count):
        self.worker_count = worker_count

    def map(self, work_func, inputs):
        return Parallel(n_jobs=self.worker_count, prefer="threads")(delayed(work_func)(i) for i in inputs)
