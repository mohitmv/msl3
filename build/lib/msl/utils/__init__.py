
import os, json, time
from msl import *


import argparse
from msl.utils.queue_runner import Queue_Runner
# from msl.utils.sqlary import Sqlary_v1 as Sqlary



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






def retry_if_fail(operator, exceptions=None, default_value=None, retry_limit=10, inp=(), on_error=None):
	while retry_limit > 0:
		output = run_if_can(lambda: (operator(*inp), True), exceptions, (default_value, False), on_error=on_error);
		if(output[1]):
			break;
		none_default(on_error, id_func)("retrying.. "+str(retry_limit)+" more chance remaining", );
		retry_limit -= 1;
	return output[0];



def kill_on_interrupt(threads=[], keep_running=False): #need = [os, time]
	if(keep_running):
		try:
			is_interrupt = False;
			while True:
				time.sleep(3600*24*30);
		except KeyboardInterrupt:
			is_interrupt = True;
	else:
		is_interrupt = run_if_can(lambda: (list(i.join() for i in threads), False)[1], [KeyboardInterrupt], True);
	if is_interrupt:
		print("Killing MySelf");
		os.kill(os.getpid(), 9);
	


def sys_arg_options(options=[], default_option=None, option_help="", additional_args=[]): #need = [argparse]
	parser = argparse.ArgumentParser();
	parser.add_argument('--option', '-o', default=default_option, choices=options, help=option_help);
	list(parser.add_argument(*(i[0] if type(i[0]) == list else [i[0]]), **i[1]) for i in additional_args);
	return parser.parse_args().__dict__;





