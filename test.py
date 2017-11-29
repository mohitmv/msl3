from msl import *

from msl.utils import Queue_Runner

import time

from msl.utils.queue_runner import Queue;



def runner(x):
	print(x, "sleeping for 1 sec.");
	time.sleep(2);
	if(x['value'] == 3):
		1/0;
	print(x, "Done");



queue = Queue_Runner(operator=runner, queue_indexer=lambda x: x['id']);



list(queue.add({"id": i, "value": i}) for i in range(10));

print("Added All of them in queue");


# queue.delete(3);




# time.sleep(30);


# print("Main Thread Done.");