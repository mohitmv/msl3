

from msl import *

from msl.utils.queue_runner import Queue_Runner


class Local_Storage(dict):
	def __init__(self, storage_file, default_storage={}):
		self.storage_file = storage_file;
		dict.__init__(self, default_storage if not os.path.exists(storage_file) else json.loads(read_file(storage_file)));

	def store(self):
		write_file(self.storage_file, json.dumps(self));

	def __setitem__(self, key, val):
		dict.__setitem__(self, key, val);
		self.store();

	def __delitem__(self, key):
		dict.__delitem__(self, key);
		self.store();

	def pop(self, key):
		dict.pop(self, key);
		self.store();

	def update(self, *args, **kwargs):
		dict.update(self, *args, **kwargs);
		self.store();

	def clear(self):
		dict.clear(self);
		self.store();

	def setdefault(self, key, val=None):
		dict.setdefault(self, key, val);
		self.store();



