from msl import *

import threading, traceback

class Queue:
	def __init__(self, queue_indexer=None):
		self._queue_indexer = queue_indexer;
		self._queue_list = [];
		self._obj_map = {};

	def queue(self, obj): # Assert : set(self._obj_map.keys()) == set(self._queue_list)
		if(self._queue_indexer != None):
			obj_index = self._queue_indexer(obj);
			if(obj_index not in self._obj_map):
				self._queue_list.append(obj_index);
			self._obj_map[obj_index] = obj;
		else:
			self._queue_list.append(obj);

	def dequeue(self):
		assert(len(self._queue_list) > 0);
		if(self._queue_indexer != None):
			self._obj_map.pop(self._queue_list[0]);
		self._queue_list = self._queue_list[1:];

	def top(self):
		assert(len(self._queue_list) > 0);
		top_elm = self._queue_list[0];
		return (self._obj_map[top_elm] if self._queue_indexer != None else top_elm);

	def is_empty(self):
		return (len(self._queue_list) == 0);

	def list(self):
		return list((self._obj_map[i] if self._queue_indexer != None else i) for i in self._queue_list);

	def __repr__(self):
		return str(self.list());

	def delete(self, obj_index):
		assert(self._queue_indexer != None);
		if(obj_index in self._obj_map):
			self._obj_map.pop(obj_index);
			self._queue_list.remove(obj_index);
			return True;
		else:
			return False;

	def clear(self):
		self._queue_list = [];
		self._obj_map = {};



"""
README for Queue_Runner

default_queue_class - 
1. Not required to support multi-threading.
2. must support methods in Queue.
3. 

"""


class Queue_Runner:
	def __init__(self, operator, queue_indexer=None, default_queue_class=None, logger=print):
		self._queue = none_default(default_queue_class, Queue)(queue_indexer);

		self._queue_indexer = queue_indexer;
		self._operator = operator;
		self._logger = logger;

		self._queue_read_lock = threading.Lock();
		self._cur_obj_index = None;


	def add(self, obj): # Can be called concurrently.
		self._queue_read_lock.acquire();
		is_empty = self._queue.is_empty();
		self._queue.queue(obj);
		self._queue_read_lock.release();
		if(is_empty):
			self._runner_thread = threading.Thread(target=self._runner, args=());
			self._runner_thread.start();


	def delete(self, obj_index): #Assert( queue_indexer must be defined )
		assert(self._queue_indexer != None);
		output = False;
		self._queue_read_lock.acquire();
		if(obj_index != self._cur_obj_index):
			output = self._queue.delete(obj_index);
		self._queue_read_lock.release();
		return output;


	def _runner(self):
		self._queue_read_lock.acquire();
		is_empty = self._queue.is_empty();
		if not is_empty:
			top_element = self._queue.top();
			if(self._queue_indexer != None):
				self._cur_obj_index = self._queue_indexer(top_element);
		self._queue_read_lock.release();

		while not is_empty:
			try:
				self._operator(top_element);
			except Exception:
				self._logger(traceback.format_exc());
			self._queue_read_lock.acquire();
			self._queue.dequeue();
			is_empty = self._queue.is_empty();
			if not is_empty:
				top_element = self._queue.top();
				if(self._queue_indexer != None):
					self._cur_obj_index = self._queue_indexer(top_element);
			else:
				self._cur_obj_index = None;
			self._queue_read_lock.release();


