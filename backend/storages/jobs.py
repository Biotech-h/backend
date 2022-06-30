from backend.database.db import db_session
from backend.database.models import Job
from backend.errors import NotFoundError
from backend.schemas.job import CorrectJob


class JobsStorage():
    name = 'jobs'

    def add(self, job: CorrectJob):
        new_job = Job(
            company_uid=job.company_uid,
            name=job.name,
            salary=job.salary,
            description=job.description,
            date_published=job.date_published,
            date_expiring=job.date_expiring,
            url=job.url,
        )
        db_session.add(new_job)
        db_session.commit()

        return CorrectJob.from_orm(new_job)

    def delete(self, uid):
        job = Job.query.filter(Job.uid == uid).first()
        if not job:
            raise NotFoundError(self.name, f'uid {uid} not found')

        db_session.delete(job)
        db_session.commit()

    def update(self, job: CorrectJob):
        changed_job = Job.query.filter(Job.uid == job.uid).first()
        if not changed_job:
            raise NotFoundError(self.name, f'uid {job.uid} not found')

        changed_job.name = job.name
        changed_job.salary = job.salary
        changed_job.description = job.description
        changed_job.date_published = job.date_published
        changed_job.date_expiring = job.date_expiring
        changed_job.url = job.url

        db_session.commit()

        return CorrectJob.from_orm(changed_job)

    def get_all(self):
        return [CorrectJob.from_orm(jobs) for jobs in Job.query.all()]

    def get_by_id(self, uid):
        job = Job.query.filter(Job.uid == uid).first()
        if not job:
            raise NotFoundError(self.name, f'uid {uid} not found')

        return CorrectJob.from_orm(job)
