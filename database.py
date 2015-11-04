import pymongo

class Database_Tools:
	def __init__(self):
		client = pymongo.MongoClient('mongodb://<username>:<password>@ds049854.mongolab.com:49854/gallium-stats')
		db = client['gallium-stats']
		self.col_stats = db.stats

	def database_store(self, stats):
		new_stats_id = self.col_stats.replace_one({ u'_id': stats['_id'] }, stats, upsert=True).upserted_id
		if new_stats_id == None:
			print "_id is already in the database, information for the machine has been updated!"
		else:
			print new_stats_id
		self.database_read(stats['_id'])

	def database_read(self, new_id):
		for machine in self.col_stats.find_one({"_id": new_id}):
			print machine

	def read(self, command):
		pass
