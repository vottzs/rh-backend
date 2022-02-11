import pymongo
from app.db.mocked_data import DEFAULT_HIRING_STAGES, CANDIDATES, JOB_POSTINGS

def migrate_candidates(db):
    db.candidates.insert_many(CANDIDATES)

def migrate_job_postings(db):
    for job_posting in JOB_POSTINGS:
        db.job_postings.insert_one(job_posting)

def migrate_hiring_stages(db):
    db.default_hiring_stages.insert_one({'version': 1, 'values': DEFAULT_HIRING_STAGES, 'active': True})

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb+srv://leo_rh:Lobo@cluster0.286wa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.gestaorh
    migrate_candidates(db)
    migrate_job_postings(db)
    migrate_hiring_stages(db)