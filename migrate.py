"""
Exports example data from project to database.
"""
import os
import pymongo
from app.db.mocked_data import DEFAULT_HIRING_STAGES, CANDIDATES, JOB_POSTINGS

def migrate_candidates(db):
    print('migrate candidates')
    db.candidates.insert_many(CANDIDATES)
    print('candidates migrated')

def migrate_job_postings(db):
    for job_posting in JOB_POSTINGS:
        print('inserting job posting: ', job_posting['title'])
        db.job_postings.insert_one(job_posting)
        print('job posting inserted')

def migrate_hiring_stages(db):
    print('inserting default hiring stages')
    db.default_hiring_stages.insert_one({'version': 1, 'values': DEFAULT_HIRING_STAGES, 'active': True})
    print('default hiring stages inserted')


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