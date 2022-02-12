import os
import pymongo
from app.db.mocked_data import DEFAULT_HIRING_STAGES, CANDIDATES, JOB_POSTINGS

def migrate_candidates(db):
    db.candidates.insert_many(CANDIDATES)

def migrate_job_postings(db):
    for job_posting in JOB_POSTINGS:
        db.job_postings.insert_one(job_posting)

def migrate_hiring_stages(db):
    db.default_hiring_stages.insert_one({'version': 1, 'values': DEFAULT_HIRING_STAGES, 'active': True})

def reset_database(db):
    db.candidates.drop()
    db.job_posting.drop()
    db.default_hiring_stages.drop()

if __name__ == "__main__":
    CONNECTION_STRING = os.environ.get('GRHCONNECTIONSTRING')
    client = pymongo.MongoClient(CONNECTION_STRING)
    db = client.gestaorh
    reset_database(db)
    migrate_candidates(db)
    migrate_job_postings(db)
    migrate_hiring_stages(db)